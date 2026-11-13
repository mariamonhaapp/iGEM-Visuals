# NEUMA · Human Practices: preguntas de práctica y pitch de 10 minutos

Basado en la página de Human Practices de la wiki (2026.igem.wiki/puebla/human-practices).
Las preguntas y respuestas están en inglés para que las practiquen tal como se las harían. Las respuestas sugeridas son puntos clave, no un guion: díganlas con sus palabras.

---

## Parte 1 · Preguntas que les podrían hacer

### A. Enfoque y metodología

**1. Why did you choose an interpretive, qualitative paradigm instead of a quantitative survey?**
- We wanted to understand a *culture of diagnosis*, not just measure delays. A positivist design can count how many months a diagnosis takes, but it cannot explain why (Geertz, 1973: culture is interpreted, not measured).
- Our SWOT showed it fit our resources and context: access to clinicians in Puebla, a student team, one season.
- Our concept aims at transferability (rich description of context), not statistical generalization.

**2. What exactly do you mean by "diagnosis culture"?**
- The shared beliefs, expectations and routines through which lung cancer is recognized, or not, in Puebla.
- It is anchored in a socio-technical regime (Geels): a system that fails people, not a lack of education among them.

**3. How did you decide who your stakeholders were?**
- 77.6% of Mexicans rely on public insurance, so we went to the two main public pathways: IMSS (HGZ No. 20 "La Margarita") and ISSSTE Puebla.
- We followed the patient's diagnostic pathway: nursing, internal medicine, imaging, pathology, pulmonology, oncology, epidemiology.
- Then we widened the circle: biosensor experts (INAOE, UNAM, Latin-American Biosensors Workshop), a molecular biologist (Dr. Irma Cruz Solís), industry (Jeff Liu, FinalDose) and three focus groups of "indirect voices".

**4. How did you get access to interview doctors in public hospitals?**
- Through each hospital's Teaching and Research coordination (Dr. Israel Aguilar Cózatl at HGZ 20; Dr. Mario Alberto Sorcia Aguilar at ISSSTE).
- We submitted a research protocol, privacy notice and informed consent. Dr. Aguilar asked us to restructure the protocol following Feinstein's taxonomy.
- Then came the hard part: finding staff between shifts. We sometimes waited around 8 hours for oncology.
- The full process and templates are in our Template Repository for other teams.

**5. Why focus groups and not individual interviews with the public?**
- Culture is shared, so we wanted to see it being shared: agreement, contradiction, everyday language (Kitzinger, 1995).
- Groups make hard topics easier to talk about.
- We analysed two layers: what they said and how they felt (tone, silences, nervous laughter, tears).

**6. Who were the focus groups and why those groups?**
- A life-stage gradient: FG1, 8 high-school students; FG2, 6 biotechnology students (Tec CEM); FG3, 6 working adults aged 24–28, 4 of them active smokers.
- Today's patients are 40–60, but their exposure started when they were young, so we looked at the people who will become tomorrow's patients.

### B. Integración: ¿qué cambió por HP?

**7. Give us one concrete example of how Human Practices changed your project.**
- INAOE (June–July 2026): we replaced cysteine anchoring on gold with an AviTag–biotin / streptavidin system, using streptavidin SPR chips already validated on their platform.
- UNAM, Instituto de Química (September 2026): dCas9 did not express from our bicistronic construct; their lab advised two separate vectors (dCas9 and BirA) and in vitro biotinylation. That became our redesign (Engineering, Cycle 2), checked in silico.

**8. How did the clinical interviews change the design?**
- They gave us requirements that each have a name behind them: reliable, specific, reproducible, affordable, low burden (Table A, "HP in lab").
- They changed *where* NEUMA sits: a risk questionnaire at the first level of care, and the test ordered at the second level, where there is equipment and follow-up (Dr. Arely Pineda).
- They changed *what* NEUMA is: a triage tool, not a verdict. Pathology still confirms.

**9. What did Dr. Irma Cruz Solís contribute?**
- Validation is what decides whether NEUMA is usable. The kit needs three controls: a procedure control, the target mutation as positive control, and an unrelated reference sequence (housekeeping gene) to rule out false positives.
- A defined reading time window, field-condition testing (temperature, transport, trained staff, expiry date).
- She confirmed EGFR exon 19 deletions and L858R as a suitable panel for the Mexican population, and named PCR as the reference NEUMA will be compared against.

**10. Did any stakeholder challenge your project? How did you respond?**
- Jeff Liu (FinalDose) challenged real-time detection against PCR, pointed to ultrafast PCR as a competitor, argued that a single-mutation chip is not useful without a multiplex panel, and asked whether cell-free DNA carries the primary tumour's mutation.
- We take these as requirements, not as threats: the cfDNA question is now a sample-preparation requirement for the next validation stage, and the workshop experts also asked us to use several targets per diagnosis.
- Honest answer: these are open questions we have not solved yet.

### C. Hallazgos

**11. What was the most important finding of your HP work?**
- Late diagnosis is systemic, not a lack of education. About 82% of NSCLC cases in Mexico are diagnosed at a metastatic stage.
- The pathway takes 3 to 8 months in the public system (ISSSTE internal medicine). There is no national lung cancer screening program, unlike breast, cervical or prostate cancer.
- Patients are often the family's provider: "I feel sick, but I'll go tomorrow because I have to work; otherwise, what will my family eat?" (Nurse Jorge Jiménez Vargas).

**12. Did your stakeholders agree with each other?**
- No, and we report it. At ISSSTE one doctor said there are no access limitations; another described 3–8 months of waiting.
- They disagreed on where NEUMA should be used: internal medicine consultation, first level as prevention, or second and third level to distinguish infectious from neoplastic cough.
- Biosensor experts also had no consensus on who NEUMA would serve best.

**13. What role does the family play?**
- The family pays, pushes people to act, and is where the result is received.
- So NEUMA treats the family as an ally and a channel, not a target: invite a relative to the result if the patient wishes, no extra trips or costs, never use family history as marketing, and the patient's consent always comes first.

**14. What did the focus groups teach you that clinicians couldn't?**
- The first response to a symptom is to wait or self-medicate: the patient's side of the "just a little cough".
- Lung cancer is still seen as a "smokers' disease", although FG3 said "now everyone is prone". Pollution is felt but not counted as risk.
- Willingness depends on being told to: 10/10 if a doctor or questionnaire recommends it, lower if just offered.
- The word "diagnosis" sounds like a "verdict". People asked for next steps, empathy and psychological support.

### D. Diseño responsable, ética y seguridad

**15. What are the risks of NEUMA? What could go wrong?**
- Use-related failure: if NEUMA is used as a screen for everyone instead of as triage, it can overload imaging and pathology, or create false reassurance.
- Biological failure: low ctDNA abundance and no amplification step, which is why experts asked us to prove specificity in real samples.
- A positive result without a pathway leaves people "useless, defenseless" (FG2, FG3). That is why the result must come with next steps.

**16. How did you handle consent and personal data?**
- Informed consent and a privacy notice under Mexico's Federal Law on the Protection of Personal Data Held by Private Parties.
- Each specialist chose whether to be named or coded (Int. X). Focus group participants are identified only by group. Photos only with permission.

**17. Is a CRISPR-based diagnostic a biosafety concern?**
- The experts agreed: a CRISPR system that only detects carries little risk. The ethical concerns they named belong to gene editing.
- NEUMA detects; it does not edit DNA. Saying so clearly prevents misinformation.

**18. What about the patients themselves? Did you talk to them?**
- Not directly, and we say so openly. Patients are the most affected and the least accessible.
- We had a short written interview with the grandfather of an iGEMer from Tec CEM, a lung cancer patient, who asked us to consider the mental health of the sick, not only the physical side.
- Including patients' voices is our first next step, ideally through an ethics committee.

### E. Regulación

**19. How would NEUMA be regulated in Mexico?**
- In vitro diagnostics are medical devices under the Ley General de Salud (Art. 262) and the Reglamento de Insumos para la Salud. COFEPRIS grants the "registro sanitario" (valid five years).
- It requires performance and laboratory testing, stability studies and clinical evidence; manufacturing follows NOM-241-SSA1-2025.
- The sequence cannot be shortcut: authorized clinical protocol and ethics committee → analytical and clinical data → registro sanitario → clinical use. We are a research prototype, not a device.

**20. There is no CRISPR-specific regulation in Latin America. Isn't that a problem?**
- It is not the real obstacle. The Sherlock CRISPR SARS-CoV-2 kit was authorized by the FDA through the existing in vitro diagnostic route.
- So the question is not whether CRISPR is allowed, but whether we can demonstrate analytical and clinical performance. That is the same evidence gap clinicians, experts and Dr. Cruz Solís named independently.

### F. Preguntas críticas y de cierre

**21. What are the limitations of your HP work?**
- No direct patient interviews; few regulatory, bioethics or policy experts.
- Our interview instruments were pilot instruments, not validated by an ethics committee.
- In FG1 and FG2 the questionnaire was described before participants rated the test, so support was prompted.
- Findings are interpretations, not measurements; quotes are our translations.

**22. What would you do differently?**
- Contact regulatory, bioethics and policy experts early.
- Validate our instruments with an ethics committee so other teams can reuse them.
- Include patients and families directly.

**23. Is your HP work useful for other teams?**
- Yes: the Template Repository has our paradigm-selection guide, qualification matrix, protocol for requesting hospital interviews, privacy notice, consent form, a 101 guide for focus groups and a stakeholder letter template.
- We also show the step-by-step route to get interviews in public hospitals in Puebla.

**24. What are your next steps in Human Practices?**
- Move from the interpretive to the socio-critical paradigm: work hand in hand with the community so the change with NEUMA is visible.
- Patients' voices, clinical validation, and walking the regulatory route.

**25. How do you know the stakeholders actually support NEUMA?**
- 25 of 25 clinical stakeholders signed a letter supporting the continued development of the technology. The letters are on the wiki (some anonymized at their request).

**26. If you had to summarize your HP in one sentence?**
- "In Puebla, lung cancer is not found late because people don't care; it is found late because a system fails them, so NEUMA must enter that system as triage, not a verdict, with next steps, careful words and the family beside the patient."

### Preguntas rápidas que conviene tener memorizadas
| Dato | Respuesta |
|---|---|
| Clinical specialists interviewed | 25, July 2–28, 2026 |
| Hospitals | IMSS HGZ No. 20 "La Margarita" and ISSSTE Regional Hospital Puebla |
| Focus groups | 3 groups, 20 voices |
| Workshop forms | 8 (Buenos Aires, Aug 26–30) |
| Late diagnosis | ~82% of NSCLC diagnosed at metastatic stage |
| Public insurance | 77.6% of the population |
| Diagnostic pathway | 3–8 months (under 7 days only if hospitalized) |
| Burden | 9,665 deaths and 225,335 DALYs in 2021 |
| Lost work | 84–335 working days a year for stage IV patients; 13–30 for caregivers |
| Targets | EGFR exon 19 deletions and L858R, from ctDNA in a blood sample |
| Support letters | 25 of 25 |

---

## Parte 2 · Pitch de 10 minutos (Human Practices)

Unas 1,350 palabras: a ritmo tranquilo (130–140 palabras por minuto) dura cerca de 10 minutos. Los tiempos son guía; los textos entre corchetes son indicaciones, no se leen.

### 0:00 – 1:00 · Apertura
[Pausa. Mirar al público.]

"We all always know something. We all ignore something. Hence, we always learn." Paco Ignacio Taibo wrote that, and it became the first breath of our Human Practices.

We are NEUMA, from Puebla, Mexico. NEUMA means breath. Our project is a CRISPR-dCas9 biosensor read by surface plasmon resonance, designed to detect two EGFR mutations, exon 19 deletions and L858R, from tumour DNA in a single blood sample.

But a biosensor alone does not change anything. For us, Human Practices is the nucleus of the project: it is the why behind every experiment. So the question we asked was not only "can we detect lung cancer earlier?", but "why is lung cancer found so late in Mexico, and where could a tool like NEUMA really help?"

### 1:00 – 2:00 · El problema
In Mexico, about 82% of non-small cell lung cancer cases are diagnosed at a metastatic stage. In 2021, lung cancer caused nearly ten thousand deaths and more than 225 thousand years of healthy life lost. A working-age patient at stage four loses up to 335 working days a year, and their caregivers lose up to a month.

And here is something many people don't know: Mexico has national screening programs for breast, cervical and prostate cancer, but not for lung cancer. As an epidemiologist at ISSSTE told us: "A strategy as such? No… it is almost always a finding rather than an early detection."

### 2:00 – 3:15 · Nuestro lente
To understand this, we chose an interpretive, qualitative paradigm. Why? Because a survey could measure how long a diagnosis takes, but it could not explain *why*. As Geertz wrote, culture is an object of interpretation.

So we built a concept to guide our work: the **Diagnosis Culture in Mexico (Puebla)**. We define it as the shared beliefs, expectations and routines through which lung cancer is recognized, or not.

We were honest about our scope. A SWOT analysis showed us that our strongest access was clinical, and that 77.6% of Mexicans rely on public insurance. So we went where most patients actually go: the two main public pathways in Puebla.

### 3:15 – 5:00 · Las voces clínicas
From July 2nd to 28th, we interviewed **25 clinical specialists** at IMSS Hospital General de Zona No. 20, "La Margarita", and at the ISSSTE Regional Hospital in Puebla: nursing, internal medicine, imaging, pathology, pulmonology, oncology and epidemiology. We followed the path a patient walks.

Getting there was not easy. We submitted protocols, consent forms and privacy notices to each hospital's research coordination. And then we waited, sometimes eight hours for oncology, because patients and their families came first.

What did we hear?

First: the road is long. An internist at ISSSTE described three months for an appointment, three more for pulmonology, and slow bronchoscopy: three to eight months in total.

Second: the "little cough". Early symptoms are treated as flu, pneumonia or an ordinary cough.

Third, and the one that stayed with us, from Nurse Jorge Jiménez Vargas: *"I feel sick, but I'll go tomorrow because I have to work; otherwise, what will my family eat?"* The patient is often the family's provider.

And the specialists did not always agree. Some said access is fine; others described months of waiting. They disagreed on where NEUMA belongs: in primary care as prevention, in internal medicine, or in hospital to tell infectious from cancerous cough. We kept those disagreements, because they are part of the culture too.

### 5:00 – 6:30 · Las voces indirectas
Then we asked: what about the people who are not patients yet? We ran **three focus groups**, twenty voices along a life-stage gradient: high-school students, biotechnology students, and working adults, four of them active smokers. Today's patients are 40 to 60, but their exposure began when they were young.

We listened to what people said and to how they felt.

People still see lung cancer as a "smokers' disease", although one group told us "now everyone is prone". The first response to a symptom is to wait or self-medicate. The word "diagnosis" sounded like a "verdict". And willingness to take a test depended on being told to: everyone rated it ten out of ten if a doctor or a questionnaire recommended it.

In our first group, a student shared that their father had died of lung cancer. The whole room changed. In that moment we understood: diagnosis never happens to one person. It happens to a family.

### 6:30 – 8:00 · Lo que cambió
So, what changed because of Human Practices?

In the lab: biophotonics experts at INAOE recommended we replace our cysteine anchoring on gold with a biotin–streptavidin system on chips already validated on their platform, and we did. At UNAM's Instituto de Química, when dCas9 did not express from our first construct, Dr. Armando Hernández García's lab advised two separate vectors and in vitro biotinylation. That became our redesign.

From Dr. Irma Cruz Solís we learned that validation decides everything: three controls, a defined reading window, field conditions. And industry, through Jeff Liu of FinalDose, challenged us on PCR, multiplexing and cell-free DNA. We took those challenges as requirements for the next stage.

Every requirement in our design now has a name: reliable, specific, reproducible, affordable, low burden, each one traceable to a stakeholder.

And in the design of the use itself, NEUMA must be:
- **A triage tool, not a verdict.** Pathology still confirms.
- **Placed where the system can act:** a risk questionnaire at the first level, and the test ordered at the second level, where there is equipment and follow-up.
- **A result with next steps:** plain words, emotional support, and the family present if the patient wishes.
- **Respectful of the family economy:** one blood sample, no extra trips.

### 8:00 – 9:00 · Regulación y honestidad
We also looked at regulation. Biosensor experts told us there is no CRISPR-specific rule for diagnostics in Latin America. We treated that as a finding. In Mexico, NEUMA would be regulated as an in vitro diagnostic medical device by COFEPRIS. And a CRISPR diagnostic has already been authorized by the FDA through the existing route. So the real question is not whether CRISPR is allowed, but whether we can prove analytical and clinical performance.

We know what is missing: patients' own voices, clinical validation, regulatory and bioethics experts, and instruments validated by an ethics committee. We say it openly, and we shared all our templates so other teams can go further than we did.

### 9:00 – 10:00 · Cierre
In Puebla, lung cancer is not found late because people don't care. It is found late because a system fails them long before they reach a hospital.

All 25 of the clinical specialists we interviewed signed a letter supporting NEUMA, knowing how hard it is to bring this technology to reality in Mexico.

Our next step is to move from understanding the community to working hand in hand with it.

NEUMA means breath, and this is not our final one. Because in lung cancer every hour counts, and because, as we learned, we always learn.

Thank you.

---

### Consejos para presentarlo
- Ensayen con cronómetro; si se pasan, recorten primero el bloque de regulación (8:00–9:00) a dos frases.
- Las citas de pacientes y enfermería funcionan mejor dichas despacio y con una pausa después.
- Si lo presentan varias personas, un buen reparto es: apertura y problema · lente y voces clínicas · voces indirectas · qué cambió · regulación y cierre.
- Verifiquen con el equipo cómo nombrar al epidemiólogo de ISSSTE: la wiki dice "Dr. Gil Luna" y el deck dice "Dr. Gilberto Pérez Luna". En el pitch lo dejé como "an epidemiologist at ISSSTE" para no equivocarse.
