# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T09:17:10.077625Z`  
Current process started UTC: `2026-09-22T09:13:10.093785Z`  
1-second metadata polls in this process: **235**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2086, 2026-09-22T09:15:34.501813Z)
- `FUELINST|fuelType=OTHER|generation` = **533** (n=2086, 2026-09-22T09:15:34.501813Z)
- `FUELINST|fuelType=PS|generation` = **-169** (n=2086, 2026-09-22T09:15:34.501813Z)
- `FUELINST|fuelType=WIND|generation` = **3502** (n=2086, 2026-09-22T09:15:34.501813Z)
- `IMBALNGC|TOTAL|imbalance` = **-20** (n=342, 2026-09-22T08:49:28.013444Z)
- `INDDEM|TOTAL|demand` = **-12801** (n=342, 2026-09-22T08:49:43.488883Z)
- `INDGEN|TOTAL|generation` = **21048** (n=342, 2026-09-22T08:49:43.488883Z)
- `MELNGC|TOTAL|margin` = **38948** (n=342, 2026-09-22T08:48:40.380600Z)
- `MID|dataProvider=APXMIDP|price` = **129.53** (n=84, 2026-09-22T09:12:11.831090Z)
- `MID|dataProvider=APXMIDP|volume` = **2865.1** (n=84, 2026-09-22T09:12:11.831090Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=166, 2026-09-22T09:12:11.831090Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=166, 2026-09-22T09:12:11.831090Z)
- `NDF|TOTAL|demand` = **20320** (n=351, 2026-09-22T09:16:54.603659Z)
- `TSDF|TOTAL|demand` = **21068** (n=351, 2026-09-22T09:16:54.603659Z)
- `WINDFOR|TOTAL|generation` = **12393** (n=59, 2026-09-22T08:31:02.929426Z)

## Latest publication events

- `2026-09-22T09:16:54.603659Z` — **TSDF**: 666 rows; marker `2026-09-22T09:16:00Z`
- `2026-09-22T09:16:54.603659Z` — **NDF**: 37 rows; marker `2026-09-22T09:16:00Z`
- `2026-09-22T09:16:22.369726Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:15:45Z`
- `2026-09-22T09:15:34.501813Z` — **FUELINST**: 80 rows; marker `2026-09-22T09:15:00Z`
- `2026-09-22T09:14:14.102768Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:13:45Z`
- `2026-09-22T09:12:11.831090Z` — **MID**: 2 rows; marker `2026-09-22T09:12:03Z`
- `2026-09-22T09:12:11.831090Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:11:45Z`
- `2026-09-22T09:10:35.095630Z` — **FUELINST**: 80 rows; marker `2026-09-22T09:10:00Z`
- `2026-09-22T09:10:17.568901Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:09:45Z`
- `2026-09-22T09:08:12.952412Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:07:45Z`
- `2026-09-22T09:07:40.708983Z` — **MID**: 1 rows; marker `2026-09-22T09:05:00Z`
- `2026-09-22T09:06:20.210484Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:05:45Z`
- `2026-09-22T09:05:32.002848Z` — **FUELINST**: 80 rows; marker `2026-09-22T09:05:00Z`
- `2026-09-22T09:04:18.325629Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:03:45Z`
- `2026-09-22T09:02:24.993565Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:01:45Z`
