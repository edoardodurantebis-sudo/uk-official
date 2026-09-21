# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T21:19:41.751159Z`  
Current process started UTC: `2026-09-21T21:15:41.473848Z`  
1-second metadata polls in this process: **231**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3539, delta=7, z=3.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3532, delta=10, z=3.64 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1942, 2026-09-21T21:15:41.473858Z)
- `FUELINST|fuelType=OTHER|generation` = **485** (n=1942, 2026-09-21T21:15:41.473858Z)
- `FUELINST|fuelType=PS|generation` = **-9** (n=1942, 2026-09-21T21:15:41.473858Z)
- `FUELINST|fuelType=WIND|generation` = **3646** (n=1942, 2026-09-21T21:15:41.473858Z)
- `IMBALNGC|TOTAL|imbalance` = **-2649** (n=319, 2026-09-21T20:52:05.346372Z)
- `INDDEM|TOTAL|demand` = **-12259** (n=319, 2026-09-21T20:52:05.346372Z)
- `INDGEN|TOTAL|generation` = **18810** (n=319, 2026-09-21T20:52:05.346372Z)
- `MELNGC|TOTAL|margin` = **36086** (n=319, 2026-09-21T20:49:58.052949Z)
- `MID|dataProvider=APXMIDP|price` = **165.9** (n=60, 2026-09-21T21:12:17.454991Z)
- `MID|dataProvider=APXMIDP|volume` = **2494.1** (n=60, 2026-09-21T21:12:17.454991Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=118, 2026-09-21T21:12:17.454991Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=118, 2026-09-21T21:12:17.454991Z)
- `NDF|TOTAL|demand` = **20959** (n=327, 2026-09-21T21:18:04.701636Z)
- `TSDF|TOTAL|demand` = **21459** (n=327, 2026-09-21T21:18:04.701636Z)
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T21:18:20.735786Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:17:45Z`
- `2026-09-21T21:18:04.701636Z` — **TSDF**: 1098 rows; marker `2026-09-21T21:17:00Z`
- `2026-09-21T21:18:04.701636Z` — **NDF**: 61 rows; marker `2026-09-21T21:17:00Z`
- `2026-09-21T21:16:13.121129Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:15:45Z`
- `2026-09-21T21:15:41.473858Z` — **FUELINST**: 80 rows; marker `2026-09-21T21:15:00Z`
- `2026-09-21T21:14:09.372880Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:13:45Z`
- `2026-09-21T21:12:17.454991Z` — **MID**: 2 rows; marker `2026-09-21T21:12:03Z`
- `2026-09-21T21:12:17.454991Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:11:45Z`
- `2026-09-21T21:10:30.002938Z` — **FUELINST**: 80 rows; marker `2026-09-21T21:10:00Z`
- `2026-09-21T21:10:12.690224Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:09:45Z`
- `2026-09-21T21:08:20.398733Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:07:45Z`
- `2026-09-21T21:07:32.139464Z` — **MID**: 1 rows; marker `2026-09-21T21:05:00Z`
- `2026-09-21T21:06:12.639667Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:05:45Z`
- `2026-09-21T21:05:25.036666Z` — **FUELINST**: 80 rows; marker `2026-09-21T21:05:00Z`
- `2026-09-21T21:04:21.704769Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:03:45Z`
