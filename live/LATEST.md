# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T08:26:29.479591Z`  
Current process started UTC: `2026-09-22T08:22:29.912084Z`  
1-second metadata polls in this process: **239**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2076, 2026-09-22T08:25:28.679885Z)
- `FUELINST|fuelType=OTHER|generation` = **459** (n=2076, 2026-09-22T08:25:28.679885Z)
- `FUELINST|fuelType=PS|generation` = **-169** (n=2076, 2026-09-22T08:25:28.679885Z)
- `FUELINST|fuelType=WIND|generation` = **3711** (n=2076, 2026-09-22T08:25:28.679885Z)
- `IMBALNGC|TOTAL|imbalance` = **-1355** (n=341, 2026-09-22T08:19:38.048910Z)
- `INDDEM|TOTAL|demand` = **-12798** (n=341, 2026-09-22T08:19:38.048910Z)
- `INDGEN|TOTAL|generation` = **19713** (n=341, 2026-09-22T08:19:38.048910Z)
- `MELNGC|TOTAL|margin` = **39004** (n=341, 2026-09-22T08:18:34.342145Z)
- `MID|dataProvider=APXMIDP|price` = **133.27** (n=82, 2026-09-22T08:12:11.527697Z)
- `MID|dataProvider=APXMIDP|volume` = **3080.6** (n=82, 2026-09-22T08:12:11.527697Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=162, 2026-09-22T08:12:11.527697Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=162, 2026-09-22T08:12:11.527697Z)
- `NDF|TOTAL|demand` = **20320** (n=349, 2026-09-22T08:16:57.432568Z)
- `TSDF|TOTAL|demand` = **21068** (n=349, 2026-09-22T08:16:57.432568Z)
- `WINDFOR|TOTAL|generation` = **12340** (n=58, 2026-09-22T05:30:40.954997Z)

## Latest publication events

- `2026-09-22T08:26:16.686157Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:25:45Z`
- `2026-09-22T08:25:28.679885Z` — **FUELINST**: 80 rows; marker `2026-09-22T08:25:00Z`
- `2026-09-22T08:24:24.926743Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:23:45Z`
- `2026-09-22T08:22:17.061238Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:21:45Z`
- `2026-09-22T08:20:40.869815Z` — **FUELINST**: 80 rows; marker `2026-09-22T08:20:00Z`
- `2026-09-22T08:20:25.429497Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:19:45Z`
- `2026-09-22T08:19:38.048910Z` — **INDGEN**: 702 rows; marker `2026-09-22T08:16:00Z`
- `2026-09-22T08:19:38.048910Z` — **INDDEM**: 702 rows; marker `2026-09-22T08:16:00Z`
- `2026-09-22T08:19:38.048910Z` — **IMBALNGC**: 702 rows; marker `2026-09-22T08:16:00Z`
- `2026-09-22T08:18:34.342145Z` — **MELNGC**: 702 rows; marker `2026-09-22T08:16:00Z`
- `2026-09-22T08:18:18.620941Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:17:45Z`
- `2026-09-22T08:16:57.432568Z` — **TSDF**: 702 rows; marker `2026-09-22T08:16:00Z`
- `2026-09-22T08:16:57.432568Z` — **NDF**: 39 rows; marker `2026-09-22T08:16:00Z`
- `2026-09-22T08:16:24.316975Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:15:45Z`
- `2026-09-22T08:15:35.686009Z` — **FUELINST**: 80 rows; marker `2026-09-22T08:15:00Z`
