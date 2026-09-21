# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T14:48:20.465126Z`  
Current process started UTC: `2026-09-21T14:44:20.416362Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3497, delta=7, z=3.76 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3490, delta=1, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3489, delta=-7, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-12, z=3.83 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-2, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3498, delta=3, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3495, delta=3, z=3.79 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3492, delta=-4, z=3.73 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-2, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3498, delta=-1, z=3.91 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3508, delta=1, z=4.24 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=-4, z=3.95 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3503, delta=-10, z=4.07 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3513, delta=-2, z=4.34 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3515, delta=8, z=4.41 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1864, 2026-09-21T14:45:41.800763Z)
- `FUELINST|fuelType=OTHER|generation` = **465** (n=1864, 2026-09-21T14:45:41.800763Z)
- `FUELINST|fuelType=PS|generation` = **129** (n=1864, 2026-09-21T14:45:41.800763Z)
- `FUELINST|fuelType=WIND|generation` = **3709** (n=1864, 2026-09-21T14:45:41.800763Z)
- `IMBALNGC|TOTAL|imbalance` = **-3206** (n=306, 2026-09-21T14:23:32.193365Z)
- `INDDEM|TOTAL|demand` = **-12297** (n=306, 2026-09-21T14:23:16.787018Z)
- `INDGEN|TOTAL|generation` = **18298** (n=306, 2026-09-21T14:23:16.787018Z)
- `MELNGC|TOTAL|margin` = **36245** (n=306, 2026-09-21T14:20:21.450774Z)
- `MID|dataProvider=APXMIDP|price` = **145.05** (n=47, 2026-09-21T14:42:14.482814Z)
- `MID|dataProvider=APXMIDP|volume` = **2842.6** (n=47, 2026-09-21T14:42:14.482814Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=92, 2026-09-21T14:42:14.482814Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=92, 2026-09-21T14:42:14.482814Z)
- `NDF|TOTAL|demand` = **21004** (n=313, 2026-09-21T14:18:04.888787Z)
- `TSDF|TOTAL|demand` = **21504** (n=313, 2026-09-21T14:18:04.888787Z)
- `WINDFOR|TOTAL|generation` = **8616** (n=53, 2026-09-21T12:30:32.614458Z)

## Latest publication events

- `2026-09-21T14:46:14.322300Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:45:45Z`
- `2026-09-21T14:45:41.800763Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:45:00Z`
- `2026-09-21T14:44:22.416616Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:43:45Z`
- `2026-09-21T14:42:14.482814Z` — **MID**: 2 rows; marker `2026-09-21T14:42:04Z`
- `2026-09-21T14:42:14.482814Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:41:45Z`
- `2026-09-21T14:40:38.469200Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:40:00Z`
- `2026-09-21T14:40:23.092317Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:39:45Z`
- `2026-09-21T14:38:20.480761Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:37:45Z`
- `2026-09-21T14:37:32.424756Z` — **MID**: 1 rows; marker `2026-09-21T14:35:00Z`
- `2026-09-21T14:36:12.293438Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:35:45Z`
- `2026-09-21T14:35:40.339120Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:35:00Z`
- `2026-09-21T14:34:20.795719Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:33:45Z`
- `2026-09-21T14:32:13.137295Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:31:45Z`
- `2026-09-21T14:30:25.955293Z` — **FUELHH**: 20 rows; marker `2026-09-21T14:30:00Z`
- `2026-09-21T14:30:25.955293Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:30:00Z`
