# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T12:06:06.840537Z`  
Current process started UTC: `2026-09-18T12:02:06.640720Z`  
1-second metadata polls in this process: **160**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1399** (n=1015, 2026-09-18T12:05:37.262329Z)
- `FUELINST|fuelType=NPSHYD|generation` = **324** (n=1015, 2026-09-18T12:05:37.262329Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1015, 2026-09-18T12:05:37.262329Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1015, 2026-09-18T12:05:37.262329Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1015, 2026-09-18T12:05:37.262329Z)
- `FUELINST|fuelType=OTHER|generation` = **536** (n=1015, 2026-09-18T12:05:37.262329Z)
- `FUELINST|fuelType=PS|generation` = **-719** (n=1015, 2026-09-18T12:05:37.262329Z)
- `FUELINST|fuelType=WIND|generation` = **13886** (n=1015, 2026-09-18T12:05:37.262329Z)
- `IMBALNGC|TOTAL|imbalance` = **8949** (n=167, 2026-09-18T11:55:35.709657Z)
- `INDDEM|TOTAL|demand` = **-10744** (n=167, 2026-09-18T11:55:20.118979Z)
- `INDGEN|TOTAL|generation` = **25619** (n=167, 2026-09-18T11:55:20.118979Z)
- `MELNGC|TOTAL|margin` = **38104** (n=167, 2026-09-18T11:52:16.190142Z)
- `NDF|TOTAL|demand` = **16170** (n=171, 2026-09-18T11:49:04.559776Z)
- `TSDF|TOTAL|demand` = **16670** (n=171, 2026-09-18T11:49:29.606738Z)
- `WINDFOR|TOTAL|generation` = **7615** (n=29, 2026-09-18T10:30:46.506872Z)

## Latest publication events

- `2026-09-18T12:06:05.531034Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:06:04.058327Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:06:02.698577Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:06:01.387612Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:06:00.119415Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:05:58.775029Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:05:57.468723Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:05:56.131977Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:05:53.905339Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:05:52.591746Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:05:50.816657Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:05:49.486496Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:05:48.208710Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:05:46.879959Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:05:45.575839Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
