# TRANSCLIMA: Tropical Cyclone Risk, TC Regions

This repository contains scripts and data structures to assess **future tropical cyclone risk under climate change**.  

Results of these codes can be found in [ADD PUBLICATION OR DATA REPOSITORY LINK].

---

## Folder Structure

### `1_Hazard/return_periods`
- Contains shapefiles of return periods for each historical dataset and GCM, which serve as the base data to calculate **TC3 hazard**.
- Includes classified administrative regions in TC regions.

### `2_Exposure/`
- Exposure datasets of **coastal population in 2020**, plus population growth projections under the **SSP5 scenario (2020â€“2050)**.

### `3_Adaptive_Capacity/`
- Contains **adaptive capacity (AC) indicators**.

### `scripts/`
Python scripts for different steps of the workflow:
- **`01_hazard_individual_gcm.py`** â†’ Processes hazard outputs from individual GCMs (Global Climate Models).  
- **`02_hazard_ensemble.py`** â†’ Combines hazard information across multiple GCMs into an ensemble product.  
- **`03_TC3_risk.py`** â†’ Estimates risk from tropical cyclones (Category 3 and above).  
- **`04_statistics.py`** â†’ Runs statistical analyses (uncertainty quantification, correlation, significance testing).  

---

## Setup

### 1. Create Environment
```bash
conda env create -f environment.yml
conda activate STORM_env
```

### 2. Run Scripts
```bash
python scripts/01_hazard_individual_gcm.py
python scripts/02_hazard_ensemble.py
python scripts/03_TC3_risk.py
python scripts/04_statistics.py
```

---

## Developer

- **Name:** Itxaso Oderiz  
- **Affiliation:** IHCantabria  
- **Contact:** itxaso.oderiz@unican.es  
- **GitHub:** [@itxasoOderiz](https://github.com/itxasoOderiz)  

---

## Reference

Please cite the following reference when using or modifying any data and routines from this repository:

- Oderiz, I., Losada, I.J., & Hinkel, J. (2026). *Global hotspots of unprecedented tropical cyclone risk for targeted adaptation*. [Journal / Publisher â€” To be updated].  

---

