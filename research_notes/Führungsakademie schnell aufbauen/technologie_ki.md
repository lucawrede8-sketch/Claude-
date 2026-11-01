# Technologie-Stack & generative KI für den schnellen Aufbau einer Führungs-/Corporate Academy (2024–2026)

Research notes, compiled 2026-11-01. Method note: most pricing and adoption data come from third-party comparison sites and vendor press releases, not independent audits. Vendor-sourced claims are marked **[VENDOR]**. The pages joshbersin.com, otto-schmidt.de and ki-campus.org could not be fetched (network allowlist in this session), so claims about them rest on search snippets only.

---

## 1. Platforms for a fast start: options, pricing, implementation time, GDPR/EU hosting

### Takeaway
For a fast launch, three things matter most. Mid-market SaaS LMSs (TalentLMS, 360Learning, LearnUpon, Docebo, Absorb) go live in **weeks, not months**: about 4–16 weeks for cloud LMSs, and a 9-week academy launch on Docebo **[VENDOR]**. Published list prices exist only at the low end: TalentLMS from about $119/month, 360Learning Team from about $8/user/month. Docebo, LearnUpon, Absorb, Cornerstone and imc are quote-based and typically land in the 5-figure range per year. For external sales, Thinkific (about $49–199/month) and Kajabi (from about $179/month after the January 2026 repricing) are the creator-style options. Content libraries (LinkedIn Learning, Coursera) cost about $380–400 per user per year at team tier. The market is consolidating fast around "AI-native" platforms, for example Workday's ~$1.1B acquisition of Sana.

### Cited Findings
**Pricing (mostly third-party estimates; get quotes)**
- TalentLMS (most transparent): free plan up to 5 users; Core $119/month (≤40 users); Grow $229/month (≤70); Pro $579/month (≤500). — [costbench TalentLMS vs Docebo](https://costbench.com/compare/docebo-vs-talentlms/); [trainingcost TalentLMS](https://trainingcost.com/lms-comparison/talentlms-cost)
- 360Learning: Team plan from about $8 per active user per month (min. 5 seats, reportedly capped around 100 users); Business and Enterprise are quote-based. Sources disagree on the terms. — [rework 360Learning alternatives](https://resources.rework.com/tools/lms-training/best-360learning-alternatives); [dupple best LMS 2026](https://dupple.com/learn/best-lms-platforms)
- Docebo: no public list price. Estimates range from $7–10/user/month to roughly $25,000+/year for small deployments. One blog cites implementation fees of €10,000–30,000. Estimates conflict and look partly copied between sites, so treat them as directional only. — [costbench](https://costbench.com/compare/docebo-vs-talentlms/); [thefrontkit Docebo alternatives](https://thefrontkit.com/blogs/docebo-alternatives-2026); [Capterra](https://capterra.com/p/127213/Docebo/alternatives/)
- LearnUpon: custom pricing; estimated $6–9 per active user per month; minimum annual contracts reportedly about $10,000–15,000. — [freshlearn LearnUpon pricing](https://freshlearn.com/blog/learnupon-pricing/); [schoolmaker LearnUpon pricing](https://schoolmaker.com/blog/learnupon-pricing.md)
- LinkedIn Learning Teams: about $379.88/user/year (2–20 users, annual billing only); 21+ users custom, with aggregator estimates of about $350–500/user/year for enterprise. — [Wise SG 2025](https://wise.com/sg/blog/linkedin-learning-corporate-pricing); [trainingcost LinkedIn Learning](https://trainingcost.com/lms-pricing/linkedin-learning)
- Coursera for Business Team: $399/user/year (seat range reported as 5–125 or 5–499; unresolved); Enterprise custom; 14-day trial. — [trainingcost Coursera](https://trainingcost.com/lms-pricing/coursera-business); [Capterra IE](https://www.capterra.ie/software/1021057/coursera-for-business)
- External sales, Thinkific: $49 Basic / $99 Start / $199 Grow per month, or about $36/$74/$149 billed annually. Some sources report about a 10% increase from 13 Aug 2026 (Basic about $54). Thinkific Payments is available only in the US, UK, CA, AU and "select EU countries". Using your own Stripe on lower plans reportedly adds a surcharge. — [schoolmaker Thinkific pricing](https://schoolmaker.com/blog/thinkific-pricing.md); [cartmango Thinkific alternatives](https://cartmango.com/thinkific-alternatives/); [ruzuku](https://www.ruzuku.com/learn/articles/thinkific-pricing-plans)
- External sales, Kajabi: restructured in January 2026; plans from $179/month ($143 billed annually), up to $499/month. A former $89 "Kickstarter" plan may no longer be offered. — [schoolmaker Kajabi pricing](https://schoolmaker.com/blog/kajabi-pricing.md); [costbench Kajabi vs Thinkific](https://costbench.com/compare/kajabi-vs-thinkific/)

**Implementation time**
- Docebo case: FintechOS launched a global academy in **9 weeks** **[VENDOR case study]**. — [docebo.com](https://www.docebo.com/?p=179233); [casestudies.com](https://www.casestudies.com/company/docebo/case-study/fintechos-launches-global-academy-in-9-weeks-with-docebo)
- Cloud LMS rollouts are typically **4–16 weeks**, depending on organisation size. — [Gainsight LMS implementation](https://www.gainsight.com/blog/lms-implementation-checklist/)
- One estimate puts Docebo at 4–8 weeks (source is a competitor). — [Coggno](https://coggno.com/blog/compliance-lms-implementation-timeline-contract-to-first-completion/)
- TalentLMS: "weeks rather than months" **[VENDOR]**, and "sign-up to running courses in hours" (marketing-style claim). — [TalentLMS blog](https://www.talentlms.com/blog/steps-for-successful-lms-implementation/); [eorhq](https://eorhq.com/tools/best-lms-global-teams/)

**Analyst positioning and market moves**
- Fosway 9-Grid Learning Systems 2025: Degreed = Strategic Leader **[VENDOR PR]**; Learning Pool and Litmos = Core Leader; Thought Industries and imc Learning Suite (Scheer IMC) = Strategic Challenger. Fosway assesses Performance, Potential, Market Presence, TCO and Trajectory. — [Degreed newsroom](https://degreed.com/experience/newsroom/degreed-recognized-as-strategic-leader-2025-fosway-9-grid/); [Learning Pool](https://learningpool.com/blog/core-leader-fosway-2025); [Litmos](https://www.litmos.com/?p=56651); [Thought Industries](https://www.thoughtindustries.com/blog/2025-fosway-9-grid-distinguishes-thought-industries-as-strategic-challenger-for-learning-systems); [Scheer IMC](https://www.scheer-imc.com/?p=22142)
- Workday signed a definitive agreement to acquire Sana (Sana Learn: LMS, AI course generation, AI tutor) for about **$1.1B**, announced 16 Sep 2025. — [Workday IR PDF](https://investor.workday.com/files/doc_news/Workday-Signs-Definitive-Agreement-to-Acquire-Sana-09-16-2025-2025.pdf); [tech.eu](https://tech.eu/2025/09/16/workday-to-acquire-sana-for-11-billion/)
- "Workday Learning, powered by Sana" became generally available on 22 July 2026; the press release claims **"up to 98%" reductions in content-creation time** **[VENDOR, "up to" figure]**. — [Workday newsroom](https://en-gb.newsroom.workday.com/2026-07-22-Workday-Learning,-Powered-by-Sana,-Now-Generally-Available-as-an-AI-Native-Learning-Experience-Built-on-Workdays-Trusted-Data)
- Josh Bersin (June 2025) framed Docebo "going AI-native" and Sana expanding as the "L&D revolution": a shift from a publishing model to dynamic, on-demand content. He promotes his own Galileo Learn platform, so treat this as an analyst-with-product view. — [joshbersin.com (title/snippet only)](https://joshbersin.com/2025/06/the-ld-revolution-docebo-goes-ai-native-sana-expands-what-do-you-do/)

### Inferences
- A 10-person academy team with a few hundred to a few thousand leaders can launch in about 6–12 weeks on a SaaS LMS. TalentLMS or 360Learning Team are the cheapest with self-serve terms. Docebo, LearnUpon and Absorb make sense if the academy will also be sold externally (multi-tenant/extended enterprise, e-commerce), but budget for 5-figure annual contracts plus setup.
- Moodle Workplace/Totara and imc (German vendor, Fosway Strategic Challenger) are the "EU sovereignty / on-prem" options. They trade launch speed for control.
- For pure external B2C/B2B sales of leadership programmes, Thinkific or Kajabi are fastest, but they lack enterprise LMS features (SSO/HR integration, compliance reporting). EU VAT and payment handling must be checked.
- Buying a content library (about €350–400/user/year) is expensive at scale. For leadership academies it is usually better to license selectively and build the proprietary core curriculum with AI tools.

### Gaps
- EU/Frankfurt data residency for Docebo, LearnUpon and TalentLMS was **not confirmed** in sources found. Request DPA, sub-processor list and hosting region from each vendor. (From prior knowledge, not verified here: 360Learning is French-headquartered and imc is German, which is often an argument for EU hosting.)
- No primary 2025/2026 Craig Weiss or Gartner data was retrieved. No verified pricing for Absorb, Cornerstone, imc, Moodle Workplace, Totara or Degreed.
- Thinkific and Kajabi handling of EU VAT was not confirmed.

---

## 2. Generative AI in L&D: authoring, video, AI role-play and coaching; evidence of speed, cost and effectiveness

### Takeaway
Generative AI clearly speeds up content production. The documented figures are mostly vendor-reported: about 62% / 8 days faster training-video production (Synthesia user survey), about 50% faster course creation in Synthesia case studies, and "up to 98%" in Workday/Sana. The strongest independent evidence on knowledge-worker productivity is the Harvard/BCG "jagged frontier" field experiment. For AI coaching and role-play (Valence Nadia, CoachHub AIMY, BetterUp, LinkedIn role-play), there is **no independent peer-reviewed outcome evidence for specific products**. What exists is adoption and satisfaction data plus early perception studies. AI coaching should therefore be positioned as scalable practice and reflection, complementing human coaching rather than replacing it.

### Cited Findings
**Adoption and trend reports**
- LinkedIn Workplace Learning Report 2025 (via secondary summaries): 71% of L&D professionals are experimenting with or integrating AI; organisations with strong career-development programmes more often describe themselves as AI "leading/accelerating" (51% vs 36%). Not verified against the original PDF. — [thirst.io summary](https://thirst.io/blog/workplace-learning-report-2025/); [LinkedIn community post](https://tcommunity.linkedin.com/talent-industry-insights-46/2025-workplace-learning-report-the-rise-of-career-champions-1266)
- Josh Bersin argues that more than 60% of L&D work could be automated by AI. No published methodology was found. — [trainingmag](https://trainingmag.com/how-ai-is-not-just-transforming-but-revolutionizing-ld/); [diginomica](https://diginomica.com/why-its-time-learn-use-ai-overhaul-ld-josh-bersin-calls-organizations-throw-old-fashioned-training)
- mmb Trendmonitor 2024/2025 ("Lernen wird intelligenter", 71 experts): trend towards AI-supported, dialogic and individual learning, with growing expectations around quality assurance and ethics. mmb Trendmonitor 2025/2026 ("Übernehmen KI-Tech-Unternehmen bald den digitalen Bildungsmarkt?"): 77% of respondents see time relief for instructors through AI. — [mmb 2024/25 PDF](https://www.mmb-institut.de/wp-content/uploads/mmb-Trendmonitor_2024-2025.pdf); [mmb 2025/26 PDF](https://www.mmb-institut.de/wp-content/uploads/mmb-Trendmonitor_2025-2026.pdf); [fernstudi.net](https://www.fernstudi.net/news/ki-auf-dem-vormarsch-lernassistenten-und-adaptive-learning-praegen-die-zukunft-der-weiterbildung); [Haufe Learning Delphi](https://www.haufe.de/personal/hr-management/learning-delphi_80_509292.html)
- McKinsey HR-Monitor 2025 (Germany): companies are saving on AI upskilling and missing opportunities (headline only). — [McKinsey DE press](https://www.mckinsey.com/de/news/presse/2025-07-21-hr-monitor-2025)
- Philippa Hardman / Synthesia 2025 survey of 400+ L&D professionals: AI use is spreading across the whole learning lifecycle, not just "build". — [Hardman Substack](https://drphilippahardman.substack.com/p/beyond-faster-content-how-ai-is-quietly)

**Content creation: speed and cost**
- Synthesia survey of 102 of its own L&D users: average training-video production time cut by **8 days (62%)** with AI tools **[VENDOR, self-selected sample]**. — [Synthesia stats](https://www.synthesia.io/learn/training-videos/stats)
- Synthesia case studies: APA cut video creation time by 50%; Forecast cut course creation time by 50%; BESTSELLER cut classroom time by 50% **[VENDOR]**. — [APA](https://synthesia.io/case-studies/apa); [Forecast](https://www.synthesia.io/case-studies/forecast); [BESTSELLER](https://synthesia.io/case-studies/bestseller)
- Synthesia also promotes a UCL study on AI-generated video for adult learners **[VENDOR-promoted research]**. — [Synthesia/UCL](https://www.synthesia.io/post/new-ucl-study-shows-the-benefits-of-using-ai-generated-videos-for-adult-learners)
- HeyGen 2025 L&D report: more than 80% of L&D teams have five or fewer people, yet nearly a third produce 21+ training videos per month **[VENDOR]**. — [HeyGen report](https://www.heygen.com/blog/ai-video-learning-and-development-report-2025)
- Workday/Sana: "up to 98%" reduction in content-creation time **[VENDOR]**. — [Workday newsroom](https://en-gb.newsroom.workday.com/2026-07-22-Workday-Learning,-Powered-by-Sana,-Now-Generally-Available-as-an-AI-Native-Learning-Experience-Built-on-Workdays-Trusted-Data)

**Independent productivity evidence**
- Dell'Acqua et al., "Navigating the Jagged Technological Frontier" (HBS Working Paper 24-013, 2023): 758 BCG consultants used GPT-4. On tasks inside AI's frontier they completed about 12.2% more tasks, about 25.1% faster, with more than 40% higher quality. On a task outside the frontier, AI users were less likely to be correct. Figures come from my prior knowledge; the paper could not be fetched here, so verify before quoting. — [HBS working paper page](https://www.hbs.edu/faculty/Pages/item.aspx?num=64700)

**AI coaching and role-play for leaders**
- Valence (AI coach "Nadia", launched early 2023): deployments at Experian, Delta, Kraft Heinz and General Mills; more than 1M coaching conversations; one case reports 90% regular use and NPS 91; claims cost as low as about 2% of a human coach **[VENDOR/trade press]**. — [People Managing People](https://peoplemanagingpeople.com/performance-management/ai-coaching-results/); [HR Executive](https://hrexecutive.com/the-new-coaching-stack-a-3-tier-model-for-ai-and-human-coaching/); [Realtid (SE)](https://www.realtid.se/karriar-ledarskap/nya-verktyg-kapar-kostnaden-for-chefscoachning/)
- BetterUp: hybrid AI + human coaching. Its own survey found 52% of workers want both. The "Grow" AI-coach pilot reported +16% workplace confidence and 95% satisfaction. The 14x ROI claim comes from BetterUp's own study, not an independent audit **[VENDOR]**. — [People Managing People](https://peoplemanagingpeople.com/performance-management/ai-coaching-results/)
- CoachHub: network of 3,500+ human coaches plus the AIMY AI coach; enterprise quote-only. **No outcome data found for AIMY.** — [lindy.ai overview](https://www.lindy.ai/blog/ai-coach); [People Managing People](https://peoplemanagingpeople.com/performance-management/ai-coaching-results/)
- HR Executive proposes a three-tier coaching model: AI for scale, then group or human coaching, then executive coaching. — [HR Executive](https://hrexecutive.com/the-new-coaching-stack-a-3-tier-model-for-ai-and-human-coaching/)
- CommCoach (arXiv 2505.14452, 2025): managers see LLM role-play as useful practice for workplace communication when it offers customisation, iterative feedback and contextual adaptation. They raised concerns about realism and bias in AI personas. This is a perception study, not an outcome study. — [arXiv](https://arxiv.org/abs/2505.14452v2)
- HKU randomised field experiment: AI-assisted training improved managerial effectiveness in employee training, more strongly under transformational leaders. Only a summary was seen; effect sizes unverified. — [HKU Business School](https://hkubs.hku.hk/event/from-overwhelmed-to-empowered-how-artificial-intelligence-augments-managers-in-employee-training)
- LinkedIn's role-play tool: more than 90% of managers who used it over three months found the time valuable (self-reported). — [WorkforceHub](https://www.workforcehub.com/blog/managing-people-building-confidence-and-equipping-leaders/)
- Claim of $2.5B savings at IBM from AI-driven training: no methodology, do not rely on it. — [exec.com](https://www.exec.com/learn/ai-roleplays-for-manager-training)
- A trial of a chatbot coach found that outcomes were best predicted by the coachee's starting self-efficacy and hope. It used older chatbot technology; authors and journal were not verified. — reported in [People Managing People](https://peoplemanagingpeople.com/performance-management/ai-coaching-results/)

### Inferences
- Realistic planning assumption for a lean team: about 30–60% time savings on first-draft content (scripts, outlines, quizzes, video). Treat "up to 98%" as best-case marketing. Review and SME validation remain the bottleneck.
- The highest-value AI uses for a leadership academy are: (a) rapid authoring (LMS-native AI plus Articulate/Rise AI, Synthesia/HeyGen for video and translation); (b) AI role-play for difficult conversations (feedback, conflict, performance); (c) AI coaching between human sessions; (d) admin automation (enrolment, reminders, reporting).
- The jagged-frontier result argues for clear "AI-in / AI-out" task rules and human review for nuanced leadership content.

### Gaps
- No primary data retrieved on the LinkedIn WLR 2025 original PDF, Brandon Hall or Fosway AI surveys, or the Synthesia "AI in L&D Report 2025/2026" (one secondary cite claims 84–88% report faster production; unverified).
- No figures found for Articulate AI Assistant, 360Learning AI, Docebo AI Creator, Hone or CoachHub AIMY time savings or outcomes.
- No independent RCT on any named commercial AI leadership coach.

---

## 3. EU AI Act, GDPR (DSGVO) and works council co-determination (BetrVG) for learning tech

### Takeaway
Three German/EU legal layers apply. **Art. 4 AI Act (AI literacy)** has applied since 2 Feb 2025. The **Digital Omnibus on AI (Reg. (EU) 2026/1744, in force 27 July 2026)** softened it from "ensure a sufficient level" to "take measures to support" AI literacy. The obligation still exists, it has no specific Art. 99 fine, and national enforcement starts 2 Aug 2026. Learning platforms that log individual progress or scores are objectively capable of monitoring behaviour or performance, which triggers **co-determination under §87(1) Nr. 6 BetrVG**, so a works agreement (Betriebsvereinbarung) is needed. AI-literacy training itself falls under §§96–98 BetrVG (vocational training). Under the Omnibus, high-risk HR obligations reportedly move to 2 Dec 2027.

### Cited Findings
- Digital Omnibus on AI = Regulation (EU) 2026/1744, adopted 8 July 2026, published in the OJ 24 July 2026, in force 27 July 2026. — [Lewis Silkin](https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today-102nedo); [Mondaq](https://www.mondaq.com/uk/new-technology/1823160/the-digital-omnibus-on-ai-enters-into-force-today)
- Amended Art. 4: providers and deployers must take measures to support AI literacy among staff and others operating AI on their behalf, replacing "ensure a sufficient level"; no individual level must be guaranteed. New Art. 4(2) obliges the Commission and Member States to support companies, especially SMEs. The duty applies since 2 Feb 2025; supervision/enforcement by national authorities from 2 Aug 2026; Art. 4 is not among obligations with specific fines under Art. 99. Secondary sources; the EUR-Lex text was not checked. — [KI-Campus (title: "AI literacy remains mandatory")](https://ki-campus.org/en/blog/eu-ai-act-ai-omnibus-recalibrates-article-4-ai-literacy-remains-mandatory); [DPO Consulting](https://www.dpo-consulting.com/blog/ai-act-what-the-digital-omnibus-really-changes-for-companies); [aiactblog.nl](https://www.aiactblog.nl/en/posts/digital-omnibus-ai-act-what-changes-what-now-2026); [ECIJA](https://www.ecija.com/en/news-and-insights/la-importancia-de-la-alfabetizacion-en-ia-pese-a-la-simplificacion-normativa-del-ria-por-el-digital-omnibus-europeo/)
- High-risk AI in HR/personnel (Annex III) deadline reportedly moved from 2 Aug 2026 to **2 Dec 2027**. — [ki-syndikat (practice page)](https://www.ki-syndikat.de/fuer-unternehmen/betriebsvereinbarung-ki/); [aiactblog.nl](https://www.aiactblog.nl/en/posts/digital-omnibus-ai-act-what-changes-what-now-2026)
- §87(1) Nr. 6 BetrVG applies as soon as a system is **objectively capable** of recording behaviour or performance; no monitoring intent is required. If negotiations fail, the conciliation board (Einigungsstelle, §87(2)) decides. — [ki-syndikat](https://www.ki-syndikat.de/fuer-unternehmen/betriebsvereinbarung-ki/); [CMS: KI-Transformation und Betriebsrat](https://cms.law/de/deu/legal-updates/ki-transformation-und-betriebsrat-mitbestimmung-richtig-gestalten)
- ArbG Hamburg, 16.01.2024 (24 BVGa 1/24): no co-determination right for ChatGPT used via employees' own browser accounts, because the employer could not record behaviour or performance data. This does not transfer to company-run platforms with logging. — [Gleiss Lutz](https://www.gleisslutz.com/de/know-how/arbeitsgericht-hamburg-zu-chatgpt-kein-mitbestimmungsrecht-des-betriebsrats); [CMS](https://cms.law/de/deu/legal-updates/kein-mitbestimmungsrecht-des-betriebsrats-bei-chatgpt-co)
- Deloitte Legal assigns the introduction and implementation of AI-literacy trainings to works-council participation under §§97, 98 BetrVG (vocational training). — [Deloitte Legal webcast PDF, 06.11.2024](https://www2.deloitte.com/content/dam/Deloitte/dl/Documents/legal/Deloitte%20Legal%20Webcast%2006.11.2024.pdf)
- Further guidance on AI and the works council, and on AI in HR under the AI Act. — [CMS: Einführung von KI](https://cms.law/de/deu/legal-updates/Einfuehrung-von-KI-im-Unternehmen-Einbindung-des-Betriebsrats); [Grant Thornton 2026](https://www.grantthornton.de/themen/2026/ki-einsatz-im-hr-bereich-arbeitsrechtliche-aspekte-vor-dem-hintergrund-der-eu-ki-verordnung/); [ZAAR LMU handout 2024](https://www.zaar.uni-muenchen.de/veranstaltungen/vortragsreihe/archiv/2024/stoeckert/handout.pdf)

### Inferences
- Plan for a **framework works agreement (Rahmen-BV) on IT/AI and learning platforms** from day 1, covering: purpose limitation (learning, not performance assessment); aggregated reporting thresholds; deletion periods; no use of learning or coaching-chat data for HR decisions; and the AI-coach conversation logs. This is typically the critical-path item for go-live in Germany, and it can take longer than the technical setup.
- §90 BetrVG (information and consultation on technical installations) and §80(3) (expert advice) also usually apply. These come from prior knowledge, not sourced here.
- GDPR: a data processing agreement (Art. 28) is needed; prefer EU hosting or SCCs/DPF; a DPIA (Art. 35) is likely for AI coaching that processes personal reflections. Treat this as standard practice; no specific source was retrieved in this session.
- The academy can turn Art. 4 into a programme: an "AI literacy for leaders" module serves compliance and is strategic content at the same time.
- AI coaching or role-play that **evaluates** leaders (scoring used for promotion) risks drifting toward Annex III high-risk (employment decisions). Keep it developmental only.

### Gaps
- No court decision found specifically on LMSs; the application of §87(1) Nr. 6 to LMSs is inferred from the general "objective suitability" standard (established BAG case law, not retrieved here).
- The consolidated EUR-Lex text of Reg. 2026/1744 was not checked.

---

## 4. Recommended lean stack for a 10-person academy team

### Takeaway
A pragmatic 2026 lean stack combines five layers: (1) a mid-market SaaS LMS/LXP with built-in AI authoring and EU hosting, with extended-enterprise/e-commerce capability if external sales are planned; (2) one AI video tool; (3) an enterprise LLM copilot for drafting; (4) a selective content library or AI role-play/coaching add-on; (5) a Betriebsrat-approved data concept. Indicative cost for a few hundred learners is low-to-mid five figures per year excluding a content library. All cost figures are estimates assembled from the sources above.

### Cited Findings
- Small L&D teams are the norm: more than 80% have five or fewer people **[VENDOR survey, HeyGen]**. — [HeyGen](https://www.heygen.com/blog/ai-video-learning-and-development-report-2025)
- Low-cost LMS entry points: TalentLMS from $119/month; 360Learning about $8/user/month. — [costbench](https://costbench.com/compare/docebo-vs-talentlms/); [rework](https://resources.rework.com/tools/lms-training/best-360learning-alternatives)
- Enterprise-grade LMSs with academy/external features (Docebo, LearnUpon) run about $10–25k+/year plus setup. — [freshlearn](https://freshlearn.com/blog/learnupon-pricing/); [thefrontkit](https://thefrontkit.com/blogs/docebo-alternatives-2026)
- External sales: Thinkific $49–199/month; Kajabi $179–499/month. — [schoolmaker Thinkific](https://schoolmaker.com/blog/thinkific-pricing.md); [schoolmaker Kajabi](https://schoolmaker.com/blog/kajabi-pricing.md)
- A tiered coaching model (AI for scale, human coaching for critical moments) is emerging. — [HR Executive](https://hrexecutive.com/the-new-coaching-stack-a-3-tier-model-for-ai-and-human-coaching/)
- 9-week academy launch reference **[VENDOR]**. — [Docebo/FintechOS](https://www.docebo.com/?p=179233)

### Inferences (recommendation sketch; not sourced as a whole)
- **Option A, "speed and low cost" (internal only):** 360Learning or TalentLMS (both with AI course generation) + Synthesia or HeyGen for video and multilingual versions + enterprise LLM (Microsoft 365 Copilot / ChatGPT Enterprise / Claude) for scripts, cases and quizzes + LinkedIn Learning licences only for a target group. Go-live in about 6–8 weeks, with the works agreement in parallel.
- **Option B, "academy as a business" (internal + external customers):** Docebo or LearnUpon (extended enterprise, e-commerce, multi-portal) or, for B2C-style sales, Thinkific/Kajabi as a sales front end. Expect about 8–12 weeks and higher TCO.
- **Option C, "EU sovereignty / Konzern":** imc Learning Suite or Moodle Workplace/Totara, hosted in Germany. Slower start, maximum control, simpler works-council and data-protection approval.
- **AI coaching/role-play add-on:** pilot one tool (e.g. Valence, CoachHub AIMY, BetterUp, Hone, or LMS-native role-play) with 30–50 leaders for 3 months. Measure usage, behaviour transfer and 360° change, since independent effectiveness evidence is lacking.
- **Governance:** framework works agreement, DPIA, AI-use policy, and an Art. 4 literacy module, since leaders are themselves deployers' staff.
- **Team roles (10 people):** about 1 head, 2 programme/curriculum designers, 2 AI-enabled content producers, 1 LMS/learning-ops admin, 1 data/analytics + compliance, 2 facilitators/coach managers, 1 sales/partner manager if selling externally. This is an inference, not sourced.

### Gaps
- No independent TCO benchmarks for a 10-person academy were found.
- Pricing for Synthesia, HeyGen, Articulate 360 AI, Hone, Valence and CoachHub was not retrieved; Valence and CoachHub are quote-based.
