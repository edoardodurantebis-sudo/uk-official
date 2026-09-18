# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T22:19:10.578249Z`  
Current process started UTC: `2026-09-18T22:15:09.418903Z`  
1-second metadata polls in this process: **167**  
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

- `FUELINST|fuelType=INTVKL|generation` = **443** (n=1093, 2026-09-18T22:15:26.515476Z)
- `FUELINST|fuelType=NPSHYD|generation` = **445** (n=1093, 2026-09-18T22:15:26.515476Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1093, 2026-09-18T22:15:26.515476Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1093, 2026-09-18T22:15:26.515476Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1093, 2026-09-18T22:15:26.515476Z)
- `FUELINST|fuelType=OTHER|generation` = **953** (n=1093, 2026-09-18T22:15:26.515476Z)
- `FUELINST|fuelType=PS|generation` = **-637** (n=1093, 2026-09-18T22:15:26.515476Z)
- `FUELINST|fuelType=WIND|generation` = **16288** (n=1093, 2026-09-18T22:15:26.515476Z)
- `IMBALNGC|TOTAL|imbalance` = **8990** (n=180, 2026-09-18T21:52:19.139822Z)
- `INDDEM|TOTAL|demand` = **-10889** (n=180, 2026-09-18T21:52:19.139822Z)
- `INDGEN|TOTAL|generation` = **26185** (n=180, 2026-09-18T21:52:02.917847Z)
- `MELNGC|TOTAL|margin` = **37609** (n=180, 2026-09-18T21:50:11.622492Z)
- `NDF|TOTAL|demand` = **16550** (n=185, 2026-09-18T22:18:11.088451Z)
- `TSDF|TOTAL|demand` = **17194** (n=185, 2026-09-18T22:18:11.088451Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T22:19:09.294193Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:19:08.015789Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:19:06.707839Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:19:05.287145Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:19:03.938839Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:19:02.608311Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:19:01.241018Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:18:59.305806Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:18:58.023219Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:18:56.706495Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:18:55.345179Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:18:54.069099Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:18:52.705216Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:18:51.231648Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:18:49.908752Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
