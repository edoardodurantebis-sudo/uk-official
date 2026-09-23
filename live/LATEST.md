# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T02:03:33.364186Z`  
Current process started UTC: `2026-09-23T01:59:33.131448Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2287, 2026-09-23T02:00:36.504244Z)
- `FUELINST|fuelType=OTHER|generation` = **201** (n=2287, 2026-09-23T02:00:36.504244Z)
- `FUELINST|fuelType=PS|generation` = **147** (n=2287, 2026-09-23T02:00:36.504244Z)
- `FUELINST|fuelType=WIND|generation` = **5042** (n=2287, 2026-09-23T02:00:36.504244Z)
- `IMBALNGC|TOTAL|imbalance` = **-7980** (n=376, 2026-09-23T01:51:53.095817Z)
- `INDDEM|TOTAL|demand` = **-12433** (n=376, 2026-09-23T01:51:53.095817Z)
- `INDGEN|TOTAL|generation` = **13193** (n=376, 2026-09-23T01:51:53.095817Z)
- `MELNGC|TOTAL|margin` = **37215** (n=376, 2026-09-23T01:49:49.004084Z)
- `MID|dataProvider=APXMIDP|price` = **138.27** (n=117, 2026-09-23T01:42:11.249486Z)
- `MID|dataProvider=APXMIDP|volume` = **2548.5** (n=117, 2026-09-23T01:42:11.249486Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=230, 2026-09-23T01:42:11.249486Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=230, 2026-09-23T01:42:11.249486Z)
- `NDF|TOTAL|demand` = **20673** (n=384, 2026-09-23T01:47:40.219823Z)
- `TSDF|TOTAL|demand` = **21173** (n=384, 2026-09-23T01:47:40.219823Z)
- `WINDFOR|TOTAL|generation` = **13770** (n=64, 2026-09-22T23:30:32.481751Z)

## Latest publication events

- `2026-09-23T02:02:13.554739Z` — **FREQ**: 5761 rows; marker `2026-09-23T02:01:45Z`
- `2026-09-23T02:00:36.504244Z` — **FUELHH**: 20 rows; marker `2026-09-23T02:00:00Z`
- `2026-09-23T02:00:36.504244Z` — **FUELINST**: 80 rows; marker `2026-09-23T02:00:00Z`
- `2026-09-23T02:00:21.075810Z` — **FREQ**: 5761 rows; marker `2026-09-23T01:59:45Z`
- `2026-09-23T01:58:02.125131Z` — **FREQ**: 5761 rows; marker `2026-09-23T01:57:45Z`
- `2026-09-23T01:56:26.657417Z` — **FREQ**: 5761 rows; marker `2026-09-23T01:55:45Z`
- `2026-09-23T01:55:38.476392Z` — **FUELINST**: 80 rows; marker `2026-09-23T01:55:00Z`
- `2026-09-23T01:54:17.092328Z` — **FREQ**: 5761 rows; marker `2026-09-23T01:53:45Z`
- `2026-09-23T01:52:24.959275Z` — **FREQ**: 5761 rows; marker `2026-09-23T01:51:45Z`
- `2026-09-23T01:51:53.095817Z` — **INDGEN**: 936 rows; marker `2026-09-23T01:47:00Z`
- `2026-09-23T01:51:53.095817Z` — **INDDEM**: 936 rows; marker `2026-09-23T01:47:00Z`
- `2026-09-23T01:51:53.095817Z` — **IMBALNGC**: 936 rows; marker `2026-09-23T01:47:00Z`
- `2026-09-23T01:50:36.719237Z` — **FUELINST**: 80 rows; marker `2026-09-23T01:50:00Z`
- `2026-09-23T01:50:21.162849Z` — **FREQ**: 5761 rows; marker `2026-09-23T01:49:45Z`
- `2026-09-23T01:49:49.004084Z` — **MELNGC**: 936 rows; marker `2026-09-23T01:47:00Z`
