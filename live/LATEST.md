# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T07:14:36.992946Z`  
Current process started UTC: `2026-09-22T07:10:36.887932Z`  
1-second metadata polls in this process: **239**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2061, 2026-09-22T07:10:24.438271Z)
- `FUELINST|fuelType=OTHER|generation` = **963** (n=2061, 2026-09-22T07:10:24.438271Z)
- `FUELINST|fuelType=PS|generation` = **-172** (n=2061, 2026-09-22T07:10:24.438271Z)
- `FUELINST|fuelType=WIND|generation` = **3502** (n=2061, 2026-09-22T07:10:24.438271Z)
- `IMBALNGC|TOTAL|imbalance` = **-3140** (n=339, 2026-09-22T06:50:20.460352Z)
- `INDDEM|TOTAL|demand` = **-12450** (n=339, 2026-09-22T06:50:04.675753Z)
- `INDGEN|TOTAL|generation` = **18321** (n=339, 2026-09-22T06:50:04.675753Z)
- `MELNGC|TOTAL|margin` = **37797** (n=339, 2026-09-22T06:49:04.524075Z)
- `MID|dataProvider=APXMIDP|price` = **150.92** (n=80, 2026-09-22T07:12:15.900395Z)
- `MID|dataProvider=APXMIDP|volume` = **2883.3** (n=80, 2026-09-22T07:12:15.900395Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=158, 2026-09-22T07:12:15.900395Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=158, 2026-09-22T07:12:15.900395Z)
- `NDF|TOTAL|demand` = **20959** (n=346, 2026-09-22T06:47:28.586481Z)
- `TSDF|TOTAL|demand` = **21461** (n=346, 2026-09-22T06:47:28.586481Z)
- `WINDFOR|TOTAL|generation` = **12340** (n=58, 2026-09-22T05:30:40.954997Z)

## Latest publication events

- `2026-09-22T07:14:07.849999Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:13:45Z`
- `2026-09-22T07:12:15.900395Z` — **MID**: 2 rows; marker `2026-09-22T07:12:03Z`
- `2026-09-22T07:12:15.900395Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:11:45Z`
- `2026-09-22T07:10:24.438271Z` — **FUELINST**: 80 rows; marker `2026-09-22T07:10:00Z`
- `2026-09-22T07:10:08.350675Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:09:45Z`
- `2026-09-22T07:08:16.432842Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:07:45Z`
- `2026-09-22T07:06:24.611426Z` — **MID**: 1 rows; marker `2026-09-22T07:05:00Z`
- `2026-09-22T07:06:24.611426Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:05:45Z`
- `2026-09-22T07:05:59.924922Z` — **FUELINST**: 80 rows; marker `2026-09-22T07:05:00Z`
- `2026-09-22T07:04:06.996918Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:03:45Z`
- `2026-09-22T07:02:12.807841Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:01:45Z`
- `2026-09-22T07:00:39.015165Z` — **FUELINST**: 80 rows; marker `2026-09-22T07:00:00Z`
- `2026-09-22T07:00:22.662308Z` — **FUELHH**: 20 rows; marker `2026-09-22T07:00:00Z`
- `2026-09-22T07:00:06.498864Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:59:45Z`
- `2026-09-22T06:58:13.979529Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:57:45Z`
