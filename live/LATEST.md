# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T15:03:27.853241Z`  
Current process started UTC: `2026-09-16T14:59:27.910760Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3282, delta=0, z=-3.58 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1269** (n=505, 2026-09-16T15:00:32.042962Z)
- `FUELINST|fuelType=NPSHYD|generation` = **379** (n=505, 2026-09-16T15:00:32.042962Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3295** (n=505, 2026-09-16T15:00:32.042962Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=505, 2026-09-16T15:00:32.042962Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=505, 2026-09-16T15:00:32.042962Z)
- `FUELINST|fuelType=OTHER|generation` = **442** (n=505, 2026-09-16T15:00:32.042962Z)
- `FUELINST|fuelType=PS|generation` = **233** (n=505, 2026-09-16T15:00:32.042962Z)
- `FUELINST|fuelType=WIND|generation` = **5433** (n=505, 2026-09-16T15:00:32.042962Z)
- `IMBALNGC|TOTAL|imbalance` = **6731** (n=83, 2026-09-16T14:53:31.076071Z)
- `INDDEM|TOTAL|demand` = **-11776** (n=83, 2026-09-16T14:53:14.892448Z)
- `INDGEN|TOTAL|generation` = **25511** (n=83, 2026-09-16T14:53:14.892448Z)
- `MELNGC|TOTAL|margin` = **34664** (n=83, 2026-09-16T14:50:36.190848Z)
- `NDF|TOTAL|demand` = **18280** (n=85, 2026-09-16T14:48:13.119768Z)
- `TSDF|TOTAL|demand` = **18780** (n=85, 2026-09-16T14:48:13.119768Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T15:02:24.413211Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:01:45Z`
- `2026-09-16T15:00:32.042962Z` — **FUELHH**: 20 rows; marker `2026-09-16T15:00:00Z`
- `2026-09-16T15:00:32.042962Z` — **FUELINST**: 80 rows; marker `2026-09-16T15:00:00Z`
- `2026-09-16T15:00:15.941730Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:59:45Z`
- `2026-09-16T14:58:14.261575Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:57:45Z`
- `2026-09-16T14:56:05.824605Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:55:45Z`
- `2026-09-16T14:55:33.683238Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:55:00Z`
- `2026-09-16T14:54:19.152461Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:53:45Z`
- `2026-09-16T14:53:31.076071Z` — **IMBALNGC**: 1332 rows; marker `2026-09-16T14:47:00Z`
- `2026-09-16T14:53:14.892448Z` — **INDGEN**: 1332 rows; marker `2026-09-16T14:47:00Z`
- `2026-09-16T14:53:14.892448Z` — **INDDEM**: 1332 rows; marker `2026-09-16T14:47:00Z`
- `2026-09-16T14:52:11.068472Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:51:45Z`
- `2026-09-16T14:50:51.593487Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:50:00Z`
- `2026-09-16T14:50:36.190848Z` — **MELNGC**: 1332 rows; marker `2026-09-16T14:47:00Z`
- `2026-09-16T14:50:20.625428Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:49:45Z`
