# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T02:42:00.587360Z`  
Current process started UTC: `2026-09-22T02:38:01.067653Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=0, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-7, z=3.94 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-2, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=1, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3659, delta=5, z=4.06 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=2, z=4.01 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3652, delta=2, z=4.00 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=5, z=3.99 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=-8, z=3.94 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3655, delta=1, z=4.18 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-1, z=4.06 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-4, z=4.09 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3658, delta=3, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3655, delta=2, z=4.14 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-3, z=4.13 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2007, 2026-09-22T02:40:24.230550Z)
- `FUELINST|fuelType=OTHER|generation` = **262** (n=2007, 2026-09-22T02:40:24.230550Z)
- `FUELINST|fuelType=PS|generation` = **-165** (n=2007, 2026-09-22T02:40:24.230550Z)
- `FUELINST|fuelType=WIND|generation` = **4131** (n=2007, 2026-09-22T02:40:24.230550Z)
- `IMBALNGC|TOTAL|imbalance` = **-2655** (n=330, 2026-09-22T02:20:29.341334Z)
- `INDDEM|TOTAL|demand` = **-12497** (n=330, 2026-09-22T02:20:29.341334Z)
- `INDGEN|TOTAL|generation` = **18804** (n=330, 2026-09-22T02:20:29.341334Z)
- `MELNGC|TOTAL|margin` = **37822** (n=330, 2026-09-22T02:19:26.245104Z)
- `MID|dataProvider=APXMIDP|price` = **140.43** (n=70, 2026-09-22T02:12:31.895816Z)
- `MID|dataProvider=APXMIDP|volume` = **2075.8** (n=70, 2026-09-22T02:12:31.895816Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=139, 2026-09-22T02:37:32.415397Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=139, 2026-09-22T02:37:32.415397Z)
- `NDF|TOTAL|demand` = **20959** (n=337, 2026-09-22T02:17:19.223859Z)
- `TSDF|TOTAL|demand` = **21459** (n=337, 2026-09-22T02:17:19.223859Z)
- `WINDFOR|TOTAL|generation` = **9503** (n=56, 2026-09-21T23:30:37.821418Z)

## Latest publication events

- `2026-09-22T02:40:24.230550Z` — **FUELINST**: 80 rows; marker `2026-09-22T02:40:00Z`
- `2026-09-22T02:40:08.606143Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:39:45Z`
- `2026-09-22T02:38:17.069670Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:37:45Z`
- `2026-09-22T02:37:32.415397Z` — **MID**: 1 rows; marker `2026-09-22T02:35:00Z`
- `2026-09-22T02:36:12.155722Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:35:45Z`
- `2026-09-22T02:35:24.649971Z` — **FUELINST**: 80 rows; marker `2026-09-22T02:35:00Z`
- `2026-09-22T02:34:04.683775Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:33:45Z`
- `2026-09-22T02:32:07.742246Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:31:45Z`
- `2026-09-22T02:30:46.993669Z` — **FUELHH**: 20 rows; marker `2026-09-22T02:30:00Z`
- `2026-09-22T02:30:46.993669Z` — **FUELINST**: 80 rows; marker `2026-09-22T02:30:00Z`
- `2026-09-22T02:30:30.520378Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:29:45Z`
- `2026-09-22T02:28:24.260571Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:27:45Z`
- `2026-09-22T02:26:16.247448Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:25:45Z`
- `2026-09-22T02:25:28.811619Z` — **FUELINST**: 80 rows; marker `2026-09-22T02:25:00Z`
- `2026-09-22T02:24:12.569885Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:23:45Z`
