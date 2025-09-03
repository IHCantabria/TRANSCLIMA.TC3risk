# TRANSCLIMA: Tropical cyclone risk, TC regions

This repository contains scripts and data structures to assess future tropical cyclone under climate change. 

Results of this codes can be found in and are 

---

## 📂 Folder Structure

### `1_Hazard/return_periods`
- Contains shape files of return periods for each historical and GCMs, which are the base data to calculate TC3hazard and classified administrative regions in TC regions

### `2_Exposure/`
- Includes exposure datasets of coastal population of 2020 + population growth under SSP5 sceenario between 2020 and 2050.

### `3_Adaptive_Capacity/`
- Contains AC indicators.

### `scripts/`
Python scripts for different steps of the workflow:
- **`01_hazard_individual_gcm.py`**: Processes hazard outputs from individual GCMs (Global Climate Models).
- **`02_hazard_ensemble.py`**: Combines hazard information across multiple GCMs into an ensemble product.
- **`03_TC3_risk.py`**: Estimates risk from tropical cyclones (Category 3 and above).
- **`04_statistics.py`**: Runs statistical analyses (uncertainty quantification, correlation, significance testing).

---

## ⚙️ Setup

### 1. Create Environment
```bash
conda env create -f environment.yml
conda activate STORM_env

### 1. Implementing the code
python scripts/01_hazard_individual_gcm.py
python scripts/02_hazard_ensemble.py
python 03_TC3_risk.py
python 04_statistics.py



## 👩‍💻 Developer

Name: [Itxaso Odériz]
Affiliation: [IHCantabria]
Contact: [itxaso.oderiz@unican.es]
GitHub: [@itxasoOderiz]


## Reference 
 Cite following references when you use or modify any data and routine belongs to this dataset.

      Oderiz, I.,  Losada, I.J., Hinkel, J. (2026). Global hotspots of unprecedented tropical cyclone risk for targeted adaptation
