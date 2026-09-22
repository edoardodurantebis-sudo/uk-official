# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T05:11:39.967167Z`  
Current process started UTC: `2026-09-22T05:07:39.898831Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=-3, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3663, delta=14, z=3.65 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-2, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-5, z=3.50 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=6, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3647, delta=3, z=3.52 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3650, delta=-4, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3646, delta=-9, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3655, delta=-1, z=3.65 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=6, z=3.67 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=4, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3646, delta=-1, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3647, delta=-3, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-1, z=3.78 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2037, 2026-09-22T05:10:20.913231Z)
- `FUELINST|fuelType=OTHER|generation` = **332** (n=2037, 2026-09-22T05:10:20.913231Z)
- `FUELINST|fuelType=PS|generation` = **-173** (n=2037, 2026-09-22T05:10:20.913231Z)
- `FUELINST|fuelType=WIND|generation` = **3456** (n=2037, 2026-09-22T05:10:20.913231Z)
- `IMBALNGC|TOTAL|imbalance` = **-3312** (n=335, 2026-09-22T04:55:01.456740Z)
- `INDDEM|TOTAL|demand` = **-12523** (n=335, 2026-09-22T04:55:01.456740Z)
- `INDGEN|TOTAL|generation` = **18147** (n=335, 2026-09-22T04:55:01.456740Z)
- `MELNGC|TOTAL|margin` = **37794** (n=335, 2026-09-22T04:49:13.325517Z)
- `MID|dataProvider=APXMIDP|price` = **152.57** (n=75, 2026-09-22T04:42:14.229530Z)
- `MID|dataProvider=APXMIDP|volume` = **2244.1** (n=75, 2026-09-22T04:42:14.229530Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=149, 2026-09-22T05:07:39.898840Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=149, 2026-09-22T05:07:39.898840Z)
- `NDF|TOTAL|demand` = **20959** (n=342, 2026-09-22T04:47:21.419553Z)
- `TSDF|TOTAL|demand` = **21459** (n=342, 2026-09-22T04:47:21.419553Z)
- `WINDFOR|TOTAL|generation` = **11644** (n=57, 2026-09-22T03:30:45.244161Z)

## Latest publication events

- `2026-09-22T05:10:20.913231Z` — **FUELINST**: 80 rows; marker `2026-09-22T05:10:00Z`
- `2026-09-22T05:10:04.850553Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:09:45Z`
- `2026-09-22T05:08:12.365313Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:07:45Z`
- `2026-09-22T05:07:39.898840Z` — **MID**: 1 rows; marker `2026-09-22T05:05:00Z`
- `2026-09-22T05:06:06.913738Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:05:45Z`
- `2026-09-22T05:05:34.699776Z` — **FUELINST**: 80 rows; marker `2026-09-22T05:05:00Z`
- `2026-09-22T05:04:14.163234Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:03:45Z`
- `2026-09-22T05:02:27.335964Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:01:45Z`
- `2026-09-22T05:00:50.488972Z` — **FUELHH**: 20 rows; marker `2026-09-22T05:00:00Z`
- `2026-09-22T05:00:34.217029Z` — **FUELINST**: 80 rows; marker `2026-09-22T05:00:00Z`
- `2026-09-22T05:00:18.408404Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:59:45Z`
- `2026-09-22T04:58:18.600044Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:57:45Z`
- `2026-09-22T04:56:26.412501Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:55:45Z`
- `2026-09-22T04:55:38.822184Z` — **FUELINST**: 80 rows; marker `2026-09-22T04:55:00Z`
- `2026-09-22T04:55:01.456740Z` — **INDGEN**: 828 rows; marker `2026-09-22T04:46:00Z`
