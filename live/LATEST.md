# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T23:22:34.771024Z`  
Current process started UTC: `2026-09-21T23:18:34.985120Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3636, delta=-1, z=4.80 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3637, delta=3, z=4.85 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3634, delta=-8, z=4.83 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1967, 2026-09-21T23:20:27.879984Z)
- `FUELINST|fuelType=OTHER|generation` = **481** (n=1967, 2026-09-21T23:20:27.879984Z)
- `FUELINST|fuelType=PS|generation` = **-229** (n=1967, 2026-09-21T23:20:27.879984Z)
- `FUELINST|fuelType=WIND|generation` = **3526** (n=1967, 2026-09-21T23:20:27.879984Z)
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
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T23:22:21.959693Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:21:45Z`
- `2026-09-21T23:21:49.574733Z` — **IMBALNGC**: 1026 rows; marker `2026-09-21T23:17:00Z`
- `2026-09-21T23:21:15.927702Z` — **INDGEN**: 1026 rows; marker `2026-09-21T23:17:00Z`
- `2026-09-21T23:21:15.927702Z` — **INDDEM**: 1026 rows; marker `2026-09-21T23:17:00Z`
- `2026-09-21T23:20:27.879984Z` — **FUELINST**: 80 rows; marker `2026-09-21T23:20:00Z`
- `2026-09-21T23:20:11.054115Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:19:45Z`
- `2026-09-21T23:19:39.547553Z` — **MELNGC**: 1026 rows; marker `2026-09-21T23:17:00Z`
- `2026-09-21T23:18:09.955027Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:17:45Z`
- `2026-09-21T23:17:38.428444Z` — **TSDF**: 1026 rows; marker `2026-09-21T23:17:00Z`
- `2026-09-21T23:17:21.026219Z` — **NDF**: 57 rows; marker `2026-09-21T23:17:00Z`
- `2026-09-21T23:16:16.480124Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:15:45Z`
- `2026-09-21T23:15:27.390068Z` — **FUELINST**: 80 rows; marker `2026-09-21T23:15:00Z`
- `2026-09-21T23:14:22.055938Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:13:45Z`
- `2026-09-21T23:12:18.557209Z` — **MID**: 2 rows; marker `2026-09-21T23:12:03Z`
- `2026-09-21T23:12:18.557209Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:11:45Z`
