# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T14:17:20.545651Z`  
Current process started UTC: `2026-09-16T14:13:21.013647Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3285, delta=-3, z=-4.41 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3288, delta=-3, z=-4.14 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=496, 2026-09-16T14:15:28.844641Z)
- `FUELINST|fuelType=NPSHYD|generation` = **354** (n=496, 2026-09-16T14:15:28.844641Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3287** (n=496, 2026-09-16T14:15:28.844641Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=496, 2026-09-16T14:15:28.844641Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=496, 2026-09-16T14:15:28.844641Z)
- `FUELINST|fuelType=OTHER|generation` = **521** (n=496, 2026-09-16T14:15:28.844641Z)
- `FUELINST|fuelType=PS|generation` = **233** (n=496, 2026-09-16T14:15:28.844641Z)
- `FUELINST|fuelType=WIND|generation` = **5226** (n=496, 2026-09-16T14:15:28.844641Z)
- `IMBALNGC|TOTAL|imbalance` = **6633** (n=81, 2026-09-16T13:52:58.897421Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=81, 2026-09-16T13:52:58.897421Z)
- `INDGEN|TOTAL|generation` = **25413** (n=81, 2026-09-16T13:52:58.897421Z)
- `MELNGC|TOTAL|margin` = **35109** (n=81, 2026-09-16T13:50:19.333000Z)
- `NDF|TOTAL|demand` = **18280** (n=83, 2026-09-16T13:47:47.305117Z)
- `TSDF|TOTAL|demand` = **18780** (n=83, 2026-09-16T13:48:12.126230Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T14:16:18.035825Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:15:45Z`
- `2026-09-16T14:15:28.844641Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:15:00Z`
- `2026-09-16T14:14:09.018100Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:13:45Z`
- `2026-09-16T14:12:08.577348Z` — **MID**: 0 rows; marker `2026-09-16T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T14:12:08.577348Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:11:45Z`
- `2026-09-16T14:10:33.058565Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:10:00Z`
- `2026-09-16T14:10:16.402313Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:09:45Z`
- `2026-09-16T14:08:09.385396Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:07:45Z`
- `2026-09-16T14:07:53.164912Z` — **MID**: 0 rows; marker `2026-09-16T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T14:06:17.680335Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:05:45Z`
- `2026-09-16T14:05:29.634193Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:05:00Z`
- `2026-09-16T14:04:20.224166Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:03:45Z`
- `2026-09-16T14:02:11.579799Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:01:45Z`
- `2026-09-16T14:00:51.382879Z` — **FUELHH**: 20 rows; marker `2026-09-16T14:00:00Z`
- `2026-09-16T14:00:35.258620Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:00:00Z`
