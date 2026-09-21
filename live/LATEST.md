# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T14:35:41.381907Z`  
Current process started UTC: `2026-09-21T14:31:41.132402Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3507, delta=-3, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3510, delta=2, z=4.33 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1862, 2026-09-21T14:35:40.339120Z)
- `FUELINST|fuelType=OTHER|generation` = **446** (n=1862, 2026-09-21T14:35:40.339120Z)
- `FUELINST|fuelType=PS|generation` = **65** (n=1862, 2026-09-21T14:35:40.339120Z)
- `FUELINST|fuelType=WIND|generation` = **4204** (n=1862, 2026-09-21T14:35:40.339120Z)
- `IMBALNGC|TOTAL|imbalance` = **-3206** (n=306, 2026-09-21T14:23:32.193365Z)
- `INDDEM|TOTAL|demand` = **-12297** (n=306, 2026-09-21T14:23:16.787018Z)
- `INDGEN|TOTAL|generation` = **18298** (n=306, 2026-09-21T14:23:16.787018Z)
- `MELNGC|TOTAL|margin` = **36245** (n=306, 2026-09-21T14:20:21.450774Z)
- `MID|dataProvider=APXMIDP|price` = **145.73** (n=46, 2026-09-21T14:12:12.402077Z)
- `MID|dataProvider=APXMIDP|volume` = **3192.1** (n=46, 2026-09-21T14:12:12.402077Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=90, 2026-09-21T14:12:12.402077Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=90, 2026-09-21T14:12:12.402077Z)
- `NDF|TOTAL|demand` = **21004** (n=313, 2026-09-21T14:18:04.888787Z)
- `TSDF|TOTAL|demand` = **21504** (n=313, 2026-09-21T14:18:04.888787Z)
- `WINDFOR|TOTAL|generation` = **8616** (n=53, 2026-09-21T12:30:32.614458Z)

## Latest publication events

- `2026-09-21T14:35:40.339120Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:35:00Z`
- `2026-09-21T14:34:20.795719Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:33:45Z`
- `2026-09-21T14:32:13.137295Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:31:45Z`
- `2026-09-21T14:30:25.955293Z` — **FUELHH**: 20 rows; marker `2026-09-21T14:30:00Z`
- `2026-09-21T14:30:25.955293Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:30:00Z`
- `2026-09-21T14:30:08.905708Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:29:45Z`
- `2026-09-21T14:28:16.602532Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:27:45Z`
- `2026-09-21T14:26:13.174653Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:25:45Z`
- `2026-09-21T14:25:25.600545Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:25:00Z`
- `2026-09-21T14:24:21.987172Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:23:45Z`
- `2026-09-21T14:23:32.193365Z` — **IMBALNGC**: 1350 rows; marker `2026-09-21T14:17:00Z`
- `2026-09-21T14:23:16.787018Z` — **INDGEN**: 1350 rows; marker `2026-09-21T14:17:00Z`
- `2026-09-21T14:23:16.787018Z` — **INDDEM**: 1350 rows; marker `2026-09-21T14:17:00Z`
- `2026-09-21T14:22:12.494992Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:21:45Z`
- `2026-09-21T14:20:37.139527Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:20:00Z`
