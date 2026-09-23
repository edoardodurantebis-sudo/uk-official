# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T09:31:37.667732Z`  
Current process started UTC: `2026-09-23T09:27:37.208984Z`  
1-second metadata polls in this process: **236**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2377, 2026-09-23T09:30:33.246125Z)
- `FUELINST|fuelType=OTHER|generation` = **689** (n=2377, 2026-09-23T09:30:33.246125Z)
- `FUELINST|fuelType=PS|generation` = **-19** (n=2377, 2026-09-23T09:30:33.246125Z)
- `FUELINST|fuelType=WIND|generation` = **9955** (n=2377, 2026-09-23T09:30:33.246125Z)
- `IMBALNGC|TOTAL|imbalance` = **-5115** (n=390, 2026-09-23T09:23:22.551360Z)
- `INDDEM|TOTAL|demand` = **-12682** (n=390, 2026-09-23T09:22:39.228143Z)
- `INDGEN|TOTAL|generation` = **15913** (n=390, 2026-09-23T09:22:55.466813Z)
- `MELNGC|TOTAL|margin` = **40723** (n=390, 2026-09-23T09:22:23.729348Z)
- `MID|dataProvider=APXMIDP|price` = **123.07** (n=132, 2026-09-23T09:12:21.471335Z)
- `MID|dataProvider=APXMIDP|volume` = **3290.4** (n=132, 2026-09-23T09:12:21.471335Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=260, 2026-09-23T09:12:21.471335Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=260, 2026-09-23T09:12:21.471335Z)
- `NDF|TOTAL|demand` = **20282** (n=399, 2026-09-23T09:19:27.544656Z)
- `TSDF|TOTAL|demand` = **21028** (n=399, 2026-09-23T09:19:27.544656Z)
- `WINDFOR|TOTAL|generation` = **6996** (n=67, 2026-09-23T08:30:29.420655Z)

## Latest publication events

- `2026-09-23T09:30:33.246125Z` — **FUELHH**: 20 rows; marker `2026-09-23T09:30:00Z`
- `2026-09-23T09:30:33.246125Z` — **FUELINST**: 80 rows; marker `2026-09-23T09:30:00Z`
- `2026-09-23T09:30:17.270602Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:29:45Z`
- `2026-09-23T09:28:25.216930Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:27:45Z`
- `2026-09-23T09:26:19.925350Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:25:45Z`
- `2026-09-23T09:25:31.721114Z` — **FUELINST**: 80 rows; marker `2026-09-23T09:25:00Z`
- `2026-09-23T09:24:10.910249Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:23:45Z`
- `2026-09-23T09:23:22.551360Z` — **IMBALNGC**: 666 rows; marker `2026-09-23T09:19:00Z`
- `2026-09-23T09:22:55.466813Z` — **INDGEN**: 666 rows; marker `2026-09-23T09:19:00Z`
- `2026-09-23T09:22:39.228143Z` — **INDDEM**: 666 rows; marker `2026-09-23T09:19:00Z`
- `2026-09-23T09:22:23.729348Z` — **MELNGC**: 666 rows; marker `2026-09-23T09:19:00Z`
- `2026-09-23T09:22:07.695699Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:21:45Z`
- `2026-09-23T09:20:31.553984Z` — **FUELINST**: 80 rows; marker `2026-09-23T09:20:00Z`
- `2026-09-23T09:20:15.761483Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:19:45Z`
- `2026-09-23T09:19:27.544656Z` — **TSDF**: 666 rows; marker `2026-09-23T09:19:00Z`
