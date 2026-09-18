# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T05:38:06.238591Z`  
Current process started UTC: `2026-09-18T05:34:06.146703Z`  
1-second metadata polls in this process: **172**  
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

- `FUELINST|fuelType=INTVKL|generation` = **954** (n=937, 2026-09-18T05:35:27.811651Z)
- `FUELINST|fuelType=NPSHYD|generation` = **482** (n=937, 2026-09-18T05:35:27.811651Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=937, 2026-09-18T05:35:27.811651Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=937, 2026-09-18T05:35:27.811651Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=937, 2026-09-18T05:35:27.811651Z)
- `FUELINST|fuelType=OTHER|generation` = **819** (n=937, 2026-09-18T05:35:27.811651Z)
- `FUELINST|fuelType=PS|generation` = **296** (n=937, 2026-09-18T05:35:27.811651Z)
- `FUELINST|fuelType=WIND|generation` = **13803** (n=937, 2026-09-18T05:35:27.811651Z)
- `IMBALNGC|TOTAL|imbalance` = **10704** (n=155, 2026-09-18T05:20:21.081324Z)
- `INDDEM|TOTAL|demand` = **-11169** (n=155, 2026-09-18T05:20:21.081324Z)
- `INDGEN|TOTAL|generation` = **27518** (n=155, 2026-09-18T05:20:21.081324Z)
- `MELNGC|TOTAL|margin` = **38019** (n=155, 2026-09-18T05:19:16.747972Z)
- `NDF|TOTAL|demand` = **16314** (n=158, 2026-09-18T05:17:26.772425Z)
- `TSDF|TOTAL|demand` = **16814** (n=158, 2026-09-18T05:17:26.772425Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T05:38:04.932838Z` — **MID**: 0 rows; marker `2026-09-18T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:38:03.603519Z` — **MID**: 0 rows; marker `2026-09-18T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:38:02.280708Z` — **MID**: 0 rows; marker `2026-09-18T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:38:00.971578Z` — **MID**: 0 rows; marker `2026-09-18T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:37:59.645210Z` — **MID**: 0 rows; marker `2026-09-18T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:37:58.387451Z` — **MID**: 0 rows; marker `2026-09-18T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:37:57.077782Z` — **MID**: 0 rows; marker `2026-09-18T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:37:55.307178Z` — **MID**: 0 rows; marker `2026-09-18T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:37:53.970981Z` — **MID**: 0 rows; marker `2026-09-18T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:37:52.665463Z` — **MID**: 0 rows; marker `2026-09-18T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:37:51.349806Z` — **MID**: 0 rows; marker `2026-09-18T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:37:50.042656Z` — **MID**: 0 rows; marker `2026-09-18T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:37:48.699644Z` — **MID**: 0 rows; marker `2026-09-18T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:37:47.378607Z` — **MID**: 0 rows; marker `2026-09-18T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:37:46.060444Z` — **MID**: 0 rows; marker `2026-09-18T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
