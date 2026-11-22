# Week 3: Cross-Validation Results

Evaluation uses Leave-One-Out Cross-Validation (LOOCV). All estimators use identical held-out folds.

| Dataset    | Estimator           |   Projects |      MAE |   MMRE (%) |   Pred(25) (%) |
|:-----------|:--------------------|-----------:|---------:|-----------:|---------------:|
| COCOMO81   | Mean Baseline       |         63 |  906.022 |  1850.84   |        4.7619  |
| COCOMO81   | Median Baseline     |         63 |  647.076 |   252.462  |       11.1111  |
| COCOMO81   | Size-Based Baseline |         63 |  553.105 |    69.8803 |       28.5714  |
| COCOMO81   | Ridge Regression    |         63 |  995.53  |  2343.82   |        6.34921 |
| COCOMO81   | Random Forest       |         63 |  560.504 |   177.981  |       17.4603  |
| COCOMO81   | Gradient Boosting   |         63 |  465.887 |   187.075  |       17.4603  |
| Desharnais | Mean Baseline       |         81 | 3201.04  |   123.176  |       18.5185  |
| Desharnais | Median Baseline     |         81 | 2912.65  |    85.4044 |       25.9259  |
| Desharnais | Size-Based Baseline |         81 | 2050.18  |    66.4007 |       43.2099  |
| Desharnais | Ridge Regression    |         81 | 2054.73  |    64.8745 |       32.0988  |
| Desharnais | Random Forest       |         81 | 2149.55  |    60.4983 |       34.5679  |
| Desharnais | Gradient Boosting   |         81 | 1966.03  |    49.4885 |       38.2716  |
