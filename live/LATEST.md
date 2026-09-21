# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T16:43:12.700714Z`  
Current process started UTC: `2026-09-21T16:39:12.833650Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=5, z=3.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=-1, z=3.61 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3506, delta=4, z=3.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3505, delta=1, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=1, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3503, delta=-6, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=3, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3506, delta=-1, z=3.72 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3507, delta=5, z=3.76 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3502, delta=7, z=3.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3502, delta=-4, z=3.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3506, delta=0, z=3.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3506, delta=2, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=5, z=3.75 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=5, z=3.65 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1887, 2026-09-21T16:40:36.177009Z)
- `FUELINST|fuelType=OTHER|generation` = **1498** (n=1887, 2026-09-21T16:40:36.177009Z)
- `FUELINST|fuelType=PS|generation` = **322** (n=1887, 2026-09-21T16:40:36.177009Z)
- `FUELINST|fuelType=WIND|generation` = **3283** (n=1887, 2026-09-21T16:40:36.177009Z)
- `IMBALNGC|TOTAL|imbalance` = **-3071** (n=310, 2026-09-21T16:23:11.472727Z)
- `INDDEM|TOTAL|demand` = **-12280** (n=310, 2026-09-21T16:22:55.453530Z)
- `INDGEN|TOTAL|generation` = **18388** (n=310, 2026-09-21T16:22:55.453530Z)
- `MELNGC|TOTAL|margin` = **36276** (n=310, 2026-09-21T16:20:15.056024Z)
- `MID|dataProvider=APXMIDP|price` = **203.05** (n=51, 2026-09-21T16:42:11.789467Z)
- `MID|dataProvider=APXMIDP|volume` = **3543.2** (n=51, 2026-09-21T16:42:11.789467Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=100, 2026-09-21T16:42:11.789467Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=100, 2026-09-21T16:42:11.789467Z)
- `NDF|TOTAL|demand` = **20959** (n=317, 2026-09-21T16:18:22.784357Z)
- `TSDF|TOTAL|demand` = **21459** (n=317, 2026-09-21T16:18:22.784357Z)
- `WINDFOR|TOTAL|generation` = **8620** (n=54, 2026-09-21T16:30:47.714491Z)

## Latest publication events

- `2026-09-21T16:42:27.124436Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:41:45Z`
- `2026-09-21T16:42:11.789467Z` — **MID**: 2 rows; marker `2026-09-21T16:42:03Z`
- `2026-09-21T16:40:36.177009Z` — **FUELINST**: 80 rows; marker `2026-09-21T16:40:00Z`
- `2026-09-21T16:40:17.094385Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:39:45Z`
- `2026-09-21T16:38:13.146281Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:37:45Z`
- `2026-09-21T16:37:24.939100Z` — **MID**: 1 rows; marker `2026-09-21T16:35:00Z`
- `2026-09-21T16:36:21.065929Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:35:45Z`
- `2026-09-21T16:35:33.680869Z` — **FUELINST**: 80 rows; marker `2026-09-21T16:35:00Z`
- `2026-09-21T16:34:16.306533Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:33:45Z`
- `2026-09-21T16:32:24.389880Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:31:45Z`
- `2026-09-21T16:30:47.714491Z` — **WINDFOR**: 73 rows; marker `2026-09-21T16:30:00Z`
- `2026-09-21T16:30:47.714491Z` — **FUELHH**: 20 rows; marker `2026-09-21T16:30:00Z`
- `2026-09-21T16:30:47.714491Z` — **FUELINST**: 80 rows; marker `2026-09-21T16:30:00Z`
- `2026-09-21T16:30:17.674185Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:29:45Z`
- `2026-09-21T16:28:25.584992Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:27:45Z`
