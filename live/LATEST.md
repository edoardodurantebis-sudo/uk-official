# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T03:55:16.197266Z`  
Current process started UTC: `2026-09-22T03:51:15.961253Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-3, z=3.73 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-1, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3658, delta=1, z=3.81 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3657, delta=7, z=3.81 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3655, delta=1, z=3.88 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=2, z=3.73 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-9, z=3.72 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-3, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=-1, z=3.91 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=6, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3655, delta=1, z=3.87 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3654, delta=1, z=3.96 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-2, z=3.87 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=2, z=3.92 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=1, z=3.91 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2021, 2026-09-22T03:50:29.821745Z)
- `FUELINST|fuelType=OTHER|generation` = **433** (n=2021, 2026-09-22T03:50:29.821745Z)
- `FUELINST|fuelType=PS|generation` = **-711** (n=2021, 2026-09-22T03:50:29.821745Z)
- `FUELINST|fuelType=WIND|generation` = **3727** (n=2021, 2026-09-22T03:50:29.821745Z)
- `IMBALNGC|TOTAL|imbalance` = **-3236** (n=333, 2026-09-22T03:51:48.287512Z)
- `INDDEM|TOTAL|demand` = **-12505** (n=333, 2026-09-22T03:51:31.963247Z)
- `INDGEN|TOTAL|generation` = **18223** (n=333, 2026-09-22T03:51:31.963247Z)
- `MELNGC|TOTAL|margin` = **37799** (n=333, 2026-09-22T03:50:14.132078Z)
- `MID|dataProvider=APXMIDP|price` = **152.69** (n=73, 2026-09-22T03:42:20.599411Z)
- `MID|dataProvider=APXMIDP|volume` = **2378.9** (n=73, 2026-09-22T03:42:20.599411Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=144, 2026-09-22T03:42:20.599411Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=144, 2026-09-22T03:42:20.599411Z)
- `NDF|TOTAL|demand` = **20959** (n=340, 2026-09-22T03:48:21.169915Z)
- `TSDF|TOTAL|demand` = **21459** (n=340, 2026-09-22T03:48:21.169915Z)
- `WINDFOR|TOTAL|generation` = **11644** (n=57, 2026-09-22T03:30:45.244161Z)

## Latest publication events

- `2026-09-22T03:52:19.934935Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:51:45Z`
- `2026-09-22T03:51:48.287512Z` — **IMBALNGC**: 864 rows; marker `2026-09-22T03:47:00Z`
- `2026-09-22T03:51:31.963247Z` — **INDGEN**: 864 rows; marker `2026-09-22T03:47:00Z`
- `2026-09-22T03:51:31.963247Z` — **INDDEM**: 864 rows; marker `2026-09-22T03:47:00Z`
- `2026-09-22T03:50:29.821745Z` — **FUELINST**: 80 rows; marker `2026-09-22T03:50:00Z`
- `2026-09-22T03:50:14.132078Z` — **MELNGC**: 864 rows; marker `2026-09-22T03:47:00Z`
- `2026-09-22T03:50:14.132078Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:49:45Z`
- `2026-09-22T03:48:21.169915Z` — **TSDF**: 864 rows; marker `2026-09-22T03:47:00Z`
- `2026-09-22T03:48:21.169915Z` — **NDF**: 48 rows; marker `2026-09-22T03:47:00Z`
- `2026-09-22T03:48:21.169915Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:47:45Z`
- `2026-09-22T03:46:19.607952Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:45:45Z`
- `2026-09-22T03:45:31.578220Z` — **FUELINST**: 80 rows; marker `2026-09-22T03:45:00Z`
- `2026-09-22T03:44:12.116051Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:43:45Z`
- `2026-09-22T03:42:20.599411Z` — **MID**: 2 rows; marker `2026-09-22T03:42:04Z`
- `2026-09-22T03:42:20.599411Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:41:45Z`
