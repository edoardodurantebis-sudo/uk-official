# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T22:27:08.819520Z`  
Current process started UTC: `2026-09-21T22:23:08.729321Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3637, delta=3, z=4.85 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3634, delta=-8, z=4.83 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3642, delta=3, z=5.00 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3639, delta=0, z=4.98 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3639, delta=-6, z=5.01 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3645, delta=24, z=5.33 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=4, z=5.15 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3641, delta=-1, z=5.12 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3642, delta=-1, z=5.17 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3643, delta=-6, z=5.23 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=1, z=5.37 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=7, z=5.40 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3621, delta=45, z=5.10 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3641, delta=11, z=5.31 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3630, delta=10, z=5.15 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1956, 2026-09-21T22:25:33.882964Z)
- `FUELINST|fuelType=OTHER|generation` = **249** (n=1956, 2026-09-21T22:25:33.882964Z)
- `FUELINST|fuelType=PS|generation` = **-8** (n=1956, 2026-09-21T22:25:33.882964Z)
- `FUELINST|fuelType=WIND|generation` = **3799** (n=1956, 2026-09-21T22:25:33.882964Z)
- `IMBALNGC|TOTAL|imbalance` = **-2499** (n=322, 2026-09-21T22:21:52.151342Z)
- `INDDEM|TOTAL|demand` = **-12258** (n=322, 2026-09-21T22:21:52.151342Z)
- `INDGEN|TOTAL|generation` = **18960** (n=322, 2026-09-21T22:21:52.151342Z)
- `MELNGC|TOTAL|margin` = **36232** (n=322, 2026-09-21T22:19:44.434107Z)
- `MID|dataProvider=APXMIDP|price` = **139.3** (n=62, 2026-09-21T22:12:14.250493Z)
- `MID|dataProvider=APXMIDP|volume` = **1973.2** (n=62, 2026-09-21T22:12:14.250493Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=122, 2026-09-21T22:12:14.250493Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=122, 2026-09-21T22:12:14.250493Z)
- `NDF|TOTAL|demand` = **20959** (n=329, 2026-09-21T22:17:50.638512Z)
- `TSDF|TOTAL|demand` = **21459** (n=329, 2026-09-21T22:18:07.177529Z)
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T22:26:22.005132Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:25:45Z`
- `2026-09-21T22:25:33.882964Z` — **FUELINST**: 80 rows; marker `2026-09-21T22:25:00Z`
- `2026-09-21T22:24:12.737207Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:23:45Z`
- `2026-09-21T22:22:08.159809Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:21:45Z`
- `2026-09-21T22:21:52.151342Z` — **INDGEN**: 1062 rows; marker `2026-09-21T22:17:00Z`
- `2026-09-21T22:21:52.151342Z` — **INDDEM**: 1062 rows; marker `2026-09-21T22:17:00Z`
- `2026-09-21T22:21:52.151342Z` — **IMBALNGC**: 1062 rows; marker `2026-09-21T22:17:00Z`
- `2026-09-21T22:20:32.570770Z` — **FUELINST**: 80 rows; marker `2026-09-21T22:20:00Z`
- `2026-09-21T22:20:16.352362Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:19:45Z`
- `2026-09-21T22:19:44.434107Z` — **MELNGC**: 1062 rows; marker `2026-09-21T22:17:00Z`
- `2026-09-21T22:18:07.177529Z` — **TSDF**: 1062 rows; marker `2026-09-21T22:17:00Z`
- `2026-09-21T22:18:07.177529Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:17:45Z`
- `2026-09-21T22:17:50.638512Z` — **NDF**: 59 rows; marker `2026-09-21T22:17:00Z`
- `2026-09-21T22:16:14.823072Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:15:45Z`
- `2026-09-21T22:15:26.360144Z` — **FUELINST**: 80 rows; marker `2026-09-21T22:15:00Z`
