# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T16:18:56.679180Z`  
Current process started UTC: `2026-09-22T16:14:57.039656Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=237, delta=23, z=6.22 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=214, delta=19, z=5.60 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=195, delta=18, z=5.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=177, delta=84, z=4.58 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3729, delta=7, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3732, delta=1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3731, delta=9, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3737, delta=0, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3722, delta=43, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3737, delta=4, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3733, delta=3, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3730, delta=10, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3136, delta=-128, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3264, delta=142, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3122, delta=169, z=3.61 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2170, 2026-09-22T16:15:29.042958Z)
- `FUELINST|fuelType=OTHER|generation` = **1366** (n=2170, 2026-09-22T16:15:29.042958Z)
- `FUELINST|fuelType=PS|generation` = **1355** (n=2170, 2026-09-22T16:15:29.042958Z)
- `FUELINST|fuelType=WIND|generation` = **1316** (n=2170, 2026-09-22T16:15:29.042958Z)
- `IMBALNGC|TOTAL|imbalance` = **-7942** (n=356, 2026-09-22T15:52:27.014740Z)
- `INDDEM|TOTAL|demand` = **-12476** (n=356, 2026-09-22T15:52:10.596481Z)
- `INDGEN|TOTAL|generation` = **13231** (n=356, 2026-09-22T15:52:10.596481Z)
- `MELNGC|TOTAL|margin` = **37185** (n=356, 2026-09-22T15:49:44.825117Z)
- `MID|dataProvider=APXMIDP|price` = **220.01** (n=98, 2026-09-22T16:12:19.390750Z)
- `MID|dataProvider=APXMIDP|volume` = **4569.7** (n=98, 2026-09-22T16:12:19.390750Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=194, 2026-09-22T16:12:19.390750Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=194, 2026-09-22T16:12:19.390750Z)
- `NDF|TOTAL|demand` = **20673** (n=365, 2026-09-22T16:17:53.440278Z)
- `TSDF|TOTAL|demand` = **21173** (n=365, 2026-09-22T16:17:53.440278Z)
- `WINDFOR|TOTAL|generation` = **13082** (n=61, 2026-09-22T12:30:43.630179Z)

## Latest publication events

- `2026-09-22T16:18:09.417695Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:17:45Z`
- `2026-09-22T16:17:53.440278Z` — **TSDF**: 1278 rows; marker `2026-09-22T16:17:00Z`
- `2026-09-22T16:17:53.440278Z` — **NDF**: 71 rows; marker `2026-09-22T16:17:00Z`
- `2026-09-22T16:16:17.316222Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:15:45Z`
- `2026-09-22T16:15:29.042958Z` — **FUELINST**: 80 rows; marker `2026-09-22T16:15:00Z`
- `2026-09-22T16:14:27.954866Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:13:45Z`
- `2026-09-22T16:12:19.390750Z` — **MID**: 2 rows; marker `2026-09-22T16:12:03Z`
- `2026-09-22T16:12:19.390750Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:11:45Z`
- `2026-09-22T16:10:43.729864Z` — **FUELINST**: 80 rows; marker `2026-09-22T16:10:00Z`
- `2026-09-22T16:10:43.729864Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:09:45Z`
- `2026-09-22T16:08:17.879664Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:07:45Z`
- `2026-09-22T16:06:26.011683Z` — **MID**: 1 rows; marker `2026-09-22T16:05:00Z`
- `2026-09-22T16:06:26.011683Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:05:45Z`
- `2026-09-22T16:05:42.123272Z` — **FUELINST**: 80 rows; marker `2026-09-22T16:05:00Z`
- `2026-09-22T16:04:22.298564Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:03:45Z`
