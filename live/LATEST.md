# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T02:29:24.339921Z`  
Current process started UTC: `2026-09-23T02:25:24.652086Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2292, 2026-09-23T02:25:24.652097Z)
- `FUELINST|fuelType=OTHER|generation` = **264** (n=2292, 2026-09-23T02:25:24.652097Z)
- `FUELINST|fuelType=PS|generation` = **142** (n=2292, 2026-09-23T02:25:24.652097Z)
- `FUELINST|fuelType=WIND|generation` = **5299** (n=2292, 2026-09-23T02:25:24.652097Z)
- `IMBALNGC|TOTAL|imbalance` = **-7977** (n=377, 2026-09-23T02:21:13.396680Z)
- `INDDEM|TOTAL|demand` = **-12420** (n=377, 2026-09-23T02:21:13.396680Z)
- `INDGEN|TOTAL|generation` = **13196** (n=377, 2026-09-23T02:21:13.396680Z)
- `MELNGC|TOTAL|margin` = **38662** (n=377, 2026-09-23T02:19:42.842140Z)
- `MID|dataProvider=APXMIDP|price` = **146.46** (n=118, 2026-09-23T02:12:49.852416Z)
- `MID|dataProvider=APXMIDP|volume` = **2573.9** (n=118, 2026-09-23T02:12:49.852416Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=232, 2026-09-23T02:12:49.852416Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=232, 2026-09-23T02:12:49.852416Z)
- `NDF|TOTAL|demand` = **20673** (n=385, 2026-09-23T02:17:50.154424Z)
- `TSDF|TOTAL|demand` = **21173** (n=385, 2026-09-23T02:17:50.154424Z)
- `WINDFOR|TOTAL|generation` = **13770** (n=64, 2026-09-22T23:30:32.481751Z)

## Latest publication events

- `2026-09-23T02:28:20.089235Z` — **FREQ**: 5761 rows; marker `2026-09-23T02:27:45Z`
- `2026-09-23T02:26:12.792118Z` — **FREQ**: 5761 rows; marker `2026-09-23T02:25:45Z`
- `2026-09-23T02:25:24.652097Z` — **FUELINST**: 80 rows; marker `2026-09-23T02:25:00Z`
- `2026-09-23T02:24:08.730949Z` — **FREQ**: 5761 rows; marker `2026-09-23T02:23:45Z`
- `2026-09-23T02:22:17.130218Z` — **FREQ**: 5761 rows; marker `2026-09-23T02:21:45Z`
- `2026-09-23T02:21:13.396680Z` — **INDGEN**: 918 rows; marker `2026-09-23T02:17:00Z`
- `2026-09-23T02:21:13.396680Z` — **INDDEM**: 918 rows; marker `2026-09-23T02:17:00Z`
- `2026-09-23T02:21:13.396680Z` — **IMBALNGC**: 918 rows; marker `2026-09-23T02:17:00Z`
- `2026-09-23T02:20:30.743499Z` — **FUELINST**: 80 rows; marker `2026-09-23T02:20:00Z`
- `2026-09-23T02:20:14.542657Z` — **FREQ**: 5761 rows; marker `2026-09-23T02:19:45Z`
- `2026-09-23T02:19:42.842140Z` — **MELNGC**: 918 rows; marker `2026-09-23T02:17:00Z`
- `2026-09-23T02:18:22.072442Z` — **FREQ**: 5761 rows; marker `2026-09-23T02:17:45Z`
- `2026-09-23T02:17:50.154424Z` — **TSDF**: 918 rows; marker `2026-09-23T02:17:00Z`
- `2026-09-23T02:17:50.154424Z` — **NDF**: 51 rows; marker `2026-09-23T02:17:00Z`
- `2026-09-23T02:16:18.626945Z` — **FREQ**: 5761 rows; marker `2026-09-23T02:15:45Z`
