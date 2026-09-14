# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T21:55:44.816552Z`  
Current process started UTC: `2026-09-14T21:51:44.824662Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

No qualified anomaly yet (series are warming up or no threshold was crossed).

## Latest market values

- `FUELINST|fuelType=INTNSL|generation` = **925** (n=12, 2026-09-14T21:55:29.481531Z)
- `FUELINST|fuelType=INTVKL|generation` = **-1082** (n=12, 2026-09-14T21:55:29.481531Z)
- `FUELINST|fuelType=NPSHYD|generation` = **454** (n=12, 2026-09-14T21:55:29.481531Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3318** (n=12, 2026-09-14T21:55:29.481531Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=12, 2026-09-14T21:55:29.481531Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=12, 2026-09-14T21:55:29.481531Z)
- `FUELINST|fuelType=OTHER|generation` = **109** (n=12, 2026-09-14T21:55:29.481531Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=12, 2026-09-14T21:55:29.481531Z)
- `FUELINST|fuelType=WIND|generation` = **12829** (n=12, 2026-09-14T21:55:29.481531Z)
- `IMBALNGC|TOTAL|imbalance` = **-15** (n=3, 2026-09-14T21:51:44.824674Z)
- `INDDEM|TOTAL|demand` = **-12253** (n=3, 2026-09-14T21:51:44.824674Z)
- `INDGEN|TOTAL|generation` = **20469** (n=3, 2026-09-14T21:51:44.824674Z)
- `MELNGC|TOTAL|margin` = **32283** (n=3, 2026-09-14T21:50:04.672506Z)
- `NDF|TOTAL|demand` = **19934** (n=3, 2026-09-14T21:47:57.557399Z)
- `TSDF|TOTAL|demand` = **20485** (n=3, 2026-09-14T21:47:57.557399Z)

## Latest publication events

- `2026-09-14T21:55:29.481531Z` — **FUELINST**: 80 rows; marker `2026-09-14T21:55:00Z`
- `2026-09-14T21:54:08.255213Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:53:45Z`
- `2026-09-14T21:52:16.755149Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:51:45Z`
- `2026-09-14T21:51:44.824674Z` — **INDGEN**: 1080 rows; marker `2026-09-14T21:47:00Z`
- `2026-09-14T21:51:44.824674Z` — **INDDEM**: 1080 rows; marker `2026-09-14T21:47:00Z`
- `2026-09-14T21:51:44.824674Z` — **IMBALNGC**: 1080 rows; marker `2026-09-14T21:47:00Z`
- `2026-09-14T21:50:36.114375Z` — **FUELINST**: 80 rows; marker `2026-09-14T21:50:00Z`
- `2026-09-14T21:50:20.677033Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:49:45Z`
- `2026-09-14T21:50:04.672506Z` — **MELNGC**: 1080 rows; marker `2026-09-14T21:47:00Z`
- `2026-09-14T21:48:13.192177Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:47:45Z`
- `2026-09-14T21:47:57.557399Z` — **TSDF**: 1080 rows; marker `2026-09-14T21:47:00Z`
- `2026-09-14T21:47:57.557399Z` — **NDF**: 60 rows; marker `2026-09-14T21:47:00Z`
- `2026-09-14T21:46:21.017634Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:45:45Z`
- `2026-09-14T21:45:32.692059Z` — **FUELINST**: 80 rows; marker `2026-09-14T21:45:00Z`
- `2026-09-14T21:44:13.031685Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:43:45Z`
