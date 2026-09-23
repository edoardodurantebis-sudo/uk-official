# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T08:19:43.707420Z`  
Current process started UTC: `2026-09-23T08:15:43.832643Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=165, delta=-434, z=1.76 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=437, delta=-153, z=5.21 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3204, delta=-351, z=3.66 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=599, delta=-36, z=7.95 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=0, z=7.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=0, z=7.34 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3238, delta=-72, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=0, z=7.43 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3310, delta=62, z=3.73 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=-2, z=7.53 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3248, delta=-217, z=3.65 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=592, delta=-48, z=7.65 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3465, delta=-220, z=3.99 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=640, delta=7, z=8.44 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3555, delta=892, z=4.30 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2362, 2026-09-23T08:15:43.832651Z)
- `FUELINST|fuelType=OTHER|generation` = **367** (n=2362, 2026-09-23T08:15:43.832651Z)
- `FUELINST|fuelType=PS|generation` = **-291** (n=2362, 2026-09-23T08:15:43.832651Z)
- `FUELINST|fuelType=WIND|generation` = **10478** (n=2362, 2026-09-23T08:15:43.832651Z)
- `IMBALNGC|TOTAL|imbalance` = **-7454** (n=387, 2026-09-23T07:20:50.693900Z)
- `INDDEM|TOTAL|demand` = **-12650** (n=387, 2026-09-23T07:20:50.693900Z)
- `INDGEN|TOTAL|generation` = **13965** (n=387, 2026-09-23T07:20:50.693900Z)
- `MELNGC|TOTAL|margin` = **39298** (n=388, 2026-09-23T08:19:28.840514Z)
- `MID|dataProvider=APXMIDP|price` = **128.24** (n=130, 2026-09-23T08:12:19.627914Z)
- `MID|dataProvider=APXMIDP|volume` = **3273.7** (n=130, 2026-09-23T08:12:19.627914Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=256, 2026-09-23T08:12:19.627914Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=256, 2026-09-23T08:12:19.627914Z)
- `NDF|TOTAL|demand` = **20282** (n=397, 2026-09-23T08:17:37.537799Z)
- `TSDF|TOTAL|demand` = **21028** (n=397, 2026-09-23T08:17:37.537799Z)
- `WINDFOR|TOTAL|generation` = **7305** (n=66, 2026-09-23T05:30:43.471788Z)

## Latest publication events

- `2026-09-23T08:19:28.840514Z` — **MELNGC**: 702 rows; marker `2026-09-23T08:17:00Z`
- `2026-09-23T08:18:09.227604Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:17:45Z`
- `2026-09-23T08:17:37.537799Z` — **TSDF**: 702 rows; marker `2026-09-23T08:17:00Z`
- `2026-09-23T08:17:37.537799Z` — **NDF**: 39 rows; marker `2026-09-23T08:17:00Z`
- `2026-09-23T08:16:17.380497Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:15:45Z`
- `2026-09-23T08:15:43.832651Z` — **FUELINST**: 80 rows; marker `2026-09-23T08:15:00Z`
- `2026-09-23T08:14:12.084324Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:13:45Z`
- `2026-09-23T08:12:19.627914Z` — **MID**: 2 rows; marker `2026-09-23T08:12:02Z`
- `2026-09-23T08:12:19.627914Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:11:45Z`
- `2026-09-23T08:10:30.083612Z` — **FUELINST**: 80 rows; marker `2026-09-23T08:10:00Z`
- `2026-09-23T08:10:14.056132Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:09:45Z`
- `2026-09-23T08:08:03.731835Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:07:45Z`
- `2026-09-23T08:07:31.959473Z` — **MID**: 1 rows; marker `2026-09-23T08:05:00Z`
- `2026-09-23T08:06:14.096665Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:05:45Z`
- `2026-09-23T08:05:26.286739Z` — **FUELINST**: 80 rows; marker `2026-09-23T08:05:00Z`
