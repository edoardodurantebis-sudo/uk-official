# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T14:46:40.656853Z`  
Current process started UTC: `2026-09-16T14:42:40.966844Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3282, delta=-3, z=-3.63 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3286, delta=2, z=-3.65 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3285, delta=6, z=-3.64 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3279, delta=-1, z=-4.31 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3284, delta=-5, z=-4.28 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3280, delta=-3, z=-4.29 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3283, delta=-4, z=-4.06 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3287, delta=3, z=-3.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3284, delta=0, z=-4.09 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3284, delta=-3, z=-4.16 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3287, delta=-2, z=-3.91 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3289, delta=-4, z=-4.11 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3289, delta=-1, z=-3.74 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3290, delta=2, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3288, delta=3, z=-3.98 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=502, 2026-09-16T14:45:24.175467Z)
- `FUELINST|fuelType=NPSHYD|generation` = **367** (n=502, 2026-09-16T14:45:24.175467Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3282** (n=502, 2026-09-16T14:45:24.175467Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=502, 2026-09-16T14:45:24.175467Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=502, 2026-09-16T14:45:24.175467Z)
- `FUELINST|fuelType=OTHER|generation` = **522** (n=502, 2026-09-16T14:45:24.175467Z)
- `FUELINST|fuelType=PS|generation` = **233** (n=502, 2026-09-16T14:45:24.175467Z)
- `FUELINST|fuelType=WIND|generation` = **5428** (n=502, 2026-09-16T14:45:24.175467Z)
- `IMBALNGC|TOTAL|imbalance` = **6670** (n=82, 2026-09-16T14:23:34.552018Z)
- `INDDEM|TOTAL|demand` = **-11776** (n=82, 2026-09-16T14:23:34.552018Z)
- `INDGEN|TOTAL|generation` = **25450** (n=82, 2026-09-16T14:23:34.552018Z)
- `MELNGC|TOTAL|margin` = **34664** (n=82, 2026-09-16T14:20:27.682808Z)
- `NDF|TOTAL|demand` = **18280** (n=84, 2026-09-16T14:18:19.617927Z)
- `TSDF|TOTAL|demand` = **18780** (n=84, 2026-09-16T14:18:19.617927Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T14:46:11.960280Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:45:45Z`
- `2026-09-16T14:45:24.175467Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:45:00Z`
- `2026-09-16T14:44:02.978464Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:43:45Z`
- `2026-09-16T14:42:11.324256Z` — **MID**: 0 rows; marker `2026-09-16T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T14:42:11.324256Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:41:45Z`
- `2026-09-16T14:40:35.783619Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:40:00Z`
- `2026-09-16T14:40:03.400728Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:39:45Z`
- `2026-09-16T14:38:27.858029Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:37:45Z`
- `2026-09-16T14:36:24.326591Z` — **MID**: 0 rows; marker `2026-09-16T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T14:36:24.326591Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:35:45Z`
- `2026-09-16T14:35:36.280309Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:35:00Z`
- `2026-09-16T14:34:16.438329Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:33:45Z`
- `2026-09-16T14:32:15.113565Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:31:45Z`
- `2026-09-16T14:30:39.673714Z` — **FUELHH**: 20 rows; marker `2026-09-16T14:30:00Z`
- `2026-09-16T14:30:39.673714Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:30:00Z`
