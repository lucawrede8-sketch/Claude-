#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3-Jahres-Szenariomodell für den Aufbau einer externen Weiterbildungsakademie
(Deutschland, 10 FTE, Start November 2026).

Reines Python (nur Standardbibliothek). Aufruf:
    python3 -I szenario_modell.py            -> schreibt szenarien.md ins selbe Verzeichnis
    python3 -I szenario_modell.py --stdout   -> gibt Markdown auf stdout aus

Modelllogik (vereinfacht, monatlich über 36 Monate, Nov 2026 – Okt 2029):
  Erlöse:  (a) offene Seminare, (b) Inhouse-Trainings, (c) Zertifikatslehrgänge,
           (d) Live-Online/Webinare, (e) E-Learning-Abo, (f) Ankerkunde/Muttergesellschaft
  Variable Kosten: Honorartrainer (nur für Tage über der internen Trainerkapazität),
           Reise, Raum, Catering/Unterlagen, Zertifikate/Badges, Content-Lizenz E-Learning,
           variable Vertriebskosten (CAC)
  Fixkosten: Personal 10 FTE (+31 % Aufschlag), Basis-Marketing, Plattform/Software,
           Zertifizierung (AZAV, ZFU, ISO), Recht/Steuer, Overhead, Aufbau-Einmalkosten
  Deckungsbeitrag = Umsatz - variable Kosten; EBIT = DB - Fixkosten;
  kumulierter Cash = kumuliertes EBIT (ohne Zahlungsziele, Steuern, Capex/AfA).
"""

import copy
import os
import sys

# ---------------------------------------------------------------------------
# 1. Annahmen (Basis = realistisches Szenario). Jede Annahme mit Quelle/Markierung.
# ---------------------------------------------------------------------------

JAHRE = ["Jahr 1 (Nov 26–Okt 27)", "Jahr 2 (Nov 27–Okt 28)", "Jahr 3 (Nov 28–Okt 29)"]
MONATSNAMEN = ["Nov", "Dez", "Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt"]

# Quellenkürzel (Dateien im Ordner research_notes/…)
Q_PREIS = "wettbewerb_preise.md"
Q_PROD = "produkt_delivery.md"
Q_MARKT = "markt_nachfrage.md"
Q_GTM = "gtm_vertrieb.md"
Q_TEAM = "team_rollen_budget.md"
Q_RECHT = "recht_zertifizierung_foerderung.md"
EIGEN = "eigene Annahme"

# Jede Annahme: key -> (Wert realistisch, Einheit, Quelle/Markierung)
BASIS = {
    # --- (a) offene Seminare ---
    "preis_offen_tag": (650, "€ netto / TN / Tag", f"{Q_PREIS}: TÜV NORD 1-Tag 650–660 €, Inferenz-Korridor Energie-Fachseminar 550–700 €/Tag"),
    "tage_offen": (1.5, "Tage / Termin", f"{EIGEN} (Mix aus 1- und 2-Tages-Seminaren)"),
    "max_tn_offen": (12, "TN / Termin (Kapazität)", f"{Q_PROD}: Obergrenze ~15 TN üblich; {EIGEN} 12"),
    "auslastung_offen": (0.60, "Anteil belegter Plätze", f"{EIGEN}; keine Branchenwerte gefunden ({Q_PREIS} Gaps)"),
    "ausfall_offen": (0.25, "Anteil abgesagter Termine", f"{EIGEN}; AGB-Mindest-TN 3–10, keine Branchen-Durchführungsquote ({Q_PREIS} §3)"),
    "termine_offen": ([40, 75, 100], "geplante Termine / Jahr", f"{EIGEN} (Hochlauf)"),
    # --- (b) Inhouse ---
    "preis_inhouse_tag": (3000, "€ netto / Trainingstag", f"{Q_PREIS}: Inhouse-Gruppe 2.000–5.000 €/Tag; Beispiel 3.950 €/Tag"),
    "inhouse_tage": ([60, 130, 200], "Trainingstage / Jahr", f"{EIGEN} (Hochlauf)"),
    "tage_je_inhouse_kunde": (4, "Tage / Kunde / Jahr", EIGEN),
    "neukundenanteil_inhouse": ([1.0, 0.6, 0.5], "Anteil Neukunden an Inhouse-Kunden", f"{EIGEN}; keine Wiederbuchungsquoten gefunden ({Q_GTM} §2)"),
    # --- (c) Zertifikatslehrgänge ---
    "preis_lehrgang": (2400, "€ netto / TN", f"{Q_PREIS}: TAE 5 Tage 2.100 €; Führungskraft (IHK) 1.595 € + 200 €; KI-Manager (IHK) 2.990 €"),
    "tage_lehrgang": (5, "Tage / Durchgang", f"{Q_PREIS}: TAE/TÜV 5-Tage-Formate"),
    "max_tn_lehrgang": (12, "TN / Durchgang", EIGEN),
    "auslastung_lehrgang": (0.60, "Anteil belegter Plätze", EIGEN),
    "ausfall_lehrgang": (0.15, "Anteil abgesagter Durchgänge", EIGEN),
    "lehrgaenge": ([2, 5, 8], "Durchgänge / Jahr", f"{EIGEN}; {Q_PROD} §2: IHK-Lizenz dauert Monate"),
    "zertifikat_je_tn": (200, "€ / TN (IHK-Zertifikat/Prüfung)", f"{Q_PREIS}: TA Bildungszentrum 200 € IHK-Zertifikat"),
    # --- (d) Live-Online / Webinare ---
    "preis_online": (350, "€ netto / TN (Halbtag)", f"{Q_PREIS}: VfEW 320–370 € Online-Regulierungsseminar; Inferenz 300–400 €"),
    "tage_online": (0.5, "Tage / Termin", f"{Q_PREIS}: 2–4-h-Formate"),
    "max_tn_online": (25, "TN / Termin", EIGEN),
    "auslastung_online": (0.50, "Anteil belegter Plätze", f"{EIGEN}; {Q_GTM}: Webinar-Teilnahmequote 40–60 % (Vendor)"),
    "ausfall_online": (0.20, "Anteil abgesagter Termine", EIGEN),
    "termine_online": ([20, 45, 70], "Termine / Jahr", EIGEN),
    # --- (e) E-Learning-Abo ---
    "preis_elearning_monat": (5.0, "€ / Lizenz / Monat", f"{EIGEN}; Referenz generische Flatrate Haufe 1,11–1,67 €/MA/Monat ({Q_PREIS}, {Q_GTM}); Aufschlag für Branchencontent"),
    "lizenzen_je_kunde": (60, "Lizenzen / Firmenkunde", f"{Q_PREIS}: Haufe Mindestpaket 50 Lizenzen; {EIGEN} 60"),
    "kunden_elearning": ([3, 10, 20], "Firmenkunden (Jahresende)", EIGEN),
    "content_lizenz_anteil": (0.40, "Anteil Content-Lizenzkosten am E-Learning-Umsatz", f"{EIGEN}; keine Reseller-Margen gefunden ({Q_PROD} §3)"),
    # --- (f) Ankerkunde / Muttergesellschaft ---
    "anker_anteil": (0.30, "Anteil der Kapazität (0 / 30 / 50 %)", "Parameter lt. Auftrag; Szenario-Zuordnung eigene Annahme"),
    "kapazitaet_tage": ([300, 500, 650], "Durchführungstage Kapazität / Jahr", f"{EIGEN}: interne Trainer + Honorarpool"),
    "anker_preisfaktor": (0.90, "Faktor auf Inhouse-Tagessatz (Konzernverrechnung)", f"{EIGEN}; {Q_PREIS}: Mitglieder-/Konzernrabatte 10–20 % üblich"),
    # --- Personal ---
    "gehaelter": ({
        "Leitung Akademie": 100000,
        "Key Account / Vertrieb (2)": 140000,
        "Marketing / Content": 58000,
        "Produktmanagement / Learning Architect": 75000,
        "Seminarorganisation / Backoffice (2)": 96000,
        "Interne Trainer:innen / Fachexpert:innen (3)": 216000,
    }, "€ Brutto-Jahresgehälter, 10 FTE (Summe 685.000 €)", f"{Q_TEAM} §5 Planwerte (Leitung 100k, Architect 75k, PM 62k, ID 60k…); Rollenmix für externen Markt {EIGEN}"),
    "aufschlag_personal": (0.31, "Aufschlag auf Bruttogehalt (AG-SV + Gemeinkosten)", f"{Q_TEAM} §5: +21 % SV + ~10 % Gemeinkosten (Faustregel, nicht quellenbelegt)"),
    "gehaltssteigerung": (0.03, "p. a.", EIGEN),
    "fte_hochlauf": ([6, 8, 10], "FTE in Nov / Dez 2026 / ab Jan 2027", EIGEN),
    "interne_trainertage": (330, "Durchführungstage / Jahr (3 interne Trainer × 110)", f"{EIGEN}; {Q_TEAM} §6: Skalierung über Faculty/Pool statt FTE"),
    # --- Honorartrainer ---
    "honorar_tagessatz": (1400, "€ / Tag (inkl. Vorbereitung)", f"{Q_PREIS}/{Q_TEAM}: managerSeminare Ø 1.357 €/Tag; BDVT 2026 ab 1.500 €"),
    "reise_je_trainertag": (150, "€ / Honorartrainertag", f"{Q_PREIS}: Reisepauschale 200 € je Einsatz (Anbieterbeispiel); {EIGEN} 150"),
    # --- Räume / Catering / Material ---
    "raum_je_tag": (600, "€ / Seminartag (offen, Lehrgang)", f"{Q_PREIS} §3 Inferenz: Raum/Technik 800–1.500 € je 2-Tages-Seminar"),
    "catering_je_tn_tag": (70, "€ / TN / Präsenztag (Catering, Unterlagen)", f"{Q_PREIS} §3: 100–150 €/TN/Tag inkl. Raumanteil; {Q_TEAM}: 130 € Raum+Verpflegung; {EIGEN} 70 ohne Raum"),
    "badge_je_tn": (15, "€ / TN (Teilnahmebescheinigung/Open Badge)", EIGEN),
    "material_online_je_tn": (10, "€ / TN Live-Online", EIGEN),
    # --- Marketing / Vertrieb (CAC) ---
    "cac_offen_je_tn": (120, "€ / Teilnehmer:in offenes Seminar", f"{EIGEN}; {Q_GTM} §2: CPL 70–150 € (LinkedIn, Agentur), Portale/SEA"),
    "cac_inhouse_je_neukunde": (3000, "€ / Inhouse-Neukunde", f"{EIGEN}: CPL ~100 € ÷ Lead→Kunde ~3,5 % ({Q_GTM} §2 Rechenbeispiel)"),
    "cac_lehrgang_je_tn": (200, "€ / Lehrgangs-TN", EIGEN),
    "cac_online_je_tn": (40, "€ / Live-Online-TN", EIGEN),
    "cac_elearning_je_kunde": (1500, "€ / E-Learning-Firmenkunde", EIGEN),
    "marketing_fix": ([120000, 100000, 100000], "€ / Jahr (Website, Content, Webinare, Messen, Verbände)", f"{EIGEN}; {Q_GTM} §1/§6: Thought Leadership, Verbände, Ausschreibungen"),
    # --- Plattform / Software ---
    "software_jahr": (48000, "€ / Jahr (Seminarverwaltung, LMS, Webinar-Tool, CRM, Badges)", f"{Q_PROD} §5: 'low hundreds to low thousands €/Monat' (Inferenz); {EIGEN} 4.000 €/Monat"),
    "software_setup": (25000, "€ einmalig (Jahr 1)", EIGEN),
    # --- Zertifizierung ---
    "azav_erst": (12000, "€ einmalig Trägerzulassung + QM-Aufbau (Jahr 1)", f"{Q_RECHT} §5: AZAV gesamt 5.000–70.000 € (Anbieterangabe); {EIGEN} unteres Drittel"),
    "azav_jahr": (3000, "€ / Jahr Überwachung (ab Jahr 2)", EIGEN),
    "azav_massnahme_je": (1500, "€ je Maßnahmenzulassung", EIGEN),
    "lehrgangsprodukte_neu": ([2, 2, 1], "neue Lehrgangsprodukte / Jahr (AZAV-Maßnahmen)", EIGEN),
    "zfu_kurse_neu": ([1, 2, 1], "ZFU-pflichtige Fernlehrgänge neu / Jahr", f"{EIGEN}; {Q_RECHT} §3: nur asynchrone Kurse mit Lernerfolgskontrolle"),
    "zfu_gebuehr_faktor": (1.5, "× Kurspreis, min. 1.050 €", f"Vorgabe Auftrag; {Q_RECHT} §3 (FIM-Portal, Gebührenstand ggf. veraltet)"),
    "zfu_gebuehr_min": (1050, "€", f"Vorgabe Auftrag; {Q_RECHT} §3"),
    "iso_erst": (10000, "€ einmalig ISO 9001/21001 Erstzertifizierung inkl. Beratung (Jahr 1)", f"{EIGEN}; keine Quelle ({Q_RECHT} Gaps)"),
    "iso_jahr": (3000, "€ / Jahr Überwachungsaudit (ab Jahr 2)", EIGEN),
    # --- Recht / Steuer / Overhead / Aufbau ---
    "recht_steuer": ([30000, 20000, 20000], "€ / Jahr (Gründung, AGB, § 127 SGB IV, § 4 Nr. 21 UStG, Buchhaltung)", f"{EIGEN}; {Q_RECHT}, {Q_PROD} §4"),
    "overhead": ([60000, 60000, 60000], "€ / Jahr (Versicherung, Reisen Vertrieb, Sonstiges)", EIGEN),
    "aufbau_einmalig": (40000, "€ einmalig (Marke, Website, Erstproduktion Content)", EIGEN),
}


def basiswerte():
    """Nur die Zahlenwerte aus BASIS (ohne Einheit/Quelle)."""
    return {k: copy.deepcopy(v[0]) for k, v in BASIS.items()}


# Szenario-Überschreibungen (alles eigene Annahmen; Spreizung orientiert sich an
# Preiskorridoren der Notizen: Preise ±10 %, Auslastung ±15 Punkte, Volumen ±35 %).
SZENARIEN = {
    "pessimistisch": {
        "preis_offen_tag": 580, "preis_inhouse_tag": 2600, "preis_lehrgang": 2100,
        "preis_online": 300, "preis_elearning_monat": 3.0,
        "auslastung_offen": 0.45, "auslastung_lehrgang": 0.45, "auslastung_online": 0.40,
        "ausfall_offen": 0.35, "ausfall_lehrgang": 0.25, "ausfall_online": 0.30,
        "termine_offen": [26, 49, 65], "inhouse_tage": [39, 85, 130],
        "lehrgaenge": [1, 3, 5], "termine_online": [13, 29, 45], "kunden_elearning": [2, 6, 12],
        "anker_anteil": 0.0, "honorar_tagessatz": 1500,
        "neukundenanteil_inhouse": [1.0, 0.7, 0.6],
    },
    "realistisch": {},
    "optimistisch": {
        "preis_offen_tag": 720, "preis_inhouse_tag": 3400, "preis_lehrgang": 2700,
        "preis_online": 400, "preis_elearning_monat": 7.0,
        "auslastung_offen": 0.75, "auslastung_lehrgang": 0.75, "auslastung_online": 0.60,
        "ausfall_offen": 0.15, "ausfall_lehrgang": 0.10, "ausfall_online": 0.10,
        "termine_offen": [52, 98, 130], "inhouse_tage": [78, 170, 260],
        "lehrgaenge": [3, 7, 10], "termine_online": [26, 59, 90], "kunden_elearning": [4, 14, 28],
        "anker_anteil": 0.50, "honorar_tagessatz": 1300,
        "neukundenanteil_inhouse": [1.0, 0.5, 0.4],
    },
}

# Monatsgewichte (Verteilung der Jahresmengen; Jahr 1 = Hochlauf, danach Saisonalität)
GEWICHTE_J1 = [0.0, 0.1, 0.3, 0.5, 0.7, 0.8, 0.9, 1.0, 0.9, 0.5, 1.2, 1.3]
GEWICHTE_J2 = [1.1, 0.6, 1.0, 1.1, 1.2, 1.0, 1.1, 1.1, 0.9, 0.5, 1.2, 1.1]
GEWICHTE_ANKER_J1 = [0.0, 0.0] + [1.0] * 10   # Ankerkunde ab Jan 2027


def _norm(w):
    s = sum(w)
    return [x / s for x in w]


def gewichte(jahr, anker=False):
    if jahr == 0:
        return _norm(GEWICHTE_ANKER_J1 if anker else GEWICHTE_J1)
    return _norm(GEWICHTE_J2)


# ---------------------------------------------------------------------------
# 2. Rechenkern
# ---------------------------------------------------------------------------

def lauf(p):
    """Rechnet 36 Monate und liefert Monatsreihen + Jahreswerte."""
    N = 36
    reihen = {k: [0.0] * N for k in [
        "umsatz_offen", "umsatz_inhouse", "umsatz_lehrgang", "umsatz_online",
        "umsatz_elearning", "umsatz_anker", "umsatz",
        "tn_offen", "tn_lehrgang", "tn_online", "tn_elearning", "tn_anker", "tn",
        "tage_offen", "tage_inhouse", "tage_lehrgang", "tage_online", "tage_anker", "tage",
        "tage_intern", "tage_honorar",
        "k_honorar", "k_reise", "k_raum", "k_catering", "k_zertifikat", "k_content", "k_cac",
        "var_kosten", "db",
        "k_personal", "k_marketing_fix", "k_software", "k_zertifizierung", "k_recht",
        "k_overhead", "k_aufbau", "fix_kosten", "ebit", "cash_kum", "fte",
    ]}
    gehalt_summe = sum(p["gehaelter"].values())
    zfu_gebuehr = max(p["zfu_gebuehr_min"], p["zfu_gebuehr_faktor"] * p["preis_lehrgang"])
    anker_tagessatz = p["preis_inhouse_tag"] * p["anker_preisfaktor"]
    kum = 0.0
    for m in range(N):
        y, mi = divmod(m, 12)
        w = gewichte(y)[mi]
        wa = gewichte(y, anker=True)[mi]
        r = {}
        # (a) offene Seminare
        durch = p["termine_offen"][y] * w * (1 - p["ausfall_offen"])
        tn = durch * p["max_tn_offen"] * p["auslastung_offen"]
        tage = durch * p["tage_offen"]
        r["tn_offen"], r["tage_offen"] = tn, tage
        r["umsatz_offen"] = tn * p["tage_offen"] * p["preis_offen_tag"]
        raum = tage * p["raum_je_tag"]
        catering = tn * p["tage_offen"] * p["catering_je_tn_tag"]
        zert = tn * p["badge_je_tn"]
        cac = tn * p["cac_offen_je_tn"]
        # (b) Inhouse
        tage_ih = p["inhouse_tage"][y] * w
        r["tage_inhouse"] = tage_ih
        r["umsatz_inhouse"] = tage_ih * p["preis_inhouse_tag"]
        neukunden = tage_ih / p["tage_je_inhouse_kunde"] * p["neukundenanteil_inhouse"][y]
        cac += neukunden * p["cac_inhouse_je_neukunde"]
        # (c) Zertifikatslehrgänge
        durch_l = p["lehrgaenge"][y] * w * (1 - p["ausfall_lehrgang"])
        tn_l = durch_l * p["max_tn_lehrgang"] * p["auslastung_lehrgang"]
        tage_l = durch_l * p["tage_lehrgang"]
        r["tn_lehrgang"], r["tage_lehrgang"] = tn_l, tage_l
        r["umsatz_lehrgang"] = tn_l * p["preis_lehrgang"]
        raum += tage_l * p["raum_je_tag"]
        catering += tn_l * p["tage_lehrgang"] * p["catering_je_tn_tag"]
        zert += tn_l * p["zertifikat_je_tn"]
        cac += tn_l * p["cac_lehrgang_je_tn"]
        # (d) Live-Online
        durch_o = p["termine_online"][y] * w * (1 - p["ausfall_online"])
        tn_o = durch_o * p["max_tn_online"] * p["auslastung_online"]
        tage_o = durch_o * p["tage_online"]
        r["tn_online"], r["tage_online"] = tn_o, tage_o
        r["umsatz_online"] = tn_o * p["preis_online"]
        zert += tn_o * p["material_online_je_tn"]
        cac += tn_o * p["cac_online_je_tn"]
        # (e) E-Learning-Abo: Kundenbestand wächst linear innerhalb des Jahres
        start = p["kunden_elearning"][y - 1] if y > 0 else 0
        ziel = p["kunden_elearning"][y]
        kunden = start + (ziel - start) * (mi + 1) / 12
        if y == 0 and mi < 2:
            kunden = 0.0
        lizenzen = kunden * p["lizenzen_je_kunde"]
        r["tn_elearning"] = lizenzen
        r["umsatz_elearning"] = lizenzen * p["preis_elearning_monat"]
        content = r["umsatz_elearning"] * p["content_lizenz_anteil"]
        neukunden_el = max(0.0, (ziel - start) / 12) if not (y == 0 and mi < 2) else 0.0
        cac += neukunden_el * p["cac_elearning_je_kunde"]
        # (f) Ankerkunde: Anteil der Kapazität als Inhouse-Tage zum Konzernpreis
        tage_a = p["kapazitaet_tage"][y] * p["anker_anteil"] * wa
        r["tage_anker"] = tage_a
        r["umsatz_anker"] = tage_a * anker_tagessatz
        r["tn_anker"] = tage_a * 12  # Annahme: 12 TN je Ankerkunden-Trainingstag (nur Statistik)
        # Trainerkapazität
        tage_ges = tage + tage_ih + tage_l + tage_o + tage_a
        intern_cap = p["interne_trainertage"] / 12 * (p["fte_hochlauf"][min(m, 2)] / 10)
        tage_intern = min(tage_ges, intern_cap)
        tage_hon = tage_ges - tage_intern
        r["tage"], r["tage_intern"], r["tage_honorar"] = tage_ges, tage_intern, tage_hon
        r["k_honorar"] = tage_hon * p["honorar_tagessatz"]
        r["k_reise"] = tage_hon * p["reise_je_trainertag"]
        r["k_raum"], r["k_catering"], r["k_zertifikat"], r["k_content"], r["k_cac"] = raum, catering, zert, content, cac
        r["umsatz"] = sum(r[k] for k in ["umsatz_offen", "umsatz_inhouse", "umsatz_lehrgang", "umsatz_online", "umsatz_elearning", "umsatz_anker"])
        r["tn"] = r["tn_offen"] + r["tn_lehrgang"] + r["tn_online"]  # Präsenz/Live-TN ohne E-Learning-Lizenzen und Ankerkunde
        r["var_kosten"] = sum(r[k] for k in ["k_honorar", "k_reise", "k_raum", "k_catering", "k_zertifikat", "k_content", "k_cac"])
        r["db"] = r["umsatz"] - r["var_kosten"]
        # Fixkosten
        fte = p["fte_hochlauf"][min(m, 2)]
        r["fte"] = fte
        r["k_personal"] = gehalt_summe * (1 + p["aufschlag_personal"]) * (1 + p["gehaltssteigerung"]) ** y / 12 * fte / 10
        r["k_marketing_fix"] = p["marketing_fix"][y] / 12
        r["k_software"] = p["software_jahr"] / 12 + (p["software_setup"] if m == 0 else 0)
        zertifizierung = 0.0
        if m == 2:
            zertifizierung += p["azav_erst"]
        if m == 5:
            zertifizierung += p["iso_erst"]
        if y >= 1:
            zertifizierung += (p["azav_jahr"] + p["iso_jahr"]) / 12
        zertifizierung += (p["lehrgangsprodukte_neu"][y] * p["azav_massnahme_je"] + p["zfu_kurse_neu"][y] * zfu_gebuehr) / 12
        r["k_zertifizierung"] = zertifizierung
        r["k_recht"] = p["recht_steuer"][y] / 12
        r["k_overhead"] = p["overhead"][y] / 12
        r["k_aufbau"] = p["aufbau_einmalig"] / 3 if m < 3 else 0.0
        r["fix_kosten"] = sum(r[k] for k in ["k_personal", "k_marketing_fix", "k_software", "k_zertifizierung", "k_recht", "k_overhead", "k_aufbau"])
        r["ebit"] = r["db"] - r["fix_kosten"]
        kum += r["ebit"]
        r["cash_kum"] = kum
        for k, v in r.items():
            reihen[k][m] = v

    # Jahreswerte
    jahre = []
    for y in range(3):
        sl = slice(12 * y, 12 * y + 12)
        j = {k: sum(v[sl]) for k, v in reihen.items() if k not in ("cash_kum", "fte", "tn_elearning")}
        j["cash_kum"] = reihen["cash_kum"][12 * y + 11]
        j["fte"] = sum(reihen["fte"][sl]) / 12
        j["lizenzen_elearning"] = reihen["tn_elearning"][12 * y + 11]
        j["umsatz_je_fte"] = j["umsatz"] / j["fte"]
        j["db_marge"] = j["db"] / j["umsatz"] if j["umsatz"] else 0.0
        j["ebit_marge"] = j["ebit"] / j["umsatz"] if j["umsatz"] else 0.0
        jahre.append(j)

    # Break-even-Monate
    def _nachhaltig(m):
        # positiver Monat, dessen folgende 12 Monate (mind. 6 verfügbare) in Summe positiv sind
        fenster = reihen["ebit"][m:m + 12]
        return reihen["ebit"][m] > 0 and len(fenster) >= 6 and sum(fenster) > 0
    be_monat_ebit = next((m for m in range(N) if _nachhaltig(m)), None)
    be_monat_cash = next((m for m in range(N) if reihen["cash_kum"][m] >= 0 and m > 0), None)
    finanzbedarf = -min(reihen["cash_kum"])

    return {
        "reihen": reihen, "jahre": jahre,
        "be_monat_ebit": be_monat_ebit, "be_monat_cash": be_monat_cash,
        "finanzbedarf": finanzbedarf, "zfu_gebuehr": zfu_gebuehr, "anker_tagessatz": anker_tagessatz,
    }


def break_even_tn(p, fix_umlage_je_tag=0.0):
    """Break-even-Teilnehmende je Durchführung (direkte Kosten bzw. inkl. Fixkostenumlage je Tag).
    Annahme: Durchführung durch Honorartrainer (Grenzkostenbetrachtung)."""
    out = {}
    tr = p["honorar_tagessatz"] + p["reise_je_trainertag"]
    # offenes Seminar
    fix = (tr + p["raum_je_tag"] + fix_umlage_je_tag) * p["tage_offen"]
    var = p["catering_je_tn_tag"] * p["tage_offen"] + p["badge_je_tn"] + p["cac_offen_je_tn"]
    erloes = p["preis_offen_tag"] * p["tage_offen"]
    out["Offenes Seminar (1,5 Tage)"] = (fix / (erloes - var), erloes, var, fix, p["max_tn_offen"])
    # Lehrgang
    fix = (tr + p["raum_je_tag"] + fix_umlage_je_tag) * p["tage_lehrgang"]
    var = p["catering_je_tn_tag"] * p["tage_lehrgang"] + p["zertifikat_je_tn"] + p["cac_lehrgang_je_tn"]
    erloes = p["preis_lehrgang"]
    out["Zertifikatslehrgang (5 Tage)"] = (fix / (erloes - var), erloes, var, fix, p["max_tn_lehrgang"])
    # Live-Online
    fix = (tr + fix_umlage_je_tag) * p["tage_online"]
    var = p["material_online_je_tn"] + p["cac_online_je_tn"]
    erloes = p["preis_online"]
    out["Live-Online (Halbtag)"] = (fix / (erloes - var), erloes, var, fix, p["max_tn_online"])
    return out


# ---------------------------------------------------------------------------
# 3. Formatierung
# ---------------------------------------------------------------------------

def eur(x, k=True):
    if k:
        return f"{x / 1000:,.0f} T€".replace(",", ".")
    return f"{x:,.0f} €".replace(",", ".")


def num(x, d=0):
    s = f"{x:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def pct(x):
    return f"{x * 100:,.0f} %".replace(",", ".")


def monat_label(m):
    if m is None:
        return "nicht innerhalb von 36 Monaten"
    y, mi = divmod(m, 12)
    jahr = 2026 + (y + (1 if mi >= 2 else 0))
    return f"Monat {m + 1} ({MONATSNAMEN[mi]} {jahr})"


PROZENT_KEYS = ("auslastung", "ausfall", "anteil", "aufschlag", "steigerung")


def fmt_wert(v, key=""):
    prozent = any(s in key for s in PROZENT_KEYS)
    if isinstance(v, dict):
        return "; ".join(f"{k}: {num(x)} €" for k, x in v.items())
    if isinstance(v, list):
        return " / ".join(fmt_wert(x, key) for x in v)
    if prozent:
        return pct(v)
    if isinstance(v, float):
        return num(v, 2 if v < 100 else 0)
    return num(v)


def szenario_wert(key, name):
    return SZENARIEN[name].get(key, BASIS[key][0])


# ---------------------------------------------------------------------------
# 4. Markdown-Report
# ---------------------------------------------------------------------------

def report():
    L = []
    A = L.append
    ergebnisse = {}
    params = {}
    for name in ["pessimistisch", "realistisch", "optimistisch"]:
        p = basiswerte()
        p.update(copy.deepcopy(SZENARIEN[name]))
        params[name] = p
        ergebnisse[name] = lauf(p)

    A("# Szenariomodell externe Weiterbildungsakademie (10 FTE, Start Nov 2026)")
    A("")
    A("Erzeugt von `szenario_modell.py` (reines Python, Standardbibliothek). Alle Beträge netto in Euro, "
      "Planjahre laufen jeweils Nov–Okt (Jahr 1 = Nov 2026–Okt 2027). "
      "Das Modell ist eine transparente Grobplanung, keine Prognose: Die meisten Mengenannahmen sind "
      "eigene Setzungen, weil die Recherche keine Branchenkennzahlen zu Auslastung, Durchführungsquote, "
      "CAC oder Margen geliefert hat (siehe Warnhinweise am Ende).")
    A("")
    A("## 1. Annahmen")
    A("")
    A("Werte je Szenario (pessimistisch / realistisch / optimistisch). Leer = wie realistisch. "
      "Quelle verweist auf die Research-Notizen; „eigene Annahme“ = nicht quellenbelegt.")
    A("")
    A("| Parameter | Pessimistisch | Realistisch | Optimistisch | Einheit | Quelle / Markierung |")
    A("|---|---|---|---|---|---|")
    for key, (val, einheit, quelle) in BASIS.items():
        pe = SZENARIEN["pessimistisch"].get(key)
        op = SZENARIEN["optimistisch"].get(key)
        A(f"| `{key}` | {fmt_wert(pe, key) if pe is not None else ''} | {fmt_wert(val, key)} | {fmt_wert(op, key) if op is not None else ''} | {einheit} | {quelle} |")
    A("")
    A("Weitere Modellregeln (eigene Annahmen): Monatsverteilung der Jahresmengen mit Hochlauf in Jahr 1 "
      f"(Gewichte Nov–Okt: {', '.join(str(x) for x in GEWICHTE_J1)}) und Saisonalität ab Jahr 2 "
      f"({', '.join(str(x) for x in GEWICHTE_J2)}); Ankerkunde ab Jan 2027 gleichverteilt. "
      "Interne Trainerkapazität wird zuerst genutzt, nur darüber hinausgehende Tage werden mit Honorartrainern "
      "besetzt. Kumulierter Cash = kumuliertes EBIT (keine Zahlungsziele, Steuern, Investitionen/AfA, kein "
      "Working Capital). Abgesagte Termine verursachen im Modell keine Kosten (konservativ wäre: Marketing "
      "bereits ausgegeben).")
    A("")
    A("**Umsatzsteuer (§ 4 Nr. 21 UStG), nur qualitativ:** Mit Bescheinigung der Landesbehörde können "
      "berufliche Fortbildungsleistungen umsatzsteuerfrei sein. Für vorsteuerabzugsberechtigte B2B-Kunden "
      "(Kernzielgruppe) bringt das keinen Preisvorteil, kostet der Akademie aber den eigenen Vorsteuerabzug "
      "(Software, Räume, Honorare). Für B2C/Privatzahler wäre es ein Preisvorteil von bis zu 19 %. "
      "Bei umsatzsteuerlicher Organschaft mit der Muttergesellschaft gilt die Tochter als Teil des Organträgers. "
      "Das Modell rechnet netto und ohne diesen Effekt; Entscheidung mit Steuerberater (Quelle: "
      f"{Q_RECHT} §2).")
    A("")

    # ---- Ergebnisse je Szenario ----
    A("## 2. Ergebnisse je Szenario")
    A("")
    for name in ["pessimistisch", "realistisch", "optimistisch"]:
        e = ergebnisse[name]
        p = params[name]
        j = e["jahre"]
        A(f"### 2.{['pessimistisch', 'realistisch', 'optimistisch'].index(name) + 1} Szenario {name} "
          f"(Ankerkunde {pct(p['anker_anteil'])} der Kapazität)")
        A("")
        A("| Kennzahl | " + " | ".join(JAHRE) + " | Summe 3 Jahre |")
        A("|---|---|---|---|---|")
        rows = [
            ("Umsatz gesamt", "umsatz", eur, True),
            ("– davon offene Seminare", "umsatz_offen", eur, True),
            ("– davon Inhouse", "umsatz_inhouse", eur, True),
            ("– davon Zertifikatslehrgänge", "umsatz_lehrgang", eur, True),
            ("– davon Live-Online", "umsatz_online", eur, True),
            ("– davon E-Learning-Abo", "umsatz_elearning", eur, True),
            ("– davon Ankerkunde", "umsatz_anker", eur, True),
            ("Variable Kosten", "var_kosten", eur, True),
            ("Deckungsbeitrag (DB I)", "db", eur, True),
            ("DB-Marge", "db_marge", pct, False),
            ("Fixkosten", "fix_kosten", eur, True),
            ("– davon Personal (inkl. 31 % Aufschlag)", "k_personal", eur, True),
            ("EBIT", "ebit", eur, True),
            ("EBIT-Marge", "ebit_marge", pct, False),
            ("Kumulierter Cash (Jahresende)", "cash_kum", eur, False),
            ("Teilnehmende (offen + Lehrgang + Live-Online)", "tn", num, True),
            ("E-Learning-Lizenzen (Jahresende)", "lizenzen_elearning", num, False),
            ("Teilnehmer-Äquivalent Ankerkunde (12 TN/Tag)", "tn_anker", num, True),
            ("Umsatz je FTE", "umsatz_je_fte", lambda x: eur(x), False),
            ("Benötigte Durchführungstage gesamt", "tage", num, True),
            ("– davon intern besetzt", "tage_intern", num, True),
            ("– davon Honorartrainer", "tage_honorar", num, True),
        ]
        for label, key, f, summe in rows:
            vals = [f(jj[key]) for jj in j]
            if summe:
                tot = f(sum(jj[key] for jj in j))
            elif key == "cash_kum":
                tot = f(j[-1][key])
            elif key == "umsatz_je_fte":
                tot = f(sum(jj["umsatz"] for jj in j) / sum(jj["fte"] for jj in j))
            elif key in ("db_marge", "ebit_marge"):
                num_key = "db" if key == "db_marge" else "ebit"
                tot = f(sum(jj[num_key] for jj in j) / sum(jj["umsatz"] for jj in j))
            else:
                tot = f(j[-1][key])
            A(f"| {label} | " + " | ".join(vals) + f" | {tot} |")
        A("")
        A(f"- Break-even (erster Monat mit positivem EBIT, dessen folgende 12 Monate in Summe positiv sind): **{monat_label(e['be_monat_ebit'])}**")
        A(f"- Kumulierter Cash wieder ≥ 0: **{monat_label(e['be_monat_cash'])}**")
        A(f"- Maximaler Finanzierungsbedarf (tiefster kumulierter Cash): **{eur(e['finanzbedarf'])}**")
        A(f"- Ankerkunden-Tagessatz: {num(e['anker_tagessatz'])} €; ZFU-Gebühr je Fernlehrgang: {num(e['zfu_gebuehr'])} €")
        A("")
        # Kostenstruktur Jahr 3
        j3 = j[2]
        A(f"Kostenstruktur {JAHRE[2]}:")
        A("")
        A("| Kostenblock | Betrag | Anteil an Gesamtkosten |")
        A("|---|---|---|")
        bloecke = [
            ("Personal 10 FTE", "k_personal"), ("Honorartrainer + Reise", None),
            ("Räume + Catering/Unterlagen", None), ("Zertifikate/Badges + Content-Lizenzen", None),
            ("Vertrieb variabel (CAC)", "k_cac"), ("Marketing fix", "k_marketing_fix"),
            ("Plattform/Software", "k_software"), ("Zertifizierung (AZAV/ZFU/ISO)", "k_zertifizierung"),
            ("Recht/Steuer", "k_recht"), ("Overhead", "k_overhead"),
        ]
        gesamt = j3["var_kosten"] + j3["fix_kosten"]
        for label, key in bloecke:
            if key:
                v = j3[key]
            elif label.startswith("Honorar"):
                v = j3["k_honorar"] + j3["k_reise"]
            elif label.startswith("Räume"):
                v = j3["k_raum"] + j3["k_catering"]
            else:
                v = j3["k_zertifikat"] + j3["k_content"]
            A(f"| {label} | {eur(v)} | {pct(v / gesamt)} |")
        A(f"| **Gesamtkosten** | **{eur(gesamt)}** | 100 % |")
        A("")

    # ---- Break-even-TN je Format ----
    A("## 3. Break-even-Teilnehmende je Seminarformat (realistische Preise und Kosten)")
    A("")
    p = params["realistisch"]
    e = ergebnisse["realistisch"]
    fix_j3 = e["jahre"][2]["fix_kosten"]
    tage_j3 = e["jahre"][2]["tage"]
    umlage = fix_j3 / tage_j3 if tage_j3 else 0.0
    be_direkt = break_even_tn(p)
    be_voll = break_even_tn(p, umlage)
    A("Grenzkostenbetrachtung je Durchführung mit Honorartrainer: Break-even-TN = Fixkosten je Durchführung ÷ "
      "(Erlös je TN − variable Kosten je TN). „Vollkosten“ legt zusätzlich die Fixkosten des Jahres 3 "
      f"({eur(fix_j3)}) auf alle Durchführungstage ({num(tage_j3)} Tage) um = {num(umlage)} € je Tag.")
    A("")
    A("| Format | Erlös je TN | Var. Kosten je TN | Direkte Fixkosten je Durchführung | Break-even TN (direkt) | Break-even TN (Vollkosten) | Kapazität je Durchführung |")
    A("|---|---|---|---|---|---|---|")
    for fmt, (be, erl, var, fix, cap) in be_direkt.items():
        be_v = be_voll[fmt][0]
        A(f"| {fmt} | {num(erl)} € | {num(var)} € | {num(fix)} € | {num(be, 1)} | {num(be_v, 1)} | {cap} |")
    db_inhouse = p["preis_inhouse_tag"] - p["honorar_tagessatz"] - p["reise_je_trainertag"]
    A("")
    A(f"Inhouse-Training: DB je Tag mit Honorartrainer = {num(p['preis_inhouse_tag'])} − {num(p['honorar_tagessatz'] + p['reise_je_trainertag'])} = "
      f"**{num(db_inhouse)} €**; allein über Inhouse wären {num(fix_j3 / db_inhouse)} Honorartrainer-Tage p. a. zur Fixkostendeckung nötig "
      f"(mit internen Trainern entsprechend weniger: DB je Tag ≈ Tagessatz).")
    A("")

    # ---- Sensitivitäten ----
    A("## 4. Sensitivitäten (Basis: realistisches Szenario)")
    A("")
    sens = [
        ("Basis realistisch", {}),
        ("Auslastung −20 % (relativ)", {"auslastung_offen": 0.8, "auslastung_lehrgang": 0.8, "auslastung_online": 0.8}),
        ("Auslastung +20 % (relativ)", {"auslastung_offen": 1.2, "auslastung_lehrgang": 1.2, "auslastung_online": 1.2}),
        ("Preis −15 % (alle Formate)", {"preis_offen_tag": 0.85, "preis_inhouse_tag": 0.85, "preis_lehrgang": 0.85, "preis_online": 0.85, "preis_elearning_monat": 0.85}),
        ("Preis +15 % (alle Formate)", {"preis_offen_tag": 1.15, "preis_inhouse_tag": 1.15, "preis_lehrgang": 1.15, "preis_online": 1.15, "preis_elearning_monat": 1.15}),
        ("Trainerhonorar −20 %", {"honorar_tagessatz": 0.8}),
        ("Trainerhonorar +20 %", {"honorar_tagessatz": 1.2}),
        ("Ankerkunde nein (0 %)", {"anker_anteil": "0"}),
        ("Ankerkunde ja (30 %, = Basis)", {"anker_anteil": "0.3"}),
        ("Ankerkunde 50 %", {"anker_anteil": "0.5"}),
    ]
    A("| Variante | Umsatz J3 | EBIT J1 | EBIT J2 | EBIT J3 | Kum. Cash Ende J3 | Max. Finanzbedarf | Break-even-Monat (EBIT) | Δ EBIT J3 vs. Basis |")
    A("|---|---|---|---|---|---|---|---|---|")
    basis_ebit3 = ergebnisse["realistisch"]["jahre"][2]["ebit"]
    for label, mult in sens:
        p = basiswerte()
        for k, f in mult.items():
            if isinstance(f, str):
                p[k] = float(f)
            else:
                p[k] = p[k] * f
        r = lauf(p)
        j = r["jahre"]
        A(f"| {label} | {eur(j[2]['umsatz'])} | {eur(j[0]['ebit'])} | {eur(j[1]['ebit'])} | {eur(j[2]['ebit'])} | "
          f"{eur(j[2]['cash_kum'])} | {eur(r['finanzbedarf'])} | {monat_label(r['be_monat_ebit'])} | {eur(j[2]['ebit'] - basis_ebit3)} |")
    A("")
    # Kombi-Sensitivität: Preis und Auslastung gleichzeitig
    A("Kombinierte Sensitivität EBIT Jahr 3 (realistisch, Ankerkunde 30 %): Preis × Auslastung")
    A("")
    A("| Preis \\ Auslastung | −20 % | Basis | +20 % |")
    A("|---|---|---|---|")
    for pl, pf in [("−15 %", 0.85), ("Basis", 1.0), ("+15 %", 1.15)]:
        cells = []
        for af in [0.8, 1.0, 1.2]:
            p = basiswerte()
            for k in ["preis_offen_tag", "preis_inhouse_tag", "preis_lehrgang", "preis_online", "preis_elearning_monat"]:
                p[k] *= pf
            for k in ["auslastung_offen", "auslastung_lehrgang", "auslastung_online"]:
                p[k] *= af
            cells.append(eur(lauf(p)["jahre"][2]["ebit"]))
        A(f"| {pl} | " + " | ".join(cells) + " |")
    A("")

    # ---- Interpretation ----
    r_real, r_pess, r_opt = ergebnisse["realistisch"], ergebnisse["pessimistisch"], ergebnisse["optimistisch"]
    jr = r_real["jahre"]
    pers_anteil = jr[2]["k_personal"] / (jr[2]["var_kosten"] + jr[2]["fix_kosten"])
    anker_anteil_umsatz = jr[2]["umsatz_anker"] / jr[2]["umsatz"]
    A("## 5. Interpretation")
    A("")
    personal_voll = sum(p["gehaelter"].values()) * (1 + p["aufschlag_personal"])
    trainer_vollkosten = 72000 * (1 + p["aufschlag_personal"])
    A(f"1. **Der Personalblock bestimmt den Break-even.** 10 FTE kosten mit 31 % Aufschlag rund "
      f"{eur(personal_voll)} p. a. ab Vollbesetzung und machen im realistischen Jahr 3 {pct(pers_anteil)} der Gesamtkosten aus. "
      f"Dieser Block ist fix, bevor der erste Euro Umsatz fließt; deshalb liegt das EBIT in Jahr 1 in allen Szenarien deutlich negativ "
      f"({eur(r_pess['jahre'][0]['ebit'])} bis {eur(r_opt['jahre'][0]['ebit'])}).")
    A(f"2. **Realistisch wird der laufende Break-even erst {monat_label(r_real['be_monat_ebit'])} erreicht**, der kumulierte Cash ist Ende Jahr 3 bei "
      f"{eur(jr[2]['cash_kum'])}; der maximale Finanzierungsbedarf beträgt {eur(r_real['finanzbedarf'])}. "
      f"Pessimistisch (ohne Ankerkunde, −10 % Preise, −35 % Volumen) bleibt das EBIT alle drei Jahre negativ "
      f"(kum. {eur(r_pess['jahre'][2]['cash_kum'])}); optimistisch (50 % Ankerkunde) dreht das EBIT {monat_label(r_opt['be_monat_ebit'])}.")
    A(f"3. **Der Ankerkunde ist der größte einzelne Hebel.** Er liefert realistisch {pct(anker_anteil_umsatz)} des Umsatzes in Jahr 3 ohne "
      f"Vertriebskosten und ohne Ausfallrisiko; ohne ihn (Sensitivität „Ankerkunde nein“) verschiebt sich der Break-even über den Planungshorizont hinaus. "
      f"Umgekehrt ist das ein Klumpenrisiko: Die Akademie steht und fällt mit einem verbindlichen Mehrjahres-Kontingent der Muttergesellschaft.")
    A("4. **Inhouse-Trainings tragen den höchsten Deckungsbeitrag je Tag** (realistisch "
      f"{num(db_inhouse)} € mit Honorartrainer, nahezu der volle Tagessatz mit internen Trainern), weil Raum, Catering und Teilnehmerakquise entfallen und "
      "kein Mindest-TN-Risiko besteht. Offene Seminare sind dagegen das riskanteste Format: Bei 25 % Absagequote und 60 % Auslastung bleibt vom Listenpreis "
      "wenig übrig, obwohl der Break-even je Durchführung bei nur ~4 TN liegt.")
    A("5. **Preis wirkt stärker als Auslastung und Honorar.** ±15 % Preis verändern das EBIT in Jahr 3 um rund "
      f"±{eur(abs(lauf(dict(basiswerte(), **{k: basiswerte()[k] * 1.15 for k in ['preis_offen_tag', 'preis_inhouse_tag', 'preis_lehrgang', 'preis_online', 'preis_elearning_monat']}))['jahre'][2]['ebit'] - basis_ebit3))}, "
      "weil der Preis auf alle Erlösströme inkl. Ankerkunde durchschlägt; Auslastung betrifft nur die drei teilnehmerbasierten Formate, das Honorar nur die Tage über der internen Kapazität.")
    A("6. **Interne Trainerkapazität (330 Tage) ist der zweitwichtigste Kostenhebel.** Jeder Tag, den ein interner Trainer statt eines Honorartrainers hält, spart "
      f"{num(p['honorar_tagessatz'] + p['reise_je_trainertag'])} €; bei {num(jr[2]['tage_honorar'])} Honorartagen in Jahr 3 sind das "
      f"{eur(jr[2]['k_honorar'] + jr[2]['k_reise'])}. Eine vierte interne Trainerstelle (72 T€ Gehalt, {eur(trainer_vollkosten)} Vollkosten) rechnet sich ab etwa "
      f"{num(trainer_vollkosten / (p['honorar_tagessatz'] + p['reise_je_trainertag']))} ersetzten Honorartagen pro Jahr.")
    A("7. **Live-Online und E-Learning sind margenstark, aber klein.** Live-Online hat den niedrigsten Break-even (~2–3 TN), E-Learning ist nach Content-Lizenz "
      "noch zu 60 % Deckungsbeitrag, trägt aber realistisch nur einen einstelligen Prozentanteil zum Umsatz bei. Beide eignen sich als Lead-Magnet und Ergänzung, nicht als Fundament.")
    A("8. **Umsatz je FTE** liegt realistisch in Jahr 3 bei {0}; das ist für einen Seminaranbieter eher niedrig (Benchmark-Lücke, siehe Warnhinweise). "
      "Das deutet darauf hin, dass entweder das Team schlanker starten (6–8 FTE, Rest nach Nachweis der Nachfrage) oder die Hochlaufkurve durch ein Startkontingent steiler werden muss.".format(eur(jr[2]['umsatz_je_fte'])))
    A("")

    # ---- Warnhinweise ----
    A("## 6. Warnhinweise: schwach belegte Zahlen")
    A("")
    A("- **Volumen (Termine, Inhouse-Tage, Lehrgänge, E-Learning-Kunden) und Hochlaufkurve:** vollständig eigene Annahmen. Es gibt keine Benchmarks für Akademie-Neugründungen in Deutschland (produkt_delivery.md §6 Gaps).")
    A("- **Auslastung (60 %) und Absagequote (25 %):** keine Branchenwerte gefunden; nur AGB-Konventionen (Mindest-TN 3–10) und das Indiz der TÜV-NORD-Rabattaktion 2026 als Auslastungsdruck (wettbewerb_preise.md §3).")
    A("- **CAC-Werte:** abgeleitet aus US-lastigen Agentur-/Vendor-Benchmarks (CPL 70–150 €, Lead→Kunde low single digit); keine DACH-Daten für Trainingsanbieter (gtm_vertrieb.md §2 Gaps).")
    A("- **Ankerkunden-Volumen und -Preis (90 % des Marktpreises):** reine Setzung; ob die Muttergesellschaft 30–50 % der Kapazität verbindlich abnimmt, ist die wichtigste zu klärende Frage.")
    A("- **Personalkosten:** Gehälter aus Portalen (gehalt.de, StepStone) für Konzern-/Großstadtniveau; 31 % Aufschlag ist Faustregel ohne Quelle (team_rollen_budget.md §5).")
    A("- **Trainerhonorar 1.400 €/Tag:** managerSeminare-Honorarstudie ohne verifiziertes Erhebungsjahr; BDVT 2026 nennt ab 1.500–2.000 €. Zusätzlich Scheinselbstständigkeitsrisiko ab 2028 (§ 127 SGB IV läuft 31.12.2027 aus) – könnte Honorarmodell verteuern (produkt_delivery.md §4).")
    A("- **Zertifizierungskosten:** AZAV-Spanne 5.000–70.000 € ist Anbieterangabe; ISO-Kosten ohne Quelle; ZFU-Gebührenstand laut FIM-Portal ggf. veraltet (recht_zertifizierung_foerderung.md).")
    A("- **Preise:** teils nur aus Suchindex-Snippets (Haufe, BDEW), Direktabruf blockiert; vor Verwendung im Original verifizieren (wettbewerb_preise.md Methodik).")
    A("- **E-Learning:** Preis 5 €/Lizenz/Monat und 40 % Content-Lizenzkosten sind Setzungen; die Marktreferenz (Haufe 1,11–1,67 €) ist generischer Content, Reseller-Konditionen unbekannt.")
    A("- **Marktumfeld:** wbmonitor-Klima 2025 bei −4, McKinsey −24 % Weiterbildungsbudget pro Kopf 2026 (beides Snippets). Ein Markteintritt 2026/27 trifft auf einen Verdrängungsmarkt; das realistische Szenario unterstellt dennoch Hochlauf (markt_nachfrage.md §1).")
    A("- **Modellvereinfachungen:** Cash = EBIT (keine Zahlungsziele/Vorauszahlungen, keine Steuern, kein Capex), abgesagte Termine kostenlos, keine Preissteigerung über die Jahre, Ankerkunden-Teilnehmerzahl nur Statistik (12 TN/Tag).")
    A("")
    A("## 7. Monatsreihe realistisch (Kurzform)")
    A("")
    A("| Monat | Umsatz | Var. Kosten | Fixkosten | EBIT | Kum. Cash | Tage gesamt | davon Honorar |")
    A("|---|---|---|---|---|---|---|---|")
    rr = r_real["reihen"]
    for m in range(36):
        A(f"| {monat_label(m)} | {eur(rr['umsatz'][m])} | {eur(rr['var_kosten'][m])} | {eur(rr['fix_kosten'][m])} | {eur(rr['ebit'][m])} | {eur(rr['cash_kum'][m])} | {num(rr['tage'][m])} | {num(rr['tage_honorar'][m])} |")
    A("")
    return "\n".join(L), ergebnisse


def main():
    md, ergebnisse = report()
    if "--stdout" in sys.argv:
        sys.stdout.write(md)
        return
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "szenarien.md")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(md)
    # Kurzübersicht auf der Konsole
    for name, e in ergebnisse.items():
        j = e["jahre"]
        print(f"{name:14s} Umsatz J1/J2/J3: {eur(j[0]['umsatz'])} / {eur(j[1]['umsatz'])} / {eur(j[2]['umsatz'])} | "
              f"EBIT: {eur(j[0]['ebit'])} / {eur(j[1]['ebit'])} / {eur(j[2]['ebit'])} | kum. Cash J3: {eur(j[2]['cash_kum'])} | "
              f"Finanzbedarf: {eur(e['finanzbedarf'])} | BE: {monat_label(e['be_monat_ebit'])}")
    print(f"geschrieben: {out}")


if __name__ == "__main__":
    main()
