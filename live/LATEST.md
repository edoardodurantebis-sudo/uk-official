# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T13:34:41.648645Z`  
Current process started UTC: `2026-09-18T13:30:41.579554Z`  
1-second metadata polls in this process: **175**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1389** (n=1032, 2026-09-18T13:30:41.579566Z)
- `FUELINST|fuelType=NPSHYD|generation` = **318** (n=1032, 2026-09-18T13:30:41.579566Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1032, 2026-09-18T13:30:41.579566Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1032, 2026-09-18T13:30:41.579566Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1032, 2026-09-18T13:30:41.579566Z)
- `FUELINST|fuelType=OTHER|generation` = **551** (n=1032, 2026-09-18T13:30:41.579566Z)
- `FUELINST|fuelType=PS|generation` = **-690** (n=1032, 2026-09-18T13:30:41.579566Z)
- `FUELINST|fuelType=WIND|generation` = **15142** (n=1032, 2026-09-18T13:30:41.579566Z)
- `IMBALNGC|TOTAL|imbalance` = **8935** (n=170, 2026-09-18T13:25:04.803083Z)
- `INDDEM|TOTAL|demand` = **-10745** (n=170, 2026-09-18T13:25:04.803083Z)
- `INDGEN|TOTAL|generation` = **25605** (n=170, 2026-09-18T13:25:04.803083Z)
- `MELNGC|TOTAL|margin` = **38174** (n=170, 2026-09-18T13:21:37.459648Z)
- `NDF|TOTAL|demand` = **16170** (n=174, 2026-09-18T13:18:55.653418Z)
- `TSDF|TOTAL|demand` = **16670** (n=174, 2026-09-18T13:18:55.653418Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T13:34:40.506067Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:34:39.293245Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:34:38.118845Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:34:36.936726Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:34:35.744913Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:34:34.129546Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:34:32.953956Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:34:31.719383Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:34:30.522693Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:34:29.327797Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:34:28.142653Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:34:26.971320Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:34:25.793745Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:34:24.623036Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:34:22.862064Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
