# Project Estimation Engine — Week 1 Data Exploration

**Intern:** Armish Shaikh  
**Programme:** Zalvantic Internship Programme  
**Domain:** Data Science

## Week 1 objective
Collect and understand public software-effort data. This starter project explores two public datasets:
- **COCOMO-81** — 63 projects; effort is recorded in person-months.
- **Desharnais** — 81 projects; effort is recorded in person-hours.

The two datasets are analyzed separately. Do not combine their effort values directly because their units differ.

## Repository structure
```text
week1_project_estimation/
├── data/
│   ├── raw/                 # downloaded source files; do not edit manually
│   └── processed/
├── docs/
│   └── data_dictionary.md
├── notebooks/
│   └── 01_explore.ipynb
├── .github/
│   └── pull_request_template.md
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup (Windows PowerShell)
```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the notebook
```powershell
jupyter notebook
```
Open `notebooks/01_explore.ipynb` and run all cells from top to bottom. The first data-loading cell downloads the public CSV files into `data/raw/`. An internet connection is required for the first run.

## Data sources
1. COCOMO-81 CSV: https://raw.githubusercontent.com/Derek-Jones/Software-estimation-datasets/main/COCOMO-81.csv
2. Desharnais CSV: https://raw.githubusercontent.com/Derek-Jones/Software-estimation-datasets/main/Desharnais.csv

The source repository describes these as public software-estimation datasets and provides dataset provenance. Preserve source attribution when reusing them.

## Important data-handling notes
- Keep the original downloaded files unchanged in `data/raw/`.
- COCOMO-81 `actual` is measured in **person-months**.
- Desharnais `Effort` is measured in **person-hours**.
- In Desharnais, `-1` is used as a missing/sentinel value in some experience fields. The notebook reports this and converts it to missing (`NaN`) only in the analysis copy.
- The notebook checks missing values, duplicates, descriptive statistics, and IQR outliers. It does not delete outliers automatically.
- This week is exploratory only. No predictive model is trained.

## Week 1 completion checklist
- [ ] Repository and virtual environment created
- [ ] Two public datasets downloaded
- [ ] Data dictionary reviewed and committed
- [ ] Notebook run successfully
- [ ] At least six plots reviewed, each with a one-sentence takeaway
- [ ] Work committed on branch `week-1-data-exploration`
- [ ] Pull request opened with title: `Week 1: Collect and understand the estimation data`

## Attribution
Datasets: Derek Jones, *Software-estimation-datasets* GitHub repository. Dataset records retain the original dataset names and definitions. Internship project: Zalvantic Internship Programme.
