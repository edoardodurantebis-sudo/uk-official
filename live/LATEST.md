# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T17:42:43.023021Z`  
Current process started UTC: `2026-09-18T17:38:42.553743Z`  
1-second metadata polls in this process: **222**  
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

- `FUELINST|fuelType=INTVKL|generation` = **763** (n=1059, 2026-09-18T17:40:33.709584Z)
- `FUELINST|fuelType=NPSHYD|generation` = **455** (n=1059, 2026-09-18T17:40:33.709584Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1059, 2026-09-18T17:40:33.709584Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=1059, 2026-09-18T17:40:33.709584Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1059, 2026-09-18T17:40:33.709584Z)
- `FUELINST|fuelType=OTHER|generation` = **1634** (n=1059, 2026-09-18T17:40:33.709584Z)
- `FUELINST|fuelType=PS|generation` = **678** (n=1059, 2026-09-18T17:40:33.709584Z)
- `FUELINST|fuelType=WIND|generation` = **16923** (n=1059, 2026-09-18T17:40:33.709584Z)
- `IMBALNGC|TOTAL|imbalance` = **8521** (n=174, 2026-09-18T15:23:28.385039Z)
- `INDDEM|TOTAL|demand` = **-10767** (n=174, 2026-09-18T15:23:10.555240Z)
- `INDGEN|TOTAL|generation` = **25571** (n=174, 2026-09-18T15:23:28.385039Z)
- `MELNGC|TOTAL|margin` = **38024** (n=174, 2026-09-18T15:20:56.613821Z)
- `NDF|TOTAL|demand` = **16550** (n=178, 2026-09-18T15:18:18.353381Z)
- `TSDF|TOTAL|demand` = **17050** (n=178, 2026-09-18T15:18:18.353381Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T17:42:42.016539Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T17:42:41.002059Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T17:42:39.564415Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T17:42:38.535548Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T17:42:37.535430Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T17:42:36.522557Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T17:42:35.503637Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T17:42:34.482118Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T17:42:33.477149Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T17:42:32.459978Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T17:42:31.447906Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T17:42:30.435260Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T17:42:29.416220Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T17:42:28.406044Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T17:42:27.371746Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
