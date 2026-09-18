# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T09:47:28.616789Z`  
Current process started UTC: `2026-09-18T09:43:27.759272Z`  
1-second metadata polls in this process: **174**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=987, 2026-09-18T09:45:39.969749Z)
- `FUELINST|fuelType=NPSHYD|generation` = **345** (n=987, 2026-09-18T09:45:39.969749Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=987, 2026-09-18T09:45:39.969749Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=987, 2026-09-18T09:45:39.969749Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=987, 2026-09-18T09:45:39.969749Z)
- `FUELINST|fuelType=OTHER|generation` = **835** (n=987, 2026-09-18T09:45:39.969749Z)
- `FUELINST|fuelType=PS|generation` = **-423** (n=987, 2026-09-18T09:45:39.969749Z)
- `FUELINST|fuelType=WIND|generation` = **11847** (n=987, 2026-09-18T09:45:39.969749Z)
- `IMBALNGC|TOTAL|imbalance` = **8100** (n=162, 2026-09-18T09:20:18.018457Z)
- `INDDEM|TOTAL|demand` = **-13185** (n=162, 2026-09-18T09:19:45.552785Z)
- `INDGEN|TOTAL|generation` = **27193** (n=162, 2026-09-18T09:19:45.552785Z)
- `MELNGC|TOTAL|margin` = **36209** (n=162, 2026-09-18T09:19:13.657509Z)
- `NDF|TOTAL|demand` = **16454** (n=167, 2026-09-18T09:47:20.937653Z)
- `TSDF|TOTAL|demand` = **19093** (n=167, 2026-09-18T09:47:20.937653Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T09:47:27.432832Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:47:26.060607Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:47:24.468062Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:47:20.937653Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:47:20.937653Z` — **TSDF**: 648 rows; marker `2026-09-18T09:46:00Z`
- `2026-09-18T09:47:20.937653Z` — **NDF**: 36 rows; marker `2026-09-18T09:46:00Z`
- `2026-09-18T09:47:19.124286Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:47:17.741599Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:47:16.163028Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:47:14.996313Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:47:13.783391Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:47:12.475267Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:47:11.268031Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:47:10.035273Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:47:08.662985Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
