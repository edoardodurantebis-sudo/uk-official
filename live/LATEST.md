# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T13:30:31.424435Z`  
Current process started UTC: `2026-09-18T13:26:30.379063Z`  
1-second metadata polls in this process: **225**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1389** (n=1031, 2026-09-18T13:25:39.302658Z)
- `FUELINST|fuelType=NPSHYD|generation` = **318** (n=1031, 2026-09-18T13:25:39.302658Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=1031, 2026-09-18T13:25:39.302658Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1031, 2026-09-18T13:25:39.302658Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1031, 2026-09-18T13:25:39.302658Z)
- `FUELINST|fuelType=OTHER|generation` = **565** (n=1031, 2026-09-18T13:25:39.302658Z)
- `FUELINST|fuelType=PS|generation` = **-705** (n=1031, 2026-09-18T13:25:39.302658Z)
- `FUELINST|fuelType=WIND|generation` = **15085** (n=1031, 2026-09-18T13:25:39.302658Z)
- `IMBALNGC|TOTAL|imbalance` = **8935** (n=170, 2026-09-18T13:25:04.803083Z)
- `INDDEM|TOTAL|demand` = **-10745** (n=170, 2026-09-18T13:25:04.803083Z)
- `INDGEN|TOTAL|generation` = **25605** (n=170, 2026-09-18T13:25:04.803083Z)
- `MELNGC|TOTAL|margin` = **38174** (n=170, 2026-09-18T13:21:37.459648Z)
- `NDF|TOTAL|demand` = **16170** (n=174, 2026-09-18T13:18:55.653418Z)
- `TSDF|TOTAL|demand` = **16670** (n=174, 2026-09-18T13:18:55.653418Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T13:30:30.370112Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:30:29.369978Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:30:28.369900Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:30:26.018204Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:30:26.018204Z` — **FREQ**: 5761 rows; marker `2026-09-18T13:29:45Z`
- `2026-09-18T13:30:24.878986Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:30:23.878899Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:30:22.830831Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:30:21.821444Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:30:20.760190Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:30:19.760085Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:30:18.760002Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:30:17.731139Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:30:16.728381Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:30:15.728318Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
