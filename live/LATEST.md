# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T01:17:03.136589Z`  
Current process started UTC: `2026-09-22T01:13:03.278677Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=1, z=4.25 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-1, z=4.25 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-6, z=4.29 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3659, delta=7, z=4.50 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=-1, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=2, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3659, delta=1, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3658, delta=-1, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3659, delta=2, z=4.47 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3657, delta=5, z=4.47 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3652, delta=3, z=4.54 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3652, delta=-1, z=4.42 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=1, z=4.46 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3652, delta=0, z=4.46 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3652, delta=2, z=4.49 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1990, 2026-09-22T01:15:29.356338Z)
- `FUELINST|fuelType=OTHER|generation` = **189** (n=1990, 2026-09-22T01:15:29.356338Z)
- `FUELINST|fuelType=PS|generation` = **-281** (n=1990, 2026-09-22T01:15:29.356338Z)
- `FUELINST|fuelType=WIND|generation` = **3640** (n=1990, 2026-09-22T01:15:29.356338Z)
- `IMBALNGC|TOTAL|imbalance` = **-2698** (n=327, 2026-09-22T00:51:05.358533Z)
- `INDDEM|TOTAL|demand` = **-12391** (n=327, 2026-09-22T00:50:49.434730Z)
- `INDGEN|TOTAL|generation` = **18761** (n=327, 2026-09-22T00:50:49.434730Z)
- `MELNGC|TOTAL|margin` = **36169** (n=327, 2026-09-22T00:49:29.610690Z)
- `MID|dataProvider=APXMIDP|price` = **138.2** (n=68, 2026-09-22T01:12:18.064520Z)
- `MID|dataProvider=APXMIDP|volume` = **2291.2** (n=68, 2026-09-22T01:12:18.064520Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=134, 2026-09-22T01:12:18.064520Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=134, 2026-09-22T01:12:18.064520Z)
- `NDF|TOTAL|demand` = **20959** (n=334, 2026-09-22T00:47:37.452998Z)
- `TSDF|TOTAL|demand` = **21459** (n=334, 2026-09-22T00:47:37.452998Z)
- `WINDFOR|TOTAL|generation` = **9503** (n=56, 2026-09-21T23:30:37.821418Z)

## Latest publication events

- `2026-09-22T01:16:17.362415Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:15:45Z`
- `2026-09-22T01:15:29.356338Z` — **FUELINST**: 80 rows; marker `2026-09-22T01:15:00Z`
- `2026-09-22T01:14:09.286715Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:13:45Z`
- `2026-09-22T01:12:18.064520Z` — **MID**: 2 rows; marker `2026-09-22T01:12:03Z`
- `2026-09-22T01:12:18.064520Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:11:45Z`
- `2026-09-22T01:10:25.997810Z` — **FUELINST**: 80 rows; marker `2026-09-22T01:10:00Z`
- `2026-09-22T01:10:10.370904Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:09:45Z`
- `2026-09-22T01:08:06.898156Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:07:45Z`
- `2026-09-22T01:07:34.757759Z` — **MID**: 1 rows; marker `2026-09-22T01:05:00Z`
- `2026-09-22T01:06:30.475822Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:05:45Z`
- `2026-09-22T01:05:25.362458Z` — **FUELINST**: 80 rows; marker `2026-09-22T01:05:00Z`
- `2026-09-22T01:04:09.951875Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:03:45Z`
- `2026-09-22T01:02:17.725684Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:01:45Z`
- `2026-09-22T01:00:40.898289Z` — **FUELHH**: 20 rows; marker `2026-09-22T01:00:00Z`
- `2026-09-22T01:00:24.664856Z` — **FUELINST**: 80 rows; marker `2026-09-22T01:00:00Z`
