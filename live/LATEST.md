# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T22:05:58.143621Z`  
Current process started UTC: `2026-09-18T22:01:57.665091Z`  
1-second metadata polls in this process: **133**  
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

- `FUELINST|fuelType=INTVKL|generation` = **511** (n=1091, 2026-09-18T22:05:45.756601Z)
- `FUELINST|fuelType=NPSHYD|generation` = **444** (n=1091, 2026-09-18T22:05:45.756601Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1091, 2026-09-18T22:05:45.756601Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1091, 2026-09-18T22:05:45.756601Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1091, 2026-09-18T22:05:45.756601Z)
- `FUELINST|fuelType=OTHER|generation` = **466** (n=1091, 2026-09-18T22:05:45.756601Z)
- `FUELINST|fuelType=PS|generation` = **-237** (n=1091, 2026-09-18T22:05:45.756601Z)
- `FUELINST|fuelType=WIND|generation` = **16542** (n=1091, 2026-09-18T22:05:45.756601Z)
- `IMBALNGC|TOTAL|imbalance` = **8990** (n=180, 2026-09-18T21:52:19.139822Z)
- `INDDEM|TOTAL|demand` = **-10889** (n=180, 2026-09-18T21:52:19.139822Z)
- `INDGEN|TOTAL|generation` = **26185** (n=180, 2026-09-18T21:52:02.917847Z)
- `MELNGC|TOTAL|margin` = **37609** (n=180, 2026-09-18T21:50:11.622492Z)
- `NDF|TOTAL|demand` = **16550** (n=184, 2026-09-18T21:47:51.291826Z)
- `TSDF|TOTAL|demand` = **17194** (n=184, 2026-09-18T21:47:51.291826Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T22:05:56.558941Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:05:54.951758Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:05:53.345707Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:05:51.771697Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:05:50.004389Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:05:48.398938Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:05:45.756601Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:05:45.756601Z` — **FUELINST**: 80 rows; marker `2026-09-18T22:05:00Z`
- `2026-09-18T22:05:44.018273Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:05:42.230397Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:05:40.376421Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:05:38.708475Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:05:36.839364Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:05:34.999595Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:05:33.392733Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
