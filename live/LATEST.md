# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T09:59:26.074983Z`  
Current process started UTC: `2026-09-22T09:55:25.760790Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3136, delta=-128, z=3.61 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2094, 2026-09-22T09:55:25.760799Z)
- `FUELINST|fuelType=OTHER|generation` = **488** (n=2094, 2026-09-22T09:55:25.760799Z)
- `FUELINST|fuelType=PS|generation` = **-170** (n=2094, 2026-09-22T09:55:25.760799Z)
- `FUELINST|fuelType=WIND|generation` = **3775** (n=2094, 2026-09-22T09:55:25.760799Z)
- `IMBALNGC|TOTAL|imbalance` = **3833** (n=344, 2026-09-22T09:49:20.892309Z)
- `INDDEM|TOTAL|demand` = **-13095** (n=344, 2026-09-22T09:49:20.892309Z)
- `INDGEN|TOTAL|generation` = **24901** (n=344, 2026-09-22T09:49:20.892309Z)
- `MELNGC|TOTAL|margin` = **40269** (n=344, 2026-09-22T09:48:48.787526Z)
- `MID|dataProvider=APXMIDP|price` = **129.11** (n=85, 2026-09-22T09:42:13.470430Z)
- `MID|dataProvider=APXMIDP|volume` = **3364.7** (n=85, 2026-09-22T09:42:13.470430Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=168, 2026-09-22T09:42:13.470430Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=168, 2026-09-22T09:42:13.470430Z)
- `NDF|TOTAL|demand` = **20320** (n=352, 2026-09-22T09:46:55.536738Z)
- `TSDF|TOTAL|demand` = **21068** (n=352, 2026-09-22T09:46:55.536738Z)
- `WINDFOR|TOTAL|generation` = **12393** (n=59, 2026-09-22T08:31:02.929426Z)

## Latest publication events

- `2026-09-22T09:58:20.920484Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:57:45Z`
- `2026-09-22T09:56:13.457200Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:55:45Z`
- `2026-09-22T09:55:25.760799Z` — **FUELINST**: 80 rows; marker `2026-09-22T09:55:00Z`
- `2026-09-22T09:54:08.986259Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:53:45Z`
- `2026-09-22T09:52:16.586228Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:51:45Z`
- `2026-09-22T09:50:24.979326Z` — **FUELINST**: 80 rows; marker `2026-09-22T09:50:00Z`
- `2026-09-22T09:50:08.798093Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:49:45Z`
- `2026-09-22T09:49:20.892309Z` — **INDGEN**: 648 rows; marker `2026-09-22T09:46:00Z`
- `2026-09-22T09:49:20.892309Z` — **INDDEM**: 648 rows; marker `2026-09-22T09:46:00Z`
- `2026-09-22T09:49:20.892309Z` — **IMBALNGC**: 648 rows; marker `2026-09-22T09:46:00Z`
- `2026-09-22T09:48:48.787526Z` — **MELNGC**: 648 rows; marker `2026-09-22T09:46:00Z`
- `2026-09-22T09:48:16.271001Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:47:45Z`
- `2026-09-22T09:46:55.536738Z` — **TSDF**: 648 rows; marker `2026-09-22T09:46:00Z`
- `2026-09-22T09:46:55.536738Z` — **NDF**: 36 rows; marker `2026-09-22T09:46:00Z`
- `2026-09-22T09:46:13.639595Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:45:45Z`
