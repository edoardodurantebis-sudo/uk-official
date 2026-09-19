# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T12:23:39.096643Z`  
Current process started UTC: `2026-09-19T12:19:38.717330Z`  
1-second metadata polls in this process: **224**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16749, delta=-28, z=-3.66 -> state changed
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16777, delta=25, z=-3.78 -> state changed
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16752, delta=-9313, z=-3.94 -> state changed
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **161** (n=1262, 2026-09-19T12:20:27.906867Z)
- `FUELINST|fuelType=NPSHYD|generation` = **283** (n=1262, 2026-09-19T12:20:27.906867Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3323** (n=1262, 2026-09-19T12:20:27.906867Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1262, 2026-09-19T12:20:27.906867Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1262, 2026-09-19T12:20:27.906867Z)
- `FUELINST|fuelType=OTHER|generation` = **496** (n=1262, 2026-09-19T12:20:27.906867Z)
- `FUELINST|fuelType=PS|generation` = **-617** (n=1262, 2026-09-19T12:20:27.906867Z)
- `FUELINST|fuelType=WIND|generation` = **15327** (n=1262, 2026-09-19T12:20:27.906867Z)
- `IMBALNGC|TOTAL|imbalance` = **-3260** (n=207, 2026-09-19T11:54:43.988227Z)
- `INDDEM|TOTAL|demand` = **-11780** (n=207, 2026-09-19T11:54:43.988227Z)
- `INDGEN|TOTAL|generation` = **16749** (n=207, 2026-09-19T11:54:43.988227Z)
- `MELNGC|TOTAL|margin` = **36757** (n=208, 2026-09-19T12:20:45.809462Z)
- `NDF|TOTAL|demand` = **19509** (n=213, 2026-09-19T12:18:29.074439Z)
- `TSDF|TOTAL|demand` = **20009** (n=213, 2026-09-19T12:18:29.074439Z)
- `WINDFOR|TOTAL|generation` = **6656** (n=36, 2026-09-19T10:30:47.910212Z)

## Latest publication events

- `2026-09-19T12:23:38.072511Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:23:37.072375Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:23:36.072213Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:23:35.072064Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:23:34.071932Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:23:33.071832Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:23:32.071702Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:23:31.071565Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:23:30.071435Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:23:29.071300Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:23:27.517390Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:23:26.517240Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:23:25.517102Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:23:24.516968Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:23:23.516872Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
