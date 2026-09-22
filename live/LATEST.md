# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T04:45:59.013769Z`  
Current process started UTC: `2026-09-22T04:41:58.227395Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3658, delta=1, z=3.81 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2032, 2026-09-22T04:45:26.278033Z)
- `FUELINST|fuelType=OTHER|generation` = **352** (n=2032, 2026-09-22T04:45:26.278033Z)
- `FUELINST|fuelType=PS|generation` = **-163** (n=2032, 2026-09-22T04:45:26.278033Z)
- `FUELINST|fuelType=WIND|generation` = **3436** (n=2032, 2026-09-22T04:45:26.278033Z)
- `IMBALNGC|TOTAL|imbalance` = **-3324** (n=334, 2026-09-22T04:20:26.160081Z)
- `INDDEM|TOTAL|demand` = **-12520** (n=334, 2026-09-22T04:20:26.160081Z)
- `INDGEN|TOTAL|generation` = **18135** (n=334, 2026-09-22T04:20:26.160081Z)
- `MELNGC|TOTAL|margin` = **37794** (n=334, 2026-09-22T04:19:22.013813Z)
- `MID|dataProvider=APXMIDP|price` = **152.57** (n=75, 2026-09-22T04:42:14.229530Z)
- `MID|dataProvider=APXMIDP|volume` = **2244.1** (n=75, 2026-09-22T04:42:14.229530Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=148, 2026-09-22T04:42:14.229530Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=148, 2026-09-22T04:42:14.229530Z)
- `NDF|TOTAL|demand` = **20959** (n=341, 2026-09-22T04:17:30.952649Z)
- `TSDF|TOTAL|demand` = **21459** (n=341, 2026-09-22T04:17:30.952649Z)
- `WINDFOR|TOTAL|generation` = **11644** (n=57, 2026-09-22T03:30:45.244161Z)

## Latest publication events

- `2026-09-22T04:45:26.278033Z` — **FUELINST**: 80 rows; marker `2026-09-22T04:45:00Z`
- `2026-09-22T04:44:22.193950Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:43:45Z`
- `2026-09-22T04:42:14.229530Z` — **MID**: 2 rows; marker `2026-09-22T04:42:04Z`
- `2026-09-22T04:42:14.229530Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:41:45Z`
- `2026-09-22T04:40:27.182988Z` — **FUELINST**: 80 rows; marker `2026-09-22T04:40:00Z`
- `2026-09-22T04:40:10.364526Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:39:45Z`
- `2026-09-22T04:38:18.924571Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:37:45Z`
- `2026-09-22T04:37:30.689537Z` — **MID**: 1 rows; marker `2026-09-22T04:35:00Z`
- `2026-09-22T04:36:11.088444Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:35:45Z`
- `2026-09-22T04:35:22.762030Z` — **FUELINST**: 80 rows; marker `2026-09-22T04:35:00Z`
- `2026-09-22T04:34:19.247632Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:33:45Z`
- `2026-09-22T04:32:16.900910Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:31:45Z`
- `2026-09-22T04:30:40.095897Z` — **FUELHH**: 20 rows; marker `2026-09-22T04:30:00Z`
- `2026-09-22T04:30:23.817294Z` — **FUELINST**: 80 rows; marker `2026-09-22T04:30:00Z`
- `2026-09-22T04:30:08.146640Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:29:45Z`
