# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T13:53:21.918094Z`  
Current process started UTC: `2026-09-21T13:49:22.192666Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3513, delta=-2, z=4.34 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3515, delta=8, z=4.41 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3507, delta=-3, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3510, delta=2, z=4.33 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3507, delta=0, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3508, delta=4, z=4.30 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=0, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=-3, z=4.25 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3507, delta=-2, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=1, z=4.42 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3508, delta=0, z=4.42 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3507, delta=-6, z=4.49 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3508, delta=4, z=4.45 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=1, z=4.37 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3503, delta=-6, z=4.36 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1853, 2026-09-21T13:50:41.919590Z)
- `FUELINST|fuelType=OTHER|generation` = **448** (n=1853, 2026-09-21T13:50:41.919590Z)
- `FUELINST|fuelType=PS|generation` = **219** (n=1853, 2026-09-21T13:50:41.919590Z)
- `FUELINST|fuelType=WIND|generation` = **4290** (n=1853, 2026-09-21T13:50:41.919590Z)
- `IMBALNGC|TOTAL|imbalance` = **-3231** (n=304, 2026-09-21T13:23:53.188521Z)
- `INDDEM|TOTAL|demand` = **-12240** (n=304, 2026-09-21T13:23:53.188521Z)
- `INDGEN|TOTAL|generation` = **18273** (n=304, 2026-09-21T13:23:37.898078Z)
- `MELNGC|TOTAL|margin` = **36267** (n=305, 2026-09-21T13:50:26.201478Z)
- `MID|dataProvider=APXMIDP|price` = **148.28** (n=45, 2026-09-21T13:42:11.242539Z)
- `MID|dataProvider=APXMIDP|volume` = **3520.7** (n=45, 2026-09-21T13:42:11.242539Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=88, 2026-09-21T13:42:11.242539Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=88, 2026-09-21T13:42:11.242539Z)
- `NDF|TOTAL|demand` = **21004** (n=312, 2026-09-21T13:48:21.083702Z)
- `TSDF|TOTAL|demand` = **21504** (n=312, 2026-09-21T13:48:21.083702Z)
- `WINDFOR|TOTAL|generation` = **8616** (n=53, 2026-09-21T12:30:32.614458Z)

## Latest publication events

- `2026-09-21T13:52:18.169726Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:51:45Z`
- `2026-09-21T13:50:41.919590Z` — **FUELINST**: 80 rows; marker `2026-09-21T13:50:00Z`
- `2026-09-21T13:50:26.201478Z` — **MELNGC**: 1368 rows; marker `2026-09-21T13:47:00Z`
- `2026-09-21T13:50:26.201478Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:49:45Z`
- `2026-09-21T13:48:21.083702Z` — **TSDF**: 1368 rows; marker `2026-09-21T13:47:00Z`
- `2026-09-21T13:48:21.083702Z` — **NDF**: 76 rows; marker `2026-09-21T13:47:00Z`
- `2026-09-21T13:48:21.083702Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:47:45Z`
- `2026-09-21T13:46:28.474311Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:45:45Z`
- `2026-09-21T13:45:40.690336Z` — **FUELINST**: 80 rows; marker `2026-09-21T13:45:00Z`
- `2026-09-21T13:44:20.531436Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:43:45Z`
- `2026-09-21T13:42:26.539296Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:41:45Z`
- `2026-09-21T13:42:11.242539Z` — **MID**: 2 rows; marker `2026-09-21T13:42:04Z`
- `2026-09-21T13:40:51.747841Z` — **FUELINST**: 80 rows; marker `2026-09-21T13:40:00Z`
- `2026-09-21T13:40:22.277938Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:39:45Z`
- `2026-09-21T13:38:13.974663Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:37:45Z`
