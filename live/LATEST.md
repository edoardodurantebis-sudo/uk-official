# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T07:21:37.328112Z`  
Current process started UTC: `2026-09-15T07:17:36.796591Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=822, delta=0, z=5.33 -> generation-mix component moved
- **FUELINST** `fuelType=INTEW` `generation` — instantaneous generation mix [fuelType=INTEW] generation: value=-454, delta=-24, z=-3.82 -> generation-mix component moved
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=822, delta=20, z=6.11 -> generation-mix component moved
- **FUELINST** `fuelType=INTEW` `generation` — instantaneous generation mix [fuelType=INTEW] generation: value=-430, delta=-26, z=-3.81 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1404** (n=125, 2026-09-15T07:20:32.548006Z)
- `FUELINST|fuelType=NPSHYD|generation` = **434** (n=125, 2026-09-15T07:20:32.548006Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3320** (n=125, 2026-09-15T07:20:32.548006Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=125, 2026-09-15T07:20:32.548006Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=125, 2026-09-15T07:20:32.548006Z)
- `FUELINST|fuelType=OTHER|generation` = **1481** (n=125, 2026-09-15T07:20:32.548006Z)
- `FUELINST|fuelType=PS|generation` = **-259** (n=125, 2026-09-15T07:20:32.548006Z)
- `FUELINST|fuelType=WIND|generation` = **12799** (n=125, 2026-09-15T07:20:32.548006Z)
- `IMBALNGC|TOTAL|imbalance` = **-454** (n=22, 2026-09-15T07:20:16.723769Z)
- `INDDEM|TOTAL|demand` = **-12285** (n=22, 2026-09-15T07:20:00.229572Z)
- `INDGEN|TOTAL|generation` = **20030** (n=22, 2026-09-15T07:20:16.723769Z)
- `MELNGC|TOTAL|margin` = **34133** (n=22, 2026-09-15T07:18:40.859983Z)
- `NDF|TOTAL|demand` = **19934** (n=22, 2026-09-15T07:17:10.602011Z)
- `TSDF|TOTAL|demand` = **20484** (n=22, 2026-09-15T07:16:54.235813Z)
- `WINDFOR|TOTAL|generation` = **17059** (n=3, 2026-09-15T05:30:39.125309Z)

## Latest publication events

- `2026-09-15T07:20:32.548006Z` — **FUELINST**: 80 rows; marker `2026-09-15T07:20:00Z`
- `2026-09-15T07:20:16.723769Z` — **INDGEN**: 738 rows; marker `2026-09-15T07:16:00Z`
- `2026-09-15T07:20:16.723769Z` — **IMBALNGC**: 738 rows; marker `2026-09-15T07:16:00Z`
- `2026-09-15T07:20:16.723769Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:19:45Z`
- `2026-09-15T07:20:00.229572Z` — **INDDEM**: 738 rows; marker `2026-09-15T07:16:00Z`
- `2026-09-15T07:18:40.859983Z` — **MELNGC**: 738 rows; marker `2026-09-15T07:16:00Z`
- `2026-09-15T07:18:08.800635Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:17:45Z`
- `2026-09-15T07:17:10.602011Z` — **NDF**: 41 rows; marker `2026-09-15T07:16:00Z`
- `2026-09-15T07:16:54.235813Z` — **TSDF**: 738 rows; marker `2026-09-15T07:16:00Z`
- `2026-09-15T07:16:05.538493Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:15:45Z`
- `2026-09-15T07:15:33.572404Z` — **FUELINST**: 80 rows; marker `2026-09-15T07:15:00Z`
- `2026-09-15T07:14:13.615055Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:13:45Z`
- `2026-09-15T07:12:15.899415Z` — **MID**: 0 rows; marker `2026-09-15T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T07:12:15.899415Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:11:45Z`
- `2026-09-15T07:10:23.235670Z` — **FUELINST**: 80 rows; marker `2026-09-15T07:10:00Z`
