# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T15:17:59.135260Z`  
Current process started UTC: `2026-09-21T15:13:59.085154Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3495, delta=3, z=3.79 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3492, delta=-4, z=3.73 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1870, 2026-09-21T15:15:34.609850Z)
- `FUELINST|fuelType=OTHER|generation` = **479** (n=1870, 2026-09-21T15:15:34.609850Z)
- `FUELINST|fuelType=PS|generation` = **-21** (n=1870, 2026-09-21T15:15:34.609850Z)
- `FUELINST|fuelType=WIND|generation` = **3346** (n=1870, 2026-09-21T15:15:34.609850Z)
- `IMBALNGC|TOTAL|imbalance` = **-3207** (n=307, 2026-09-21T14:53:36.483430Z)
- `INDDEM|TOTAL|demand` = **-12297** (n=307, 2026-09-21T14:53:21.042989Z)
- `INDGEN|TOTAL|generation` = **18297** (n=307, 2026-09-21T14:53:21.042989Z)
- `MELNGC|TOTAL|margin` = **36253** (n=307, 2026-09-21T14:50:57.433989Z)
- `MID|dataProvider=APXMIDP|price` = **141.2** (n=48, 2026-09-21T15:12:19.798978Z)
- `MID|dataProvider=APXMIDP|volume` = **3356.4** (n=48, 2026-09-21T15:12:19.798978Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=94, 2026-09-21T15:12:19.798978Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=94, 2026-09-21T15:12:19.798978Z)
- `NDF|TOTAL|demand` = **21004** (n=314, 2026-09-21T14:48:33.964949Z)
- `TSDF|TOTAL|demand` = **21504** (n=314, 2026-09-21T14:48:33.964949Z)
- `WINDFOR|TOTAL|generation` = **8616** (n=53, 2026-09-21T12:30:32.614458Z)

## Latest publication events

- `2026-09-21T15:16:22.797744Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:15:45Z`
- `2026-09-21T15:15:34.609850Z` — **FUELINST**: 80 rows; marker `2026-09-21T15:15:00Z`
- `2026-09-21T15:14:15.087213Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:13:45Z`
- `2026-09-21T15:12:19.798978Z` — **MID**: 2 rows; marker `2026-09-21T15:12:03Z`
- `2026-09-21T15:12:19.798978Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:11:45Z`
- `2026-09-21T15:10:27.101453Z` — **FUELINST**: 80 rows; marker `2026-09-21T15:10:00Z`
- `2026-09-21T15:10:10.942159Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:09:45Z`
- `2026-09-21T15:08:06.556662Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:07:45Z`
- `2026-09-21T15:06:30.015271Z` — **MID**: 1 rows; marker `2026-09-21T15:05:00Z`
- `2026-09-21T15:06:12.838603Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:05:45Z`
- `2026-09-21T15:05:24.552154Z` — **FUELINST**: 80 rows; marker `2026-09-21T15:05:00Z`
- `2026-09-21T15:04:07.412197Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:03:45Z`
- `2026-09-21T15:02:15.156195Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:01:45Z`
- `2026-09-21T15:00:42.830868Z` — **FUELHH**: 20 rows; marker `2026-09-21T15:00:00Z`
- `2026-09-21T15:00:26.767132Z` — **FUELINST**: 80 rows; marker `2026-09-21T15:00:00Z`
