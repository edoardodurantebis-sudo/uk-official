# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T04:54:50.380359Z`  
Current process started UTC: `2026-09-22T04:50:50.301963Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=0, z=3.65 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=-4, z=3.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-3, z=3.73 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-1, z=3.78 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2033, 2026-09-22T04:50:50.301973Z)
- `FUELINST|fuelType=OTHER|generation` = **388** (n=2033, 2026-09-22T04:50:50.301973Z)
- `FUELINST|fuelType=PS|generation` = **-171** (n=2033, 2026-09-22T04:50:50.301973Z)
- `FUELINST|fuelType=WIND|generation` = **3463** (n=2033, 2026-09-22T04:50:50.301973Z)
- `IMBALNGC|TOTAL|imbalance` = **-3312** (n=335, 2026-09-22T04:50:50.301973Z)
- `INDDEM|TOTAL|demand` = **-12523** (n=335, 2026-09-22T04:50:50.301973Z)
- `INDGEN|TOTAL|generation` = **18147** (n=335, 2026-09-22T04:50:50.301973Z)
- `MELNGC|TOTAL|margin` = **37794** (n=335, 2026-09-22T04:49:13.325517Z)
- `MID|dataProvider=APXMIDP|price` = **152.57** (n=75, 2026-09-22T04:42:14.229530Z)
- `MID|dataProvider=APXMIDP|volume` = **2244.1** (n=75, 2026-09-22T04:42:14.229530Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=148, 2026-09-22T04:42:14.229530Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=148, 2026-09-22T04:42:14.229530Z)
- `NDF|TOTAL|demand` = **20959** (n=342, 2026-09-22T04:47:21.419553Z)
- `TSDF|TOTAL|demand` = **21459** (n=342, 2026-09-22T04:47:21.419553Z)
- `WINDFOR|TOTAL|generation` = **11644** (n=57, 2026-09-22T03:30:45.244161Z)

## Latest publication events

- `2026-09-22T04:54:18.145602Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:53:45Z`
- `2026-09-22T04:52:10.513756Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:51:45Z`
- `2026-09-22T04:50:50.301973Z` — **INDGEN**: 828 rows; marker `2026-09-22T04:46:00Z`
- `2026-09-22T04:50:50.301973Z` — **INDDEM**: 828 rows; marker `2026-09-22T04:46:00Z`
- `2026-09-22T04:50:50.301973Z` — **IMBALNGC**: 828 rows; marker `2026-09-22T04:46:00Z`
- `2026-09-22T04:50:50.301973Z` — **FUELINST**: 80 rows; marker `2026-09-22T04:50:00Z`
- `2026-09-22T04:50:50.301973Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:49:45Z`
- `2026-09-22T04:49:13.325517Z` — **MELNGC**: 828 rows; marker `2026-09-22T04:46:00Z`
- `2026-09-22T04:48:09.547373Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:47:45Z`
- `2026-09-22T04:47:21.419553Z` — **TSDF**: 828 rows; marker `2026-09-22T04:46:00Z`
- `2026-09-22T04:47:21.419553Z` — **NDF**: 46 rows; marker `2026-09-22T04:47:00Z`
- `2026-09-22T04:46:17.662100Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:45:45Z`
- `2026-09-22T04:45:26.278033Z` — **FUELINST**: 80 rows; marker `2026-09-22T04:45:00Z`
- `2026-09-22T04:44:22.193950Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:43:45Z`
- `2026-09-22T04:42:14.229530Z` — **MID**: 2 rows; marker `2026-09-22T04:42:04Z`
