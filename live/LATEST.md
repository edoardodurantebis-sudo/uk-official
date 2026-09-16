# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T13:52:13.017685Z`  
Current process started UTC: `2026-09-16T13:48:12.126222Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3287, delta=3, z=-3.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3284, delta=0, z=-4.09 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=491, 2026-09-16T13:50:19.333000Z)
- `FUELINST|fuelType=NPSHYD|generation` = **354** (n=491, 2026-09-16T13:50:19.333000Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3287** (n=491, 2026-09-16T13:50:19.333000Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=491, 2026-09-16T13:50:19.333000Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=491, 2026-09-16T13:50:19.333000Z)
- `FUELINST|fuelType=OTHER|generation` = **480** (n=491, 2026-09-16T13:50:19.333000Z)
- `FUELINST|fuelType=PS|generation` = **-3** (n=491, 2026-09-16T13:50:19.333000Z)
- `FUELINST|fuelType=WIND|generation` = **4765** (n=491, 2026-09-16T13:50:19.333000Z)
- `IMBALNGC|TOTAL|imbalance` = **6480** (n=80, 2026-09-16T13:24:32.797833Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=80, 2026-09-16T13:24:17.142806Z)
- `INDGEN|TOTAL|generation` = **25260** (n=80, 2026-09-16T13:24:17.142806Z)
- `MELNGC|TOTAL|margin` = **35109** (n=81, 2026-09-16T13:50:19.333000Z)
- `NDF|TOTAL|demand` = **18280** (n=83, 2026-09-16T13:47:47.305117Z)
- `TSDF|TOTAL|demand` = **18780** (n=83, 2026-09-16T13:48:12.126230Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T13:52:10.909228Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:51:45Z`
- `2026-09-16T13:50:19.333000Z` — **MELNGC**: 1368 rows; marker `2026-09-16T13:47:00Z`
- `2026-09-16T13:50:19.333000Z` — **FUELINST**: 80 rows; marker `2026-09-16T13:50:00Z`
- `2026-09-16T13:50:03.238137Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:49:45Z`
- `2026-09-16T13:48:12.126230Z` — **TSDF**: 1368 rows; marker `2026-09-16T13:47:00Z`
- `2026-09-16T13:48:12.126230Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:47:45Z`
- `2026-09-16T13:47:47.305117Z` — **NDF**: 76 rows; marker `2026-09-16T13:47:00Z`
- `2026-09-16T13:46:10.698211Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:45:45Z`
- `2026-09-16T13:45:38.644454Z` — **FUELINST**: 80 rows; marker `2026-09-16T13:45:00Z`
- `2026-09-16T13:44:18.288973Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:43:45Z`
- `2026-09-16T13:42:25.943350Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:41:45Z`
- `2026-09-16T13:42:10.079602Z` — **MID**: 0 rows; marker `2026-09-16T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T13:40:34.580372Z` — **FUELINST**: 80 rows; marker `2026-09-16T13:40:00Z`
- `2026-09-16T13:40:18.474775Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:39:45Z`
- `2026-09-16T13:38:27.728163Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:37:45Z`
