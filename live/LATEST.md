# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T14:27:16.087385Z`  
Current process started UTC: `2026-09-21T14:23:15.786881Z`  
1-second metadata polls in this process: **232**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3507, delta=0, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3508, delta=4, z=4.30 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=0, z=4.23 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1860, 2026-09-21T14:25:25.600545Z)
- `FUELINST|fuelType=OTHER|generation` = **467** (n=1860, 2026-09-21T14:25:25.600545Z)
- `FUELINST|fuelType=PS|generation` = **-6** (n=1860, 2026-09-21T14:25:25.600545Z)
- `FUELINST|fuelType=WIND|generation` = **4351** (n=1860, 2026-09-21T14:25:25.600545Z)
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

- `2026-09-21T14:26:13.174653Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:25:45Z`
- `2026-09-21T14:25:25.600545Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:25:00Z`
- `2026-09-21T14:24:21.987172Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:23:45Z`
- `2026-09-21T14:23:32.193365Z` — **IMBALNGC**: 1350 rows; marker `2026-09-21T14:17:00Z`
- `2026-09-21T14:23:16.787018Z` — **INDGEN**: 1350 rows; marker `2026-09-21T14:17:00Z`
- `2026-09-21T14:23:16.787018Z` — **INDDEM**: 1350 rows; marker `2026-09-21T14:17:00Z`
- `2026-09-21T14:22:12.494992Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:21:45Z`
- `2026-09-21T14:20:37.139527Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:20:00Z`
- `2026-09-21T14:20:21.450774Z` — **MELNGC**: 1350 rows; marker `2026-09-21T14:17:00Z`
- `2026-09-21T14:20:21.450774Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:19:45Z`
- `2026-09-21T14:18:20.466291Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:17:45Z`
- `2026-09-21T14:18:04.888787Z` — **TSDF**: 1350 rows; marker `2026-09-21T14:17:00Z`
- `2026-09-21T14:18:04.888787Z` — **NDF**: 75 rows; marker `2026-09-21T14:17:00Z`
- `2026-09-21T14:16:13.014839Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:15:45Z`
- `2026-09-21T14:15:24.690272Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:15:00Z`
