# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T13:57:37.196377Z`  
Current process started UTC: `2026-09-21T13:53:36.984740Z`  
1-second metadata polls in this process: **227**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3503, delta=-10, z=4.07 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1854, 2026-09-21T13:55:45.088006Z)
- `FUELINST|fuelType=OTHER|generation` = **448** (n=1854, 2026-09-21T13:55:45.088006Z)
- `FUELINST|fuelType=PS|generation` = **219** (n=1854, 2026-09-21T13:55:45.088006Z)
- `FUELINST|fuelType=WIND|generation` = **4268** (n=1854, 2026-09-21T13:55:45.088006Z)
- `IMBALNGC|TOTAL|imbalance` = **-3238** (n=305, 2026-09-21T13:53:53.274334Z)
- `INDDEM|TOTAL|demand` = **-12297** (n=305, 2026-09-21T13:53:36.984750Z)
- `INDGEN|TOTAL|generation` = **18266** (n=305, 2026-09-21T13:53:36.984750Z)
- `MELNGC|TOTAL|margin` = **36267** (n=305, 2026-09-21T13:50:26.201478Z)
- `MID|dataProvider=APXMIDP|price` = **148.28** (n=45, 2026-09-21T13:42:11.242539Z)
- `MID|dataProvider=APXMIDP|volume` = **3520.7** (n=45, 2026-09-21T13:42:11.242539Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=88, 2026-09-21T13:42:11.242539Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=88, 2026-09-21T13:42:11.242539Z)
- `NDF|TOTAL|demand` = **21004** (n=312, 2026-09-21T13:48:21.083702Z)
- `TSDF|TOTAL|demand` = **21504** (n=312, 2026-09-21T13:48:21.083702Z)
- `WINDFOR|TOTAL|generation` = **8616** (n=53, 2026-09-21T12:30:32.614458Z)

## Latest publication events

- `2026-09-21T13:56:16.809499Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:55:45Z`
- `2026-09-21T13:55:45.088006Z` — **FUELINST**: 80 rows; marker `2026-09-21T13:55:00Z`
- `2026-09-21T13:54:25.319112Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:53:45Z`
- `2026-09-21T13:53:53.274334Z` — **IMBALNGC**: 1368 rows; marker `2026-09-21T13:47:00Z`
- `2026-09-21T13:53:36.984750Z` — **INDGEN**: 1368 rows; marker `2026-09-21T13:47:00Z`
- `2026-09-21T13:53:36.984750Z` — **INDDEM**: 1368 rows; marker `2026-09-21T13:47:00Z`
- `2026-09-21T13:52:18.169726Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:51:45Z`
- `2026-09-21T13:50:41.919590Z` — **FUELINST**: 80 rows; marker `2026-09-21T13:50:00Z`
- `2026-09-21T13:50:26.201478Z` — **MELNGC**: 1368 rows; marker `2026-09-21T13:47:00Z`
- `2026-09-21T13:50:26.201478Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:49:45Z`
- `2026-09-21T13:48:21.083702Z` — **TSDF**: 1368 rows; marker `2026-09-21T13:47:00Z`
- `2026-09-21T13:48:21.083702Z` — **NDF**: 76 rows; marker `2026-09-21T13:47:00Z`
- `2026-09-21T13:48:21.083702Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:47:45Z`
- `2026-09-21T13:46:28.474311Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:45:45Z`
- `2026-09-21T13:45:40.690336Z` — **FUELINST**: 80 rows; marker `2026-09-21T13:45:00Z`
