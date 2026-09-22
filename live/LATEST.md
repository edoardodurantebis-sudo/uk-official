# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T07:27:13.085999Z`  
Current process started UTC: `2026-09-22T07:23:13.114985Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3136, delta=-128, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3264, delta=142, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3122, delta=169, z=3.61 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=-1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3662, delta=5, z=3.53 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3659, delta=11, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3659, delta=-2, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=1, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=-3, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3663, delta=14, z=3.65 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-2, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-5, z=3.50 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2064, 2026-09-22T07:25:37.041629Z)
- `FUELINST|fuelType=OTHER|generation` = **863** (n=2064, 2026-09-22T07:25:37.041629Z)
- `FUELINST|fuelType=PS|generation` = **-174** (n=2064, 2026-09-22T07:25:37.041629Z)
- `FUELINST|fuelType=WIND|generation` = **3521** (n=2064, 2026-09-22T07:25:37.041629Z)
- `IMBALNGC|TOTAL|imbalance` = **-3831** (n=340, 2026-09-22T07:19:53.015943Z)
- `INDDEM|TOTAL|demand` = **-12688** (n=340, 2026-09-22T07:19:53.015943Z)
- `INDGEN|TOTAL|generation` = **17876** (n=340, 2026-09-22T07:19:53.015943Z)
- `MELNGC|TOTAL|margin` = **37783** (n=340, 2026-09-22T07:19:04.110635Z)
- `MID|dataProvider=APXMIDP|price` = **150.92** (n=80, 2026-09-22T07:12:15.900395Z)
- `MID|dataProvider=APXMIDP|volume` = **2883.3** (n=80, 2026-09-22T07:12:15.900395Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=158, 2026-09-22T07:12:15.900395Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=158, 2026-09-22T07:12:15.900395Z)
- `NDF|TOTAL|demand` = **20959** (n=347, 2026-09-22T07:17:12.886968Z)
- `TSDF|TOTAL|demand` = **21707** (n=347, 2026-09-22T07:17:12.886968Z)
- `WINDFOR|TOTAL|generation` = **12340** (n=58, 2026-09-22T05:30:40.954997Z)

## Latest publication events

- `2026-09-22T07:26:24.459222Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:25:45Z`
- `2026-09-22T07:25:37.041629Z` — **FUELINST**: 80 rows; marker `2026-09-22T07:25:00Z`
- `2026-09-22T07:24:17.284831Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:23:45Z`
- `2026-09-22T07:22:15.933569Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:21:45Z`
- `2026-09-22T07:20:39.848650Z` — **FUELINST**: 80 rows; marker `2026-09-22T07:20:00Z`
- `2026-09-22T07:20:24.419598Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:19:45Z`
- `2026-09-22T07:19:53.015943Z` — **INDGEN**: 738 rows; marker `2026-09-22T07:16:00Z`
- `2026-09-22T07:19:53.015943Z` — **INDDEM**: 738 rows; marker `2026-09-22T07:16:00Z`
- `2026-09-22T07:19:53.015943Z` — **IMBALNGC**: 738 rows; marker `2026-09-22T07:16:00Z`
- `2026-09-22T07:19:04.110635Z` — **MELNGC**: 738 rows; marker `2026-09-22T07:16:00Z`
- `2026-09-22T07:18:16.323920Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:17:45Z`
- `2026-09-22T07:17:12.886968Z` — **TSDF**: 738 rows; marker `2026-09-22T07:16:00Z`
- `2026-09-22T07:17:12.886968Z` — **NDF**: 41 rows; marker `2026-09-22T07:16:00Z`
- `2026-09-22T07:16:09.066897Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:15:45Z`
- `2026-09-22T07:15:36.765876Z` — **FUELINST**: 80 rows; marker `2026-09-22T07:15:00Z`
