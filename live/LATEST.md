# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T12:53:12.068167Z`  
Current process started UTC: `2026-09-16T12:49:12.649761Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3290, delta=0, z=-4.16 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3290, delta=-7, z=-4.24 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3295, delta=-5, z=-3.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3297, delta=3, z=-3.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3294, delta=-4, z=-4.20 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3298, delta=-3, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3290, delta=-7, z=-5.03 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3297, delta=-24, z=-4.07 -> generation-mix component moved
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11768, delta=3343, z=1.00 -> demand pressure up
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-15111, delta=-1226, z=-8.15 -> demand pressure easing
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-13885, delta=0, z=-5.69 -> demand pressure easing
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-13885, delta=-1204, z=-7.82 -> demand pressure easing
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.27 -> generation-mix component moved
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.52 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.55 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=479, 2026-09-16T12:50:32.688065Z)
- `FUELINST|fuelType=NPSHYD|generation` = **353** (n=479, 2026-09-16T12:50:32.688065Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3290** (n=479, 2026-09-16T12:50:32.688065Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=479, 2026-09-16T12:50:32.688065Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=479, 2026-09-16T12:50:32.688065Z)
- `FUELINST|fuelType=OTHER|generation` = **474** (n=479, 2026-09-16T12:50:32.688065Z)
- `FUELINST|fuelType=PS|generation` = **-5** (n=479, 2026-09-16T12:50:32.688065Z)
- `FUELINST|fuelType=WIND|generation` = **3943** (n=479, 2026-09-16T12:50:32.688065Z)
- `IMBALNGC|TOTAL|imbalance` = **6066** (n=78, 2026-09-16T12:23:48.551845Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=78, 2026-09-16T12:23:32.543133Z)
- `INDGEN|TOTAL|generation` = **24846** (n=78, 2026-09-16T12:23:32.543133Z)
- `MELNGC|TOTAL|margin` = **35502** (n=79, 2026-09-16T12:50:48.860242Z)
- `NDF|TOTAL|demand` = **18280** (n=81, 2026-09-16T12:48:32.910664Z)
- `TSDF|TOTAL|demand` = **18780** (n=81, 2026-09-16T12:48:32.910664Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T12:52:25.313481Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:51:45Z`
- `2026-09-16T12:50:48.860242Z` — **MELNGC**: 1404 rows; marker `2026-09-16T12:48:00Z`
- `2026-09-16T12:50:32.688065Z` — **FUELINST**: 80 rows; marker `2026-09-16T12:50:00Z`
- `2026-09-16T12:50:16.837760Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:49:45Z`
- `2026-09-16T12:48:32.910664Z` — **TSDF**: 1404 rows; marker `2026-09-16T12:48:00Z`
- `2026-09-16T12:48:32.910664Z` — **NDF**: 78 rows; marker `2026-09-16T12:48:00Z`
- `2026-09-16T12:48:17.010212Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:47:45Z`
- `2026-09-16T12:46:25.302962Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:45:45Z`
- `2026-09-16T12:45:37.698789Z` — **FUELINST**: 80 rows; marker `2026-09-16T12:45:00Z`
- `2026-09-16T12:44:18.967312Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:43:45Z`
- `2026-09-16T12:42:27.646953Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:41:45Z`
- `2026-09-16T12:42:11.580675Z` — **MID**: 0 rows; marker `2026-09-16T12:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T12:40:27.902578Z` — **FUELINST**: 80 rows; marker `2026-09-16T12:40:00Z`
- `2026-09-16T12:40:27.902578Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:39:45Z`
- `2026-09-16T12:38:20.245690Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:37:45Z`
