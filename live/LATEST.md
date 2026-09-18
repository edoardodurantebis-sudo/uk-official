# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T22:31:44.768686Z`  
Current process started UTC: `2026-09-18T22:27:44.204251Z`  
1-second metadata polls in this process: **157**  
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

- `FUELINST|fuelType=INTVKL|generation` = **443** (n=1096, 2026-09-18T22:30:29.813223Z)
- `FUELINST|fuelType=NPSHYD|generation` = **443** (n=1096, 2026-09-18T22:30:29.813223Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1096, 2026-09-18T22:30:29.813223Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1096, 2026-09-18T22:30:29.813223Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1096, 2026-09-18T22:30:29.813223Z)
- `FUELINST|fuelType=OTHER|generation` = **1085** (n=1096, 2026-09-18T22:30:29.813223Z)
- `FUELINST|fuelType=PS|generation` = **-710** (n=1096, 2026-09-18T22:30:29.813223Z)
- `FUELINST|fuelType=WIND|generation` = **16059** (n=1096, 2026-09-18T22:30:29.813223Z)
- `IMBALNGC|TOTAL|imbalance` = **8984** (n=181, 2026-09-18T22:23:06.697614Z)
- `INDDEM|TOTAL|demand` = **-10889** (n=181, 2026-09-18T22:22:50.501799Z)
- `INDGEN|TOTAL|generation` = **26179** (n=181, 2026-09-18T22:23:06.697614Z)
- `MELNGC|TOTAL|margin` = **37591** (n=181, 2026-09-18T22:20:41.960616Z)
- `NDF|TOTAL|demand` = **16550** (n=185, 2026-09-18T22:18:11.088451Z)
- `TSDF|TOTAL|demand` = **17194** (n=185, 2026-09-18T22:18:11.088451Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T22:31:43.313935Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:31:41.855999Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:31:40.389273Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:31:38.952486Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:31:37.490902Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:31:35.708888Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:31:34.253848Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:31:32.814641Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:31:31.361152Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:31:29.881002Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:31:28.440793Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:31:26.992618Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:31:25.494300Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:31:24.020701Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:31:22.548446Z` — **MID**: 0 rows; marker `2026-09-18T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
