# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T16:27:27.321053Z`  
Current process started UTC: `2026-09-22T16:23:27.318080Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=381, delta=82, z=10.10 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=299, delta=62, z=7.92 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2172, 2026-09-22T16:25:34.964441Z)
- `FUELINST|fuelType=OTHER|generation` = **1526** (n=2172, 2026-09-22T16:25:34.964441Z)
- `FUELINST|fuelType=PS|generation` = **1357** (n=2172, 2026-09-22T16:25:34.964441Z)
- `FUELINST|fuelType=WIND|generation` = **1305** (n=2172, 2026-09-22T16:25:34.964441Z)
- `IMBALNGC|TOTAL|imbalance` = **-7943** (n=357, 2026-09-22T16:22:23.715090Z)
- `INDDEM|TOTAL|demand` = **-12476** (n=357, 2026-09-22T16:22:08.285666Z)
- `INDGEN|TOTAL|generation` = **13230** (n=357, 2026-09-22T16:22:08.285666Z)
- `MELNGC|TOTAL|margin` = **37153** (n=357, 2026-09-22T16:19:43.389491Z)
- `MID|dataProvider=APXMIDP|price` = **220.01** (n=98, 2026-09-22T16:12:19.390750Z)
- `MID|dataProvider=APXMIDP|volume` = **4569.7** (n=98, 2026-09-22T16:12:19.390750Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=194, 2026-09-22T16:12:19.390750Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=194, 2026-09-22T16:12:19.390750Z)
- `NDF|TOTAL|demand` = **20673** (n=365, 2026-09-22T16:17:53.440278Z)
- `TSDF|TOTAL|demand` = **21173** (n=365, 2026-09-22T16:17:53.440278Z)
- `WINDFOR|TOTAL|generation` = **13082** (n=61, 2026-09-22T12:30:43.630179Z)

## Latest publication events

- `2026-09-22T16:26:06.874918Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:25:45Z`
- `2026-09-22T16:25:34.964441Z` — **FUELINST**: 80 rows; marker `2026-09-22T16:25:00Z`
- `2026-09-22T16:24:15.324306Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:23:45Z`
- `2026-09-22T16:22:23.715090Z` — **IMBALNGC**: 1278 rows; marker `2026-09-22T16:17:00Z`
- `2026-09-22T16:22:08.285666Z` — **INDGEN**: 1278 rows; marker `2026-09-22T16:17:00Z`
- `2026-09-22T16:22:08.285666Z` — **INDDEM**: 1278 rows; marker `2026-09-22T16:17:00Z`
- `2026-09-22T16:22:08.285666Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:21:45Z`
- `2026-09-22T16:20:31.731317Z` — **FUELINST**: 80 rows; marker `2026-09-22T16:20:00Z`
- `2026-09-22T16:20:15.415110Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:19:45Z`
- `2026-09-22T16:19:43.389491Z` — **MELNGC**: 1278 rows; marker `2026-09-22T16:17:00Z`
- `2026-09-22T16:18:09.417695Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:17:45Z`
- `2026-09-22T16:17:53.440278Z` — **TSDF**: 1278 rows; marker `2026-09-22T16:17:00Z`
- `2026-09-22T16:17:53.440278Z` — **NDF**: 71 rows; marker `2026-09-22T16:17:00Z`
- `2026-09-22T16:16:17.316222Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:15:45Z`
- `2026-09-22T16:15:29.042958Z` — **FUELINST**: 80 rows; marker `2026-09-22T16:15:00Z`
