# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T21:33:11.514043Z`  
Current process started UTC: `2026-09-22T21:29:12.070196Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2233, 2026-09-22T21:30:49.527904Z)
- `FUELINST|fuelType=OTHER|generation` = **190** (n=2233, 2026-09-22T21:30:49.527904Z)
- `FUELINST|fuelType=PS|generation` = **143** (n=2233, 2026-09-22T21:30:49.527904Z)
- `FUELINST|fuelType=WIND|generation` = **2376** (n=2233, 2026-09-22T21:30:49.527904Z)
- `IMBALNGC|TOTAL|imbalance` = **-8019** (n=367, 2026-09-22T21:21:02.373107Z)
- `INDDEM|TOTAL|demand` = **-12477** (n=367, 2026-09-22T21:20:46.150531Z)
- `INDGEN|TOTAL|generation` = **13154** (n=367, 2026-09-22T21:21:02.373107Z)
- `MELNGC|TOTAL|margin` = **37210** (n=367, 2026-09-22T21:19:26.566063Z)
- `MID|dataProvider=APXMIDP|price` = **166.13** (n=108, 2026-09-22T21:12:19.399781Z)
- `MID|dataProvider=APXMIDP|volume` = **3509.9** (n=108, 2026-09-22T21:12:19.399781Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=214, 2026-09-22T21:12:19.399781Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=214, 2026-09-22T21:12:19.399781Z)
- `NDF|TOTAL|demand` = **20673** (n=375, 2026-09-22T21:17:35.637342Z)
- `TSDF|TOTAL|demand` = **21173** (n=375, 2026-09-22T21:17:35.637342Z)
- `WINDFOR|TOTAL|generation` = **13612** (n=63, 2026-09-22T19:30:53.095849Z)

## Latest publication events

- `2026-09-22T21:32:09.144489Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:31:45Z`
- `2026-09-22T21:30:49.527904Z` — **FUELHH**: 20 rows; marker `2026-09-22T21:30:00Z`
- `2026-09-22T21:30:49.527904Z` — **FUELINST**: 80 rows; marker `2026-09-22T21:30:00Z`
- `2026-09-22T21:30:17.967145Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:29:45Z`
- `2026-09-22T21:28:14.502175Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:27:45Z`
- `2026-09-22T21:26:06.970705Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:25:45Z`
- `2026-09-22T21:25:34.912230Z` — **FUELINST**: 80 rows; marker `2026-09-22T21:25:00Z`
- `2026-09-22T21:24:29.883122Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:23:45Z`
- `2026-09-22T21:22:22.184927Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:21:45Z`
- `2026-09-22T21:21:02.373107Z` — **INDGEN**: 1098 rows; marker `2026-09-22T21:17:00Z`
- `2026-09-22T21:21:02.373107Z` — **IMBALNGC**: 1098 rows; marker `2026-09-22T21:17:00Z`
- `2026-09-22T21:20:46.150531Z` — **INDDEM**: 1098 rows; marker `2026-09-22T21:17:00Z`
- `2026-09-22T21:20:46.150531Z` — **FUELINST**: 80 rows; marker `2026-09-22T21:20:00Z`
- `2026-09-22T21:20:14.901084Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:19:45Z`
- `2026-09-22T21:19:26.566063Z` — **MELNGC**: 1098 rows; marker `2026-09-22T21:17:00Z`
