# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T09:48:27.184092Z`  
Current process started UTC: `2026-09-23T09:44:27.770480Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3187, delta=-614, z=-1.49 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=772, delta=-9447, z=-0.02 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=0, delta=-871, z=-0.35 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3202, delta=1895, z=-1.32 -> generation-mix component moved
- **FUELINST** `fuelType=COAL` `generation` — instantaneous generation mix [fuelType=COAL] generation: value=0, delta=-795, z=-0.02 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=10219, delta=9339, z=13.89 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=871, delta=871, z=11.02 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=1307, delta=-2493, z=-13.96 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=165, delta=-434, z=1.76 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=437, delta=-153, z=5.21 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3204, delta=-351, z=3.66 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=599, delta=-36, z=7.95 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=0, z=7.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=0, z=7.34 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3238, delta=-72, z=3.61 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2380, 2026-09-23T09:45:31.694735Z)
- `FUELINST|fuelType=OTHER|generation` = **571** (n=2380, 2026-09-23T09:45:31.694735Z)
- `FUELINST|fuelType=PS|generation` = **-569** (n=2380, 2026-09-23T09:45:31.694735Z)
- `FUELINST|fuelType=WIND|generation` = **9543** (n=2380, 2026-09-23T09:45:31.694735Z)
- `IMBALNGC|TOTAL|imbalance` = **-5115** (n=390, 2026-09-23T09:23:22.551360Z)
- `INDDEM|TOTAL|demand` = **-12682** (n=390, 2026-09-23T09:22:39.228143Z)
- `INDGEN|TOTAL|generation` = **15913** (n=390, 2026-09-23T09:22:55.466813Z)
- `MELNGC|TOTAL|margin` = **40723** (n=390, 2026-09-23T09:22:23.729348Z)
- `MID|dataProvider=APXMIDP|price` = **121.85** (n=133, 2026-09-23T09:42:10.371965Z)
- `MID|dataProvider=APXMIDP|volume` = **3598.6** (n=133, 2026-09-23T09:42:10.371965Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=262, 2026-09-23T09:42:10.371965Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=262, 2026-09-23T09:42:10.371965Z)
- `NDF|TOTAL|demand` = **20282** (n=399, 2026-09-23T09:19:27.544656Z)
- `TSDF|TOTAL|demand` = **21028** (n=399, 2026-09-23T09:19:27.544656Z)
- `WINDFOR|TOTAL|generation` = **6996** (n=67, 2026-09-23T08:30:29.420655Z)

## Latest publication events

- `2026-09-23T09:48:12.278977Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:47:45Z`
- `2026-09-23T09:46:20.571143Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:45:45Z`
- `2026-09-23T09:45:31.694735Z` — **FUELINST**: 80 rows; marker `2026-09-23T09:45:00Z`
- `2026-09-23T09:44:27.770487Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:43:45Z`
- `2026-09-23T09:42:26.373793Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:41:45Z`
- `2026-09-23T09:42:10.371965Z` — **MID**: 2 rows; marker `2026-09-23T09:42:03Z`
- `2026-09-23T09:40:33.922297Z` — **FUELINST**: 80 rows; marker `2026-09-23T09:40:00Z`
- `2026-09-23T09:40:17.605647Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:39:45Z`
- `2026-09-23T09:38:26.120673Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:37:45Z`
- `2026-09-23T09:37:22.528640Z` — **MID**: 1 rows; marker `2026-09-23T09:35:00Z`
- `2026-09-23T09:36:19.174734Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:35:45Z`
- `2026-09-23T09:35:35.914264Z` — **FUELINST**: 80 rows; marker `2026-09-23T09:35:00Z`
- `2026-09-23T09:34:16.304083Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:33:45Z`
- `2026-09-23T09:32:23.539349Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:31:45Z`
- `2026-09-23T09:30:33.246125Z` — **FUELHH**: 20 rows; marker `2026-09-23T09:30:00Z`
