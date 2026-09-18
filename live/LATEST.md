# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T18:58:51.199174Z`  
Current process started UTC: `2026-09-18T18:54:50.204202Z`  
1-second metadata polls in this process: **134**  
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

- `FUELINST|fuelType=INTVKL|generation` = **943** (n=1074, 2026-09-18T18:55:21.869936Z)
- `FUELINST|fuelType=NPSHYD|generation` = **492** (n=1074, 2026-09-18T18:55:21.869936Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1074, 2026-09-18T18:55:21.869936Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1074, 2026-09-18T18:55:21.869936Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1074, 2026-09-18T18:55:21.869936Z)
- `FUELINST|fuelType=OTHER|generation` = **1413** (n=1074, 2026-09-18T18:55:21.869936Z)
- `FUELINST|fuelType=PS|generation` = **294** (n=1074, 2026-09-18T18:55:21.869936Z)
- `FUELINST|fuelType=WIND|generation` = **16608** (n=1074, 2026-09-18T18:55:21.869936Z)
- `IMBALNGC|TOTAL|imbalance` = **9037** (n=177, 2026-09-18T18:53:19.505898Z)
- `INDDEM|TOTAL|demand` = **-10885** (n=177, 2026-09-18T18:53:19.505898Z)
- `INDGEN|TOTAL|generation` = **26231** (n=177, 2026-09-18T18:53:19.505898Z)
- `MELNGC|TOTAL|margin` = **37526** (n=177, 2026-09-18T18:50:36.144384Z)
- `NDF|TOTAL|demand` = **16550** (n=181, 2026-09-18T18:48:17.389891Z)
- `TSDF|TOTAL|demand` = **17194** (n=181, 2026-09-18T18:48:17.389891Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T18:58:49.159479Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:58:47.442804Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:58:45.753556Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:58:44.052188Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:58:42.353185Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:58:40.654070Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:58:38.961094Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:58:37.269972Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:58:35.555011Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:58:33.378406Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:58:31.695412Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:58:29.998735Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:58:28.293265Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:58:26.602396Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:58:24.910286Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
