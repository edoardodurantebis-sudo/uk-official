# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T08:39:24.029529Z`  
Current process started UTC: `2026-09-19T08:35:22.992090Z`  
1-second metadata polls in this process: **224**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-10744, delta=3052, z=1.92 -> demand pressure up
- **WINDFOR** `TOTAL` `generation` — wind forecast [TOTAL] generation: value=7845, delta=-11023, z=-4.38 -> renewable cushion down / residual-load pressure up
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=80, delta=-38, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=97, delta=-21, z=4.20 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.28 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=118, delta=27, z=6.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.70 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=-1, z=5.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=0, z=6.01 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=91, delta=9, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=11, z=6.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=108, delta=29, z=5.66 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **910** (n=1217, 2026-09-19T08:35:22.992097Z)
- `FUELINST|fuelType=NPSHYD|generation` = **367** (n=1217, 2026-09-19T08:35:22.992097Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1217, 2026-09-19T08:35:22.992097Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1217, 2026-09-19T08:35:22.992097Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1217, 2026-09-19T08:35:22.992097Z)
- `FUELINST|fuelType=OTHER|generation` = **326** (n=1217, 2026-09-19T08:35:22.992097Z)
- `FUELINST|fuelType=PS|generation` = **-422** (n=1217, 2026-09-19T08:35:22.992097Z)
- `FUELINST|fuelType=WIND|generation` = **15103** (n=1217, 2026-09-19T08:35:22.992097Z)
- `IMBALNGC|TOTAL|imbalance` = **8998** (n=200, 2026-09-19T08:19:37.431448Z)
- `INDDEM|TOTAL|demand` = **-12081** (n=200, 2026-09-19T08:19:21.440084Z)
- `INDGEN|TOTAL|generation` = **26793** (n=200, 2026-09-19T08:19:21.440084Z)
- `MELNGC|TOTAL|margin` = **37615** (n=200, 2026-09-19T08:18:31.551947Z)
- `NDF|TOTAL|demand` = **15940** (n=205, 2026-09-19T08:17:14.399276Z)
- `TSDF|TOTAL|demand` = **17802** (n=205, 2026-09-19T08:17:14.399276Z)
- `WINDFOR|TOTAL|generation` = **6987** (n=35, 2026-09-19T08:30:39.402179Z)

## Latest publication events

- `2026-09-19T08:39:22.661948Z` — **MID**: 0 rows; marker `2026-09-19T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:39:21.658774Z` — **MID**: 0 rows; marker `2026-09-19T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:39:20.632546Z` — **MID**: 0 rows; marker `2026-09-19T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:39:19.578642Z` — **MID**: 0 rows; marker `2026-09-19T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:39:18.527772Z` — **MID**: 0 rows; marker `2026-09-19T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:39:17.494039Z` — **MID**: 0 rows; marker `2026-09-19T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:39:16.463200Z` — **MID**: 0 rows; marker `2026-09-19T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:39:15.463132Z` — **MID**: 0 rows; marker `2026-09-19T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:39:14.430291Z` — **MID**: 0 rows; marker `2026-09-19T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:39:13.367350Z` — **MID**: 0 rows; marker `2026-09-19T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:39:12.340186Z` — **MID**: 0 rows; marker `2026-09-19T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:39:11.317432Z` — **MID**: 0 rows; marker `2026-09-19T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:39:10.317361Z` — **MID**: 0 rows; marker `2026-09-19T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:39:09.301230Z` — **MID**: 0 rows; marker `2026-09-19T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:39:08.284834Z` — **MID**: 0 rows; marker `2026-09-19T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
