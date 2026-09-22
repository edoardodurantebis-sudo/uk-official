# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T02:24:59.360333Z`  
Current process started UTC: `2026-09-22T02:20:59.616568Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=3, z=4.20 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-5, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-1, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-1, z=4.21 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3655, delta=1, z=4.24 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2003, 2026-09-22T02:20:29.341334Z)
- `FUELINST|fuelType=OTHER|generation` = **129** (n=2003, 2026-09-22T02:20:29.341334Z)
- `FUELINST|fuelType=PS|generation` = **-164** (n=2003, 2026-09-22T02:20:29.341334Z)
- `FUELINST|fuelType=WIND|generation` = **4062** (n=2003, 2026-09-22T02:20:29.341334Z)
- `IMBALNGC|TOTAL|imbalance` = **-2655** (n=330, 2026-09-22T02:20:29.341334Z)
- `INDDEM|TOTAL|demand` = **-12497** (n=330, 2026-09-22T02:20:29.341334Z)
- `INDGEN|TOTAL|generation` = **18804** (n=330, 2026-09-22T02:20:29.341334Z)
- `MELNGC|TOTAL|margin` = **37822** (n=330, 2026-09-22T02:19:26.245104Z)
- `MID|dataProvider=APXMIDP|price` = **140.43** (n=70, 2026-09-22T02:12:31.895816Z)
- `MID|dataProvider=APXMIDP|volume` = **2075.8** (n=70, 2026-09-22T02:12:31.895816Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=138, 2026-09-22T02:12:31.895816Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=138, 2026-09-22T02:12:31.895816Z)
- `NDF|TOTAL|demand` = **20959** (n=337, 2026-09-22T02:17:19.223859Z)
- `TSDF|TOTAL|demand` = **21459** (n=337, 2026-09-22T02:17:19.223859Z)
- `WINDFOR|TOTAL|generation` = **9503** (n=56, 2026-09-21T23:30:37.821418Z)

## Latest publication events

- `2026-09-22T02:24:12.569885Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:23:45Z`
- `2026-09-22T02:22:20.625976Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:21:45Z`
- `2026-09-22T02:20:29.341334Z` — **INDGEN**: 918 rows; marker `2026-09-22T02:16:00Z`
- `2026-09-22T02:20:29.341334Z` — **INDDEM**: 918 rows; marker `2026-09-22T02:16:00Z`
- `2026-09-22T02:20:29.341334Z` — **IMBALNGC**: 918 rows; marker `2026-09-22T02:16:00Z`
- `2026-09-22T02:20:29.341334Z` — **FUELINST**: 80 rows; marker `2026-09-22T02:20:00Z`
- `2026-09-22T02:20:13.859110Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:19:45Z`
- `2026-09-22T02:19:26.245104Z` — **MELNGC**: 918 rows; marker `2026-09-22T02:16:00Z`
- `2026-09-22T02:18:22.789993Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:17:45Z`
- `2026-09-22T02:17:19.223859Z` — **TSDF**: 918 rows; marker `2026-09-22T02:16:00Z`
- `2026-09-22T02:17:19.223859Z` — **NDF**: 51 rows; marker `2026-09-22T02:16:00Z`
- `2026-09-22T02:16:16.379715Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:15:45Z`
- `2026-09-22T02:15:28.095019Z` — **FUELINST**: 80 rows; marker `2026-09-22T02:15:00Z`
- `2026-09-22T02:14:24.391884Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:13:45Z`
- `2026-09-22T02:12:31.895816Z` — **MID**: 2 rows; marker `2026-09-22T02:12:04Z`
