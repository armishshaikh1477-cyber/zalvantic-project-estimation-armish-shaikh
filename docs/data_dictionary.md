# Week 1 Data Dictionary

The project uses two datasets. Their effort units differ, so analyze them separately unless a justified unit conversion and harmonization strategy is introduced later.

## 1. COCOMO-81

**Source file:** `COCOMO-81.csv`  
**Source:** https://github.com/Derek-Jones/Software-estimation-datasets  
**Rows:** 63 projects  
**Target:** `actual`  
**Target unit:** person-months

| Column | Meaning |
|---|---|
| `num` | Project record identifier |
| `dev_mode` | Development mode: organic, semidetached, or embedded |
| `rely` | Required software reliability cost-driver multiplier |
| `data` | Database size cost-driver multiplier |
| `cplx` | Product complexity cost-driver multiplier |
| `time` | Execution-time constraint multiplier |
| `stor` | Main-storage constraint multiplier |
| `virt` | Virtual-machine volatility multiplier |
| `turn` | Computer turnaround-time multiplier |
| `acap` | Analyst capability multiplier |
| `aexp` | Applications experience multiplier |
| `pcap` | Programmer capability multiplier |
| `vexp` | Virtual-machine experience multiplier |
| `lexp` | Programming-language experience multiplier |
| `modp` | Use of modern programming practices multiplier |
| `tool` | Use of software tools multiplier |
| `sced` | Required development schedule multiplier |
| `loc` | Size measure as supplied by the source dataset (commonly interpreted as KLOC in COCOMO data) |
| `actual` | Actual development effort in person-months; prediction target |

The numeric cost-driver columns are multipliers, not raw counts. Interpret their values using the COCOMO-I rating scale documentation before modeling.

## 2. Desharnais

**Source file:** `Desharnais.csv`  
**Source:** https://github.com/Derek-Jones/Software-estimation-datasets  
**Rows:** 81 projects  
**Target:** `Effort`  
**Target unit:** person-hours

| Column | Meaning |
|---|---|
| `id` | Dataset record identifier |
| `Project` | Project identifier |
| `TeamExp` | Team experience rating |
| `ManagerExp` | Manager experience rating |
| `YearEnd` | Year in which the project ended (two-digit year as supplied) |
| `Length` | Project duration/length measure as supplied by the dataset |
| `Effort` | Actual project effort in person-hours; prediction target |
| `Transactions` | Number of transactions |
| `Entities` | Number of entities |
| `PointsNonAdjust` | Unadjusted function points |
| `Adjustment` | Adjustment factor/percentage as supplied |
| `PointsAjust` | Adjusted function points |
| `Language` | Programming-language category code |

**Data-quality note:** The source notes four incomplete records (projects 38, 44, 66, and 75). Some experience fields use `-1` as a sentinel for unavailable information. Treat `-1` as missing in an analysis copy, and preserve the raw file unchanged. Do not assume the numeric language codes have an ordinal meaning.

## Cross-dataset cautions

- COCOMO-81 effort is in person-months; Desharnais effort is in person-hours.
- Dataset sizes are small (63 and 81 projects), so descriptive results and outlier flags should be interpreted cautiously.
- The notebook uses the IQR rule to flag potential outliers. A flagged record is not automatically an error and should not be deleted without investigation.
