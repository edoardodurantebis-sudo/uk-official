# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T17:00:42.280488Z`  
Current process started UTC: `2026-09-21T16:56:41.128724Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3506, delta=0, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=3, z=3.54 -> generation-mix component moved
- **FUELINST** `fuelType=CCGT` `generation` — instantaneous generation mix [fuelType=CCGT] generation: value=13464, delta=103, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3507, delta=-3, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3510, delta=1, z=3.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=5, z=3.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=-1, z=3.61 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3506, delta=4, z=3.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3505, delta=1, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=1, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3503, delta=-6, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=3, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3506, delta=-1, z=3.72 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3507, delta=5, z=3.76 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3502, delta=7, z=3.71 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1891, 2026-09-21T17:00:25.468923Z)
- `FUELINST|fuelType=OTHER|generation` = **2012** (n=1891, 2026-09-21T17:00:25.468923Z)
- `FUELINST|fuelType=PS|generation` = **348** (n=1891, 2026-09-21T17:00:25.468923Z)
- `FUELINST|fuelType=WIND|generation` = **3347** (n=1891, 2026-09-21T17:00:25.468923Z)
- `IMBALNGC|TOTAL|imbalance` = **-3026** (n=311, 2026-09-21T16:52:56.638577Z)
- `INDDEM|TOTAL|demand` = **-12277** (n=311, 2026-09-21T16:52:40.661443Z)
- `INDGEN|TOTAL|generation` = **18433** (n=311, 2026-09-21T16:52:40.661443Z)
- `MELNGC|TOTAL|margin` = **36274** (n=311, 2026-09-21T16:50:05.101867Z)
- `MID|dataProvider=APXMIDP|price` = **203.05** (n=51, 2026-09-21T16:42:11.789467Z)
- `MID|dataProvider=APXMIDP|volume` = **3543.2** (n=51, 2026-09-21T16:42:11.789467Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=100, 2026-09-21T16:42:11.789467Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=100, 2026-09-21T16:42:11.789467Z)
- `NDF|TOTAL|demand` = **20959** (n=318, 2026-09-21T16:48:12.642517Z)
- `TSDF|TOTAL|demand` = **21459** (n=318, 2026-09-21T16:47:56.912365Z)
- `WINDFOR|TOTAL|generation` = **8620** (n=54, 2026-09-21T16:30:47.714491Z)

## Latest publication events

- `2026-09-21T17:00:40.926790Z` — **FUELHH**: 20 rows; marker `2026-09-21T17:00:00Z`
- `2026-09-21T17:00:25.468923Z` — **FUELINST**: 80 rows; marker `2026-09-21T17:00:00Z`
- `2026-09-21T17:00:09.116003Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:59:45Z`
- `2026-09-21T16:58:17.186996Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:57:45Z`
- `2026-09-21T16:56:41.128731Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:55:45Z`
- `2026-09-21T16:55:19.666489Z` — **FUELINST**: 80 rows; marker `2026-09-21T16:55:00Z`
- `2026-09-21T16:54:15.982271Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:53:45Z`
- `2026-09-21T16:52:56.638577Z` — **IMBALNGC**: 1260 rows; marker `2026-09-21T16:47:00Z`
- `2026-09-21T16:52:40.661443Z` — **INDGEN**: 1260 rows; marker `2026-09-21T16:47:00Z`
- `2026-09-21T16:52:40.661443Z` — **INDDEM**: 1260 rows; marker `2026-09-21T16:47:00Z`
- `2026-09-21T16:52:09.128778Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:51:45Z`
- `2026-09-21T16:50:37.539678Z` — **FUELINST**: 80 rows; marker `2026-09-21T16:50:00Z`
- `2026-09-21T16:50:21.495692Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:49:45Z`
- `2026-09-21T16:50:05.101867Z` — **MELNGC**: 1260 rows; marker `2026-09-21T16:47:00Z`
- `2026-09-21T16:48:28.971558Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:47:45Z`
