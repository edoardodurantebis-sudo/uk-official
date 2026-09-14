# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T22:04:09.611535Z`  
Current process started UTC: `2026-09-14T22:00:09.983463Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=279, delta=-26, z=-14.31 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTNSL|generation` = **1015** (n=13, 2026-09-14T22:00:26.225522Z)
- `FUELINST|fuelType=INTVKL|generation` = **-986** (n=13, 2026-09-14T22:00:26.225522Z)
- `FUELINST|fuelType=NPSHYD|generation` = **454** (n=13, 2026-09-14T22:00:26.225522Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3314** (n=13, 2026-09-14T22:00:26.225522Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=13, 2026-09-14T22:00:26.225522Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=13, 2026-09-14T22:00:26.225522Z)
- `FUELINST|fuelType=OTHER|generation` = **101** (n=13, 2026-09-14T22:00:26.225522Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=13, 2026-09-14T22:00:26.225522Z)
- `FUELINST|fuelType=WIND|generation` = **12733** (n=13, 2026-09-14T22:00:26.225522Z)
- `IMBALNGC|TOTAL|imbalance` = **-15** (n=3, 2026-09-14T21:51:44.824674Z)
- `INDDEM|TOTAL|demand` = **-12253** (n=3, 2026-09-14T21:51:44.824674Z)
- `INDGEN|TOTAL|generation` = **20469** (n=3, 2026-09-14T21:51:44.824674Z)
- `MELNGC|TOTAL|margin` = **32283** (n=3, 2026-09-14T21:50:04.672506Z)
- `NDF|TOTAL|demand` = **19934** (n=3, 2026-09-14T21:47:57.557399Z)
- `TSDF|TOTAL|demand` = **20485** (n=3, 2026-09-14T21:47:57.557399Z)

## Latest publication events

- `2026-09-14T22:02:19.801410Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:01:45Z`
- `2026-09-14T22:00:58.473805Z` — **FUELHH**: 20 rows; marker `2026-09-14T22:00:00Z`
- `2026-09-14T22:00:26.225522Z` — **FUELINST**: 80 rows; marker `2026-09-14T22:00:00Z`
- `2026-09-14T22:00:26.225522Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:59:45Z`
- `2026-09-14T21:58:22.313211Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:57:45Z`
- `2026-09-14T21:56:13.927850Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:55:45Z`
- `2026-09-14T21:55:29.481531Z` — **FUELINST**: 80 rows; marker `2026-09-14T21:55:00Z`
- `2026-09-14T21:54:08.255213Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:53:45Z`
- `2026-09-14T21:52:16.755149Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:51:45Z`
- `2026-09-14T21:51:44.824674Z` — **INDGEN**: 1080 rows; marker `2026-09-14T21:47:00Z`
- `2026-09-14T21:51:44.824674Z` — **INDDEM**: 1080 rows; marker `2026-09-14T21:47:00Z`
- `2026-09-14T21:51:44.824674Z` — **IMBALNGC**: 1080 rows; marker `2026-09-14T21:47:00Z`
- `2026-09-14T21:50:36.114375Z` — **FUELINST**: 80 rows; marker `2026-09-14T21:50:00Z`
- `2026-09-14T21:50:20.677033Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:49:45Z`
- `2026-09-14T21:50:04.672506Z` — **MELNGC**: 1080 rows; marker `2026-09-14T21:47:00Z`
