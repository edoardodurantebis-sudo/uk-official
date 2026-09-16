# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T15:54:02.331677Z`  
Current process started UTC: `2026-09-16T15:50:02.742374Z`  
1-second metadata polls in this process: **232**  
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

- `FUELINST|fuelType=INTVKL|generation` = **777** (n=515, 2026-09-16T15:50:21.744441Z)
- `FUELINST|fuelType=NPSHYD|generation` = **393** (n=515, 2026-09-16T15:50:21.744441Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3302** (n=515, 2026-09-16T15:50:21.744441Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=515, 2026-09-16T15:50:21.744441Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=515, 2026-09-16T15:50:21.744441Z)
- `FUELINST|fuelType=OTHER|generation` = **575** (n=515, 2026-09-16T15:50:21.744441Z)
- `FUELINST|fuelType=PS|generation` = **223** (n=515, 2026-09-16T15:50:21.744441Z)
- `FUELINST|fuelType=WIND|generation` = **5389** (n=515, 2026-09-16T15:50:21.744441Z)
- `IMBALNGC|TOTAL|imbalance` = **6407** (n=85, 2026-09-16T15:53:34.313893Z)
- `INDDEM|TOTAL|demand` = **-11776** (n=85, 2026-09-16T15:53:34.313893Z)
- `INDGEN|TOTAL|generation` = **25528** (n=85, 2026-09-16T15:53:34.313893Z)
- `MELNGC|TOTAL|margin` = **34237** (n=85, 2026-09-16T15:50:37.832483Z)
- `NDF|TOTAL|demand` = **18621** (n=87, 2026-09-16T15:48:30.092448Z)
- `TSDF|TOTAL|demand` = **19121** (n=87, 2026-09-16T15:48:30.092448Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T15:53:34.313893Z` — **INDGEN**: 1296 rows; marker `2026-09-16T15:47:00Z`
- `2026-09-16T15:53:34.313893Z` — **INDDEM**: 1296 rows; marker `2026-09-16T15:47:00Z`
- `2026-09-16T15:53:34.313893Z` — **IMBALNGC**: 1296 rows; marker `2026-09-16T15:48:00Z`
- `2026-09-16T15:52:14.016583Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:51:45Z`
- `2026-09-16T15:50:37.832483Z` — **MELNGC**: 1296 rows; marker `2026-09-16T15:48:00Z`
- `2026-09-16T15:50:21.744441Z` — **FUELINST**: 80 rows; marker `2026-09-16T15:50:00Z`
- `2026-09-16T15:50:21.744441Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:49:45Z`
- `2026-09-16T15:48:30.092448Z` — **TSDF**: 1296 rows; marker `2026-09-16T15:48:00Z`
- `2026-09-16T15:48:30.092448Z` — **NDF**: 72 rows; marker `2026-09-16T15:48:00Z`
- `2026-09-16T15:48:14.580066Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:47:45Z`
- `2026-09-16T15:46:06.658373Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:45:45Z`
- `2026-09-16T15:45:50.468593Z` — **FUELINST**: 80 rows; marker `2026-09-16T15:45:00Z`
- `2026-09-16T15:44:18.987331Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:43:45Z`
- `2026-09-16T15:42:26.804991Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:41:45Z`
- `2026-09-16T15:42:10.592136Z` — **MID**: 0 rows; marker `2026-09-16T15:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
