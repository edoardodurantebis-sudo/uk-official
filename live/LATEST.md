# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T12:23:31.969231Z`  
Current process started UTC: `2026-09-18T12:19:30.897619Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **1389** (n=1018, 2026-09-18T12:20:35.485089Z)
- `FUELINST|fuelType=NPSHYD|generation` = **317** (n=1018, 2026-09-18T12:20:35.485089Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1018, 2026-09-18T12:20:35.485089Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1018, 2026-09-18T12:20:35.485089Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1018, 2026-09-18T12:20:35.485089Z)
- `FUELINST|fuelType=OTHER|generation` = **554** (n=1018, 2026-09-18T12:20:35.485089Z)
- `FUELINST|fuelType=PS|generation` = **-710** (n=1018, 2026-09-18T12:20:35.485089Z)
- `FUELINST|fuelType=WIND|generation` = **14462** (n=1018, 2026-09-18T12:20:35.485089Z)
- `IMBALNGC|TOTAL|imbalance` = **8949** (n=167, 2026-09-18T11:55:35.709657Z)
- `INDDEM|TOTAL|demand` = **-10744** (n=167, 2026-09-18T11:55:20.118979Z)
- `INDGEN|TOTAL|generation` = **25619** (n=167, 2026-09-18T11:55:20.118979Z)
- `MELNGC|TOTAL|margin` = **38104** (n=168, 2026-09-18T12:21:55.537431Z)
- `NDF|TOTAL|demand` = **16170** (n=172, 2026-09-18T12:19:30.897632Z)
- `TSDF|TOTAL|demand` = **16670** (n=172, 2026-09-18T12:19:30.897632Z)
- `WINDFOR|TOTAL|generation` = **7615** (n=29, 2026-09-18T10:30:46.506872Z)

## Latest publication events

- `2026-09-18T12:23:30.580369Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:23:29.580304Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:23:28.580199Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:23:27.580092Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:23:26.579996Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:23:25.579937Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:23:24.579816Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:23:23.579709Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:23:22.579632Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:23:21.579567Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:23:20.579498Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:23:19.579426Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:23:18.579401Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:23:17.579333Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:23:16.406947Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
