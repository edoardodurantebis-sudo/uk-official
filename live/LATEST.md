# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T21:28:07.725120Z`  
Current process started UTC: `2026-09-21T21:24:08.031726Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3557, delta=8, z=4.06 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3534, delta=22, z=3.69 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3549, delta=2, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3547, delta=8, z=3.90 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1944, 2026-09-21T21:25:32.799618Z)
- `FUELINST|fuelType=OTHER|generation` = **337** (n=1944, 2026-09-21T21:25:32.799618Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1944, 2026-09-21T21:25:32.799618Z)
- `FUELINST|fuelType=WIND|generation` = **3852** (n=1944, 2026-09-21T21:25:32.799618Z)
- `IMBALNGC|TOTAL|imbalance` = **-2609** (n=320, 2026-09-21T21:22:34.462060Z)
- `INDDEM|TOTAL|demand` = **-12255** (n=320, 2026-09-21T21:22:18.668387Z)
- `INDGEN|TOTAL|generation` = **18850** (n=320, 2026-09-21T21:22:18.668387Z)
- `MELNGC|TOTAL|margin` = **36065** (n=320, 2026-09-21T21:20:42.770480Z)
- `MID|dataProvider=APXMIDP|price` = **165.9** (n=60, 2026-09-21T21:12:17.454991Z)
- `MID|dataProvider=APXMIDP|volume` = **2494.1** (n=60, 2026-09-21T21:12:17.454991Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=118, 2026-09-21T21:12:17.454991Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=118, 2026-09-21T21:12:17.454991Z)
- `NDF|TOTAL|demand` = **20959** (n=327, 2026-09-21T21:18:04.701636Z)
- `TSDF|TOTAL|demand` = **21459** (n=327, 2026-09-21T21:18:04.701636Z)
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T21:26:20.913259Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:25:45Z`
- `2026-09-21T21:25:32.799618Z` — **FUELINST**: 80 rows; marker `2026-09-21T21:25:00Z`
- `2026-09-21T21:24:12.032231Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:23:45Z`
- `2026-09-21T21:22:34.462060Z` — **IMBALNGC**: 1098 rows; marker `2026-09-21T21:17:00Z`
- `2026-09-21T21:22:18.668387Z` — **INDGEN**: 1098 rows; marker `2026-09-21T21:17:00Z`
- `2026-09-21T21:22:18.668387Z` — **INDDEM**: 1098 rows; marker `2026-09-21T21:17:00Z`
- `2026-09-21T21:22:18.668387Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:21:45Z`
- `2026-09-21T21:20:42.770480Z` — **MELNGC**: 1098 rows; marker `2026-09-21T21:17:00Z`
- `2026-09-21T21:20:27.263578Z` — **FUELINST**: 80 rows; marker `2026-09-21T21:20:00Z`
- `2026-09-21T21:20:27.263578Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:19:45Z`
- `2026-09-21T21:18:20.735786Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:17:45Z`
- `2026-09-21T21:18:04.701636Z` — **TSDF**: 1098 rows; marker `2026-09-21T21:17:00Z`
- `2026-09-21T21:18:04.701636Z` — **NDF**: 61 rows; marker `2026-09-21T21:17:00Z`
- `2026-09-21T21:16:13.121129Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:15:45Z`
- `2026-09-21T21:15:41.473858Z` — **FUELINST**: 80 rows; marker `2026-09-21T21:15:00Z`
