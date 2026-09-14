# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T21:51:34.436586Z`  
Current process started UTC: `2026-09-14T21:47:35.043699Z`  
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

- `FUELINST|fuelType=INTNSL|generation` = **883** (n=11, 2026-09-14T21:50:36.114375Z)
- `FUELINST|fuelType=INTVKL|generation` = **-1082** (n=11, 2026-09-14T21:50:36.114375Z)
- `FUELINST|fuelType=NPSHYD|generation` = **453** (n=11, 2026-09-14T21:50:36.114375Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3317** (n=11, 2026-09-14T21:50:36.114375Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=11, 2026-09-14T21:50:36.114375Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=11, 2026-09-14T21:50:36.114375Z)
- `FUELINST|fuelType=OTHER|generation` = **106** (n=11, 2026-09-14T21:50:36.114375Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=11, 2026-09-14T21:50:36.114375Z)
- `FUELINST|fuelType=WIND|generation` = **12934** (n=11, 2026-09-14T21:50:36.114375Z)
- `IMBALNGC|TOTAL|imbalance` = **-29** (n=2, 2026-09-14T21:34:59.351255Z)
- `INDDEM|TOTAL|demand` = **-12253** (n=2, 2026-09-14T21:34:59.351255Z)
- `INDGEN|TOTAL|generation` = **20456** (n=2, 2026-09-14T21:34:59.351255Z)
- `MELNGC|TOTAL|margin` = **32283** (n=3, 2026-09-14T21:50:04.672506Z)
- `NDF|TOTAL|demand` = **19934** (n=3, 2026-09-14T21:47:57.557399Z)
- `TSDF|TOTAL|demand` = **20485** (n=3, 2026-09-14T21:47:57.557399Z)

## Latest publication events

- `2026-09-14T21:50:36.114375Z` — **FUELINST**: 80 rows; marker `2026-09-14T21:50:00Z`
- `2026-09-14T21:50:20.677033Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:49:45Z`
- `2026-09-14T21:50:04.672506Z` — **MELNGC**: 1080 rows; marker `2026-09-14T21:47:00Z`
- `2026-09-14T21:48:13.192177Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:47:45Z`
- `2026-09-14T21:47:57.557399Z` — **TSDF**: 1080 rows; marker `2026-09-14T21:47:00Z`
- `2026-09-14T21:47:57.557399Z` — **NDF**: 60 rows; marker `2026-09-14T21:47:00Z`
- `2026-09-14T21:46:21.017634Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:45:45Z`
- `2026-09-14T21:45:32.692059Z` — **FUELINST**: 80 rows; marker `2026-09-14T21:45:00Z`
- `2026-09-14T21:44:13.031685Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:43:45Z`
- `2026-09-14T21:42:10.040791Z` — **MID**: 0 rows; marker `2026-09-14T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T21:42:10.040791Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:41:45Z`
- `2026-09-14T21:40:49.827152Z` — **FUELINST**: 80 rows; marker `2026-09-14T21:40:00Z`
- `2026-09-14T21:40:17.441090Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:39:45Z`
- `2026-09-14T21:38:10.064473Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:37:45Z`
- `2026-09-14T21:37:22.483234Z` — **MID**: 0 rows; marker `2026-09-14T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
