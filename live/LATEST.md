# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T02:43:41.121403Z`  
Current process started UTC: `2026-09-17T02:39:40.607686Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-809, delta=-1, z=-3.66 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-808, delta=-1, z=-3.71 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-792, delta=-154, z=-3.97 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.22 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-807, delta=0, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-807, delta=0, z=-3.80 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-807, delta=0, z=-3.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-807, delta=-24, z=-3.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-783, delta=-46, z=-3.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-737, delta=-46, z=-3.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-638, delta=-42, z=-3.94 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-691, delta=-46, z=-3.80 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-645, delta=-22, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=0, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=0, z=-3.80 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1447** (n=614, 2026-09-17T02:40:32.034513Z)
- `FUELINST|fuelType=NPSHYD|generation` = **422** (n=614, 2026-09-17T02:40:32.034513Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=614, 2026-09-17T02:40:32.034513Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=614, 2026-09-17T02:40:32.034513Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=614, 2026-09-17T02:40:32.034513Z)
- `FUELINST|fuelType=OTHER|generation` = **337** (n=614, 2026-09-17T02:40:32.034513Z)
- `FUELINST|fuelType=PS|generation` = **-548** (n=614, 2026-09-17T02:40:32.034513Z)
- `FUELINST|fuelType=WIND|generation` = **13412** (n=614, 2026-09-17T02:40:32.034513Z)
- `IMBALNGC|TOTAL|imbalance` = **6512** (n=102, 2026-09-17T02:20:53.960752Z)
- `INDDEM|TOTAL|demand` = **-11527** (n=102, 2026-09-17T02:20:38.099754Z)
- `INDGEN|TOTAL|generation` = **25633** (n=102, 2026-09-17T02:20:38.099754Z)
- `MELNGC|TOTAL|margin` = **35851** (n=102, 2026-09-17T02:19:02.355909Z)
- `NDF|TOTAL|demand` = **18621** (n=104, 2026-09-17T02:17:42.741584Z)
- `TSDF|TOTAL|demand` = **19121** (n=104, 2026-09-17T02:17:42.741584Z)
- `WINDFOR|TOTAL|generation` = **20102** (n=17, 2026-09-16T23:30:41.101363Z)

## Latest publication events

- `2026-09-17T02:42:24.025980Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:41:45Z`
- `2026-09-17T02:42:07.994872Z` — **MID**: 0 rows; marker `2026-09-17T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T02:40:32.034513Z` — **FUELINST**: 80 rows; marker `2026-09-17T02:40:00Z`
- `2026-09-17T02:40:16.660892Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:39:45Z`
- `2026-09-17T02:38:08.514167Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:37:45Z`
- `2026-09-17T02:37:36.745275Z` — **MID**: 0 rows; marker `2026-09-17T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T02:36:16.757038Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:35:45Z`
- `2026-09-17T02:35:29.319641Z` — **FUELINST**: 80 rows; marker `2026-09-17T02:35:00Z`
- `2026-09-17T02:34:14.294445Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:33:45Z`
- `2026-09-17T02:32:05.558538Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:31:45Z`
- `2026-09-17T02:30:37.094688Z` — **FUELHH**: 20 rows; marker `2026-09-17T02:30:00Z`
- `2026-09-17T02:30:19.999267Z` — **FUELINST**: 80 rows; marker `2026-09-17T02:30:00Z`
- `2026-09-17T02:30:04.375361Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:29:45Z`
- `2026-09-17T02:28:12.571457Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:27:45Z`
- `2026-09-17T02:26:04.179191Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:25:45Z`
