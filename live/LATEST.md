# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T13:56:23.978771Z`  
Current process started UTC: `2026-09-16T13:52:23.892970Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3283, delta=-4, z=-4.06 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=492, 2026-09-16T13:55:22.038432Z)
- `FUELINST|fuelType=NPSHYD|generation` = **352** (n=492, 2026-09-16T13:55:22.038432Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3283** (n=492, 2026-09-16T13:55:22.038432Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=492, 2026-09-16T13:55:22.038432Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=492, 2026-09-16T13:55:22.038432Z)
- `FUELINST|fuelType=OTHER|generation` = **400** (n=492, 2026-09-16T13:55:22.038432Z)
- `FUELINST|fuelType=PS|generation` = **-3** (n=492, 2026-09-16T13:55:22.038432Z)
- `FUELINST|fuelType=WIND|generation` = **4859** (n=492, 2026-09-16T13:55:22.038432Z)
- `IMBALNGC|TOTAL|imbalance` = **6633** (n=81, 2026-09-16T13:52:58.897421Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=81, 2026-09-16T13:52:58.897421Z)
- `INDGEN|TOTAL|generation` = **25413** (n=81, 2026-09-16T13:52:58.897421Z)
- `MELNGC|TOTAL|margin` = **35109** (n=81, 2026-09-16T13:50:19.333000Z)
- `NDF|TOTAL|demand` = **18280** (n=83, 2026-09-16T13:47:47.305117Z)
- `TSDF|TOTAL|demand` = **18780** (n=83, 2026-09-16T13:48:12.126230Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T13:56:10.119403Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:55:45Z`
- `2026-09-16T13:55:22.038432Z` — **FUELINST**: 80 rows; marker `2026-09-16T13:55:00Z`
- `2026-09-16T13:54:02.585393Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:53:45Z`
- `2026-09-16T13:52:58.897421Z` — **INDGEN**: 1368 rows; marker `2026-09-16T13:47:00Z`
- `2026-09-16T13:52:58.897421Z` — **INDDEM**: 1368 rows; marker `2026-09-16T13:47:00Z`
- `2026-09-16T13:52:58.897421Z` — **IMBALNGC**: 1368 rows; marker `2026-09-16T13:47:00Z`
- `2026-09-16T13:52:10.909228Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:51:45Z`
- `2026-09-16T13:50:19.333000Z` — **MELNGC**: 1368 rows; marker `2026-09-16T13:47:00Z`
- `2026-09-16T13:50:19.333000Z` — **FUELINST**: 80 rows; marker `2026-09-16T13:50:00Z`
- `2026-09-16T13:50:03.238137Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:49:45Z`
- `2026-09-16T13:48:12.126230Z` — **TSDF**: 1368 rows; marker `2026-09-16T13:47:00Z`
- `2026-09-16T13:48:12.126230Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:47:45Z`
- `2026-09-16T13:47:47.305117Z` — **NDF**: 76 rows; marker `2026-09-16T13:47:00Z`
- `2026-09-16T13:46:10.698211Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:45:45Z`
- `2026-09-16T13:45:38.644454Z` — **FUELINST**: 80 rows; marker `2026-09-16T13:45:00Z`
