# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T08:18:00.138180Z`  
Current process started UTC: `2026-09-22T08:13:59.647891Z`  
1-second metadata polls in this process: **236**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2074, 2026-09-22T08:15:35.686009Z)
- `FUELINST|fuelType=OTHER|generation` = **603** (n=2074, 2026-09-22T08:15:35.686009Z)
- `FUELINST|fuelType=PS|generation` = **-169** (n=2074, 2026-09-22T08:15:35.686009Z)
- `FUELINST|fuelType=WIND|generation` = **3662** (n=2074, 2026-09-22T08:15:35.686009Z)
- `IMBALNGC|TOTAL|imbalance` = **-3831** (n=340, 2026-09-22T07:19:53.015943Z)
- `INDDEM|TOTAL|demand` = **-12688** (n=340, 2026-09-22T07:19:53.015943Z)
- `INDGEN|TOTAL|generation` = **17876** (n=340, 2026-09-22T07:19:53.015943Z)
- `MELNGC|TOTAL|margin` = **37783** (n=340, 2026-09-22T07:19:04.110635Z)
- `MID|dataProvider=APXMIDP|price` = **133.27** (n=82, 2026-09-22T08:12:11.527697Z)
- `MID|dataProvider=APXMIDP|volume` = **3080.6** (n=82, 2026-09-22T08:12:11.527697Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=162, 2026-09-22T08:12:11.527697Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=162, 2026-09-22T08:12:11.527697Z)
- `NDF|TOTAL|demand` = **20320** (n=349, 2026-09-22T08:16:57.432568Z)
- `TSDF|TOTAL|demand` = **21068** (n=349, 2026-09-22T08:16:57.432568Z)
- `WINDFOR|TOTAL|generation` = **12340** (n=58, 2026-09-22T05:30:40.954997Z)

## Latest publication events

- `2026-09-22T08:16:57.432568Z` — **TSDF**: 702 rows; marker `2026-09-22T08:16:00Z`
- `2026-09-22T08:16:57.432568Z` — **NDF**: 39 rows; marker `2026-09-22T08:16:00Z`
- `2026-09-22T08:16:24.316975Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:15:45Z`
- `2026-09-22T08:15:35.686009Z` — **FUELINST**: 80 rows; marker `2026-09-22T08:15:00Z`
- `2026-09-22T08:14:15.649351Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:13:45Z`
- `2026-09-22T08:12:11.527697Z` — **MID**: 2 rows; marker `2026-09-22T08:12:03Z`
- `2026-09-22T08:12:11.527697Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:11:45Z`
- `2026-09-22T08:10:35.524463Z` — **FUELINST**: 80 rows; marker `2026-09-22T08:10:00Z`
- `2026-09-22T08:10:18.959151Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:09:45Z`
- `2026-09-22T08:08:15.075333Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:07:45Z`
- `2026-09-22T08:07:26.825305Z` — **MID**: 1 rows; marker `2026-09-22T08:05:00Z`
- `2026-09-22T08:06:21.941898Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:05:45Z`
- `2026-09-22T08:05:33.032681Z` — **FUELINST**: 80 rows; marker `2026-09-22T08:05:00Z`
- `2026-09-22T08:04:16.834278Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:03:45Z`
- `2026-09-22T08:02:08.504481Z` — **FREQ**: 5761 rows; marker `2026-09-22T08:01:45Z`
