# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T16:00:35.793081Z`  
Current process started UTC: `2026-09-21T15:56:35.697915Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3502, delta=-4, z=3.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3506, delta=0, z=3.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3506, delta=2, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=5, z=3.75 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=5, z=3.65 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3494, delta=1, z=3.55 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3495, delta=2, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3493, delta=-1, z=3.54 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3494, delta=-1, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3495, delta=0, z=3.62 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3495, delta=-4, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=6, z=3.74 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3493, delta=4, z=3.61 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3493, delta=-3, z=3.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3489, delta=-6, z=3.53 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1879, 2026-09-21T16:00:22.149156Z)
- `FUELINST|fuelType=OTHER|generation` = **804** (n=1879, 2026-09-21T16:00:22.149156Z)
- `FUELINST|fuelType=PS|generation` = **-88** (n=1879, 2026-09-21T16:00:22.149156Z)
- `FUELINST|fuelType=WIND|generation` = **3354** (n=1879, 2026-09-21T16:00:22.149156Z)
- `IMBALNGC|TOTAL|imbalance` = **-3079** (n=309, 2026-09-21T15:53:41.642372Z)
- `INDDEM|TOTAL|demand` = **-12275** (n=309, 2026-09-21T15:53:25.333103Z)
- `INDGEN|TOTAL|generation` = **18380** (n=309, 2026-09-21T15:53:25.333103Z)
- `MELNGC|TOTAL|margin` = **36206** (n=309, 2026-09-21T15:51:00.108038Z)
- `MID|dataProvider=APXMIDP|price` = **151.77** (n=49, 2026-09-21T15:42:16.502521Z)
- `MID|dataProvider=APXMIDP|volume` = **3803.1** (n=49, 2026-09-21T15:42:16.502521Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=96, 2026-09-21T15:42:16.502521Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=96, 2026-09-21T15:42:16.502521Z)
- `NDF|TOTAL|demand` = **20959** (n=316, 2026-09-21T15:48:05.319974Z)
- `TSDF|TOTAL|demand` = **21459** (n=316, 2026-09-21T15:48:05.319974Z)
- `WINDFOR|TOTAL|generation` = **8616** (n=53, 2026-09-21T12:30:32.614458Z)

## Latest publication events

- `2026-09-21T16:00:22.149156Z` — **FUELINST**: 80 rows; marker `2026-09-21T16:00:00Z`
- `2026-09-21T16:00:22.149156Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:59:45Z`
- `2026-09-21T15:58:11.979724Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:57:45Z`
- `2026-09-21T15:56:07.464847Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:55:45Z`
- `2026-09-21T15:55:36.040285Z` — **FUELINST**: 80 rows; marker `2026-09-21T15:55:00Z`
- `2026-09-21T15:53:59.465495Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:53:45Z`
- `2026-09-21T15:53:41.642372Z` — **IMBALNGC**: 1296 rows; marker `2026-09-21T15:47:00Z`
- `2026-09-21T15:53:25.333103Z` — **INDGEN**: 1296 rows; marker `2026-09-21T15:47:00Z`
- `2026-09-21T15:53:25.333103Z` — **INDDEM**: 1296 rows; marker `2026-09-21T15:47:00Z`
- `2026-09-21T15:52:04.357588Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:51:45Z`
- `2026-09-21T15:51:00.108038Z` — **MELNGC**: 1296 rows; marker `2026-09-21T15:47:00Z`
- `2026-09-21T15:50:44.475127Z` — **FUELINST**: 80 rows; marker `2026-09-21T15:50:00Z`
- `2026-09-21T15:50:28.952561Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:49:45Z`
- `2026-09-21T15:48:21.455126Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:47:45Z`
- `2026-09-21T15:48:05.319974Z` — **TSDF**: 1296 rows; marker `2026-09-21T15:47:00Z`
