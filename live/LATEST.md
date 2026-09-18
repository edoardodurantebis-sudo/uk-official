# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T21:53:09.205755Z`  
Current process started UTC: `2026-09-18T21:49:08.138711Z`  
1-second metadata polls in this process: **224**  
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

- `FUELINST|fuelType=INTVKL|generation` = **696** (n=1088, 2026-09-18T21:50:43.142865Z)
- `FUELINST|fuelType=NPSHYD|generation` = **428** (n=1088, 2026-09-18T21:50:43.142865Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3344** (n=1088, 2026-09-18T21:50:43.142865Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1088, 2026-09-18T21:50:43.142865Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1088, 2026-09-18T21:50:43.142865Z)
- `FUELINST|fuelType=OTHER|generation` = **353** (n=1088, 2026-09-18T21:50:43.142865Z)
- `FUELINST|fuelType=PS|generation` = **77** (n=1088, 2026-09-18T21:50:43.142865Z)
- `FUELINST|fuelType=WIND|generation` = **16800** (n=1088, 2026-09-18T21:50:43.142865Z)
- `IMBALNGC|TOTAL|imbalance` = **8990** (n=180, 2026-09-18T21:52:19.139822Z)
- `INDDEM|TOTAL|demand` = **-10889** (n=180, 2026-09-18T21:52:19.139822Z)
- `INDGEN|TOTAL|generation` = **26185** (n=180, 2026-09-18T21:52:02.917847Z)
- `MELNGC|TOTAL|margin` = **37609** (n=180, 2026-09-18T21:50:11.622492Z)
- `NDF|TOTAL|demand` = **16550** (n=184, 2026-09-18T21:47:51.291826Z)
- `TSDF|TOTAL|demand` = **17194** (n=184, 2026-09-18T21:47:51.291826Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T21:53:07.424724Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:53:06.424649Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:53:05.424564Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:53:04.424487Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:53:03.424419Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:53:02.424350Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:53:01.391561Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:53:00.391480Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:52:59.391399Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:52:58.347288Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:52:57.347211Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:52:56.347131Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:52:55.347064Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:52:54.346995Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:52:53.337214Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
