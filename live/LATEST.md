# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T20:49:59.416193Z`  
Current process started UTC: `2026-09-21T20:45:58.813880Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3572, delta=9, z=4.31 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3563, delta=6, z=4.16 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3557, delta=8, z=4.06 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3534, delta=22, z=3.69 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3549, delta=2, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3547, delta=8, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3539, delta=7, z=3.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3532, delta=10, z=3.64 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=146, delta=-39, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=0, z=3.62 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=0, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=-12, z=3.66 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=161, delta=-8, z=4.02 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=185, delta=-45, z=4.95 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1936, 2026-09-21T20:45:30.568155Z)
- `FUELINST|fuelType=OTHER|generation` = **369** (n=1936, 2026-09-21T20:45:30.568155Z)
- `FUELINST|fuelType=PS|generation` = **291** (n=1936, 2026-09-21T20:45:30.568155Z)
- `FUELINST|fuelType=WIND|generation` = **3374** (n=1936, 2026-09-21T20:45:30.568155Z)
- `IMBALNGC|TOTAL|imbalance` = **-2707** (n=318, 2026-09-21T20:22:10.806468Z)
- `INDDEM|TOTAL|demand` = **-12258** (n=318, 2026-09-21T20:21:54.518829Z)
- `INDGEN|TOTAL|generation` = **18752** (n=318, 2026-09-21T20:21:54.518829Z)
- `MELNGC|TOTAL|margin` = **36086** (n=319, 2026-09-21T20:49:58.052949Z)
- `MID|dataProvider=APXMIDP|price` = **162.85** (n=59, 2026-09-21T20:42:18.441146Z)
- `MID|dataProvider=APXMIDP|volume` = **2588.8** (n=59, 2026-09-21T20:42:18.441146Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=116, 2026-09-21T20:42:18.441146Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=116, 2026-09-21T20:42:18.441146Z)
- `NDF|TOTAL|demand` = **20959** (n=326, 2026-09-21T20:47:34.289449Z)
- `TSDF|TOTAL|demand` = **21459** (n=326, 2026-09-21T20:47:34.289449Z)
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T20:49:58.052949Z` — **MELNGC**: 1116 rows; marker `2026-09-21T20:47:00Z`
- `2026-09-21T20:48:22.399327Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:47:45Z`
- `2026-09-21T20:47:34.289449Z` — **TSDF**: 1116 rows; marker `2026-09-21T20:47:00Z`
- `2026-09-21T20:47:34.289449Z` — **NDF**: 62 rows; marker `2026-09-21T20:47:00Z`
- `2026-09-21T20:46:30.862170Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:45:45Z`
- `2026-09-21T20:45:30.568155Z` — **FUELINST**: 80 rows; marker `2026-09-21T20:45:00Z`
- `2026-09-21T20:44:26.634398Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:43:45Z`
- `2026-09-21T20:42:18.441146Z` — **MID**: 2 rows; marker `2026-09-21T20:42:03Z`
- `2026-09-21T20:42:18.441146Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:41:45Z`
- `2026-09-21T20:40:42.847558Z` — **FUELINST**: 80 rows; marker `2026-09-21T20:40:00Z`
- `2026-09-21T20:40:27.218708Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:39:45Z`
- `2026-09-21T20:38:19.762009Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:37:45Z`
- `2026-09-21T20:37:31.695115Z` — **MID**: 1 rows; marker `2026-09-21T20:35:00Z`
- `2026-09-21T20:36:14.350700Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:35:45Z`
- `2026-09-21T20:35:42.619608Z` — **FUELINST**: 80 rows; marker `2026-09-21T20:35:00Z`
