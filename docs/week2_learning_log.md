
# Week 2 Learning Log: Baseline Estimators

## 1. Objective

The objective of Week 2 was to establish baseline models that future
machine learning models must outperform.

The project implemented Mean, Median, and size-based estimators,
along with MAE, MMRE, and Pred(25) evaluation metrics.

## 2. Baseline Estimators

Three types of baseline approaches were evaluated:

- Mean Baseline: predicts the average effort from the training data.
- Median Baseline: predicts the median effort from the training data.
- Size-Based Baseline:
  - COCOMO81: Basic COCOMO using project size (KLOC) and development mode.
  - Desharnais: a size-to-effort ratio learned from training data.

## 3. Evaluation Method

An 80/20 train/test split was used with random_state=42.

The datasets were evaluated separately because their effort units
are different:

- COCOMO81: person-months.
- Desharnais: person-hours.

Only training data was used to calculate the Mean, Median, and
Desharnais size-ratio coefficient.

## 4. Evaluation Metrics

- MAE (Mean Absolute Error): measures the average absolute difference
  between actual and predicted effort.
- MMRE (Mean Magnitude of Relative Error): measures average relative
  prediction error.
- Pred(25): measures the percentage of predictions whose relative
  error is 25% or less.

## 5. Results

### COCOMO81

| Estimator | MAE | MMRE (%) | Pred(25) (%) |
|---|---:|---:|---:|
| Mean | 676.700 | 2350.318 | 7.692 |
| Median | 293.769 | 308.271 | 7.692 |
| Basic COCOMO | 171.926 | 73.148 | 23.077 |

Basic COCOMO achieved the lowest MAE and MMRE and the highest
Pred(25) among the three COCOMO81 baselines.

### Desharnais

| Estimator | MAE | MMRE (%) | Pred(25) (%) |
|---|---:|---:|---:|
| Mean | 2796.683 | 187.246 | 29.412 |
| Median | 2715.412 | 128.824 | 17.647 |
| Size Ratio | 1730.825 | 82.049 | 35.294 |

The Size Ratio estimator achieved the lowest MAE and MMRE and
the highest Pred(25) among the Desharnais baselines.

## 6. Discussion

The results show that size-based estimation performed better than
the simple Mean and Median baselines on this test split.

Basic COCOMO provided the strongest results for COCOMO81.
The size-ratio approach provided the strongest results for
Desharnais.

However, the MMRE values indicate that prediction errors remain
substantial. The results should not be treated as proof of strong
generalization because each dataset was evaluated using one
train/test split.

The datasets are relatively small, so additional validation would
be useful in future work.

## 7. Limitations

- The datasets contain only 63 and 81 projects.
- Results depend on the selected train/test split.
- COCOMO81 effort is measured in person-months, while Desharnais
  effort is measured in person-hours.
- Raw MAE values should not be compared across the two datasets.
- A single test split does not establish how well a model will
  perform on unseen future projects.

## 8. Learning Outcomes

During Week 2, I learned:

1. How Mean and Median baselines work.
2. How Basic COCOMO estimates software development effort.
3. How to build a size-based estimator using training data.
4. How to calculate MAE, MMRE, and Pred(25).
5. How to separate training and testing data.
6. How to compare baseline models using a results table.
7. How to write unit tests for evaluation metrics.

## 9. Conclusion

Week 2 established the baseline performance for both datasets.
These results will serve as a reference for evaluating the
regression models developed in Week 3.
