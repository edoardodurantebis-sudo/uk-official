# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T14:08:57.591485Z`  
Current process started UTC: `2026-09-16T14:04:57.630291Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3285, delta=-3, z=-4.41 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3288, delta=-3, z=-4.14 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3291, delta=-1, z=-3.85 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=494, 2026-09-16T14:05:29.634193Z)
- `FUELINST|fuelType=NPSHYD|generation` = **353** (n=494, 2026-09-16T14:05:29.634193Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3279** (n=494, 2026-09-16T14:05:29.634193Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=494, 2026-09-16T14:05:29.634193Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=494, 2026-09-16T14:05:29.634193Z)
- `FUELINST|fuelType=OTHER|generation` = **379** (n=494, 2026-09-16T14:05:29.634193Z)
- `FUELINST|fuelType=PS|generation` = **219** (n=494, 2026-09-16T14:05:29.634193Z)
- `FUELINST|fuelType=WIND|generation` = **4980** (n=494, 2026-09-16T14:05:29.634193Z)
- `IMBALNGC|TOTAL|imbalance` = **6633** (n=81, 2026-09-16T13:52:58.897421Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=81, 2026-09-16T13:52:58.897421Z)
- `INDGEN|TOTAL|generation` = **25413** (n=81, 2026-09-16T13:52:58.897421Z)
- `MELNGC|TOTAL|margin` = **35109** (n=81, 2026-09-16T13:50:19.333000Z)
- `NDF|TOTAL|demand` = **18280** (n=83, 2026-09-16T13:47:47.305117Z)
- `TSDF|TOTAL|demand` = **18780** (n=83, 2026-09-16T13:48:12.126230Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T14:08:09.385396Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:07:45Z`
- `2026-09-16T14:07:53.164912Z` — **MID**: 0 rows; marker `2026-09-16T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T14:06:17.680335Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:05:45Z`
- `2026-09-16T14:05:29.634193Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:05:00Z`
- `2026-09-16T14:04:20.224166Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:03:45Z`
- `2026-09-16T14:02:11.579799Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:01:45Z`
- `2026-09-16T14:00:51.382879Z` — **FUELHH**: 20 rows; marker `2026-09-16T14:00:00Z`
- `2026-09-16T14:00:35.258620Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:00:00Z`
- `2026-09-16T14:00:19.466363Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:59:45Z`
- `2026-09-16T13:58:11.302698Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:57:45Z`
- `2026-09-16T13:56:10.119403Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:55:45Z`
- `2026-09-16T13:55:22.038432Z` — **FUELINST**: 80 rows; marker `2026-09-16T13:55:00Z`
- `2026-09-16T13:54:02.585393Z` — **FREQ**: 5761 rows; marker `2026-09-16T13:53:45Z`
- `2026-09-16T13:52:58.897421Z` — **INDGEN**: 1368 rows; marker `2026-09-16T13:47:00Z`
- `2026-09-16T13:52:58.897421Z` — **INDDEM**: 1368 rows; marker `2026-09-16T13:47:00Z`
