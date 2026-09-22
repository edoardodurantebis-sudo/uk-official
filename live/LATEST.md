# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T06:40:52.901761Z`  
Current process started UTC: `2026-09-22T06:36:52.710336Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=-1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3662, delta=5, z=3.53 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3659, delta=11, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3659, delta=-2, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=1, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=-3, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3663, delta=14, z=3.65 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-2, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-5, z=3.50 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=6, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3647, delta=3, z=3.52 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3650, delta=-4, z=3.64 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2055, 2026-09-22T06:40:40.095074Z)
- `FUELINST|fuelType=OTHER|generation` = **2953** (n=2055, 2026-09-22T06:40:40.095074Z)
- `FUELINST|fuelType=PS|generation` = **-54** (n=2055, 2026-09-22T06:40:40.095074Z)
- `FUELINST|fuelType=WIND|generation` = **3343** (n=2055, 2026-09-22T06:40:40.095074Z)
- `IMBALNGC|TOTAL|imbalance` = **-3011** (n=338, 2026-09-22T06:20:29.729318Z)
- `INDDEM|TOTAL|demand` = **-12476** (n=338, 2026-09-22T06:20:29.729318Z)
- `INDGEN|TOTAL|generation` = **18448** (n=338, 2026-09-22T06:20:29.729318Z)
- `MELNGC|TOTAL|margin` = **37790** (n=338, 2026-09-22T06:19:14.153555Z)
- `MID|dataProvider=APXMIDP|price` = **180.97** (n=78, 2026-09-22T06:12:19.847218Z)
- `MID|dataProvider=APXMIDP|volume` = **3045.3** (n=78, 2026-09-22T06:12:19.847218Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=155, 2026-09-22T06:37:27.714696Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=155, 2026-09-22T06:37:27.714696Z)
- `NDF|TOTAL|demand` = **20959** (n=345, 2026-09-22T06:17:20.431637Z)
- `TSDF|TOTAL|demand` = **21459** (n=345, 2026-09-22T06:17:20.431637Z)
- `WINDFOR|TOTAL|generation` = **12340** (n=58, 2026-09-22T05:30:40.954997Z)

## Latest publication events

- `2026-09-22T06:40:40.095074Z` — **FUELINST**: 80 rows; marker `2026-09-22T06:40:00Z`
- `2026-09-22T06:40:24.197435Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:39:45Z`
- `2026-09-22T06:38:16.178871Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:37:45Z`
- `2026-09-22T06:37:27.714696Z` — **MID**: 1 rows; marker `2026-09-22T06:35:00Z`
- `2026-09-22T06:36:23.217222Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:35:45Z`
- `2026-09-22T06:35:35.539928Z` — **FUELINST**: 80 rows; marker `2026-09-22T06:35:00Z`
- `2026-09-22T06:34:15.297487Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:33:45Z`
- `2026-09-22T06:32:39.363441Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:31:45Z`
- `2026-09-22T06:30:33.041271Z` — **FUELHH**: 20 rows; marker `2026-09-22T06:30:00Z`
- `2026-09-22T06:30:33.041271Z` — **FUELINST**: 80 rows; marker `2026-09-22T06:30:00Z`
- `2026-09-22T06:30:17.519425Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:29:45Z`
- `2026-09-22T06:28:25.335531Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:27:45Z`
- `2026-09-22T06:26:21.497972Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:25:45Z`
- `2026-09-22T06:25:34.134411Z` — **FUELINST**: 80 rows; marker `2026-09-22T06:25:00Z`
- `2026-09-22T06:24:12.539896Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:23:45Z`
