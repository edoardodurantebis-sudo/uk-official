# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T08:47:40.267408Z`  
Current process started UTC: `2026-09-22T08:43:40.246092Z`  
1-second metadata polls in this process: **234**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2080, 2026-09-22T08:45:33.293832Z)
- `FUELINST|fuelType=OTHER|generation` = **577** (n=2080, 2026-09-22T08:45:33.293832Z)
- `FUELINST|fuelType=PS|generation` = **-169** (n=2080, 2026-09-22T08:45:33.293832Z)
- `FUELINST|fuelType=WIND|generation` = **3660** (n=2080, 2026-09-22T08:45:33.293832Z)
- `IMBALNGC|TOTAL|imbalance` = **-1355** (n=341, 2026-09-22T08:19:38.048910Z)
- `INDDEM|TOTAL|demand` = **-12798** (n=341, 2026-09-22T08:19:38.048910Z)
- `INDGEN|TOTAL|generation` = **19713** (n=341, 2026-09-22T08:19:38.048910Z)
- `MELNGC|TOTAL|margin` = **39004** (n=341, 2026-09-22T08:18:34.342145Z)
- `MID|dataProvider=APXMIDP|price` = **132.64** (n=83, 2026-09-22T08:42:10.916820Z)
- `MID|dataProvider=APXMIDP|volume` = **3029.4** (n=83, 2026-09-22T08:42:10.916820Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=164, 2026-09-22T08:42:10.916820Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=164, 2026-09-22T08:42:10.916820Z)
- `NDF|TOTAL|demand` = **20320** (n=350, 2026-09-22T08:47:11.140881Z)
- `TSDF|TOTAL|demand` = **21068** (n=350, 2026-09-22T08:47:11.140881Z)
- `WINDFOR|TOTAL|generation` = **12393** (n=59, 2026-09-22T08:31:02.929426Z)

## Latest publication events

- `2026-09-22T08:47:11.140881Z` — **TSDF**: 684 rows; marker `2026-09-22T08:46:00Z`
- `2026-09-22T08:47:11.140881Z` — **NDF**: 38 rows; marker `2026-09-22T08:46:00Z`
- `2026-09-22T08:46:05.669702Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:45:45Z`
- `2026-09-22T08:45:33.293832Z` — **FUELINST**: 80 rows; marker `2026-09-22T08:45:00Z`
- `2026-09-22T08:44:12.249926Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:43:45Z`
- `2026-09-22T08:42:10.916820Z` — **MID**: 2 rows; marker `2026-09-22T08:42:04Z`
- `2026-09-22T08:42:10.916820Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:41:45Z`
- `2026-09-22T08:40:34.414959Z` — **FUELINST**: 80 rows; marker `2026-09-22T08:40:00Z`
- `2026-09-22T08:40:18.678760Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:39:45Z`
- `2026-09-22T08:38:26.901974Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:37:45Z`
- `2026-09-22T08:37:22.754806Z` — **MID**: 1 rows; marker `2026-09-22T08:35:00Z`
- `2026-09-22T08:36:18.828336Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:35:45Z`
- `2026-09-22T08:35:31.001672Z` — **FUELINST**: 80 rows; marker `2026-09-22T08:35:00Z`
- `2026-09-22T08:34:19.410649Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:33:45Z`
- `2026-09-22T08:32:23.689949Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:31:45Z`
