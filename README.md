# Identifying and Evaluating Predictors of wOBA for MLB Hitters
A sabermetrics project

## Overview
### Research Question: Which offensive metrics best predict offensive performance for MLB hitters?
This project evaluates and identifies the metrics that are the most effective predictors of overall offensive performance for MLB hitters. Offensive metrics from season *t* will be evaluated as predictors for season *t+1*. Multi-season aggregation may be explored in future work. 

### Target Metric 
[wOBA](https://library.fangraphs.com/offense/woba/) was chosen as the target metric because it is a rate-based measure that is less dependent on plate appearances than counting metrics such as wRAA or wRC. 

### Data
All data for this project is sourced from the [*pybaseball*](https://github.com/jldbc/pybaseball) Python package and consists of season-level statistics for individual MLB hitters.

## Research Plan
1. Collect and clean season-level batting data from the 2024 and 2025 MLB seasons.
2. Identify and apply a minimum plate appearance threshold.
3. Analyze year-to-year stability of offensive metrics.  
4. Examine correlations between stable 2024 metrics and 2025 wOBA.
5. Evaluate candidate metrics using simple regression models trained on 2024 data and tested on 2025 data.
6. Interpret metric effectiveness in terms of stability and predictive power.

## Project Status
- [x] Identify data source
- [x] Select target metric
- [x] Collect and clean data
- [x] Apply plate appearance threshold
- [ ] Analyze metric stability and correlation
- [ ] Create models and evaluate
- [ ] Interpret and share results