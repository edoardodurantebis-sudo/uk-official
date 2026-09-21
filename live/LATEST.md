# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T15:47:50.443272Z`  
Current process started UTC: `2026-09-21T15:43:50.613361Z`  
1-second metadata polls in this process: **233**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3495, delta=-5, z=3.69 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3500, delta=3, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3497, delta=7, z=3.76 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1876, 2026-09-21T15:45:28.313646Z)
- `FUELINST|fuelType=OTHER|generation` = **974** (n=1876, 2026-09-21T15:45:28.313646Z)
- `FUELINST|fuelType=PS|generation` = **-176** (n=1876, 2026-09-21T15:45:28.313646Z)
- `FUELINST|fuelType=WIND|generation` = **3380** (n=1876, 2026-09-21T15:45:28.313646Z)
- `IMBALNGC|TOTAL|imbalance` = **-3107** (n=308, 2026-09-21T15:23:14.349075Z)
- `INDDEM|TOTAL|demand` = **-12278** (n=308, 2026-09-21T15:23:14.349075Z)
- `INDGEN|TOTAL|generation` = **18352** (n=308, 2026-09-21T15:23:14.349075Z)
- `MELNGC|TOTAL|margin` = **36257** (n=308, 2026-09-21T15:20:37.814864Z)
- `MID|dataProvider=APXMIDP|price` = **151.77** (n=49, 2026-09-21T15:42:16.502521Z)
- `MID|dataProvider=APXMIDP|volume` = **3803.1** (n=49, 2026-09-21T15:42:16.502521Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=96, 2026-09-21T15:42:16.502521Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=96, 2026-09-21T15:42:16.502521Z)
- `NDF|TOTAL|demand` = **20959** (n=315, 2026-09-21T15:18:13.811389Z)
- `TSDF|TOTAL|demand` = **21459** (n=315, 2026-09-21T15:18:13.811389Z)
- `WINDFOR|TOTAL|generation` = **8616** (n=53, 2026-09-21T12:30:32.614458Z)

## Latest publication events

- `2026-09-21T15:46:17.305373Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:45:45Z`
- `2026-09-21T15:45:28.313646Z` — **FUELINST**: 80 rows; marker `2026-09-21T15:45:00Z`
- `2026-09-21T15:44:24.617619Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:43:45Z`
- `2026-09-21T15:42:16.502521Z` — **MID**: 2 rows; marker `2026-09-21T15:42:03Z`
- `2026-09-21T15:42:16.502521Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:41:45Z`
- `2026-09-21T15:40:40.625734Z` — **FUELINST**: 80 rows; marker `2026-09-21T15:40:00Z`
- `2026-09-21T15:40:24.647972Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:39:45Z`
- `2026-09-21T15:38:33.816760Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:37:45Z`
- `2026-09-21T15:36:25.011870Z` — **MID**: 1 rows; marker `2026-09-21T15:35:00Z`
- `2026-09-21T15:36:25.011870Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:35:45Z`
- `2026-09-21T15:35:37.282275Z` — **FUELINST**: 80 rows; marker `2026-09-21T15:35:00Z`
- `2026-09-21T15:34:21.048977Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:33:45Z`
- `2026-09-21T15:32:27.819679Z` — **FREQ**: 5761 rows; marker `2026-09-21T15:31:45Z`
- `2026-09-21T15:30:50.535442Z` — **FUELHH**: 20 rows; marker `2026-09-21T15:30:00Z`
- `2026-09-21T15:30:50.535442Z` — **FUELINST**: 80 rows; marker `2026-09-21T15:30:00Z`
