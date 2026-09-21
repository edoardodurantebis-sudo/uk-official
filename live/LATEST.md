# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T06:49:44.007403Z`  
Current process started UTC: `2026-09-21T06:45:44.101863Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3002, delta=16, z=4.00 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3490, delta=-4, z=8.08 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=839, delta=0, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2986, delta=179, z=3.99 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3494, delta=-3, z=8.45 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=839, delta=2, z=4.19 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2807, delta=272, z=3.69 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3497, delta=-3, z=8.79 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=837, delta=1, z=4.19 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3494, delta=26, z=10.16 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=833, delta=7, z=4.32 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3500, delta=5, z=9.16 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=836, delta=-1, z=4.21 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3495, delta=4, z=9.11 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=837, delta=-1, z=4.24 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1771, 2026-09-21T06:45:32.569143Z)
- `FUELINST|fuelType=OTHER|generation` = **3002** (n=1771, 2026-09-21T06:45:32.569143Z)
- `FUELINST|fuelType=PS|generation` = **230** (n=1771, 2026-09-21T06:45:32.569143Z)
- `FUELINST|fuelType=WIND|generation` = **3894** (n=1771, 2026-09-21T06:45:32.569143Z)
- `IMBALNGC|TOTAL|imbalance` = **-3867** (n=291, 2026-09-21T06:19:53.385768Z)
- `INDDEM|TOTAL|demand` = **-12146** (n=291, 2026-09-21T06:19:53.385768Z)
- `INDGEN|TOTAL|generation` = **16734** (n=291, 2026-09-21T06:19:53.385768Z)
- `MELNGC|TOTAL|margin` = **38153** (n=292, 2026-09-21T06:49:16.352219Z)
- `MID|dataProvider=APXMIDP|price` = **203.75** (n=31, 2026-09-21T06:42:20.871103Z)
- `MID|dataProvider=APXMIDP|volume` = **2489.7** (n=31, 2026-09-21T06:42:20.871103Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=62, 2026-09-21T06:42:20.871103Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=62, 2026-09-21T06:42:20.871103Z)
- `NDF|TOTAL|demand` = **20110** (n=298, 2026-09-21T06:47:23.965603Z)
- `TSDF|TOTAL|demand` = **21023** (n=298, 2026-09-21T06:47:08.433167Z)
- `WINDFOR|TOTAL|generation` = **8794** (n=50, 2026-09-21T05:30:44.368414Z)

## Latest publication events

- `2026-09-21T06:49:16.352219Z` — **MELNGC**: 756 rows; marker `2026-09-21T06:46:00Z`
- `2026-09-21T06:48:28.422418Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:47:45Z`
- `2026-09-21T06:47:23.965603Z` — **NDF**: 42 rows; marker `2026-09-21T06:46:00Z`
- `2026-09-21T06:47:08.433167Z` — **TSDF**: 756 rows; marker `2026-09-21T06:46:00Z`
- `2026-09-21T06:46:20.106370Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:45:45Z`
- `2026-09-21T06:45:32.569143Z` — **FUELINST**: 80 rows; marker `2026-09-21T06:45:00Z`
- `2026-09-21T06:44:13.086126Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:43:45Z`
- `2026-09-21T06:42:20.871103Z` — **MID**: 2 rows; marker `2026-09-21T06:42:03Z`
- `2026-09-21T06:42:20.871103Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:41:45Z`
- `2026-09-21T06:40:32.841476Z` — **FUELINST**: 80 rows; marker `2026-09-21T06:40:00Z`
- `2026-09-21T06:40:16.766593Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:39:45Z`
- `2026-09-21T06:38:24.196027Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:37:45Z`
- `2026-09-21T06:36:35.534367Z` — **MID**: 1 rows; marker `2026-09-21T06:35:00Z`
- `2026-09-21T06:36:20.130256Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:35:45Z`
- `2026-09-21T06:35:32.570234Z` — **FUELINST**: 80 rows; marker `2026-09-21T06:35:00Z`
