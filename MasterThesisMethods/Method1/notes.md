# Datasets for Models

## Dataset for `model0` (M0)
- **Dataset name**: `BTC_high_labeled_dataset_m1.csv`
- **Start date**: `1609455600` (01.01.2021)
- **Periods**: 48 (each period represents 30 days, approximately 4 years)
- **Tickers**: `["BTCUSDT"]`
- **Options**: `["high", "low", "close", "volume"]`
- **Epochs**: `1`
- **Threshold**: `0.0`  
  - Example:  
    - If `BTCUSDT:close = 0.5 > 0.0`, then `label = 1`  
    - If `BTCUSDT:close = -0.5 < 0.0`, then `label = 0`
- **Predictor**: `BTCUSDT:close`

---

## Dataset for `model1` (M1)
- **Dataset name**: `BTC_high_labeled_dataset_m1.csv`
- **Start date**: `1609455600` (01.01.2021)
- **Periods**: 48 (each period represents 30 days, approximately 4 years)
- **Tickers**: `["BTCUSDT"]`
- **Options**: `["high", "low", "close", "volume"]`
- **Epochs**: `5`
- **Threshold**: `0.5`  
  - Example:  
    - If `BTCUSDT:close = 0.5 > 0.0`, then `label = 1`  
    - If `BTCUSDT:close = -0.5 < 0.0`, then `label = 0`
- **Predictor**: `BTCUSDT:high`

---

## Dataset for `model1_1` (M1.1)
- **Dataset name**: `SOL_high_labeled_dataset_m1.csv`
- **Start date**: `1609455600` (01.01.2021)
- **Periods**: 48 (each period represents 30 days, approximately 4 years)
- **Tickers**: `["SOLUSDT"]`
- **Options**: `["high", "low", "close", "volume"]`
- **Epochs**: `5`
- **Threshold**: `0.5`  
  - Example:  
    - If `BTCUSDT:close = 0.5 > 0.0`, then `label = 1`  
    - If `BTCUSDT:close = -0.5 < 0.0`, then `label = 0`
- **Predictor**: `SOLUSDT:high`
- **Time column**: `SOLUSDT:time`
- **Data structure**: `[]`

---

## Dataset for `model1_1_2` (M1.1.2)
- **Dataset name**: `SOL_high_labeled_dataset_m1_1.csv`
- **Start date**: `1609455600` (01.01.2021)
- **Periods**: 48 (each period represents 30 days, approximately 4 years)
- **Tickers**: `["SOLUSDT"]`
- **Options**: `["high", "low", "close", "volume"]`
- **Epochs**: `5`
- **Threshold**: `0.7`  
  - Example:  
    - If `BTCUSDT:close = 0.5 > 0.0`, then `label = 1`  
    - If `BTCUSDT:close = -0.5 < 0.0`, then `label = 0`
- **Predictor**: `SOLUSDT:high`
- **Time column**: `SOLUSDT:time`
- **Data structure**: `[]`

---

## Dataset for `model1_2` (M1.2)
- **Dataset name**: `LTC_high_labeled_dataset_m1_1.csv`
- **Start date**: `1483225200` (01.01.2017)
- **Periods**: 96 (each period represents 30 days, approximately 8 years)
- **Tickers**: `["LTCUSDT"]`
- **Options**: `["high", "low", "close", "volume"]`
- **Epochs**: `5`
- **Threshold**: `0.5`  
  - Example:  
    - If `BTCUSDT:close = 0.5 > 0.0`, then `label = 1`  
    - If `BTCUSDT:close = -0.5 < 0.0`, then `label = 0`
- **Predictor**: `LTCUSDT:high`
- **Time column**: `LTCUSDT:time`
- **Data structure**: `[]`