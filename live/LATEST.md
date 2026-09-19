# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T10:08:44.123093Z`  
Current process started UTC: `2026-09-19T10:04:42.810538Z`  
1-second metadata polls in this process: **135**  
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

- `FUELINST|fuelType=INTVKL|generation` = **135** (n=1235, 2026-09-19T10:05:30.075263Z)
- `FUELINST|fuelType=NPSHYD|generation` = **302** (n=1235, 2026-09-19T10:05:30.075263Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=1235, 2026-09-19T10:05:30.075263Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1235, 2026-09-19T10:05:30.075263Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1235, 2026-09-19T10:05:30.075263Z)
- `FUELINST|fuelType=OTHER|generation` = **378** (n=1235, 2026-09-19T10:05:30.075263Z)
- `FUELINST|fuelType=PS|generation` = **-690** (n=1235, 2026-09-19T10:05:30.075263Z)
- `FUELINST|fuelType=WIND|generation` = **15748** (n=1235, 2026-09-19T10:05:30.075263Z)
- `IMBALNGC|TOTAL|imbalance` = **7793** (n=203, 2026-09-19T09:50:05.454220Z)
- `INDDEM|TOTAL|demand` = **-13214** (n=203, 2026-09-19T09:49:49.613301Z)
- `INDGEN|TOTAL|generation` = **26724** (n=203, 2026-09-19T09:49:49.613301Z)
- `MELNGC|TOTAL|margin` = **36451** (n=203, 2026-09-19T09:48:44.462675Z)
- `NDF|TOTAL|demand` = **15940** (n=208, 2026-09-19T09:47:30.580399Z)
- `TSDF|TOTAL|demand` = **18932** (n=208, 2026-09-19T09:47:30.580399Z)
- `WINDFOR|TOTAL|generation` = **6987** (n=35, 2026-09-19T08:30:39.402179Z)

## Latest publication events

- `2026-09-19T10:08:42.399971Z` — **MID**: 0 rows; marker `2026-09-19T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:08:40.074247Z` — **MID**: 0 rows; marker `2026-09-19T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:08:38.368835Z` — **MID**: 0 rows; marker `2026-09-19T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:08:36.684961Z` — **MID**: 0 rows; marker `2026-09-19T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:08:34.967340Z` — **MID**: 0 rows; marker `2026-09-19T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:08:33.268691Z` — **MID**: 0 rows; marker `2026-09-19T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:08:31.577486Z` — **MID**: 0 rows; marker `2026-09-19T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:08:29.881252Z` — **MID**: 0 rows; marker `2026-09-19T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:08:28.070388Z` — **MID**: 0 rows; marker `2026-09-19T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:08:24.094740Z` — **MID**: 0 rows; marker `2026-09-19T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:08:24.094740Z` — **FREQ**: 5761 rows; marker `2026-09-19T10:07:45Z`
- `2026-09-19T10:08:22.389712Z` — **MID**: 0 rows; marker `2026-09-19T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:08:20.648343Z` — **MID**: 0 rows; marker `2026-09-19T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:08:18.916616Z` — **MID**: 0 rows; marker `2026-09-19T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:08:17.175692Z` — **MID**: 0 rows; marker `2026-09-19T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
