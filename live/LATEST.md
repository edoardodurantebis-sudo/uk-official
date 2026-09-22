# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T06:23:57.988786Z`  
Current process started UTC: `2026-09-22T06:19:58.183690Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2051, 2026-09-22T06:20:29.729318Z)
- `FUELINST|fuelType=OTHER|generation` = **2369** (n=2051, 2026-09-22T06:20:29.729318Z)
- `FUELINST|fuelType=PS|generation` = **-174** (n=2051, 2026-09-22T06:20:29.729318Z)
- `FUELINST|fuelType=WIND|generation` = **3436** (n=2051, 2026-09-22T06:20:29.729318Z)
- `IMBALNGC|TOTAL|imbalance` = **-3011** (n=338, 2026-09-22T06:20:29.729318Z)
- `INDDEM|TOTAL|demand` = **-12476** (n=338, 2026-09-22T06:20:29.729318Z)
- `INDGEN|TOTAL|generation` = **18448** (n=338, 2026-09-22T06:20:29.729318Z)
- `MELNGC|TOTAL|margin` = **37790** (n=338, 2026-09-22T06:19:14.153555Z)
- `MID|dataProvider=APXMIDP|price` = **180.97** (n=78, 2026-09-22T06:12:19.847218Z)
- `MID|dataProvider=APXMIDP|volume` = **3045.3** (n=78, 2026-09-22T06:12:19.847218Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=154, 2026-09-22T06:12:19.847218Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=154, 2026-09-22T06:12:19.847218Z)
- `NDF|TOTAL|demand` = **20959** (n=345, 2026-09-22T06:17:20.431637Z)
- `TSDF|TOTAL|demand` = **21459** (n=345, 2026-09-22T06:17:20.431637Z)
- `WINDFOR|TOTAL|generation` = **12340** (n=58, 2026-09-22T05:30:40.954997Z)

## Latest publication events

- `2026-09-22T06:22:21.862540Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:21:45Z`
- `2026-09-22T06:20:29.729318Z` — **INDGEN**: 774 rows; marker `2026-09-22T06:16:00Z`
- `2026-09-22T06:20:29.729318Z` — **INDDEM**: 774 rows; marker `2026-09-22T06:16:00Z`
- `2026-09-22T06:20:29.729318Z` — **IMBALNGC**: 774 rows; marker `2026-09-22T06:16:00Z`
- `2026-09-22T06:20:29.729318Z` — **FUELINST**: 80 rows; marker `2026-09-22T06:20:00Z`
- `2026-09-22T06:20:14.185665Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:19:45Z`
- `2026-09-22T06:19:14.153555Z` — **MELNGC**: 774 rows; marker `2026-09-22T06:16:00Z`
- `2026-09-22T06:18:08.149785Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:17:45Z`
- `2026-09-22T06:17:20.431637Z` — **TSDF**: 774 rows; marker `2026-09-22T06:16:00Z`
- `2026-09-22T06:17:20.431637Z` — **NDF**: 43 rows; marker `2026-09-22T06:16:00Z`
- `2026-09-22T06:16:16.467290Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:15:45Z`
- `2026-09-22T06:15:45.203733Z` — **FUELINST**: 80 rows; marker `2026-09-22T06:15:00Z`
- `2026-09-22T06:14:12.136418Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:13:45Z`
- `2026-09-22T06:12:19.847218Z` — **MID**: 2 rows; marker `2026-09-22T06:12:03Z`
- `2026-09-22T06:12:19.847218Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:11:45Z`
