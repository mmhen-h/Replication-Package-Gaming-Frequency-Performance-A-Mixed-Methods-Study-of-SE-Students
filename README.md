# Replication Package
## *Gaming Frequency Performance: A Mixed-Methods Study of Software Engineering Students*
To ensure transparency and reproducibility of this study, a comprehensive replication package has been made available. This repository contains the data and scripts required to reproduce the analysis of the relationship between gaming habits and academic performance (as measured by Final Grade) across eight semesters (SP22-FA25) in an undergraduate software engineering course. We employ a hybrid inductive-deductive qualitative workflow alongside quantitative statistical testing.

**Repository Structure**
```
Replication_Package/
├── README.md                                           # Usage instructions and environment requirements
│
├── Qualitative/
│   ├── Comprehensive_Codebook.xlsx                     # 8 primary themes and 28 sub-codes with definitions
│   ├── LLM_Automation_Protocol.md                      # Gemini 3 Pro prompts and data cleaning instructions
│   ├── Keywords_and_Phrases_Reference_Map.pdf          # Mapping used for LLM deductive coding
│   ├── Qualitative_Analysis_Scripts/
│   │   ├── GenerateAuditIndexes.ipynb                  # Reproduces 25% stratified random sample
│   │   ├── CountCodes.ipynb                            # Aggregates thematic code totals
│   │   └── FrequencyFinding.ipynb                      # Calculates number of low- vs. high-frequency rows
│   └── LLM_Outputs/
│       ├── Raw_Outputs/                                # CSVs coded by Gemini 3 Pro (SP22-FA24)
|       │   ├── FA22_Exhaustive_Coded.csv               
|       │   ├── FA23_Exhaustive_Coded.csv               
|       │   ├── FA24_Exhaustive_Coded.csv               
|       │   ├── SP22_Exhaustive_Coded.csv               
|       │   ├── SP23_Exhaustive_Coded.csv               
|       │   └── SP24_Exhaustive_Coded.csv               
│       └── Audited_Outputs/                            # Post-Audit CSVs coded by Gemini 3 Pro (SP22-FA24)
|       │   ├── AUDITED_FA22_Exhaustive_Coded.csv               
|       │   ├── AUDITED_FA23_Exhaustive_Coded.csv               
|       │   ├── AUDITED_FA24_Exhaustive_Coded.csv               
|       │   ├── AUDITED_SP22_Exhaustive_Coded.csv               
|       │   ├── AUDITED_SP23_Exhaustive_Coded.csv               
|       │   └── AUDITED_SP24_Exhaustive_Coded.csv      
│
├── Quantitative/
│   ├── 
│
└── Survey - A Gaming/
    ├── Gaming_Survey.pdf                               # Original Canvas survey instrument instrument
    └── Student_Responses/
        ├── FA/                                         # Original anonymized data (Fall 2022–2025)
        │   ├── FA22_Responses.csv
        │   ├── FA23_Responses.csv
        │   ├── FA24_Responses.csv
        │   └── FA25_Responses.csv
        └── SP/                                         # Original anonymized data (Spring 2022–2025)
            ├── SP22_Responses.csv
            ├── SP23_Responses.csv
            ├── SP24_Responses.csv
            └── SP25_Responses.csv
```

## Environment Requirements
To ensure the scripts run correctly, please use the following environments:

- **Statistical Analysis:** R (Version )
- **Qualitative Code Counting and Random Sample Generator:** Python 3.9.12
- **Qualitative Frequency Splitter:** Python 3.12.12
- **Necessary Python Libraries:** pandas, numpy

## Contents

### Data
- **Data Files:** Anonymized CSV datasets (e.g., ``` FA22_Responses.csv```) containing self‑reported student gaming habits paired with final course grades. All identifiers were removed prior to inclusion.
- **Survey Instrument:** A PDF copy (```Gaming_Survey.pdf```) of the original Gaming Survey as delivered on Canvas, including all questions and multiple‑choice options exactly as presented to participants.

### Quantitative
- **Quantitative Analysis Scripts:** R scripts used for statistical testing (ANOVA, Chi-square, and Spearman correlation) and the generation of descriptive visualizations.

### Qualitative
- **Qualitative Analysis Scripts:** Python scripts used for thematic code counting, including ```CountCodes.ipnyb``` for thematic counting, ```FrequencyFinding.ipnyb``` to count the number of low‑ and high‑frequency gamers across the manually coded cohorts, and ```GenerateAuditIndexes.ipnyb``` for selecting a random 25% sample of rows for manual verification.
- **Comprehensive Codebook:** The finalized codebook (```Comprehensive_Codebook.xlsx```) which contains eight primary themes and twenty‑eight sub‑codes, each defined and illustrated with an example quote. These codes capture students’ gaming habits, study behaviors, motivations, time‑management strategies, and perceptions of learning. The codebook represents the final structure developed through iterative refinement and serves as the reference framework for all qualitative analyses reported in the study.
- **Keywords and References Map:** A structured mapping (```Keywords_and_Phrases_Reference_Map.pdf```) that lists specific keywords and phrases used by Gemini 3 Pro to automate assigning codes.
- **LLM Automation Protocol:** The prompts used with Gemini 3 Pro during the deductive coding phase, including instructions for data cleaning and markdown‑based keyword bolding (```LLM_Automation_Protocol.md```).
- **LLM Outputs:** The raw CSV outputs (e.g. ```FA22_Exhaustive_Coded.csv```) generated by Gemini 3 Pro and the post‑audit CSVs (e.g. ```AUDITED_FA22_Exhaustive_Coded.csv```) following the 25\% random sample manual verification.
  - Yellow Highlight: Rows randomly selected for the 25% manual audit.
  - Light Orange Highlight (SP Cohorts Only): Rows originally marked as UNCODED that were not part of the random 25% sample
