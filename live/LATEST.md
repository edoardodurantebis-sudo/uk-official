# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T14:21:30.464799Z`  
Current process started UTC: `2026-09-16T14:17:31.138938Z`  
1-second metadata polls in this process: **235**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=497, 2026-09-16T14:20:27.682808Z)
- `FUELINST|fuelType=NPSHYD|generation` = **356** (n=497, 2026-09-16T14:20:27.682808Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3288** (n=497, 2026-09-16T14:20:27.682808Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=497, 2026-09-16T14:20:27.682808Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=497, 2026-09-16T14:20:27.682808Z)
- `FUELINST|fuelType=OTHER|generation` = **529** (n=497, 2026-09-16T14:20:27.682808Z)
- `FUELINST|fuelType=PS|generation` = **233** (n=497, 2026-09-16T14:20:27.682808Z)
- `FUELINST|fuelType=WIND|generation` = **5292** (n=497, 2026-09-16T14:20:27.682808Z)
- `IMBALNGC|TOTAL|imbalance` = **6633** (n=81, 2026-09-16T13:52:58.897421Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=81, 2026-09-16T13:52:58.897421Z)
- `INDGEN|TOTAL|generation` = **25413** (n=81, 2026-09-16T13:52:58.897421Z)
- `MELNGC|TOTAL|margin` = **34664** (n=82, 2026-09-16T14:20:27.682808Z)
- `NDF|TOTAL|demand` = **18280** (n=84, 2026-09-16T14:18:19.617927Z)
- `TSDF|TOTAL|demand` = **18780** (n=84, 2026-09-16T14:18:19.617927Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T14:20:27.682808Z` — **MELNGC**: 1350 rows; marker `2026-09-16T14:17:00Z`
- `2026-09-16T14:20:27.682808Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:20:00Z`
- `2026-09-16T14:20:12.262057Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:19:45Z`
- `2026-09-16T14:18:19.617927Z` — **TSDF**: 1350 rows; marker `2026-09-16T14:17:00Z`
- `2026-09-16T14:18:19.617927Z` — **NDF**: 75 rows; marker `2026-09-16T14:17:00Z`
- `2026-09-16T14:18:19.617927Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:17:45Z`
- `2026-09-16T14:16:18.035825Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:15:45Z`
- `2026-09-16T14:15:28.844641Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:15:00Z`
- `2026-09-16T14:14:09.018100Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:13:45Z`
- `2026-09-16T14:12:08.577348Z` — **MID**: 0 rows; marker `2026-09-16T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T14:12:08.577348Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:11:45Z`
- `2026-09-16T14:10:33.058565Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:10:00Z`
- `2026-09-16T14:10:16.402313Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:09:45Z`
- `2026-09-16T14:08:09.385396Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:07:45Z`
- `2026-09-16T14:07:53.164912Z` — **MID**: 0 rows; marker `2026-09-16T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
