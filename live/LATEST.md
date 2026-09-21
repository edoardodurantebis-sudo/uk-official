# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T23:18:21.679371Z`  
Current process started UTC: `2026-09-21T23:14:22.055927Z`  
1-second metadata polls in this process: **233**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3643, delta=-2, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=0, z=4.72 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=-2, z=4.75 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3642, delta=4, z=4.87 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3647, delta=5, z=4.81 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3642, delta=-2, z=4.75 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3644, delta=-2, z=4.82 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3646, delta=6, z=4.88 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3640, delta=5, z=4.81 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3635, delta=-1, z=4.76 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3638, delta=-7, z=4.99 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3636, delta=-1, z=4.80 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3637, delta=3, z=4.85 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3634, delta=-8, z=4.83 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3642, delta=3, z=5.00 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1966, 2026-09-21T23:15:27.390068Z)
- `FUELINST|fuelType=OTHER|generation` = **518** (n=1966, 2026-09-21T23:15:27.390068Z)
- `FUELINST|fuelType=PS|generation` = **-138** (n=1966, 2026-09-21T23:15:27.390068Z)
- `FUELINST|fuelType=WIND|generation` = **3591** (n=1966, 2026-09-21T23:15:27.390068Z)
- `IMBALNGC|TOTAL|imbalance` = **-2493** (n=323, 2026-09-21T22:51:42.290265Z)
- `INDDEM|TOTAL|demand` = **-12379** (n=323, 2026-09-21T22:51:26.349395Z)
- `INDGEN|TOTAL|generation` = **18966** (n=323, 2026-09-21T22:51:26.349395Z)
- `MELNGC|TOTAL|margin` = **36234** (n=323, 2026-09-21T22:49:34.128825Z)
- `MID|dataProvider=APXMIDP|price` = **142.81** (n=64, 2026-09-21T23:12:18.557209Z)
- `MID|dataProvider=APXMIDP|volume` = **1777.2** (n=64, 2026-09-21T23:12:18.557209Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=126, 2026-09-21T23:12:18.557209Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=126, 2026-09-21T23:12:18.557209Z)
- `NDF|TOTAL|demand` = **20959** (n=331, 2026-09-21T23:17:21.026219Z)
- `TSDF|TOTAL|demand` = **21459** (n=331, 2026-09-21T23:17:38.428444Z)
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T23:18:09.955027Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:17:45Z`
- `2026-09-21T23:17:38.428444Z` — **TSDF**: 1026 rows; marker `2026-09-21T23:17:00Z`
- `2026-09-21T23:17:21.026219Z` — **NDF**: 57 rows; marker `2026-09-21T23:17:00Z`
- `2026-09-21T23:16:16.480124Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:15:45Z`
- `2026-09-21T23:15:27.390068Z` — **FUELINST**: 80 rows; marker `2026-09-21T23:15:00Z`
- `2026-09-21T23:14:22.055938Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:13:45Z`
- `2026-09-21T23:12:18.557209Z` — **MID**: 2 rows; marker `2026-09-21T23:12:03Z`
- `2026-09-21T23:12:18.557209Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:11:45Z`
- `2026-09-21T23:10:25.737692Z` — **FUELINST**: 80 rows; marker `2026-09-21T23:10:00Z`
- `2026-09-21T23:10:10.023749Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:09:45Z`
- `2026-09-21T23:08:07.262479Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:07:45Z`
- `2026-09-21T23:06:29.897621Z` — **MID**: 1 rows; marker `2026-09-21T23:05:00Z`
- `2026-09-21T23:06:12.992107Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:05:45Z`
- `2026-09-21T23:05:30.058354Z` — **FUELINST**: 80 rows; marker `2026-09-21T23:05:00Z`
- `2026-09-21T23:04:09.975014Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:03:45Z`
