# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T20:55:13.119257Z`  
Current process started UTC: `2026-09-22T20:51:12.568503Z`  
1-second metadata polls in this process: **233**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2225, 2026-09-22T20:50:28.831786Z)
- `FUELINST|fuelType=OTHER|generation` = **351** (n=2225, 2026-09-22T20:50:28.831786Z)
- `FUELINST|fuelType=PS|generation` = **142** (n=2225, 2026-09-22T20:50:28.831786Z)
- `FUELINST|fuelType=WIND|generation` = **2322** (n=2225, 2026-09-22T20:50:28.831786Z)
- `IMBALNGC|TOTAL|imbalance` = **-8041** (n=366, 2026-09-22T20:51:12.568510Z)
- `INDDEM|TOTAL|demand` = **-12476** (n=366, 2026-09-22T20:51:12.568510Z)
- `INDGEN|TOTAL|generation` = **13132** (n=366, 2026-09-22T20:51:12.568510Z)
- `MELNGC|TOTAL|margin` = **37210** (n=366, 2026-09-22T20:49:09.070118Z)
- `MID|dataProvider=APXMIDP|price` = **172.15** (n=107, 2026-09-22T20:42:19.623301Z)
- `MID|dataProvider=APXMIDP|volume` = **4165.1** (n=107, 2026-09-22T20:42:19.623301Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=212, 2026-09-22T20:42:19.623301Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=212, 2026-09-22T20:42:19.623301Z)
- `NDF|TOTAL|demand` = **20673** (n=374, 2026-09-22T20:47:31.732165Z)
- `TSDF|TOTAL|demand` = **21173** (n=374, 2026-09-22T20:47:47.279066Z)
- `WINDFOR|TOTAL|generation` = **13612** (n=63, 2026-09-22T19:30:53.095849Z)

## Latest publication events

- `2026-09-22T20:54:09.218669Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:53:45Z`
- `2026-09-22T20:52:16.087139Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:51:45Z`
- `2026-09-22T20:51:12.568510Z` — **INDGEN**: 1116 rows; marker `2026-09-22T20:47:00Z`
- `2026-09-22T20:51:12.568510Z` — **INDDEM**: 1116 rows; marker `2026-09-22T20:47:00Z`
- `2026-09-22T20:51:12.568510Z` — **IMBALNGC**: 1116 rows; marker `2026-09-22T20:47:00Z`
- `2026-09-22T20:50:28.831786Z` — **FUELINST**: 80 rows; marker `2026-09-22T20:50:00Z`
- `2026-09-22T20:50:13.262499Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:49:45Z`
- `2026-09-22T20:49:09.070118Z` — **MELNGC**: 1116 rows; marker `2026-09-22T20:47:00Z`
- `2026-09-22T20:48:21.011548Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:47:45Z`
- `2026-09-22T20:47:47.279066Z` — **TSDF**: 1116 rows; marker `2026-09-22T20:47:00Z`
- `2026-09-22T20:47:31.732165Z` — **NDF**: 62 rows; marker `2026-09-22T20:47:00Z`
- `2026-09-22T20:46:12.340135Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:45:45Z`
- `2026-09-22T20:45:24.001040Z` — **FUELINST**: 80 rows; marker `2026-09-22T20:45:00Z`
- `2026-09-22T20:44:20.322728Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:43:45Z`
- `2026-09-22T20:42:19.623301Z` — **MID**: 2 rows; marker `2026-09-22T20:42:03Z`
