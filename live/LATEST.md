# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T23:31:08.893326Z`  
Current process started UTC: `2026-09-21T23:27:09.145783Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3647, delta=5, z=4.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=3, z=4.73 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=5, z=4.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=2, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3643, delta=-2, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=0, z=4.72 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=-2, z=4.75 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3642, delta=4, z=4.87 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3647, delta=5, z=4.81 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3642, delta=-2, z=4.75 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3644, delta=-2, z=4.82 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3646, delta=6, z=4.88 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3640, delta=5, z=4.81 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3635, delta=-1, z=4.76 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3638, delta=-7, z=4.99 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1969, 2026-09-21T23:30:37.821418Z)
- `FUELINST|fuelType=OTHER|generation` = **249** (n=1969, 2026-09-21T23:30:37.821418Z)
- `FUELINST|fuelType=PS|generation` = **-285** (n=1969, 2026-09-21T23:30:37.821418Z)
- `FUELINST|fuelType=WIND|generation` = **3530** (n=1969, 2026-09-21T23:30:37.821418Z)
- `IMBALNGC|TOTAL|imbalance` = **-2016** (n=324, 2026-09-21T23:21:49.574733Z)
- `INDDEM|TOTAL|demand` = **-12381** (n=324, 2026-09-21T23:21:15.927702Z)
- `INDGEN|TOTAL|generation` = **19443** (n=324, 2026-09-21T23:21:15.927702Z)
- `MELNGC|TOTAL|margin` = **36167** (n=324, 2026-09-21T23:19:39.547553Z)
- `MID|dataProvider=APXMIDP|price` = **142.81** (n=64, 2026-09-21T23:12:18.557209Z)
- `MID|dataProvider=APXMIDP|volume` = **1777.2** (n=64, 2026-09-21T23:12:18.557209Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=126, 2026-09-21T23:12:18.557209Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=126, 2026-09-21T23:12:18.557209Z)
- `NDF|TOTAL|demand` = **20959** (n=331, 2026-09-21T23:17:21.026219Z)
- `TSDF|TOTAL|demand` = **21459** (n=331, 2026-09-21T23:17:38.428444Z)
- `WINDFOR|TOTAL|generation` = **9503** (n=56, 2026-09-21T23:30:37.821418Z)

## Latest publication events

- `2026-09-21T23:30:37.821418Z` — **WINDFOR**: 73 rows; marker `2026-09-21T23:30:00Z`
- `2026-09-21T23:30:37.821418Z` — **FUELHH**: 20 rows; marker `2026-09-21T23:30:00Z`
- `2026-09-21T23:30:37.821418Z` — **FUELINST**: 80 rows; marker `2026-09-21T23:30:00Z`
- `2026-09-21T23:30:21.635920Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:29:45Z`
- `2026-09-21T23:28:13.154583Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:27:45Z`
- `2026-09-21T23:26:18.119043Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:25:45Z`
- `2026-09-21T23:25:29.924306Z` — **FUELINST**: 80 rows; marker `2026-09-21T23:25:00Z`
- `2026-09-21T23:24:10.261452Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:23:45Z`
- `2026-09-21T23:22:21.959693Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:21:45Z`
- `2026-09-21T23:21:49.574733Z` — **IMBALNGC**: 1026 rows; marker `2026-09-21T23:17:00Z`
- `2026-09-21T23:21:15.927702Z` — **INDGEN**: 1026 rows; marker `2026-09-21T23:17:00Z`
- `2026-09-21T23:21:15.927702Z` — **INDDEM**: 1026 rows; marker `2026-09-21T23:17:00Z`
- `2026-09-21T23:20:27.879984Z` — **FUELINST**: 80 rows; marker `2026-09-21T23:20:00Z`
- `2026-09-21T23:20:11.054115Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:19:45Z`
- `2026-09-21T23:19:39.547553Z` — **MELNGC**: 1026 rows; marker `2026-09-21T23:17:00Z`
