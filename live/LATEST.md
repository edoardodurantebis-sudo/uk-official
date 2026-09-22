# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T21:20:31.941186Z`  
Current process started UTC: `2026-09-22T21:16:31.486345Z`  
1-second metadata polls in this process: **231**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2230, 2026-09-22T21:15:31.672742Z)
- `FUELINST|fuelType=OTHER|generation` = **341** (n=2230, 2026-09-22T21:15:31.672742Z)
- `FUELINST|fuelType=PS|generation` = **144** (n=2230, 2026-09-22T21:15:31.672742Z)
- `FUELINST|fuelType=WIND|generation` = **2308** (n=2230, 2026-09-22T21:15:31.672742Z)
- `IMBALNGC|TOTAL|imbalance` = **-8041** (n=366, 2026-09-22T20:51:12.568510Z)
- `INDDEM|TOTAL|demand` = **-12476** (n=366, 2026-09-22T20:51:12.568510Z)
- `INDGEN|TOTAL|generation` = **13132** (n=366, 2026-09-22T20:51:12.568510Z)
- `MELNGC|TOTAL|margin` = **37210** (n=367, 2026-09-22T21:19:26.566063Z)
- `MID|dataProvider=APXMIDP|price` = **166.13** (n=108, 2026-09-22T21:12:19.399781Z)
- `MID|dataProvider=APXMIDP|volume` = **3509.9** (n=108, 2026-09-22T21:12:19.399781Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=214, 2026-09-22T21:12:19.399781Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=214, 2026-09-22T21:12:19.399781Z)
- `NDF|TOTAL|demand` = **20673** (n=375, 2026-09-22T21:17:35.637342Z)
- `TSDF|TOTAL|demand` = **21173** (n=375, 2026-09-22T21:17:35.637342Z)
- `WINDFOR|TOTAL|generation` = **13612** (n=63, 2026-09-22T19:30:53.095849Z)

## Latest publication events

- `2026-09-22T21:20:14.901084Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:19:45Z`
- `2026-09-22T21:19:26.566063Z` — **MELNGC**: 1098 rows; marker `2026-09-22T21:17:00Z`
- `2026-09-22T21:18:23.035258Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:17:45Z`
- `2026-09-22T21:17:35.637342Z` — **TSDF**: 1098 rows; marker `2026-09-22T21:17:00Z`
- `2026-09-22T21:17:35.637342Z` — **NDF**: 61 rows; marker `2026-09-22T21:17:00Z`
- `2026-09-22T21:16:31.486352Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:15:45Z`
- `2026-09-22T21:15:31.672742Z` — **FUELINST**: 80 rows; marker `2026-09-22T21:15:00Z`
- `2026-09-22T21:14:27.847509Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:13:45Z`
- `2026-09-22T21:12:19.399781Z` — **MID**: 2 rows; marker `2026-09-22T21:12:03Z`
- `2026-09-22T21:12:19.399781Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:11:45Z`
- `2026-09-22T21:10:27.331561Z` — **FUELINST**: 80 rows; marker `2026-09-22T21:10:00Z`
- `2026-09-22T21:10:11.773849Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:09:45Z`
- `2026-09-22T21:08:20.298352Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:07:45Z`
- `2026-09-22T21:06:33.265125Z` — **MID**: 1 rows; marker `2026-09-22T21:05:00Z`
- `2026-09-22T21:06:16.465980Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:05:45Z`
