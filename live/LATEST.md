# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T16:48:51.049794Z`  
Current process started UTC: `2026-09-20T16:44:50.296183Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=878, delta=1, z=3.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=877, delta=0, z=3.51 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=864, delta=502, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=877, delta=-1, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=878, delta=1, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=877, delta=-1, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=878, delta=-1, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=879, delta=80, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-986, delta=2, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-983, delta=3, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=-1, z=-3.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.72 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1603, 2026-09-20T16:45:38.302890Z)
- `FUELINST|fuelType=OTHER|generation` = **868** (n=1603, 2026-09-20T16:45:38.302890Z)
- `FUELINST|fuelType=PS|generation` = **483** (n=1603, 2026-09-20T16:45:38.302890Z)
- `FUELINST|fuelType=WIND|generation` = **7959** (n=1603, 2026-09-20T16:45:38.302890Z)
- `IMBALNGC|TOTAL|imbalance` = **-5182** (n=263, 2026-09-20T16:23:14.577874Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=263, 2026-09-20T16:23:14.577874Z)
- `INDGEN|TOTAL|generation` = **15428** (n=263, 2026-09-20T16:23:14.577874Z)
- `MELNGC|TOTAL|margin` = **35898** (n=263, 2026-09-20T16:20:23.910302Z)
- `MID|dataProvider=APXMIDP|price` = **134.16** (n=3, 2026-09-20T16:42:18.136782Z)
- `MID|dataProvider=APXMIDP|volume` = **3510.2** (n=3, 2026-09-20T16:42:18.136782Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=6, 2026-09-20T16:42:18.136782Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=6, 2026-09-20T16:42:18.136782Z)
- `NDF|TOTAL|demand` = **20110** (n=270, 2026-09-20T16:47:45.958775Z)
- `TSDF|TOTAL|demand` = **20610** (n=270, 2026-09-20T16:47:45.958775Z)
- `WINDFOR|TOTAL|generation` = **2115** (n=46, 2026-09-20T16:30:40.211698Z)

## Latest publication events

- `2026-09-20T16:48:49.597139Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:47:45Z`
- `2026-09-20T16:47:45.958775Z` — **TSDF**: 1260 rows; marker `2026-09-20T16:47:00Z`
- `2026-09-20T16:47:45.958775Z` — **NDF**: 70 rows; marker `2026-09-20T16:47:00Z`
- `2026-09-20T16:46:10.357987Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:45:45Z`
- `2026-09-20T16:45:38.302890Z` — **FUELINST**: 80 rows; marker `2026-09-20T16:45:00Z`
- `2026-09-20T16:44:10.252382Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:43:45Z`
- `2026-09-20T16:42:18.136782Z` — **MID**: 2 rows; marker `2026-09-20T16:42:05Z`
- `2026-09-20T16:42:18.136782Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:41:45Z`
- `2026-09-20T16:40:26.115456Z` — **FUELINST**: 80 rows; marker `2026-09-20T16:40:00Z`
- `2026-09-20T16:40:10.560569Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:39:45Z`
- `2026-09-20T16:38:19.060073Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:37:45Z`
- `2026-09-20T16:37:31.052937Z` — **MID**: 1 rows; marker `2026-09-20T16:35:00Z`
- `2026-09-20T16:36:26.139402Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:35:45Z`
- `2026-09-20T16:35:29.830202Z` — **FUELINST**: 80 rows; marker `2026-09-20T16:35:00Z`
- `2026-09-20T16:34:09.121255Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:33:45Z`
