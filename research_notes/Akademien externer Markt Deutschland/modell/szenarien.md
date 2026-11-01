# Szenariomodell externe Weiterbildungsakademie (10 FTE, Start Nov 2026)

Erzeugt von `szenario_modell.py` (reines Python, Standardbibliothek). Alle Beträge netto in Euro, Planjahre laufen jeweils Nov–Okt (Jahr 1 = Nov 2026–Okt 2027). Das Modell ist eine transparente Grobplanung, keine Prognose: Die meisten Mengenannahmen sind eigene Setzungen, weil die Recherche keine Branchenkennzahlen zu Auslastung, Durchführungsquote, CAC oder Margen geliefert hat (siehe Warnhinweise am Ende).

## 1. Annahmen

Werte je Szenario (pessimistisch / realistisch / optimistisch). Leer = wie realistisch. Quelle verweist auf die Research-Notizen; „eigene Annahme“ = nicht quellenbelegt.

| Parameter | Pessimistisch | Realistisch | Optimistisch | Einheit | Quelle / Markierung |
|---|---|---|---|---|---|
| `preis_offen_tag` | 580 | 650 | 720 | € netto / TN / Tag | wettbewerb_preise.md: TÜV NORD 1-Tag 650–660 €, Inferenz-Korridor Energie-Fachseminar 550–700 €/Tag |
| `tage_offen` |  | 1,50 |  | Tage / Termin | eigene Annahme (Mix aus 1- und 2-Tages-Seminaren) |
| `max_tn_offen` |  | 12 |  | TN / Termin (Kapazität) | produkt_delivery.md: Obergrenze ~15 TN üblich; eigene Annahme 12 |
| `auslastung_offen` | 45 % | 60 % | 75 % | Anteil belegter Plätze | eigene Annahme; keine Branchenwerte gefunden (wettbewerb_preise.md Gaps) |
| `ausfall_offen` | 35 % | 25 % | 15 % | Anteil abgesagter Termine | eigene Annahme; AGB-Mindest-TN 3–10, keine Branchen-Durchführungsquote (wettbewerb_preise.md §3) |
| `termine_offen` | 26 / 49 / 65 | 40 / 75 / 100 | 52 / 98 / 130 | geplante Termine / Jahr | eigene Annahme (Hochlauf) |
| `preis_inhouse_tag` | 2.600 | 3.000 | 3.400 | € netto / Trainingstag | wettbewerb_preise.md: Inhouse-Gruppe 2.000–5.000 €/Tag; Beispiel 3.950 €/Tag |
| `inhouse_tage` | 39 / 85 / 130 | 60 / 130 / 200 | 78 / 170 / 260 | Trainingstage / Jahr | eigene Annahme (Hochlauf) |
| `tage_je_inhouse_kunde` |  | 4 |  | Tage / Kunde / Jahr | eigene Annahme |
| `neukundenanteil_inhouse` | 100 % / 70 % / 60 % | 100 % / 60 % / 50 % | 100 % / 50 % / 40 % | Anteil Neukunden an Inhouse-Kunden | eigene Annahme; keine Wiederbuchungsquoten gefunden (gtm_vertrieb.md §2) |
| `preis_lehrgang` | 2.100 | 2.400 | 2.700 | € netto / TN | wettbewerb_preise.md: TAE 5 Tage 2.100 €; Führungskraft (IHK) 1.595 € + 200 €; KI-Manager (IHK) 2.990 € |
| `tage_lehrgang` |  | 5 |  | Tage / Durchgang | wettbewerb_preise.md: TAE/TÜV 5-Tage-Formate |
| `max_tn_lehrgang` |  | 12 |  | TN / Durchgang | eigene Annahme |
| `auslastung_lehrgang` | 45 % | 60 % | 75 % | Anteil belegter Plätze | eigene Annahme |
| `ausfall_lehrgang` | 25 % | 15 % | 10 % | Anteil abgesagter Durchgänge | eigene Annahme |
| `lehrgaenge` | 1 / 3 / 5 | 2 / 5 / 8 | 3 / 7 / 10 | Durchgänge / Jahr | eigene Annahme; produkt_delivery.md §2: IHK-Lizenz dauert Monate |
| `zertifikat_je_tn` |  | 200 |  | € / TN (IHK-Zertifikat/Prüfung) | wettbewerb_preise.md: TA Bildungszentrum 200 € IHK-Zertifikat |
| `preis_online` | 300 | 350 | 400 | € netto / TN (Halbtag) | wettbewerb_preise.md: VfEW 320–370 € Online-Regulierungsseminar; Inferenz 300–400 € |
| `tage_online` |  | 0,50 |  | Tage / Termin | wettbewerb_preise.md: 2–4-h-Formate |
| `max_tn_online` |  | 25 |  | TN / Termin | eigene Annahme |
| `auslastung_online` | 40 % | 50 % | 60 % | Anteil belegter Plätze | eigene Annahme; gtm_vertrieb.md: Webinar-Teilnahmequote 40–60 % (Vendor) |
| `ausfall_online` | 30 % | 20 % | 10 % | Anteil abgesagter Termine | eigene Annahme |
| `termine_online` | 13 / 29 / 45 | 20 / 45 / 70 | 26 / 59 / 90 | Termine / Jahr | eigene Annahme |
| `preis_elearning_monat` | 3,00 | 5,00 | 7,00 | € / Lizenz / Monat | eigene Annahme; Referenz generische Flatrate Haufe 1,11–1,67 €/MA/Monat (wettbewerb_preise.md, gtm_vertrieb.md); Aufschlag für Branchencontent |
| `lizenzen_je_kunde` |  | 60 |  | Lizenzen / Firmenkunde | wettbewerb_preise.md: Haufe Mindestpaket 50 Lizenzen; eigene Annahme 60 |
| `kunden_elearning` | 2 / 6 / 12 | 3 / 10 / 20 | 4 / 14 / 28 | Firmenkunden (Jahresende) | eigene Annahme |
| `content_lizenz_anteil` |  | 40 % |  | Anteil Content-Lizenzkosten am E-Learning-Umsatz | eigene Annahme; keine Reseller-Margen gefunden (produkt_delivery.md §3) |
| `anker_anteil` | 0 % | 30 % | 50 % | Anteil der Kapazität (0 / 30 / 50 %) | Parameter lt. Auftrag; Szenario-Zuordnung eigene Annahme |
| `kapazitaet_tage` |  | 300 / 500 / 650 |  | Durchführungstage Kapazität / Jahr | eigene Annahme: interne Trainer + Honorarpool |
| `anker_preisfaktor` |  | 0,90 |  | Faktor auf Inhouse-Tagessatz (Konzernverrechnung) | eigene Annahme; wettbewerb_preise.md: Mitglieder-/Konzernrabatte 10–20 % üblich |
| `gehaelter` |  | Leitung Akademie: 100.000 €; Key Account / Vertrieb (2): 140.000 €; Marketing / Content: 58.000 €; Produktmanagement / Learning Architect: 75.000 €; Seminarorganisation / Backoffice (2): 96.000 €; Interne Trainer:innen / Fachexpert:innen (3): 216.000 € |  | € Brutto-Jahresgehälter, 10 FTE (Summe 685.000 €) | team_rollen_budget.md §5 Planwerte (Leitung 100k, Architect 75k, PM 62k, ID 60k…); Rollenmix für externen Markt eigene Annahme |
| `aufschlag_personal` |  | 31 % |  | Aufschlag auf Bruttogehalt (AG-SV + Gemeinkosten) | team_rollen_budget.md §5: +21 % SV + ~10 % Gemeinkosten (Faustregel, nicht quellenbelegt) |
| `gehaltssteigerung` |  | 3 % |  | p. a. | eigene Annahme |
| `fte_hochlauf` |  | 6 / 8 / 10 |  | FTE in Nov / Dez 2026 / ab Jan 2027 | eigene Annahme |
| `interne_trainertage` |  | 330 |  | Durchführungstage / Jahr (3 interne Trainer × 110) | eigene Annahme; team_rollen_budget.md §6: Skalierung über Faculty/Pool statt FTE |
| `honorar_tagessatz` | 1.500 | 1.400 | 1.300 | € / Tag (inkl. Vorbereitung) | wettbewerb_preise.md/team_rollen_budget.md: managerSeminare Ø 1.357 €/Tag; BDVT 2026 ab 1.500 € |
| `reise_je_trainertag` |  | 150 |  | € / Honorartrainertag | wettbewerb_preise.md: Reisepauschale 200 € je Einsatz (Anbieterbeispiel); eigene Annahme 150 |
| `raum_je_tag` |  | 600 |  | € / Seminartag (offen, Lehrgang) | wettbewerb_preise.md §3 Inferenz: Raum/Technik 800–1.500 € je 2-Tages-Seminar |
| `catering_je_tn_tag` |  | 70 |  | € / TN / Präsenztag (Catering, Unterlagen) | wettbewerb_preise.md §3: 100–150 €/TN/Tag inkl. Raumanteil; team_rollen_budget.md: 130 € Raum+Verpflegung; eigene Annahme 70 ohne Raum |
| `badge_je_tn` |  | 15 |  | € / TN (Teilnahmebescheinigung/Open Badge) | eigene Annahme |
| `material_online_je_tn` |  | 10 |  | € / TN Live-Online | eigene Annahme |
| `cac_offen_je_tn` |  | 120 |  | € / Teilnehmer:in offenes Seminar | eigene Annahme; gtm_vertrieb.md §2: CPL 70–150 € (LinkedIn, Agentur), Portale/SEA |
| `cac_inhouse_je_neukunde` |  | 3.000 |  | € / Inhouse-Neukunde | eigene Annahme: CPL ~100 € ÷ Lead→Kunde ~3,5 % (gtm_vertrieb.md §2 Rechenbeispiel) |
| `cac_lehrgang_je_tn` |  | 200 |  | € / Lehrgangs-TN | eigene Annahme |
| `cac_online_je_tn` |  | 40 |  | € / Live-Online-TN | eigene Annahme |
| `cac_elearning_je_kunde` |  | 1.500 |  | € / E-Learning-Firmenkunde | eigene Annahme |
| `marketing_fix` |  | 120.000 / 100.000 / 100.000 |  | € / Jahr (Website, Content, Webinare, Messen, Verbände) | eigene Annahme; gtm_vertrieb.md §1/§6: Thought Leadership, Verbände, Ausschreibungen |
| `software_jahr` |  | 48.000 |  | € / Jahr (Seminarverwaltung, LMS, Webinar-Tool, CRM, Badges) | produkt_delivery.md §5: 'low hundreds to low thousands €/Monat' (Inferenz); eigene Annahme 4.000 €/Monat |
| `software_setup` |  | 25.000 |  | € einmalig (Jahr 1) | eigene Annahme |
| `azav_erst` |  | 12.000 |  | € einmalig Trägerzulassung + QM-Aufbau (Jahr 1) | recht_zertifizierung_foerderung.md §5: AZAV gesamt 5.000–70.000 € (Anbieterangabe); eigene Annahme unteres Drittel |
| `azav_jahr` |  | 3.000 |  | € / Jahr Überwachung (ab Jahr 2) | eigene Annahme |
| `azav_massnahme_je` |  | 1.500 |  | € je Maßnahmenzulassung | eigene Annahme |
| `lehrgangsprodukte_neu` |  | 2 / 2 / 1 |  | neue Lehrgangsprodukte / Jahr (AZAV-Maßnahmen) | eigene Annahme |
| `zfu_kurse_neu` |  | 1 / 2 / 1 |  | ZFU-pflichtige Fernlehrgänge neu / Jahr | eigene Annahme; recht_zertifizierung_foerderung.md §3: nur asynchrone Kurse mit Lernerfolgskontrolle |
| `zfu_gebuehr_faktor` |  | 1,50 |  | × Kurspreis, min. 1.050 € | Vorgabe Auftrag; recht_zertifizierung_foerderung.md §3 (FIM-Portal, Gebührenstand ggf. veraltet) |
| `zfu_gebuehr_min` |  | 1.050 |  | € | Vorgabe Auftrag; recht_zertifizierung_foerderung.md §3 |
| `iso_erst` |  | 10.000 |  | € einmalig ISO 9001/21001 Erstzertifizierung inkl. Beratung (Jahr 1) | eigene Annahme; keine Quelle (recht_zertifizierung_foerderung.md Gaps) |
| `iso_jahr` |  | 3.000 |  | € / Jahr Überwachungsaudit (ab Jahr 2) | eigene Annahme |
| `recht_steuer` |  | 30.000 / 20.000 / 20.000 |  | € / Jahr (Gründung, AGB, § 127 SGB IV, § 4 Nr. 21 UStG, Buchhaltung) | eigene Annahme; recht_zertifizierung_foerderung.md, produkt_delivery.md §4 |
| `overhead` |  | 60.000 / 60.000 / 60.000 |  | € / Jahr (Versicherung, Reisen Vertrieb, Sonstiges) | eigene Annahme |
| `aufbau_einmalig` |  | 40.000 |  | € einmalig (Marke, Website, Erstproduktion Content) | eigene Annahme |

Weitere Modellregeln (eigene Annahmen): Monatsverteilung der Jahresmengen mit Hochlauf in Jahr 1 (Gewichte Nov–Okt: 0.0, 0.1, 0.3, 0.5, 0.7, 0.8, 0.9, 1.0, 0.9, 0.5, 1.2, 1.3) und Saisonalität ab Jahr 2 (1.1, 0.6, 1.0, 1.1, 1.2, 1.0, 1.1, 1.1, 0.9, 0.5, 1.2, 1.1); Ankerkunde ab Jan 2027 gleichverteilt. Interne Trainerkapazität wird zuerst genutzt, nur darüber hinausgehende Tage werden mit Honorartrainern besetzt. Kumulierter Cash = kumuliertes EBIT (keine Zahlungsziele, Steuern, Investitionen/AfA, kein Working Capital). Abgesagte Termine verursachen im Modell keine Kosten (konservativ wäre: Marketing bereits ausgegeben).

**Umsatzsteuer (§ 4 Nr. 21 UStG), nur qualitativ:** Mit Bescheinigung der Landesbehörde können berufliche Fortbildungsleistungen umsatzsteuerfrei sein. Für vorsteuerabzugsberechtigte B2B-Kunden (Kernzielgruppe) bringt das keinen Preisvorteil, kostet der Akademie aber den eigenen Vorsteuerabzug (Software, Räume, Honorare). Für B2C/Privatzahler wäre es ein Preisvorteil von bis zu 19 %. Bei umsatzsteuerlicher Organschaft mit der Muttergesellschaft gilt die Tochter als Teil des Organträgers. Das Modell rechnet netto und ohne diesen Effekt; Entscheidung mit Steuerberater (Quelle: recht_zertifizierung_foerderung.md §2).

## 2. Ergebnisse je Szenario

### 2.1 Szenario pessimistisch (Ankerkunde 0 % der Kapazität)

| Kennzahl | Jahr 1 (Nov 26–Okt 27) | Jahr 2 (Nov 27–Okt 28) | Jahr 3 (Nov 28–Okt 29) | Summe 3 Jahre |
|---|---|---|---|---|
| Umsatz gesamt | 219 T€ | 466 T€ | 693 T€ | 1.378 T€ |
| – davon offene Seminare | 79 T€ | 150 T€ | 198 T€ | 428 T€ |
| – davon Inhouse | 101 T€ | 221 T€ | 338 T€ | 660 T€ |
| – davon Zertifikatslehrgänge | 9 T€ | 26 T€ | 43 T€ | 77 T€ |
| – davon Live-Online | 27 T€ | 61 T€ | 94 T€ | 183 T€ |
| – davon E-Learning-Abo | 2 T€ | 9 T€ | 20 T€ | 31 T€ |
| – davon Ankerkunde | 0 T€ | 0 T€ | 0 T€ | 0 T€ |
| Variable Kosten | 80 T€ | 150 T€ | 210 T€ | 440 T€ |
| Deckungsbeitrag (DB I) | 139 T€ | 316 T€ | 483 T€ | 938 T€ |
| DB-Marge | 64 % | 68 % | 70 % | 68 % |
| Fixkosten | 1.204 T€ | 1.168 T€ | 1.191 T€ | 3.562 T€ |
| – davon Personal (inkl. 31 % Aufschlag) | 852 T€ | 924 T€ | 952 T€ | 2.729 T€ |
| EBIT | -1.064 T€ | -852 T€ | -708 T€ | -2.624 T€ |
| EBIT-Marge | -486 % | -183 % | -102 % | -190 % |
| Kumulierter Cash (Jahresende) | -1.064 T€ | -1.916 T€ | -2.624 T€ | -2.624 T€ |
| Teilnehmende (offen + Lehrgang + Live-Online) | 186 | 387 | 563 | 1.137 |
| E-Learning-Lizenzen (Jahresende) | 120 | 360 | 720 | 720 |
| Teilnehmer-Äquivalent Ankerkunde (12 TN/Tag) | 0 | 0 | 0 | 0 |
| Umsatz je FTE | 23 T€ | 47 T€ | 69 T€ | 47 T€ |
| Benötigte Durchführungstage gesamt | 73 | 154 | 228 | 455 |
| – davon intern besetzt | 73 | 154 | 228 | 455 |
| – davon Honorartrainer | 0 | 0 | 0 | 0 |

- Break-even (erster Monat mit positivem EBIT, dessen folgende 12 Monate in Summe positiv sind): **nicht innerhalb von 36 Monaten**
- Kumulierter Cash wieder ≥ 0: **nicht innerhalb von 36 Monaten**
- Maximaler Finanzierungsbedarf (tiefster kumulierter Cash): **2.624 T€**
- Ankerkunden-Tagessatz: 2.340 €; ZFU-Gebühr je Fernlehrgang: 3.150 €

Kostenstruktur Jahr 3 (Nov 28–Okt 29):

| Kostenblock | Betrag | Anteil an Gesamtkosten |
|---|---|---|
| Personal 10 FTE | 952 T€ | 68 % |
| Honorartrainer + Reise | 0 T€ | 0 % |
| Räume + Catering/Unterlagen | 80 T€ | 6 % |
| Zertifikate/Badges + Content-Lizenzen | 19 T€ | 1 % |
| Vertrieb variabel (CAC) | 112 T€ | 8 % |
| Marketing fix | 100 T€ | 7 % |
| Plattform/Software | 48 T€ | 3 % |
| Zertifizierung (AZAV/ZFU/ISO) | 11 T€ | 1 % |
| Recht/Steuer | 20 T€ | 1 % |
| Overhead | 60 T€ | 4 % |
| **Gesamtkosten** | **1.401 T€** | 100 % |

### 2.2 Szenario realistisch (Ankerkunde 30 % der Kapazität)

| Kennzahl | Jahr 1 (Nov 26–Okt 27) | Jahr 2 (Nov 27–Okt 28) | Jahr 3 (Nov 28–Okt 29) | Summe 3 Jahre |
|---|---|---|---|---|
| Umsatz gesamt | 739 T€ | 1.445 T€ | 2.071 T€ | 4.255 T€ |
| – davon offene Seminare | 211 T€ | 395 T€ | 526 T€ | 1.132 T€ |
| – davon Inhouse | 180 T€ | 390 T€ | 600 T€ | 1.170 T€ |
| – davon Zertifikatslehrgänge | 29 T€ | 73 T€ | 118 T€ | 220 T€ |
| – davon Live-Online | 70 T€ | 158 T€ | 245 T€ | 473 T€ |
| – davon E-Learning-Abo | 6 T€ | 24 T€ | 56 T€ | 86 T€ |
| – davon Ankerkunde | 243 T€ | 405 T€ | 526 T€ | 1.174 T€ |
| Variable Kosten | 155 T€ | 426 T€ | 778 T€ | 1.360 T€ |
| Deckungsbeitrag (DB I) | 583 T€ | 1.019 T€ | 1.293 T€ | 2.895 T€ |
| DB-Marge | 79 % | 71 % | 62 % | 68 % |
| Fixkosten | 1.204 T€ | 1.168 T€ | 1.191 T€ | 3.564 T€ |
| – davon Personal (inkl. 31 % Aufschlag) | 852 T€ | 924 T€ | 952 T€ | 2.729 T€ |
| EBIT | -621 T€ | -150 T€ | 102 T€ | -669 T€ |
| EBIT-Marge | -84 % | -10 % | 5 % | -16 % |
| Kumulierter Cash (Jahresende) | -621 T€ | -770 T€ | -669 T€ | -669 T€ |
| Teilnehmende (offen + Lehrgang + Live-Online) | 428 | 886 | 1.289 | 2.603 |
| E-Learning-Lizenzen (Jahresende) | 180 | 600 | 1.200 | 1.200 |
| Teilnehmer-Äquivalent Ankerkunde (12 TN/Tag) | 1.080 | 1.800 | 2.340 | 5.220 |
| Umsatz je FTE | 78 T€ | 145 T€ | 207 T€ | 144 T€ |
| Benötigte Durchführungstage gesamt | 212 | 404 | 569 | 1.185 |
| – davon intern besetzt | 211 | 312 | 326 | 849 |
| – davon Honorartrainer | 1 | 91 | 243 | 335 |

- Break-even (erster Monat mit positivem EBIT, dessen folgende 12 Monate in Summe positiv sind): **Monat 25 (Nov 2028)**
- Kumulierter Cash wieder ≥ 0: **nicht innerhalb von 36 Monaten**
- Maximaler Finanzierungsbedarf (tiefster kumulierter Cash): **772 T€**
- Ankerkunden-Tagessatz: 2.700 €; ZFU-Gebühr je Fernlehrgang: 3.600 €

Kostenstruktur Jahr 3 (Nov 28–Okt 29):

| Kostenblock | Betrag | Anteil an Gesamtkosten |
|---|---|---|
| Personal 10 FTE | 952 T€ | 48 % |
| Honorartrainer + Reise | 377 T€ | 19 % |
| Räume + Catering/Unterlagen | 162 T€ | 8 % |
| Zertifikate/Badges + Content-Lizenzen | 47 T€ | 2 % |
| Vertrieb variabel (CAC) | 193 T€ | 10 % |
| Marketing fix | 100 T€ | 5 % |
| Plattform/Software | 48 T€ | 2 % |
| Zertifizierung (AZAV/ZFU/ISO) | 11 T€ | 1 % |
| Recht/Steuer | 20 T€ | 1 % |
| Overhead | 60 T€ | 3 % |
| **Gesamtkosten** | **1.969 T€** | 100 % |

### 2.3 Szenario optimistisch (Ankerkunde 50 % der Kapazität)

| Kennzahl | Jahr 1 (Nov 26–Okt 27) | Jahr 2 (Nov 27–Okt 28) | Jahr 3 (Nov 28–Okt 29) | Summe 3 Jahre |
|---|---|---|---|---|
| Umsatz gesamt | 1.370 T€ | 2.672 T€ | 3.766 T€ | 7.808 T€ |
| – davon offene Seminare | 430 T€ | 810 T€ | 1.074 T€ | 2.313 T€ |
| – davon Inhouse | 265 T€ | 578 T€ | 884 T€ | 1.727 T€ |
| – davon Zertifikatslehrgänge | 66 T€ | 153 T€ | 219 T€ | 437 T€ |
| – davon Live-Online | 140 T€ | 319 T€ | 486 T€ | 945 T€ |
| – davon E-Learning-Abo | 10 T€ | 47 T€ | 109 T€ | 167 T€ |
| – davon Ankerkunde | 459 T€ | 765 T€ | 994 T€ | 2.218 T€ |
| Variable Kosten | 324 T€ | 853 T€ | 1.363 T€ | 2.540 T€ |
| Deckungsbeitrag (DB I) | 1.047 T€ | 1.819 T€ | 2.403 T€ | 5.268 T€ |
| DB-Marge | 76 % | 68 % | 64 % | 67 % |
| Fixkosten | 1.205 T€ | 1.169 T€ | 1.192 T€ | 3.565 T€ |
| – davon Personal (inkl. 31 % Aufschlag) | 852 T€ | 924 T€ | 952 T€ | 2.729 T€ |
| EBIT | -158 T€ | 650 T€ | 1.211 T€ | 1.703 T€ |
| EBIT-Marge | -12 % | 24 % | 32 % | 22 % |
| Kumulierter Cash (Jahresende) | -158 T€ | 492 T€ | 1.703 T€ | 1.703 T€ |
| Teilnehmende (offen + Lehrgang + Live-Online) | 773 | 1.603 | 2.290 | 4.666 |
| E-Learning-Lizenzen (Jahresende) | 240 | 840 | 1.680 | 1.680 |
| Teilnehmer-Äquivalent Ankerkunde (12 TN/Tag) | 1.800 | 3.000 | 3.900 | 8.700 |
| Umsatz je FTE | 144 T€ | 267 T€ | 377 T€ | 265 T€ |
| Benötigte Durchführungstage gesamt | 320 | 603 | 836 | 1.759 |
| – davon intern besetzt | 266 | 328 | 330 | 924 |
| – davon Honorartrainer | 53 | 275 | 506 | 834 |

- Break-even (erster Monat mit positivem EBIT, dessen folgende 12 Monate in Summe positiv sind): **Monat 5 (Mär 2027)**
- Kumulierter Cash wieder ≥ 0: **Monat 16 (Feb 2028)**
- Maximaler Finanzierungsbedarf (tiefster kumulierter Cash): **255 T€**
- Ankerkunden-Tagessatz: 3.060 €; ZFU-Gebühr je Fernlehrgang: 4.050 €

Kostenstruktur Jahr 3 (Nov 28–Okt 29):

| Kostenblock | Betrag | Anteil an Gesamtkosten |
|---|---|---|
| Personal 10 FTE | 952 T€ | 37 % |
| Honorartrainer + Reise | 734 T€ | 29 % |
| Räume + Catering/Unterlagen | 259 T€ | 10 % |
| Zertifikate/Badges + Content-Lizenzen | 87 T€ | 3 % |
| Vertrieb variabel (CAC) | 283 T€ | 11 % |
| Marketing fix | 100 T€ | 4 % |
| Plattform/Software | 48 T€ | 2 % |
| Zertifizierung (AZAV/ZFU/ISO) | 12 T€ | 0 % |
| Recht/Steuer | 20 T€ | 1 % |
| Overhead | 60 T€ | 2 % |
| **Gesamtkosten** | **2.555 T€** | 100 % |

## 3. Break-even-Teilnehmende je Seminarformat (realistische Preise und Kosten)

Grenzkostenbetrachtung je Durchführung mit Honorartrainer: Break-even-TN = Fixkosten je Durchführung ÷ (Erlös je TN − variable Kosten je TN). „Vollkosten“ legt zusätzlich die Fixkosten des Jahres 3 (1.191 T€) auf alle Durchführungstage (569 Tage) um = 2.091 € je Tag.

| Format | Erlös je TN | Var. Kosten je TN | Direkte Fixkosten je Durchführung | Break-even TN (direkt) | Break-even TN (Vollkosten) | Kapazität je Durchführung |
|---|---|---|---|---|---|---|
| Offenes Seminar (1,5 Tage) | 975 € | 240 € | 3.225 € | 4,4 | 8,7 | 12 |
| Zertifikatslehrgang (5 Tage) | 2.400 € | 750 € | 10.750 € | 6,5 | 12,9 | 12 |
| Live-Online (Halbtag) | 350 € | 50 € | 775 € | 2,6 | 6,1 | 25 |

Inhouse-Training: DB je Tag mit Honorartrainer = 3.000 − 1.550 = **1.450 €**; allein über Inhouse wären 821 Honorartrainer-Tage p. a. zur Fixkostendeckung nötig (mit internen Trainern entsprechend weniger: DB je Tag ≈ Tagessatz).

## 4. Sensitivitäten (Basis: realistisches Szenario)

| Variante | Umsatz J3 | EBIT J1 | EBIT J2 | EBIT J3 | Kum. Cash Ende J3 | Max. Finanzbedarf | Break-even-Monat (EBIT) | Δ EBIT J3 vs. Basis |
|---|---|---|---|---|---|---|---|---|
| Basis realistisch | 2.071 T€ | -621 T€ | -150 T€ | 102 T€ | -669 T€ | 772 T€ | Monat 25 (Nov 2028) | 0 T€ |
| Auslastung −20 % (relativ) | 1.893 T€ | -669 T€ | -246 T€ | -36 T€ | -951 T€ | 964 T€ | nicht innerhalb von 36 Monaten | -138 T€ |
| Auslastung +20 % (relativ) | 2.249 T€ | -573 T€ | -53 T€ | 239 T€ | -387 T€ | 639 T€ | Monat 16 (Feb 2028) | 138 T€ |
| Preis −15 % (alle Formate) | 1.760 T€ | -731 T€ | -364 T€ | -205 T€ | -1.300 T€ | 1.300 T€ | nicht innerhalb von 36 Monaten | -307 T€ |
| Preis +15 % (alle Formate) | 2.382 T€ | -511 T€ | 65 T€ | 409 T€ | -38 T€ | 526 T€ | Monat 13 (Nov 2027) | 307 T€ |
| Trainerhonorar −20 % | 2.071 T€ | -621 T€ | -124 T€ | 170 T€ | -575 T€ | 746 T€ | Monat 23 (Sep 2028) | 68 T€ |
| Trainerhonorar +20 % | 2.071 T€ | -621 T€ | -175 T€ | 34 T€ | -762 T€ | 805 T€ | Monat 25 (Nov 2028) | -68 T€ |
| Ankerkunde nein (0 %) | 1.545 T€ | -863 T€ | -413 T€ | -149 T€ | -1.424 T€ | 1.424 T€ | nicht innerhalb von 36 Monaten | -250 T€ |
| Ankerkunde ja (30 %, = Basis) | 2.071 T€ | -621 T€ | -150 T€ | 102 T€ | -669 T€ | 772 T€ | Monat 25 (Nov 2028) | 0 T€ |
| Ankerkunde 50 % | 2.422 T€ | -482 T€ | -20 T€ | 257 T€ | -246 T€ | 520 T€ | Monat 16 (Feb 2028) | 155 T€ |

Kombinierte Sensitivität EBIT Jahr 3 (realistisch, Ankerkunde 30 %): Preis × Auslastung

| Preis \ Auslastung | −20 % | Basis | +20 % |
|---|---|---|---|
| −15 % | -316 T€ | -205 T€ | -94 T€ |
| Basis | -36 T€ | 102 T€ | 239 T€ |
| +15 % | 244 T€ | 409 T€ | 573 T€ |

## 5. Interpretation

1. **Der Personalblock bestimmt den Break-even.** 10 FTE kosten mit 31 % Aufschlag rund 897 T€ p. a. ab Vollbesetzung und machen im realistischen Jahr 3 48 % der Gesamtkosten aus. Dieser Block ist fix, bevor der erste Euro Umsatz fließt; deshalb liegt das EBIT in Jahr 1 in allen Szenarien deutlich negativ (-1.064 T€ bis -158 T€).
2. **Realistisch wird der laufende Break-even erst Monat 25 (Nov 2028) erreicht**, der kumulierte Cash ist Ende Jahr 3 bei -669 T€; der maximale Finanzierungsbedarf beträgt 772 T€. Pessimistisch (ohne Ankerkunde, −10 % Preise, −35 % Volumen) bleibt das EBIT alle drei Jahre negativ (kum. -2.624 T€); optimistisch (50 % Ankerkunde) dreht das EBIT Monat 5 (Mär 2027).
3. **Der Ankerkunde ist der größte einzelne Hebel.** Er liefert realistisch 25 % des Umsatzes in Jahr 3 ohne Vertriebskosten und ohne Ausfallrisiko; ohne ihn (Sensitivität „Ankerkunde nein“) verschiebt sich der Break-even über den Planungshorizont hinaus. Umgekehrt ist das ein Klumpenrisiko: Die Akademie steht und fällt mit einem verbindlichen Mehrjahres-Kontingent der Muttergesellschaft.
4. **Inhouse-Trainings tragen den höchsten Deckungsbeitrag je Tag** (realistisch 1.450 € mit Honorartrainer, nahezu der volle Tagessatz mit internen Trainern), weil Raum, Catering und Teilnehmerakquise entfallen und kein Mindest-TN-Risiko besteht. Offene Seminare sind dagegen das riskanteste Format: Bei 25 % Absagequote und 60 % Auslastung bleibt vom Listenpreis wenig übrig, obwohl der Break-even je Durchführung bei nur ~4 TN liegt.
5. **Preis wirkt stärker als Auslastung und Honorar.** ±15 % Preis verändern das EBIT in Jahr 3 um rund ±307 T€, weil der Preis auf alle Erlösströme inkl. Ankerkunde durchschlägt; Auslastung betrifft nur die drei teilnehmerbasierten Formate, das Honorar nur die Tage über der internen Kapazität.
6. **Interne Trainerkapazität (330 Tage) ist der zweitwichtigste Kostenhebel.** Jeder Tag, den ein interner Trainer statt eines Honorartrainers hält, spart 1.550 €; bei 243 Honorartagen in Jahr 3 sind das 377 T€. Eine vierte interne Trainerstelle (72 T€ Gehalt, 94 T€ Vollkosten) rechnet sich ab etwa 61 ersetzten Honorartagen pro Jahr.
7. **Live-Online und E-Learning sind margenstark, aber klein.** Live-Online hat den niedrigsten Break-even (~2–3 TN), E-Learning ist nach Content-Lizenz noch zu 60 % Deckungsbeitrag, trägt aber realistisch nur einen einstelligen Prozentanteil zum Umsatz bei. Beide eignen sich als Lead-Magnet und Ergänzung, nicht als Fundament.
8. **Umsatz je FTE** liegt realistisch in Jahr 3 bei 207 T€; das ist für einen Seminaranbieter eher niedrig (Benchmark-Lücke, siehe Warnhinweise). Das deutet darauf hin, dass entweder das Team schlanker starten (6–8 FTE, Rest nach Nachweis der Nachfrage) oder die Hochlaufkurve durch ein Startkontingent steiler werden muss.

## 6. Warnhinweise: schwach belegte Zahlen

- **Volumen (Termine, Inhouse-Tage, Lehrgänge, E-Learning-Kunden) und Hochlaufkurve:** vollständig eigene Annahmen. Es gibt keine Benchmarks für Akademie-Neugründungen in Deutschland (produkt_delivery.md §6 Gaps).
- **Auslastung (60 %) und Absagequote (25 %):** keine Branchenwerte gefunden; nur AGB-Konventionen (Mindest-TN 3–10) und das Indiz der TÜV-NORD-Rabattaktion 2026 als Auslastungsdruck (wettbewerb_preise.md §3).
- **CAC-Werte:** abgeleitet aus US-lastigen Agentur-/Vendor-Benchmarks (CPL 70–150 €, Lead→Kunde low single digit); keine DACH-Daten für Trainingsanbieter (gtm_vertrieb.md §2 Gaps).
- **Ankerkunden-Volumen und -Preis (90 % des Marktpreises):** reine Setzung; ob die Muttergesellschaft 30–50 % der Kapazität verbindlich abnimmt, ist die wichtigste zu klärende Frage.
- **Personalkosten:** Gehälter aus Portalen (gehalt.de, StepStone) für Konzern-/Großstadtniveau; 31 % Aufschlag ist Faustregel ohne Quelle (team_rollen_budget.md §5).
- **Trainerhonorar 1.400 €/Tag:** managerSeminare-Honorarstudie ohne verifiziertes Erhebungsjahr; BDVT 2026 nennt ab 1.500–2.000 €. Zusätzlich Scheinselbstständigkeitsrisiko ab 2028 (§ 127 SGB IV läuft 31.12.2027 aus) – könnte Honorarmodell verteuern (produkt_delivery.md §4).
- **Zertifizierungskosten:** AZAV-Spanne 5.000–70.000 € ist Anbieterangabe; ISO-Kosten ohne Quelle; ZFU-Gebührenstand laut FIM-Portal ggf. veraltet (recht_zertifizierung_foerderung.md).
- **Preise:** teils nur aus Suchindex-Snippets (Haufe, BDEW), Direktabruf blockiert; vor Verwendung im Original verifizieren (wettbewerb_preise.md Methodik).
- **E-Learning:** Preis 5 €/Lizenz/Monat und 40 % Content-Lizenzkosten sind Setzungen; die Marktreferenz (Haufe 1,11–1,67 €) ist generischer Content, Reseller-Konditionen unbekannt.
- **Marktumfeld:** wbmonitor-Klima 2025 bei −4, McKinsey −24 % Weiterbildungsbudget pro Kopf 2026 (beides Snippets). Ein Markteintritt 2026/27 trifft auf einen Verdrängungsmarkt; das realistische Szenario unterstellt dennoch Hochlauf (markt_nachfrage.md §1).
- **Modellvereinfachungen:** Cash = EBIT (keine Zahlungsziele/Vorauszahlungen, keine Steuern, kein Capex), abgesagte Termine kostenlos, keine Preissteigerung über die Jahre, Ankerkunden-Teilnehmerzahl nur Statistik (12 TN/Tag).

## 7. Monatsreihe realistisch (Kurzform)

| Monat | Umsatz | Var. Kosten | Fixkosten | EBIT | Kum. Cash | Tage gesamt | davon Honorar |
|---|---|---|---|---|---|---|---|
| Monat 1 (Nov 2026) | 0 T€ | 0 T€ | 105 T€ | -105 T€ | -105 T€ | 0 | 0 |
| Monat 2 (Dez 2026) | 6 T€ | 2 T€ | 95 T€ | -91 T€ | -196 T€ | 1 | 0 |
| Monat 3 (Jan 2027) | 42 T€ | 6 T€ | 122 T€ | -86 T€ | -282 T€ | 13 | 0 |
| Monat 4 (Feb 2027) | 54 T€ | 10 T€ | 97 T€ | -52 T€ | -334 T€ | 16 | 0 |
| Monat 5 (Mär 2027) | 67 T€ | 13 T€ | 97 T€ | -43 T€ | -377 T€ | 19 | 0 |
| Monat 6 (Apr 2027) | 73 T€ | 15 T€ | 107 T€ | -49 T€ | -427 T€ | 21 | 0 |
| Monat 7 (Mai 2027) | 79 T€ | 17 T€ | 97 T€ | -35 T€ | -462 T€ | 22 | 0 |
| Monat 8 (Jun 2027) | 85 T€ | 19 T€ | 97 T€ | -31 T€ | -492 T€ | 24 | 0 |
| Monat 9 (Jul 2027) | 79 T€ | 17 T€ | 97 T€ | -35 T€ | -527 T€ | 22 | 0 |
| Monat 10 (Aug 2027) | 55 T€ | 10 T€ | 97 T€ | -52 T€ | -579 T€ | 16 | 0 |
| Monat 11 (Sep 2027) | 97 T€ | 22 T€ | 97 T€ | -22 T€ | -601 T€ | 27 | 0 |
| Monat 12 (Okt 2027) | 103 T€ | 25 T€ | 97 T€ | -19 T€ | -621 T€ | 28 | 1 |
| Monat 13 (Nov 2027) | 132 T€ | 41 T€ | 97 T€ | -6 T€ | -627 T€ | 37 | 10 |
| Monat 14 (Dez 2027) | 73 T€ | 15 T€ | 97 T€ | -39 T€ | -666 T€ | 20 | 0 |
| Monat 15 (Jan 2028) | 121 T€ | 34 T€ | 97 T€ | -10 T€ | -676 T€ | 34 | 6 |
| Monat 16 (Feb 2028) | 133 T€ | 41 T€ | 97 T€ | -6 T€ | -682 T€ | 37 | 10 |
| Monat 17 (Mär 2028) | 145 T€ | 49 T€ | 97 T€ | -1 T€ | -683 T€ | 41 | 13 |
| Monat 18 (Apr 2028) | 121 T€ | 34 T€ | 97 T€ | -10 T€ | -693 T€ | 34 | 6 |
| Monat 19 (Mai 2028) | 133 T€ | 41 T€ | 97 T€ | -5 T€ | -698 T€ | 37 | 10 |
| Monat 20 (Jun 2028) | 134 T€ | 41 T€ | 97 T€ | -5 T€ | -703 T€ | 37 | 10 |
| Monat 21 (Jul 2028) | 110 T€ | 27 T€ | 97 T€ | -14 T€ | -717 T€ | 31 | 3 |
| Monat 22 (Aug 2028) | 62 T€ | 13 T€ | 97 T€ | -48 T€ | -765 T€ | 17 | 0 |
| Monat 23 (Sep 2028) | 146 T€ | 49 T€ | 97 T€ | -0 T€ | -766 T€ | 41 | 13 |
| Monat 24 (Okt 2028) | 134 T€ | 42 T€ | 97 T€ | -5 T€ | -770 T€ | 37 | 10 |
| Monat 25 (Nov 2028) | 190 T€ | 75 T€ | 99 T€ | 15 T€ | -755 T€ | 53 | 25 |
| Monat 26 (Dez 2028) | 105 T€ | 23 T€ | 99 T€ | -17 T€ | -772 T€ | 29 | 1 |
| Monat 27 (Jan 2029) | 173 T€ | 65 T€ | 99 T€ | 9 T€ | -763 T€ | 48 | 20 |
| Monat 28 (Feb 2029) | 190 T€ | 75 T€ | 99 T€ | 16 T€ | -748 T€ | 53 | 25 |
| Monat 29 (Mär 2029) | 207 T€ | 86 T€ | 99 T€ | 22 T€ | -726 T€ | 57 | 30 |
| Monat 30 (Apr 2029) | 174 T€ | 65 T€ | 99 T€ | 9 T€ | -716 T€ | 48 | 20 |
| Monat 31 (Mai 2029) | 191 T€ | 76 T€ | 99 T€ | 16 T€ | -700 T€ | 53 | 25 |
| Monat 32 (Jun 2029) | 191 T€ | 76 T€ | 99 T€ | 16 T€ | -684 T€ | 53 | 25 |
| Monat 33 (Jul 2029) | 158 T€ | 55 T€ | 99 T€ | 3 T€ | -681 T€ | 43 | 16 |
| Monat 34 (Aug 2029) | 90 T€ | 19 T€ | 99 T€ | -28 T€ | -708 T€ | 24 | 0 |
| Monat 35 (Sep 2029) | 209 T€ | 87 T€ | 99 T€ | 23 T€ | -685 T€ | 57 | 30 |
| Monat 36 (Okt 2029) | 192 T€ | 76 T€ | 99 T€ | 17 T€ | -669 T€ | 53 | 25 |
