# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T08:26:37.809702Z`  
Current process started UTC: `2026-09-21T08:22:37.409794Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=0, z=6.21 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=0, z=6.28 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-3, z=6.35 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=0, z=6.54 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=0, z=6.62 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3500, delta=1, z=7.30 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=791, delta=-14, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=-2, z=6.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=0, z=6.88 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=-3, z=6.98 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=3, z=7.20 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=5, z=7.18 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=793, delta=-7, z=3.54 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-2, z=7.07 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=800, delta=-4, z=3.62 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1791, 2026-09-21T08:25:33.633328Z)
- `FUELINST|fuelType=OTHER|generation` = **1412** (n=1791, 2026-09-21T08:25:33.633328Z)
- `FUELINST|fuelType=PS|generation` = **-10** (n=1791, 2026-09-21T08:25:33.633328Z)
- `FUELINST|fuelType=WIND|generation` = **4302** (n=1791, 2026-09-21T08:25:33.633328Z)
- `IMBALNGC|TOTAL|imbalance` = **-2271** (n=294, 2026-09-21T08:19:28.892313Z)
- `INDDEM|TOTAL|demand` = **-12835** (n=294, 2026-09-21T08:19:13.069003Z)
- `INDGEN|TOTAL|generation` = **18998** (n=294, 2026-09-21T08:19:28.892313Z)
- `MELNGC|TOTAL|margin` = **38252** (n=294, 2026-09-21T08:18:56.991927Z)
- `MID|dataProvider=APXMIDP|price` = **201.31** (n=34, 2026-09-21T08:12:09.816775Z)
- `MID|dataProvider=APXMIDP|volume` = **2941.7** (n=34, 2026-09-21T08:12:09.816775Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=68, 2026-09-21T08:12:09.816775Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=68, 2026-09-21T08:12:09.816775Z)
- `NDF|TOTAL|demand` = **20110** (n=301, 2026-09-21T08:17:02.430587Z)
- `TSDF|TOTAL|demand` = **21269** (n=301, 2026-09-21T08:17:02.430587Z)
- `WINDFOR|TOTAL|generation` = **8794** (n=50, 2026-09-21T05:30:44.368414Z)

## Latest publication events

- `2026-09-21T08:26:21.436535Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:25:45Z`
- `2026-09-21T08:25:33.633328Z` — **FUELINST**: 80 rows; marker `2026-09-21T08:25:00Z`
- `2026-09-21T08:24:13.422111Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:23:45Z`
- `2026-09-21T08:22:08.887308Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:21:45Z`
- `2026-09-21T08:20:32.864774Z` — **FUELINST**: 80 rows; marker `2026-09-21T08:20:00Z`
- `2026-09-21T08:20:16.785468Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:19:45Z`
- `2026-09-21T08:19:28.892313Z` — **INDGEN**: 702 rows; marker `2026-09-21T08:16:00Z`
- `2026-09-21T08:19:28.892313Z` — **IMBALNGC**: 702 rows; marker `2026-09-21T08:16:00Z`
- `2026-09-21T08:19:13.069003Z` — **INDDEM**: 702 rows; marker `2026-09-21T08:16:00Z`
- `2026-09-21T08:18:56.991927Z` — **MELNGC**: 702 rows; marker `2026-09-21T08:16:00Z`
- `2026-09-21T08:18:24.886028Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:17:45Z`
- `2026-09-21T08:17:02.430587Z` — **TSDF**: 702 rows; marker `2026-09-21T08:16:00Z`
- `2026-09-21T08:17:02.430587Z` — **NDF**: 39 rows; marker `2026-09-21T08:16:00Z`
- `2026-09-21T08:16:15.311280Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:15:45Z`
- `2026-09-21T08:15:27.870200Z` — **FUELINST**: 80 rows; marker `2026-09-21T08:15:00Z`
