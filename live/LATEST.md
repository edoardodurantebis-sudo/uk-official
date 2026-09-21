# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T20:24:33.493547Z`  
Current process started UTC: `2026-09-21T20:20:33.606125Z`  
1-second metadata polls in this process: **233**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3539, delta=7, z=3.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3532, delta=10, z=3.64 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=146, delta=-39, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=0, z=3.62 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=0, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=-12, z=3.66 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=161, delta=-8, z=4.02 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=185, delta=-45, z=4.95 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=169, delta=-2, z=4.27 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=171, delta=-17, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=188, delta=-2, z=4.87 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=190, delta=0, z=4.96 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=190, delta=-12, z=5.00 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=202, delta=-28, z=5.39 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1931, 2026-09-21T20:20:33.606147Z)
- `FUELINST|fuelType=OTHER|generation` = **1079** (n=1931, 2026-09-21T20:20:33.606147Z)
- `FUELINST|fuelType=PS|generation` = **377** (n=1931, 2026-09-21T20:20:33.606147Z)
- `FUELINST|fuelType=WIND|generation` = **3708** (n=1931, 2026-09-21T20:20:33.606147Z)
- `IMBALNGC|TOTAL|imbalance` = **-2707** (n=318, 2026-09-21T20:22:10.806468Z)
- `INDDEM|TOTAL|demand` = **-12258** (n=318, 2026-09-21T20:21:54.518829Z)
- `INDGEN|TOTAL|generation` = **18752** (n=318, 2026-09-21T20:21:54.518829Z)
- `MELNGC|TOTAL|margin` = **36091** (n=318, 2026-09-21T20:19:44.727256Z)
- `MID|dataProvider=APXMIDP|price` = **182.5** (n=58, 2026-09-21T20:12:23.535636Z)
- `MID|dataProvider=APXMIDP|volume` = **2810.9** (n=58, 2026-09-21T20:12:23.535636Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=114, 2026-09-21T20:12:23.535636Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=114, 2026-09-21T20:12:23.535636Z)
- `NDF|TOTAL|demand` = **20959** (n=325, 2026-09-21T20:17:52.969377Z)
- `TSDF|TOTAL|demand` = **21459** (n=325, 2026-09-21T20:17:52.969377Z)
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T20:24:18.786152Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:23:45Z`
- `2026-09-21T20:22:26.748945Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:21:45Z`
- `2026-09-21T20:22:10.806468Z` — **IMBALNGC**: 1134 rows; marker `2026-09-21T20:17:00Z`
- `2026-09-21T20:21:54.518829Z` — **INDGEN**: 1134 rows; marker `2026-09-21T20:17:00Z`
- `2026-09-21T20:21:54.518829Z` — **INDDEM**: 1134 rows; marker `2026-09-21T20:17:00Z`
- `2026-09-21T20:20:33.606147Z` — **FUELINST**: 80 rows; marker `2026-09-21T20:20:00Z`
- `2026-09-21T20:20:16.850591Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:19:45Z`
- `2026-09-21T20:19:44.727256Z` — **MELNGC**: 1134 rows; marker `2026-09-21T20:17:00Z`
- `2026-09-21T20:18:08.608427Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:17:45Z`
- `2026-09-21T20:17:52.969377Z` — **TSDF**: 1134 rows; marker `2026-09-21T20:17:00Z`
- `2026-09-21T20:17:52.969377Z` — **NDF**: 63 rows; marker `2026-09-21T20:17:00Z`
- `2026-09-21T20:16:17.606330Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:15:45Z`
- `2026-09-21T20:15:38.162599Z` — **FUELINST**: 80 rows; marker `2026-09-21T20:15:00Z`
- `2026-09-21T20:14:31.792655Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:13:45Z`
- `2026-09-21T20:12:23.535636Z` — **MID**: 2 rows; marker `2026-09-21T20:12:04Z`
