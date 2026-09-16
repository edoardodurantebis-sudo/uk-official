# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T13:43:46.926739Z`  
Current process started UTC: `2026-09-16T13:39:46.292670Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3284, delta=-3, z=-4.16 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3287, delta=-2, z=-3.91 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3289, delta=-4, z=-4.11 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3289, delta=-1, z=-3.74 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3290, delta=2, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3288, delta=3, z=-3.98 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3285, delta=-3, z=-4.41 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3288, delta=-3, z=-4.14 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3291, delta=-1, z=-3.85 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3293, delta=-7, z=-3.99 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3292, delta=-3, z=-3.79 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3290, delta=0, z=-4.16 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3290, delta=-7, z=-4.24 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3295, delta=-5, z=-3.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3297, delta=3, z=-3.70 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=489, 2026-09-16T13:40:34.580372Z)
- `FUELINST|fuelType=NPSHYD|generation` = **352** (n=489, 2026-09-16T13:40:34.580372Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3284** (n=489, 2026-09-16T13:40:34.580372Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=489, 2026-09-16T13:40:34.580372Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=489, 2026-09-16T13:40:34.580372Z)
- `FUELINST|fuelType=OTHER|generation` = **420** (n=489, 2026-09-16T13:40:34.580372Z)
- `FUELINST|fuelType=PS|generation` = **-3** (n=489, 2026-09-16T13:40:34.580372Z)
- `FUELINST|fuelType=WIND|generation` = **4500** (n=489, 2026-09-16T13:40:34.580372Z)
- `IMBALNGC|TOTAL|imbalance` = **6480** (n=80, 2026-09-16T13:24:32.797833Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=80, 2026-09-16T13:24:17.142806Z)
- `INDGEN|TOTAL|generation` = **25260** (n=80, 2026-09-16T13:24:17.142806Z)
- `MELNGC|TOTAL|margin` = **35428** (n=80, 2026-09-16T13:21:05.897772Z)
- `NDF|TOTAL|demand` = **18280** (n=82, 2026-09-16T13:18:15.013324Z)
- `TSDF|TOTAL|demand` = **18780** (n=82, 2026-09-16T13:18:15.013324Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T13:42:25.943350Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:41:45Z`
- `2026-09-16T13:42:10.079602Z` — **MID**: 0 rows; marker `2026-09-16T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T13:40:34.580372Z` — **FUELINST**: 80 rows; marker `2026-09-16T13:40:00Z`
- `2026-09-16T13:40:18.474775Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:39:45Z`
- `2026-09-16T13:38:27.728163Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:37:45Z`
- `2026-09-16T13:36:19.978234Z` — **MID**: 0 rows; marker `2026-09-16T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T13:36:19.978234Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:35:45Z`
- `2026-09-16T13:35:32.123852Z` — **FUELINST**: 80 rows; marker `2026-09-16T13:35:00Z`
- `2026-09-16T13:34:28.079267Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:33:45Z`
- `2026-09-16T13:32:20.232194Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:31:45Z`
- `2026-09-16T13:30:48.604117Z` — **FUELHH**: 20 rows; marker `2026-09-16T13:30:00Z`
- `2026-09-16T13:30:48.604117Z` — **FUELINST**: 80 rows; marker `2026-09-16T13:30:00Z`
- `2026-09-16T13:30:16.631421Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:29:45Z`
- `2026-09-16T13:28:24.322558Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:27:45Z`
- `2026-09-16T13:26:24.859295Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:25:45Z`
