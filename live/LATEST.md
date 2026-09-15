# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T19:36:02.893448Z`  
Current process started UTC: `2026-09-15T19:32:02.526632Z`  
1-second metadata polls in this process: **233**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=-1, z=3.74 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.30 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=54, delta=-1, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.76 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=17, z=8.89 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.93 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.39 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.98 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=7.77 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-291** (n=272, 2026-09-15T19:35:30.347449Z)
- `FUELINST|fuelType=NPSHYD|generation` = **495** (n=272, 2026-09-15T19:35:30.347449Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3323** (n=272, 2026-09-15T19:35:30.347449Z)
- `FUELINST|fuelType=OCGT|generation` = **53** (n=272, 2026-09-15T19:35:30.347449Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=272, 2026-09-15T19:35:30.347449Z)
- `FUELINST|fuelType=OTHER|generation` = **1254** (n=272, 2026-09-15T19:35:30.347449Z)
- `FUELINST|fuelType=PS|generation` = **423** (n=272, 2026-09-15T19:35:30.347449Z)
- `FUELINST|fuelType=WIND|generation` = **10510** (n=272, 2026-09-15T19:35:30.347449Z)
- `IMBALNGC|TOTAL|imbalance` = **5756** (n=45, 2026-09-15T19:21:36.200871Z)
- `INDDEM|TOTAL|demand` = **-11911** (n=45, 2026-09-15T19:21:36.200871Z)
- `INDGEN|TOTAL|generation` = **24877** (n=45, 2026-09-15T19:21:36.200871Z)
- `MELNGC|TOTAL|margin` = **35644** (n=45, 2026-09-15T19:19:43.345950Z)
- `NDF|TOTAL|demand` = **18621** (n=46, 2026-09-15T19:17:40.131677Z)
- `TSDF|TOTAL|demand` = **19121** (n=46, 2026-09-15T19:17:40.131677Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T19:35:30.347449Z` — **FUELINST**: 80 rows; marker `2026-09-15T19:35:00Z`
- `2026-09-15T19:34:11.117932Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:33:45Z`
- `2026-09-15T19:32:18.528618Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:31:45Z`
- `2026-09-15T19:30:46.768983Z` — **WINDFOR**: 73 rows; marker `2026-09-15T19:30:00Z`
- `2026-09-15T19:30:46.768983Z` — **FUELHH**: 20 rows; marker `2026-09-15T19:30:00Z`
- `2026-09-15T19:30:30.864298Z` — **FUELINST**: 80 rows; marker `2026-09-15T19:30:00Z`
- `2026-09-15T19:30:30.864298Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:29:45Z`
- `2026-09-15T19:28:22.648194Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:27:45Z`
- `2026-09-15T19:26:20.033320Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:25:45Z`
- `2026-09-15T19:25:31.693361Z` — **FUELINST**: 80 rows; marker `2026-09-15T19:25:00Z`
- `2026-09-15T19:24:11.761880Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:23:45Z`
- `2026-09-15T19:22:08.231762Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:21:45Z`
- `2026-09-15T19:21:36.200871Z` — **INDGEN**: 1170 rows; marker `2026-09-15T19:17:00Z`
- `2026-09-15T19:21:36.200871Z` — **INDDEM**: 1170 rows; marker `2026-09-15T19:17:00Z`
- `2026-09-15T19:21:36.200871Z` — **IMBALNGC**: 1170 rows; marker `2026-09-15T19:17:00Z`
