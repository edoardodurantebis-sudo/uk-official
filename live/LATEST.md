# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T15:26:27.471239Z`  
Current process started UTC: `2026-09-21T15:22:26.479124Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3494, delta=-1, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3495, delta=0, z=3.62 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3495, delta=-4, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=6, z=3.74 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3493, delta=4, z=3.61 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1872, 2026-09-21T15:25:37.759377Z)
- `FUELINST|fuelType=OTHER|generation` = **566** (n=1872, 2026-09-21T15:25:37.759377Z)
- `FUELINST|fuelType=PS|generation` = **-21** (n=1872, 2026-09-21T15:25:37.759377Z)
- `FUELINST|fuelType=WIND|generation` = **3338** (n=1872, 2026-09-21T15:25:37.759377Z)
- `IMBALNGC|TOTAL|imbalance` = **-3107** (n=308, 2026-09-21T15:23:14.349075Z)
- `INDDEM|TOTAL|demand` = **-12278** (n=308, 2026-09-21T15:23:14.349075Z)
- `INDGEN|TOTAL|generation` = **18352** (n=308, 2026-09-21T15:23:14.349075Z)
- `MELNGC|TOTAL|margin` = **36257** (n=308, 2026-09-21T15:20:37.814864Z)
- `MID|dataProvider=APXMIDP|price` = **141.2** (n=48, 2026-09-21T15:12:19.798978Z)
- `MID|dataProvider=APXMIDP|volume` = **3356.4** (n=48, 2026-09-21T15:12:19.798978Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=94, 2026-09-21T15:12:19.798978Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=94, 2026-09-21T15:12:19.798978Z)
- `NDF|TOTAL|demand` = **20959** (n=315, 2026-09-21T15:18:13.811389Z)
- `TSDF|TOTAL|demand` = **21459** (n=315, 2026-09-21T15:18:13.811389Z)
- `WINDFOR|TOTAL|generation` = **8616** (n=53, 2026-09-21T12:30:32.614458Z)

## Latest publication events

- `2026-09-21T15:26:26.039638Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:25:45Z`
- `2026-09-21T15:25:37.759377Z` — **FUELINST**: 80 rows; marker `2026-09-21T15:25:00Z`
- `2026-09-21T15:24:18.215991Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:23:45Z`
- `2026-09-21T15:23:14.349075Z` — **INDGEN**: 1314 rows; marker `2026-09-21T15:17:00Z`
- `2026-09-21T15:23:14.349075Z` — **INDDEM**: 1314 rows; marker `2026-09-21T15:17:00Z`
- `2026-09-21T15:23:14.349075Z` — **IMBALNGC**: 1314 rows; marker `2026-09-21T15:17:00Z`
- `2026-09-21T15:22:26.479133Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:21:45Z`
- `2026-09-21T15:20:37.814864Z` — **MELNGC**: 1314 rows; marker `2026-09-21T15:17:00Z`
- `2026-09-21T15:20:37.814864Z` — **FUELINST**: 80 rows; marker `2026-09-21T15:20:00Z`
- `2026-09-21T15:20:22.228442Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:19:45Z`
- `2026-09-21T15:18:13.811389Z` — **TSDF**: 1314 rows; marker `2026-09-21T15:17:00Z`
- `2026-09-21T15:18:13.811389Z` — **NDF**: 73 rows; marker `2026-09-21T15:17:00Z`
- `2026-09-21T15:18:13.811389Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:17:45Z`
- `2026-09-21T15:16:22.797744Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:15:45Z`
- `2026-09-21T15:15:34.609850Z` — **FUELINST**: 80 rows; marker `2026-09-21T15:15:00Z`
