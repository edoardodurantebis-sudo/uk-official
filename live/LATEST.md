# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T22:52:30.794663Z`  
Current process started UTC: `2026-09-21T22:48:30.734794Z`  
1-second metadata polls in this process: **230**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3644, delta=-2, z=4.82 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3646, delta=6, z=4.88 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3640, delta=5, z=4.81 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3635, delta=-1, z=4.76 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3638, delta=-7, z=4.99 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3636, delta=-1, z=4.80 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3637, delta=3, z=4.85 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3634, delta=-8, z=4.83 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3642, delta=3, z=5.00 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3639, delta=0, z=4.98 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3639, delta=-6, z=5.01 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3645, delta=24, z=5.33 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=4, z=5.15 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3641, delta=-1, z=5.12 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3642, delta=-1, z=5.17 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1961, 2026-09-21T22:50:38.211131Z)
- `FUELINST|fuelType=OTHER|generation` = **304** (n=1961, 2026-09-21T22:50:38.211131Z)
- `FUELINST|fuelType=PS|generation` = **-8** (n=1961, 2026-09-21T22:50:38.211131Z)
- `FUELINST|fuelType=WIND|generation` = **3717** (n=1961, 2026-09-21T22:50:38.211131Z)
- `IMBALNGC|TOTAL|imbalance` = **-2493** (n=323, 2026-09-21T22:51:42.290265Z)
- `INDDEM|TOTAL|demand` = **-12379** (n=323, 2026-09-21T22:51:26.349395Z)
- `INDGEN|TOTAL|generation` = **18966** (n=323, 2026-09-21T22:51:26.349395Z)
- `MELNGC|TOTAL|margin` = **36234** (n=323, 2026-09-21T22:49:34.128825Z)
- `MID|dataProvider=APXMIDP|price` = **142.42** (n=63, 2026-09-21T22:42:08.665748Z)
- `MID|dataProvider=APXMIDP|volume` = **1648** (n=63, 2026-09-21T22:42:08.665748Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=124, 2026-09-21T22:42:08.665748Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=124, 2026-09-21T22:42:08.665748Z)
- `NDF|TOTAL|demand` = **20959** (n=330, 2026-09-21T22:47:27.701137Z)
- `TSDF|TOTAL|demand` = **21459** (n=330, 2026-09-21T22:47:44.414339Z)
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T22:52:14.495105Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:51:45Z`
- `2026-09-21T22:51:42.290265Z` — **IMBALNGC**: 1044 rows; marker `2026-09-21T22:47:00Z`
- `2026-09-21T22:51:26.349395Z` — **INDGEN**: 1044 rows; marker `2026-09-21T22:47:00Z`
- `2026-09-21T22:51:26.349395Z` — **INDDEM**: 1044 rows; marker `2026-09-21T22:47:00Z`
- `2026-09-21T22:50:38.211131Z` — **FUELINST**: 80 rows; marker `2026-09-21T22:50:00Z`
- `2026-09-21T22:50:22.718994Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:49:45Z`
- `2026-09-21T22:49:34.128825Z` — **MELNGC**: 1044 rows; marker `2026-09-21T22:47:00Z`
- `2026-09-21T22:48:30.734803Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:47:45Z`
- `2026-09-21T22:47:44.414339Z` — **TSDF**: 1044 rows; marker `2026-09-21T22:47:00Z`
- `2026-09-21T22:47:27.701137Z` — **NDF**: 58 rows; marker `2026-09-21T22:47:00Z`
- `2026-09-21T22:46:23.191001Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:45:45Z`
- `2026-09-21T22:45:35.804157Z` — **FUELINST**: 80 rows; marker `2026-09-21T22:45:00Z`
- `2026-09-21T22:44:15.854161Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:43:45Z`
- `2026-09-21T22:42:24.138158Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:41:45Z`
- `2026-09-21T22:42:08.665748Z` — **MID**: 2 rows; marker `2026-09-21T22:42:03Z`
