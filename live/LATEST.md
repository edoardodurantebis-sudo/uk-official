# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T15:05:10.389564Z`  
Current process started UTC: `2026-09-21T15:01:10.601088Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3493, delta=-3, z=3.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3489, delta=-6, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3495, delta=-5, z=3.69 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3500, delta=3, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3497, delta=7, z=3.76 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3490, delta=1, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3489, delta=-7, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-12, z=3.83 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-2, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3498, delta=3, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3495, delta=3, z=3.79 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3492, delta=-4, z=3.73 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-2, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3498, delta=-1, z=3.91 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3508, delta=1, z=4.24 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1867, 2026-09-21T15:00:26.767132Z)
- `FUELINST|fuelType=OTHER|generation` = **499** (n=1867, 2026-09-21T15:00:26.767132Z)
- `FUELINST|fuelType=PS|generation` = **129** (n=1867, 2026-09-21T15:00:26.767132Z)
- `FUELINST|fuelType=WIND|generation` = **3439** (n=1867, 2026-09-21T15:00:26.767132Z)
- `IMBALNGC|TOTAL|imbalance` = **-3207** (n=307, 2026-09-21T14:53:36.483430Z)
- `INDDEM|TOTAL|demand` = **-12297** (n=307, 2026-09-21T14:53:21.042989Z)
- `INDGEN|TOTAL|generation` = **18297** (n=307, 2026-09-21T14:53:21.042989Z)
- `MELNGC|TOTAL|margin` = **36253** (n=307, 2026-09-21T14:50:57.433989Z)
- `MID|dataProvider=APXMIDP|price` = **145.05** (n=47, 2026-09-21T14:42:14.482814Z)
- `MID|dataProvider=APXMIDP|volume` = **2842.6** (n=47, 2026-09-21T14:42:14.482814Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=92, 2026-09-21T14:42:14.482814Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=92, 2026-09-21T14:42:14.482814Z)
- `NDF|TOTAL|demand` = **21004** (n=314, 2026-09-21T14:48:33.964949Z)
- `TSDF|TOTAL|demand` = **21504** (n=314, 2026-09-21T14:48:33.964949Z)
- `WINDFOR|TOTAL|generation` = **8616** (n=53, 2026-09-21T12:30:32.614458Z)

## Latest publication events

- `2026-09-21T15:04:07.412197Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:03:45Z`
- `2026-09-21T15:02:15.156195Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:01:45Z`
- `2026-09-21T15:00:42.830868Z` — **FUELHH**: 20 rows; marker `2026-09-21T15:00:00Z`
- `2026-09-21T15:00:26.767132Z` — **FUELINST**: 80 rows; marker `2026-09-21T15:00:00Z`
- `2026-09-21T15:00:11.345603Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:59:45Z`
- `2026-09-21T14:58:02.417669Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:57:45Z`
- `2026-09-21T14:56:16.241274Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:55:45Z`
- `2026-09-21T14:55:44.058753Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:55:00Z`
- `2026-09-21T14:54:24.011800Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:53:45Z`
- `2026-09-21T14:53:36.483430Z` — **IMBALNGC**: 1332 rows; marker `2026-09-21T14:48:00Z`
- `2026-09-21T14:53:21.042989Z` — **INDGEN**: 1332 rows; marker `2026-09-21T14:47:00Z`
- `2026-09-21T14:53:21.042989Z` — **INDDEM**: 1332 rows; marker `2026-09-21T14:47:00Z`
- `2026-09-21T14:52:17.997071Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:51:45Z`
- `2026-09-21T14:50:57.433989Z` — **MELNGC**: 1332 rows; marker `2026-09-21T14:48:00Z`
- `2026-09-21T14:50:41.209220Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:50:00Z`
