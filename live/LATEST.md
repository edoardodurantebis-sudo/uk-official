# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T19:23:27.287160Z`  
Current process started UTC: `2026-09-15T19:19:27.344244Z`  
1-second metadata polls in this process: **231**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.76 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=17, z=8.89 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.93 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.39 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.98 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=7.77 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=2942, delta=440, z=3.58 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=39, delta=32, z=16.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=8.90 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=10.72 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-291** (n=269, 2026-09-15T19:20:31.365881Z)
- `FUELINST|fuelType=NPSHYD|generation` = **498** (n=269, 2026-09-15T19:20:31.365881Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3320** (n=269, 2026-09-15T19:20:31.365881Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=269, 2026-09-15T19:20:31.365881Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=269, 2026-09-15T19:20:31.365881Z)
- `FUELINST|fuelType=OTHER|generation` = **1428** (n=269, 2026-09-15T19:20:31.365881Z)
- `FUELINST|fuelType=PS|generation` = **423** (n=269, 2026-09-15T19:20:31.365881Z)
- `FUELINST|fuelType=WIND|generation` = **10406** (n=269, 2026-09-15T19:20:31.365881Z)
- `IMBALNGC|TOTAL|imbalance` = **5756** (n=45, 2026-09-15T19:21:36.200871Z)
- `INDDEM|TOTAL|demand` = **-11911** (n=45, 2026-09-15T19:21:36.200871Z)
- `INDGEN|TOTAL|generation` = **24877** (n=45, 2026-09-15T19:21:36.200871Z)
- `MELNGC|TOTAL|margin` = **35644** (n=45, 2026-09-15T19:19:43.345950Z)
- `NDF|TOTAL|demand` = **18621** (n=46, 2026-09-15T19:17:40.131677Z)
- `TSDF|TOTAL|demand` = **19121** (n=46, 2026-09-15T19:17:40.131677Z)
- `WINDFOR|TOTAL|generation` = **17795** (n=7, 2026-09-15T16:30:51.506988Z)

## Latest publication events

- `2026-09-15T19:22:08.231762Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:21:45Z`
- `2026-09-15T19:21:36.200871Z` — **INDGEN**: 1170 rows; marker `2026-09-15T19:17:00Z`
- `2026-09-15T19:21:36.200871Z` — **INDDEM**: 1170 rows; marker `2026-09-15T19:17:00Z`
- `2026-09-15T19:21:36.200871Z` — **IMBALNGC**: 1170 rows; marker `2026-09-15T19:17:00Z`
- `2026-09-15T19:20:31.365881Z` — **FUELINST**: 80 rows; marker `2026-09-15T19:20:00Z`
- `2026-09-15T19:20:31.365881Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:19:45Z`
- `2026-09-15T19:19:43.345950Z` — **MELNGC**: 1170 rows; marker `2026-09-15T19:17:00Z`
- `2026-09-15T19:18:11.847686Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:17:45Z`
- `2026-09-15T19:17:40.131677Z` — **TSDF**: 1170 rows; marker `2026-09-15T19:17:00Z`
- `2026-09-15T19:17:40.131677Z` — **NDF**: 65 rows; marker `2026-09-15T19:17:00Z`
- `2026-09-15T19:16:19.808722Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:15:45Z`
- `2026-09-15T19:15:47.502269Z` — **FUELINST**: 80 rows; marker `2026-09-15T19:15:00Z`
- `2026-09-15T19:14:16.785361Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:13:45Z`
- `2026-09-15T19:12:08.830895Z` — **MID**: 0 rows; marker `2026-09-15T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T19:12:08.830895Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:11:45Z`
