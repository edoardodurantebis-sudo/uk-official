# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T02:54:38.854789Z`  
Current process started UTC: `2026-09-23T02:50:38.459432Z`  
1-second metadata polls in this process: **235**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2297, 2026-09-23T02:50:38.459440Z)
- `FUELINST|fuelType=OTHER|generation` = **456** (n=2297, 2026-09-23T02:50:38.459440Z)
- `FUELINST|fuelType=PS|generation` = **140** (n=2297, 2026-09-23T02:50:38.459440Z)
- `FUELINST|fuelType=WIND|generation` = **5397** (n=2297, 2026-09-23T02:50:38.459440Z)
- `IMBALNGC|TOTAL|imbalance` = **-7980** (n=378, 2026-09-23T02:50:54.801224Z)
- `INDDEM|TOTAL|demand` = **-12419** (n=378, 2026-09-23T02:50:38.459440Z)
- `INDGEN|TOTAL|generation` = **13193** (n=378, 2026-09-23T02:50:38.459440Z)
- `MELNGC|TOTAL|margin` = **38682** (n=378, 2026-09-23T02:49:08.998468Z)
- `MID|dataProvider=APXMIDP|price` = **142.11** (n=119, 2026-09-23T02:42:12.123771Z)
- `MID|dataProvider=APXMIDP|volume` = **2500.7** (n=119, 2026-09-23T02:42:12.123771Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=234, 2026-09-23T02:42:12.123771Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=234, 2026-09-23T02:42:12.123771Z)
- `NDF|TOTAL|demand` = **20673** (n=386, 2026-09-23T02:47:32.010663Z)
- `TSDF|TOTAL|demand` = **21173** (n=386, 2026-09-23T02:47:32.010663Z)
- `WINDFOR|TOTAL|generation` = **13770** (n=64, 2026-09-22T23:30:32.481751Z)

## Latest publication events

- `2026-09-23T02:54:06.523795Z` — **FREQ**: 5761 rows; marker `2026-09-23T02:53:45Z`
- `2026-09-23T02:52:14.469773Z` — **FREQ**: 5761 rows; marker `2026-09-23T02:51:45Z`
- `2026-09-23T02:50:54.801224Z` — **IMBALNGC**: 900 rows; marker `2026-09-23T02:46:00Z`
- `2026-09-23T02:50:38.459440Z` — **INDGEN**: 900 rows; marker `2026-09-23T02:46:00Z`
- `2026-09-23T02:50:38.459440Z` — **INDDEM**: 900 rows; marker `2026-09-23T02:46:00Z`
- `2026-09-23T02:50:38.459440Z` — **FUELINST**: 80 rows; marker `2026-09-23T02:50:00Z`
- `2026-09-23T02:50:13.107991Z` — **FREQ**: 5761 rows; marker `2026-09-23T02:49:45Z`
- `2026-09-23T02:49:08.998468Z` — **MELNGC**: 900 rows; marker `2026-09-23T02:46:00Z`
- `2026-09-23T02:48:04.270277Z` — **FREQ**: 5761 rows; marker `2026-09-23T02:47:45Z`
- `2026-09-23T02:47:32.010663Z` — **TSDF**: 900 rows; marker `2026-09-23T02:47:00Z`
- `2026-09-23T02:47:32.010663Z` — **NDF**: 50 rows; marker `2026-09-23T02:46:00Z`
- `2026-09-23T02:46:28.288995Z` — **FREQ**: 5761 rows; marker `2026-09-23T02:45:45Z`
- `2026-09-23T02:45:40.374351Z` — **FUELINST**: 80 rows; marker `2026-09-23T02:45:00Z`
- `2026-09-23T02:44:20.011761Z` — **FREQ**: 5761 rows; marker `2026-09-23T02:43:45Z`
- `2026-09-23T02:42:27.642986Z` — **FREQ**: 5761 rows; marker `2026-09-23T02:41:45Z`
