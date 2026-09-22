# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T06:53:31.264615Z`  
Current process started UTC: `2026-09-22T06:49:31.607078Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3264, delta=142, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3122, delta=169, z=3.61 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=-1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3662, delta=5, z=3.53 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3659, delta=11, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3659, delta=-2, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=1, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=-3, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3663, delta=14, z=3.65 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-2, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-5, z=3.50 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=6, z=3.58 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2057, 2026-09-22T06:50:20.460352Z)
- `FUELINST|fuelType=OTHER|generation` = **3264** (n=2057, 2026-09-22T06:50:20.460352Z)
- `FUELINST|fuelType=PS|generation` = **-54** (n=2057, 2026-09-22T06:50:20.460352Z)
- `FUELINST|fuelType=WIND|generation` = **3374** (n=2057, 2026-09-22T06:50:20.460352Z)
- `IMBALNGC|TOTAL|imbalance` = **-3140** (n=339, 2026-09-22T06:50:20.460352Z)
- `INDDEM|TOTAL|demand` = **-12450** (n=339, 2026-09-22T06:50:04.675753Z)
- `INDGEN|TOTAL|generation` = **18321** (n=339, 2026-09-22T06:50:04.675753Z)
- `MELNGC|TOTAL|margin` = **37797** (n=339, 2026-09-22T06:49:04.524075Z)
- `MID|dataProvider=APXMIDP|price` = **181.41** (n=79, 2026-09-22T06:42:11.193979Z)
- `MID|dataProvider=APXMIDP|volume` = **3231.4** (n=79, 2026-09-22T06:42:11.193979Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=156, 2026-09-22T06:42:11.193979Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=156, 2026-09-22T06:42:11.193979Z)
- `NDF|TOTAL|demand` = **20959** (n=346, 2026-09-22T06:47:28.586481Z)
- `TSDF|TOTAL|demand` = **21461** (n=346, 2026-09-22T06:47:28.586481Z)
- `WINDFOR|TOTAL|generation` = **12340** (n=58, 2026-09-22T05:30:40.954997Z)

## Latest publication events

- `2026-09-22T06:52:12.101650Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:51:45Z`
- `2026-09-22T06:50:20.460352Z` — **IMBALNGC**: 756 rows; marker `2026-09-22T06:46:00Z`
- `2026-09-22T06:50:20.460352Z` — **FUELINST**: 80 rows; marker `2026-09-22T06:50:00Z`
- `2026-09-22T06:50:04.675753Z` — **INDGEN**: 756 rows; marker `2026-09-22T06:46:00Z`
- `2026-09-22T06:50:04.675753Z` — **INDDEM**: 756 rows; marker `2026-09-22T06:46:00Z`
- `2026-09-22T06:50:04.675753Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:49:45Z`
- `2026-09-22T06:49:04.524075Z` — **MELNGC**: 756 rows; marker `2026-09-22T06:46:00Z`
- `2026-09-22T06:48:16.912011Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:47:45Z`
- `2026-09-22T06:47:28.586481Z` — **TSDF**: 756 rows; marker `2026-09-22T06:46:00Z`
- `2026-09-22T06:47:28.586481Z` — **NDF**: 42 rows; marker `2026-09-22T06:46:00Z`
- `2026-09-22T06:46:25.028312Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:45:45Z`
- `2026-09-22T06:45:37.771924Z` — **FUELINST**: 80 rows; marker `2026-09-22T06:45:00Z`
- `2026-09-22T06:44:18.128540Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:43:45Z`
- `2026-09-22T06:42:27.195977Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:41:45Z`
- `2026-09-22T06:42:11.193979Z` — **MID**: 2 rows; marker `2026-09-22T06:42:03Z`
