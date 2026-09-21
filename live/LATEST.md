# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T20:33:05.116721Z`  
Current process started UTC: `2026-09-21T20:29:04.671356Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3534, delta=22, z=3.69 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3549, delta=2, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3547, delta=8, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3539, delta=7, z=3.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3532, delta=10, z=3.64 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=146, delta=-39, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=0, z=3.62 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=0, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=-12, z=3.66 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=161, delta=-8, z=4.02 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=185, delta=-45, z=4.95 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=169, delta=-2, z=4.27 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=171, delta=-17, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=188, delta=-2, z=4.87 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1933, 2026-09-21T20:30:41.194807Z)
- `FUELINST|fuelType=OTHER|generation` = **797** (n=1933, 2026-09-21T20:30:41.194807Z)
- `FUELINST|fuelType=PS|generation` = **253** (n=1933, 2026-09-21T20:30:41.194807Z)
- `FUELINST|fuelType=WIND|generation` = **3552** (n=1933, 2026-09-21T20:30:41.194807Z)
- `IMBALNGC|TOTAL|imbalance` = **-2707** (n=318, 2026-09-21T20:22:10.806468Z)
- `INDDEM|TOTAL|demand` = **-12258** (n=318, 2026-09-21T20:21:54.518829Z)
- `INDGEN|TOTAL|generation` = **18752** (n=318, 2026-09-21T20:21:54.518829Z)
- `MELNGC|TOTAL|margin` = **36091** (n=318, 2026-09-21T20:19:44.727256Z)
- `MID|dataProvider=APXMIDP|price` = **182.5** (n=58, 2026-09-21T20:12:23.535636Z)
- `MID|dataProvider=APXMIDP|volume` = **2810.9** (n=58, 2026-09-21T20:12:23.535636Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=114, 2026-09-21T20:12:23.535636Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=114, 2026-09-21T20:12:23.535636Z)
- `NDF|TOTAL|demand` = **20959** (n=325, 2026-09-21T20:17:52.969377Z)
- `TSDF|TOTAL|demand` = **21459** (n=325, 2026-09-21T20:17:52.969377Z)
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T20:32:17.623411Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:31:45Z`
- `2026-09-21T20:30:41.194807Z` — **FUELHH**: 20 rows; marker `2026-09-21T20:30:00Z`
- `2026-09-21T20:30:41.194807Z` — **FUELINST**: 80 rows; marker `2026-09-21T20:30:00Z`
- `2026-09-21T20:30:25.093962Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:29:45Z`
- `2026-09-21T20:28:19.685072Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:27:45Z`
- `2026-09-21T20:26:11.738911Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:25:45Z`
- `2026-09-21T20:25:39.525508Z` — **FUELINST**: 80 rows; marker `2026-09-21T20:25:00Z`
- `2026-09-21T20:24:18.786152Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:23:45Z`
- `2026-09-21T20:22:26.748945Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:21:45Z`
- `2026-09-21T20:22:10.806468Z` — **IMBALNGC**: 1134 rows; marker `2026-09-21T20:17:00Z`
- `2026-09-21T20:21:54.518829Z` — **INDGEN**: 1134 rows; marker `2026-09-21T20:17:00Z`
- `2026-09-21T20:21:54.518829Z` — **INDDEM**: 1134 rows; marker `2026-09-21T20:17:00Z`
- `2026-09-21T20:20:33.606147Z` — **FUELINST**: 80 rows; marker `2026-09-21T20:20:00Z`
- `2026-09-21T20:20:16.850591Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:19:45Z`
- `2026-09-21T20:19:44.727256Z` — **MELNGC**: 1134 rows; marker `2026-09-21T20:17:00Z`
