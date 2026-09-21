# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T21:44:54.148870Z`  
Current process started UTC: `2026-09-21T21:40:54.044756Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=1, z=5.37 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=7, z=5.40 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3621, delta=45, z=5.10 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3641, delta=11, z=5.31 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3630, delta=10, z=5.15 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3620, delta=4, z=5.00 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3616, delta=2, z=4.96 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3614, delta=9, z=4.96 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3605, delta=9, z=4.82 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3576, delta=42, z=4.41 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3596, delta=9, z=4.68 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3587, delta=7, z=4.54 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3580, delta=8, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3572, delta=9, z=4.31 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3563, delta=6, z=4.16 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1947, 2026-09-21T21:40:54.044767Z)
- `FUELINST|fuelType=OTHER|generation` = **192** (n=1947, 2026-09-21T21:40:54.044767Z)
- `FUELINST|fuelType=PS|generation` = **33** (n=1947, 2026-09-21T21:40:54.044767Z)
- `FUELINST|fuelType=WIND|generation` = **4023** (n=1947, 2026-09-21T21:40:54.044767Z)
- `IMBALNGC|TOTAL|imbalance` = **-2609** (n=320, 2026-09-21T21:22:34.462060Z)
- `INDDEM|TOTAL|demand` = **-12255** (n=320, 2026-09-21T21:22:18.668387Z)
- `INDGEN|TOTAL|generation` = **18850** (n=320, 2026-09-21T21:22:18.668387Z)
- `MELNGC|TOTAL|margin` = **36065** (n=320, 2026-09-21T21:20:42.770480Z)
- `MID|dataProvider=APXMIDP|price` = **156.16** (n=61, 2026-09-21T21:42:14.237076Z)
- `MID|dataProvider=APXMIDP|volume` = **2626.3** (n=61, 2026-09-21T21:42:14.237076Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=120, 2026-09-21T21:42:14.237076Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=120, 2026-09-21T21:42:14.237076Z)
- `NDF|TOTAL|demand` = **20959** (n=327, 2026-09-21T21:18:04.701636Z)
- `TSDF|TOTAL|demand` = **21459** (n=327, 2026-09-21T21:18:04.701636Z)
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T21:44:23.303323Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:43:45Z`
- `2026-09-21T21:42:30.246046Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:41:45Z`
- `2026-09-21T21:42:14.237076Z` — **MID**: 2 rows; marker `2026-09-21T21:42:04Z`
- `2026-09-21T21:40:54.044767Z` — **FUELINST**: 80 rows; marker `2026-09-21T21:40:00Z`
- `2026-09-21T21:40:26.002432Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:39:45Z`
- `2026-09-21T21:38:18.646495Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:37:45Z`
- `2026-09-21T21:36:16.048751Z` — **MID**: 1 rows; marker `2026-09-21T21:35:00Z`
- `2026-09-21T21:36:16.048751Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:35:45Z`
- `2026-09-21T21:35:43.738786Z` — **FUELINST**: 80 rows; marker `2026-09-21T21:35:00Z`
- `2026-09-21T21:34:24.147825Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:33:45Z`
- `2026-09-21T21:32:16.281496Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:31:45Z`
- `2026-09-21T21:30:41.102399Z` — **FUELHH**: 20 rows; marker `2026-09-21T21:30:00Z`
- `2026-09-21T21:30:41.102399Z` — **FUELINST**: 80 rows; marker `2026-09-21T21:30:00Z`
- `2026-09-21T21:30:25.738435Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:29:45Z`
- `2026-09-21T21:28:18.125805Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:27:45Z`
