# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T16:36:13.216871Z`  
Current process started UTC: `2026-09-20T16:32:12.790026Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-988, delta=26, z=-3.87 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1601, 2026-09-20T16:35:29.830202Z)
- `FUELINST|fuelType=OTHER|generation` = **958** (n=1601, 2026-09-20T16:35:29.830202Z)
- `FUELINST|fuelType=PS|generation` = **163** (n=1601, 2026-09-20T16:35:29.830202Z)
- `FUELINST|fuelType=WIND|generation` = **7972** (n=1601, 2026-09-20T16:35:29.830202Z)
- `IMBALNGC|TOTAL|imbalance` = **-5182** (n=263, 2026-09-20T16:23:14.577874Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=263, 2026-09-20T16:23:14.577874Z)
- `INDGEN|TOTAL|generation` = **15428** (n=263, 2026-09-20T16:23:14.577874Z)
- `MELNGC|TOTAL|margin` = **35898** (n=263, 2026-09-20T16:20:23.910302Z)
- `MID|dataProvider=APXMIDP|price` = **103.7** (n=2, 2026-09-20T16:12:12.901791Z)
- `MID|dataProvider=APXMIDP|volume` = **3820.3** (n=2, 2026-09-20T16:12:12.901791Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=4, 2026-09-20T16:12:12.901791Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=4, 2026-09-20T16:12:12.901791Z)
- `NDF|TOTAL|demand` = **20110** (n=269, 2026-09-20T16:17:48.642120Z)
- `TSDF|TOTAL|demand` = **20610** (n=269, 2026-09-20T16:17:48.642120Z)
- `WINDFOR|TOTAL|generation` = **2115** (n=46, 2026-09-20T16:30:40.211698Z)

## Latest publication events

- `2026-09-20T16:35:29.830202Z` — **FUELINST**: 80 rows; marker `2026-09-20T16:35:00Z`
- `2026-09-20T16:34:09.121255Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:33:45Z`
- `2026-09-20T16:32:32.946661Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:31:45Z`
- `2026-09-20T16:30:55.613727Z` — **FUELHH**: 20 rows; marker `2026-09-20T16:30:00Z`
- `2026-09-20T16:30:40.211698Z` — **WINDFOR**: 73 rows; marker `2026-09-20T16:30:00Z`
- `2026-09-20T16:30:40.211698Z` — **FUELINST**: 80 rows; marker `2026-09-20T16:30:00Z`
- `2026-09-20T16:30:08.710310Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:29:45Z`
- `2026-09-20T16:28:17.131251Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:27:45Z`
- `2026-09-20T16:26:10.733136Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:25:45Z`
- `2026-09-20T16:25:22.617303Z` — **FUELINST**: 80 rows; marker `2026-09-20T16:25:00Z`
- `2026-09-20T16:24:02.401479Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:23:45Z`
- `2026-09-20T16:23:14.577874Z` — **INDGEN**: 1278 rows; marker `2026-09-20T16:17:00Z`
- `2026-09-20T16:23:14.577874Z` — **INDDEM**: 1278 rows; marker `2026-09-20T16:17:00Z`
- `2026-09-20T16:23:14.577874Z` — **IMBALNGC**: 1278 rows; marker `2026-09-20T16:17:00Z`
- `2026-09-20T16:22:15.233962Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:21:45Z`
