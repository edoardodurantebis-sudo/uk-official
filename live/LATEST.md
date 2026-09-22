# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T09:21:25.128515Z`  
Current process started UTC: `2026-09-22T09:17:24.704450Z`  
1-second metadata polls in this process: **233**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2087, 2026-09-22T09:20:38.000635Z)
- `FUELINST|fuelType=OTHER|generation` = **542** (n=2087, 2026-09-22T09:20:38.000635Z)
- `FUELINST|fuelType=PS|generation` = **-170** (n=2087, 2026-09-22T09:20:38.000635Z)
- `FUELINST|fuelType=WIND|generation` = **3516** (n=2087, 2026-09-22T09:20:38.000635Z)
- `IMBALNGC|TOTAL|imbalance` = **2430** (n=343, 2026-09-22T09:19:17.697388Z)
- `INDDEM|TOTAL|demand` = **-12801** (n=343, 2026-09-22T09:19:01.822080Z)
- `INDGEN|TOTAL|generation` = **23498** (n=343, 2026-09-22T09:19:01.822080Z)
- `MELNGC|TOTAL|margin` = **40334** (n=343, 2026-09-22T09:18:29.864815Z)
- `MID|dataProvider=APXMIDP|price` = **129.53** (n=84, 2026-09-22T09:12:11.831090Z)
- `MID|dataProvider=APXMIDP|volume` = **2865.1** (n=84, 2026-09-22T09:12:11.831090Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=166, 2026-09-22T09:12:11.831090Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=166, 2026-09-22T09:12:11.831090Z)
- `NDF|TOTAL|demand` = **20320** (n=351, 2026-09-22T09:16:54.603659Z)
- `TSDF|TOTAL|demand` = **21068** (n=351, 2026-09-22T09:16:54.603659Z)
- `WINDFOR|TOTAL|generation` = **12393** (n=59, 2026-09-22T08:31:02.929426Z)

## Latest publication events

- `2026-09-22T09:20:38.000635Z` — **FUELINST**: 80 rows; marker `2026-09-22T09:20:00Z`
- `2026-09-22T09:20:21.568901Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:19:45Z`
- `2026-09-22T09:19:17.697388Z` — **IMBALNGC**: 666 rows; marker `2026-09-22T09:16:00Z`
- `2026-09-22T09:19:01.822080Z` — **INDGEN**: 666 rows; marker `2026-09-22T09:16:00Z`
- `2026-09-22T09:19:01.822080Z` — **INDDEM**: 666 rows; marker `2026-09-22T09:16:00Z`
- `2026-09-22T09:18:29.864815Z` — **MELNGC**: 666 rows; marker `2026-09-22T09:16:00Z`
- `2026-09-22T09:18:13.417757Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:17:45Z`
- `2026-09-22T09:16:54.603659Z` — **TSDF**: 666 rows; marker `2026-09-22T09:16:00Z`
- `2026-09-22T09:16:54.603659Z` — **NDF**: 37 rows; marker `2026-09-22T09:16:00Z`
- `2026-09-22T09:16:22.369726Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:15:45Z`
- `2026-09-22T09:15:34.501813Z` — **FUELINST**: 80 rows; marker `2026-09-22T09:15:00Z`
- `2026-09-22T09:14:14.102768Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:13:45Z`
- `2026-09-22T09:12:11.831090Z` — **MID**: 2 rows; marker `2026-09-22T09:12:03Z`
- `2026-09-22T09:12:11.831090Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:11:45Z`
- `2026-09-22T09:10:35.095630Z` — **FUELINST**: 80 rows; marker `2026-09-22T09:10:00Z`
