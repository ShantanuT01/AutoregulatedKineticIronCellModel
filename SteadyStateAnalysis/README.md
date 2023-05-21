# Steady State Analysis

## Execution Order

1. `WanderingSteadyState.ipynb`
2. `WanderingTimeTransition.nb`
3. `SmoothnessScores.ipynb`
4. `ReasonableScores.ipynb`

## File Descriptions

| File                       | Description                                                                                                                                                                                             |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WanderingSteadyState.ipynb | Determines upper half of steady state transitions from CRMs using wandering filter.                                                                                                                     |
| WanderingTimeTransition.nb | Determines upper half of time transitions using wandering filter. Takes the intersection of the best steady state and time transitions. These CRMs are used for the next filter, the smoothness filter. |
| SmoothnessScores.ipynb     | Determines top 3 CRMs using the smoothneses filter.                                                                                                                                                     |
| ReasonableScores.ipynb     | Calculates n-SP reasonableness scores for the top 3 filters.                                                                                                                                            |