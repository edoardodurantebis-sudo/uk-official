# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T07:13:14.391607Z`  
Current process started UTC: `2026-09-15T07:09:14.226289Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTVKL` `generation` — instantaneous generation mix [fuelType=INTVKL] generation: value=1366, delta=336, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=802, delta=366, z=7.22 -> generation-mix component moved
- **FUELINST** `fuelType=INTEW` `generation` — instantaneous generation mix [fuelType=INTEW] generation: value=-404, delta=-25, z=-3.77 -> generation-mix component moved
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=436, delta=500, z=5.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTEW` `generation` — instantaneous generation mix [fuelType=INTEW] generation: value=-379, delta=-26, z=-3.71 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=2583, delta=626, z=3.73 -> generation-mix component moved
- **FUELINST** `fuelType=INTEW` `generation` — instantaneous generation mix [fuelType=INTEW] generation: value=-353, delta=-24, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=INTEW` `generation` — instantaneous generation mix [fuelType=INTEW] generation: value=-329, delta=-25, z=-3.53 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2574, delta=290, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=1992, delta=-144, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2136, delta=411, z=4.17 -> generation-mix component moved
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=20484, delta=0, z=-4.01 -> demand pressure easing
- **FUELHH** `fuelType=INTNEM` `generation` — half-hour generation mix [fuelType=INTNEM] generation: value=-748, delta=-264, z=-3.70 -> generation-mix component moved
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-12413, delta=-86, z=-3.82 -> demand pressure easing
- **MELNGC** `TOTAL` `margin` — indicated margin [TOTAL] margin: value=34104, delta=1370, z=NA -> margin/tightness state changed

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1366** (n=123, 2026-09-15T07:10:23.235670Z)
- `FUELINST|fuelType=NPSHYD|generation` = **432** (n=123, 2026-09-15T07:10:23.235670Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3318** (n=123, 2026-09-15T07:10:23.235670Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=123, 2026-09-15T07:10:23.235670Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=123, 2026-09-15T07:10:23.235670Z)
- `FUELINST|fuelType=OTHER|generation` = **990** (n=123, 2026-09-15T07:10:23.235670Z)
- `FUELINST|fuelType=PS|generation` = **-262** (n=123, 2026-09-15T07:10:23.235670Z)
- `FUELINST|fuelType=WIND|generation` = **13497** (n=123, 2026-09-15T07:10:23.235670Z)
- `IMBALNGC|TOTAL|imbalance` = **-703** (n=21, 2026-09-15T06:50:27.324561Z)
- `INDDEM|TOTAL|demand` = **-12429** (n=21, 2026-09-15T06:50:11.912776Z)
- `INDGEN|TOTAL|generation` = **19781** (n=21, 2026-09-15T06:50:11.912776Z)
- `MELNGC|TOTAL|margin` = **33975** (n=21, 2026-09-15T06:49:56.392396Z)
- `NDF|TOTAL|demand` = **19934** (n=21, 2026-09-15T06:47:23.898461Z)
- `TSDF|TOTAL|demand` = **20484** (n=21, 2026-09-15T06:47:23.898461Z)
- `WINDFOR|TOTAL|generation` = **17059** (n=3, 2026-09-15T05:30:39.125309Z)

## Latest publication events

- `2026-09-15T07:12:15.899415Z` — **MID**: 0 rows; marker `2026-09-15T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T07:12:15.899415Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:11:45Z`
- `2026-09-15T07:10:23.235670Z` — **FUELINST**: 80 rows; marker `2026-09-15T07:10:00Z`
- `2026-09-15T07:10:23.235670Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:09:45Z`
- `2026-09-15T07:08:15.299620Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:07:45Z`
- `2026-09-15T07:06:23.239122Z` — **MID**: 0 rows; marker `2026-09-15T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T07:06:07.622891Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:05:45Z`
- `2026-09-15T07:05:35.632647Z` — **FUELINST**: 80 rows; marker `2026-09-15T07:05:00Z`
- `2026-09-15T07:04:05.455370Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:03:45Z`
- `2026-09-15T07:02:29.385045Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:01:45Z`
- `2026-09-15T07:00:52.657901Z` — **FUELHH**: 20 rows; marker `2026-09-15T07:00:00Z`
- `2026-09-15T07:00:52.657901Z` — **FUELINST**: 80 rows; marker `2026-09-15T07:00:00Z`
- `2026-09-15T07:00:26.369749Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:59:45Z`
- `2026-09-15T06:58:18.263622Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:57:45Z`
- `2026-09-15T06:56:19.615740Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:55:45Z`
