# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T23:43:49.294445Z`  
Current process started UTC: `2026-09-21T23:39:49.789363Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3652, delta=3, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=-4, z=4.64 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3647, delta=5, z=4.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=3, z=4.73 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=5, z=4.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=2, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3643, delta=-2, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=0, z=4.72 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=-2, z=4.75 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3642, delta=4, z=4.87 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3647, delta=5, z=4.81 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3642, delta=-2, z=4.75 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3644, delta=-2, z=4.82 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3646, delta=6, z=4.88 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3640, delta=5, z=4.81 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1971, 2026-09-21T23:40:38.021230Z)
- `FUELINST|fuelType=OTHER|generation` = **205** (n=1971, 2026-09-21T23:40:38.021230Z)
- `FUELINST|fuelType=PS|generation` = **-283** (n=1971, 2026-09-21T23:40:38.021230Z)
- `FUELINST|fuelType=WIND|generation` = **3617** (n=1971, 2026-09-21T23:40:38.021230Z)
- `IMBALNGC|TOTAL|imbalance` = **-2016** (n=324, 2026-09-21T23:21:49.574733Z)
- `INDDEM|TOTAL|demand` = **-12381** (n=324, 2026-09-21T23:21:15.927702Z)
- `INDGEN|TOTAL|generation` = **19443** (n=324, 2026-09-21T23:21:15.927702Z)
- `MELNGC|TOTAL|margin` = **36167** (n=324, 2026-09-21T23:19:39.547553Z)
- `MID|dataProvider=APXMIDP|price` = **139.68** (n=65, 2026-09-21T23:42:13.807294Z)
- `MID|dataProvider=APXMIDP|volume` = **1760.8** (n=65, 2026-09-21T23:42:13.807294Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=128, 2026-09-21T23:42:13.807294Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=128, 2026-09-21T23:42:13.807294Z)
- `NDF|TOTAL|demand` = **20959** (n=331, 2026-09-21T23:17:21.026219Z)
- `TSDF|TOTAL|demand` = **21459** (n=331, 2026-09-21T23:17:38.428444Z)
- `WINDFOR|TOTAL|generation` = **9503** (n=56, 2026-09-21T23:30:37.821418Z)

## Latest publication events

- `2026-09-21T23:42:13.807294Z` — **MID**: 2 rows; marker `2026-09-21T23:42:03Z`
- `2026-09-21T23:42:13.807294Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:41:45Z`
- `2026-09-21T23:40:38.021230Z` — **FUELINST**: 80 rows; marker `2026-09-21T23:40:00Z`
- `2026-09-21T23:40:21.791788Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:39:45Z`
- `2026-09-21T23:38:18.552290Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:37:45Z`
- `2026-09-21T23:37:14.323987Z` — **MID**: 1 rows; marker `2026-09-21T23:35:00Z`
- `2026-09-21T23:36:26.415080Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:35:45Z`
- `2026-09-21T23:35:38.064681Z` — **FUELINST**: 80 rows; marker `2026-09-21T23:35:00Z`
- `2026-09-21T23:34:21.451665Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:33:45Z`
- `2026-09-21T23:32:11.450519Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:31:45Z`
- `2026-09-21T23:30:37.821418Z` — **WINDFOR**: 73 rows; marker `2026-09-21T23:30:00Z`
- `2026-09-21T23:30:37.821418Z` — **FUELHH**: 20 rows; marker `2026-09-21T23:30:00Z`
- `2026-09-21T23:30:37.821418Z` — **FUELINST**: 80 rows; marker `2026-09-21T23:30:00Z`
- `2026-09-21T23:30:21.635920Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:29:45Z`
- `2026-09-21T23:28:13.154583Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:27:45Z`
