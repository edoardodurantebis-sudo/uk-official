# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T13:10:06.629727Z`  
Current process started UTC: `2026-09-16T13:06:06.338524Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3291, delta=-1, z=-3.85 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3293, delta=-7, z=-3.99 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3292, delta=-3, z=-3.79 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=482, 2026-09-16T13:05:21.611671Z)
- `FUELINST|fuelType=NPSHYD|generation` = **353** (n=482, 2026-09-16T13:05:21.611671Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3291** (n=482, 2026-09-16T13:05:21.611671Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=482, 2026-09-16T13:05:21.611671Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=482, 2026-09-16T13:05:21.611671Z)
- `FUELINST|fuelType=OTHER|generation` = **469** (n=482, 2026-09-16T13:05:21.611671Z)
- `FUELINST|fuelType=PS|generation` = **-3** (n=482, 2026-09-16T13:05:21.611671Z)
- `FUELINST|fuelType=WIND|generation` = **3843** (n=482, 2026-09-16T13:05:21.611671Z)
- `IMBALNGC|TOTAL|imbalance` = **6176** (n=79, 2026-09-16T12:53:54.729559Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=79, 2026-09-16T12:53:54.729559Z)
- `INDGEN|TOTAL|generation` = **24956** (n=79, 2026-09-16T12:53:54.729559Z)
- `MELNGC|TOTAL|margin` = **35502** (n=79, 2026-09-16T12:50:48.860242Z)
- `NDF|TOTAL|demand` = **18280** (n=81, 2026-09-16T12:48:32.910664Z)
- `TSDF|TOTAL|demand` = **18780** (n=81, 2026-09-16T12:48:32.910664Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T13:08:14.047588Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:07:45Z`
- `2026-09-16T13:06:22.360127Z` — **MID**: 0 rows; marker `2026-09-16T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T13:06:06.338532Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:05:45Z`
- `2026-09-16T13:05:21.611671Z` — **FUELINST**: 80 rows; marker `2026-09-16T13:05:00Z`
- `2026-09-16T13:04:16.962036Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:03:45Z`
- `2026-09-16T13:02:08.677012Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:01:45Z`
- `2026-09-16T13:00:34.778646Z` — **FUELHH**: 20 rows; marker `2026-09-16T13:00:00Z`
- `2026-09-16T13:00:34.778646Z` — **FUELINST**: 80 rows; marker `2026-09-16T13:00:00Z`
- `2026-09-16T13:00:18.406738Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:59:45Z`
- `2026-09-16T12:58:11.075523Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:57:45Z`
- `2026-09-16T12:56:18.286766Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:55:45Z`
- `2026-09-16T12:55:46.095565Z` — **FUELINST**: 80 rows; marker `2026-09-16T12:55:00Z`
- `2026-09-16T12:54:26.156999Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:53:45Z`
- `2026-09-16T12:53:54.729559Z` — **INDGEN**: 1404 rows; marker `2026-09-16T12:48:00Z`
- `2026-09-16T12:53:54.729559Z` — **INDDEM**: 1404 rows; marker `2026-09-16T12:48:00Z`
