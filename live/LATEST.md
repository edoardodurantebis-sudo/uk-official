# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T22:14:57.474791Z`  
Current process started UTC: `2026-09-18T22:10:56.752052Z`  
1-second metadata polls in this process: **232**  
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

- `FUELINST|fuelType=INTVKL|generation` = **443** (n=1092, 2026-09-18T22:10:32.645030Z)
- `FUELINST|fuelType=NPSHYD|generation` = **444** (n=1092, 2026-09-18T22:10:32.645030Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3342** (n=1092, 2026-09-18T22:10:32.645030Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1092, 2026-09-18T22:10:32.645030Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1092, 2026-09-18T22:10:32.645030Z)
- `FUELINST|fuelType=OTHER|generation` = **758** (n=1092, 2026-09-18T22:10:32.645030Z)
- `FUELINST|fuelType=PS|generation` = **-470** (n=1092, 2026-09-18T22:10:32.645030Z)
- `FUELINST|fuelType=WIND|generation` = **16447** (n=1092, 2026-09-18T22:10:32.645030Z)
- `IMBALNGC|TOTAL|imbalance` = **8990** (n=180, 2026-09-18T21:52:19.139822Z)
- `INDDEM|TOTAL|demand` = **-10889** (n=180, 2026-09-18T21:52:19.139822Z)
- `INDGEN|TOTAL|generation` = **26185** (n=180, 2026-09-18T21:52:02.917847Z)
- `MELNGC|TOTAL|margin` = **37609** (n=180, 2026-09-18T21:50:11.622492Z)
- `NDF|TOTAL|demand` = **16550** (n=184, 2026-09-18T21:47:51.291826Z)
- `TSDF|TOTAL|demand` = **17194** (n=184, 2026-09-18T21:47:51.291826Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T22:14:56.503564Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:14:55.503435Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:14:54.503368Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:14:53.503232Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:14:52.503111Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:14:51.502977Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:14:50.502869Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:14:49.502773Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:14:48.502662Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:14:47.502577Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:14:46.502443Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:14:45.502304Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:14:44.151002Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:14:43.150890Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:14:42.150798Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
