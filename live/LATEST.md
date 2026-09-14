# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T21:43:12.971383Z`  
Current process started UTC: `2026-09-14T21:39:12.432520Z`  
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

- `FUELINST|fuelType=INTNSL|generation` = **883** (n=9, 2026-09-14T21:40:49.827152Z)
- `FUELINST|fuelType=INTVKL|generation` = **-1082** (n=9, 2026-09-14T21:40:49.827152Z)
- `FUELINST|fuelType=NPSHYD|generation` = **446** (n=9, 2026-09-14T21:40:49.827152Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=9, 2026-09-14T21:40:49.827152Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=9, 2026-09-14T21:40:49.827152Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=9, 2026-09-14T21:40:49.827152Z)
- `FUELINST|fuelType=OTHER|generation` = **98** (n=9, 2026-09-14T21:40:49.827152Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=9, 2026-09-14T21:40:49.827152Z)
- `FUELINST|fuelType=WIND|generation` = **12948** (n=9, 2026-09-14T21:40:49.827152Z)
- `IMBALNGC|TOTAL|imbalance` = **-29** (n=2, 2026-09-14T21:34:59.351255Z)
- `INDDEM|TOTAL|demand` = **-12253** (n=2, 2026-09-14T21:34:59.351255Z)
- `INDGEN|TOTAL|generation` = **20456** (n=2, 2026-09-14T21:34:59.351255Z)
- `MELNGC|TOTAL|margin` = **32198** (n=2, 2026-09-14T21:34:59.351255Z)
- `NDF|TOTAL|demand` = **19934** (n=2, 2026-09-14T21:34:59.351255Z)
- `TSDF|TOTAL|demand` = **20485** (n=2, 2026-09-14T21:34:59.351255Z)

## Latest publication events

- `2026-09-14T21:42:10.040791Z` — **MID**: 0 rows; marker `2026-09-14T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T21:42:10.040791Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:41:45Z`
- `2026-09-14T21:40:49.827152Z` — **FUELINST**: 80 rows; marker `2026-09-14T21:40:00Z`
- `2026-09-14T21:40:17.441090Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:39:45Z`
- `2026-09-14T21:38:10.064473Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:37:45Z`
- `2026-09-14T21:37:22.483234Z` — **MID**: 0 rows; marker `2026-09-14T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T21:36:18.569980Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:35:45Z`
- `2026-09-14T21:35:31.233858Z` — **FUELINST**: 80 rows; marker `2026-09-14T21:35:00Z`
- `2026-09-14T21:34:59.351255Z` — **MID**: 0 rows; marker `2026-09-14T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T21:34:59.351255Z` — **MELNGC**: 1098 rows; marker `2026-09-14T21:17:00Z`
- `2026-09-14T21:34:59.351255Z` — **INDGEN**: 1098 rows; marker `2026-09-14T21:17:00Z`
- `2026-09-14T21:34:59.351255Z` — **INDDEM**: 1098 rows; marker `2026-09-14T21:17:00Z`
- `2026-09-14T21:34:59.351255Z` — **IMBALNGC**: 1098 rows; marker `2026-09-14T21:17:00Z`
- `2026-09-14T21:34:59.351255Z` — **TSDF**: 1098 rows; marker `2026-09-14T21:17:00Z`
- `2026-09-14T21:34:59.351255Z` — **NDF**: 61 rows; marker `2026-09-14T21:17:00Z`
