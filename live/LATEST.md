# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T03:37:48.992513Z`  
Current process started UTC: `2026-09-22T03:33:48.786045Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3657, delta=7, z=3.81 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3655, delta=1, z=3.88 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=2, z=3.73 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-9, z=3.72 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-3, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=-1, z=3.91 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=6, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3655, delta=1, z=3.87 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3654, delta=1, z=3.96 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-2, z=3.87 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=2, z=3.92 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=1, z=3.91 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=0, z=3.91 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=0, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-7, z=3.94 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2018, 2026-09-22T03:35:24.830493Z)
- `FUELINST|fuelType=OTHER|generation` = **384** (n=2018, 2026-09-22T03:35:24.830493Z)
- `FUELINST|fuelType=PS|generation` = **-408** (n=2018, 2026-09-22T03:35:24.830493Z)
- `FUELINST|fuelType=WIND|generation` = **3855** (n=2018, 2026-09-22T03:35:24.830493Z)
- `IMBALNGC|TOTAL|imbalance` = **-2644** (n=332, 2026-09-22T03:20:54.413938Z)
- `INDDEM|TOTAL|demand` = **-12500** (n=332, 2026-09-22T03:20:38.928388Z)
- `INDGEN|TOTAL|generation` = **18815** (n=332, 2026-09-22T03:20:38.928388Z)
- `MELNGC|TOTAL|margin` = **37794** (n=332, 2026-09-22T03:19:41.062165Z)
- `MID|dataProvider=APXMIDP|price` = **136.31** (n=72, 2026-09-22T03:12:15.087057Z)
- `MID|dataProvider=APXMIDP|volume` = **1871.5** (n=72, 2026-09-22T03:12:15.087057Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=143, 2026-09-22T03:36:29.293115Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=143, 2026-09-22T03:36:29.293115Z)
- `NDF|TOTAL|demand` = **20959** (n=339, 2026-09-22T03:17:16.111810Z)
- `TSDF|TOTAL|demand` = **21459** (n=339, 2026-09-22T03:17:32.668673Z)
- `WINDFOR|TOTAL|generation` = **11644** (n=57, 2026-09-22T03:30:45.244161Z)

## Latest publication events

- `2026-09-22T03:36:29.293115Z` — **MID**: 1 rows; marker `2026-09-22T03:35:00Z`
- `2026-09-22T03:36:12.200575Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:35:45Z`
- `2026-09-22T03:35:24.830493Z` — **FUELINST**: 80 rows; marker `2026-09-22T03:35:00Z`
- `2026-09-22T03:34:20.789804Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:33:45Z`
- `2026-09-22T03:32:21.119187Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:31:45Z`
- `2026-09-22T03:30:45.244161Z` — **WINDFOR**: 73 rows; marker `2026-09-22T03:30:00Z`
- `2026-09-22T03:30:45.244161Z` — **FUELHH**: 20 rows; marker `2026-09-22T03:30:00Z`
- `2026-09-22T03:30:28.972350Z` — **FUELINST**: 80 rows; marker `2026-09-22T03:30:00Z`
- `2026-09-22T03:30:13.052317Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:29:45Z`
- `2026-09-22T03:28:05.489176Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:27:45Z`
- `2026-09-22T03:26:13.960258Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:25:45Z`
- `2026-09-22T03:25:25.602441Z` — **FUELINST**: 80 rows; marker `2026-09-22T03:25:00Z`
- `2026-09-22T03:24:08.438919Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:23:45Z`
- `2026-09-22T03:22:16.255242Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:21:45Z`
- `2026-09-22T03:20:54.413938Z` — **IMBALNGC**: 882 rows; marker `2026-09-22T03:17:00Z`
