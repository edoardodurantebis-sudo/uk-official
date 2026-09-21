# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T07:02:21.727316Z`  
Current process started UTC: `2026-09-21T06:58:21.829490Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=2993, delta=730, z=4.09 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3494, delta=0, z=8.74 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=837, delta=4, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2981, delta=-159, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-1, z=7.94 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=832, delta=-5, z=4.04 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3140, delta=101, z=4.20 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3497, delta=7, z=8.14 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=837, delta=-1, z=4.11 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3039, delta=37, z=4.04 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3490, delta=0, z=7.94 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=838, delta=-1, z=4.14 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3002, delta=16, z=4.00 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3490, delta=-4, z=8.08 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=839, delta=0, z=4.17 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1774, 2026-09-21T07:00:46.077940Z)
- `FUELINST|fuelType=OTHER|generation` = **2981** (n=1774, 2026-09-21T07:00:46.077940Z)
- `FUELINST|fuelType=PS|generation` = **223** (n=1774, 2026-09-21T07:00:46.077940Z)
- `FUELINST|fuelType=WIND|generation` = **4165** (n=1774, 2026-09-21T07:00:46.077940Z)
- `IMBALNGC|TOTAL|imbalance` = **-4358** (n=292, 2026-09-21T06:49:56.621035Z)
- `INDDEM|TOTAL|demand` = **-12559** (n=292, 2026-09-21T06:49:56.621035Z)
- `INDGEN|TOTAL|generation` = **16665** (n=292, 2026-09-21T06:49:56.621035Z)
- `MELNGC|TOTAL|margin` = **38153** (n=292, 2026-09-21T06:49:16.352219Z)
- `MID|dataProvider=APXMIDP|price` = **203.75** (n=31, 2026-09-21T06:42:20.871103Z)
- `MID|dataProvider=APXMIDP|volume` = **2489.7** (n=31, 2026-09-21T06:42:20.871103Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=62, 2026-09-21T06:42:20.871103Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=62, 2026-09-21T06:42:20.871103Z)
- `NDF|TOTAL|demand` = **20110** (n=298, 2026-09-21T06:47:23.965603Z)
- `TSDF|TOTAL|demand` = **21023** (n=298, 2026-09-21T06:47:08.433167Z)
- `WINDFOR|TOTAL|generation` = **8794** (n=50, 2026-09-21T05:30:44.368414Z)

## Latest publication events

- `2026-09-21T07:02:06.039005Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:01:45Z`
- `2026-09-21T07:00:46.077940Z` — **FUELHH**: 20 rows; marker `2026-09-21T07:00:00Z`
- `2026-09-21T07:00:46.077940Z` — **FUELINST**: 80 rows; marker `2026-09-21T07:00:00Z`
- `2026-09-21T07:00:14.037552Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:59:45Z`
- `2026-09-21T06:58:21.829501Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:57:45Z`
- `2026-09-21T06:56:18.931543Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:55:45Z`
- `2026-09-21T06:55:31.283529Z` — **FUELINST**: 80 rows; marker `2026-09-21T06:55:00Z`
- `2026-09-21T06:54:27.220124Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:53:45Z`
- `2026-09-21T06:52:19.446545Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:51:45Z`
- `2026-09-21T06:50:43.980150Z` — **FUELINST**: 80 rows; marker `2026-09-21T06:50:00Z`
- `2026-09-21T06:50:28.005613Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:49:45Z`
- `2026-09-21T06:49:56.621035Z` — **INDGEN**: 756 rows; marker `2026-09-21T06:46:00Z`
- `2026-09-21T06:49:56.621035Z` — **INDDEM**: 756 rows; marker `2026-09-21T06:46:00Z`
- `2026-09-21T06:49:56.621035Z` — **IMBALNGC**: 756 rows; marker `2026-09-21T06:46:00Z`
- `2026-09-21T06:49:16.352219Z` — **MELNGC**: 756 rows; marker `2026-09-21T06:46:00Z`
