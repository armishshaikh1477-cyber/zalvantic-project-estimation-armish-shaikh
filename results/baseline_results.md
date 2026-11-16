# Week 2 Baseline Evaluation Results

Train/test split: 80/20, random_state=42

| Dataset    | Estimator    |   Train Projects |   Test Projects |      MAE |   MMRE (%) |   Pred(25) (%) | Effort Unit   |
|:-----------|:-------------|-----------------:|----------------:|---------:|-----------:|---------------:|:--------------|
| COCOMO81   | Mean         |               50 |              13 |  676.7   |   2350.32  |          7.692 | person-months |
| COCOMO81   | Median       |               50 |              13 |  293.769 |    308.271 |          7.692 | person-months |
| COCOMO81   | Basic COCOMO |               50 |              13 |  171.926 |     73.148 |         23.077 | person-months |
| Desharnais | Mean         |               64 |              17 | 2796.68  |    187.246 |         29.412 | person-hours  |
| Desharnais | Median       |               64 |              17 | 2715.41  |    128.824 |         17.647 | person-hours  |
| Desharnais | Size Ratio   |               64 |              17 | 1730.83  |     82.049 |         35.294 | person-hours  |
