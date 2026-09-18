# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T22:35:59.337498Z`  
Current process started UTC: `2026-09-18T22:31:57.898028Z`  
1-second metadata polls in this process: **127**  
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

- `FUELINST|fuelType=INTVKL|generation` = **443** (n=1097, 2026-09-18T22:35:33.799277Z)
- `FUELINST|fuelType=NPSHYD|generation` = **444** (n=1097, 2026-09-18T22:35:33.799277Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1097, 2026-09-18T22:35:33.799277Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1097, 2026-09-18T22:35:33.799277Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1097, 2026-09-18T22:35:33.799277Z)
- `FUELINST|fuelType=OTHER|generation` = **1466** (n=1097, 2026-09-18T22:35:33.799277Z)
- `FUELINST|fuelType=PS|generation` = **-708** (n=1097, 2026-09-18T22:35:33.799277Z)
- `FUELINST|fuelType=WIND|generation` = **15942** (n=1097, 2026-09-18T22:35:33.799277Z)
- `IMBALNGC|TOTAL|imbalance` = **8984** (n=181, 2026-09-18T22:23:06.697614Z)
- `INDDEM|TOTAL|demand` = **-10889** (n=181, 2026-09-18T22:22:50.501799Z)
- `INDGEN|TOTAL|generation` = **26179** (n=181, 2026-09-18T22:23:06.697614Z)
- `MELNGC|TOTAL|margin` = **37591** (n=181, 2026-09-18T22:20:41.960616Z)
- `NDF|TOTAL|demand` = **16550** (n=185, 2026-09-18T22:18:11.088451Z)
- `TSDF|TOTAL|demand` = **17194** (n=185, 2026-09-18T22:18:11.088451Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T22:35:57.532228Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:35:55.822759Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:35:54.095040Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:35:52.342790Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:35:50.273959Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:35:48.531400Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:35:46.822191Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:35:45.098998Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:35:43.373872Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:35:41.687091Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:35:39.963985Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:35:38.224100Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:35:36.530681Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:35:33.799277Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:35:33.799277Z` — **FUELINST**: 80 rows; marker `2026-09-18T22:35:00Z`
