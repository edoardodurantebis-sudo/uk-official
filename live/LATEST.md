# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T05:46:30.125944Z`  
Current process started UTC: `2026-09-21T05:42:30.662579Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3465, delta=-3, z=9.07 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=826, delta=3, z=4.31 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3468, delta=8, z=9.50 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=823, delta=-1, z=4.30 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3460, delta=5, z=9.18 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=824, delta=0, z=4.34 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3444, delta=44, z=9.38 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=813, delta=378, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3455, delta=6, z=9.04 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=824, delta=1, z=4.36 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3449, delta=1, z=8.81 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=823, delta=2, z=4.38 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3448, delta=-2, z=8.93 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=821, delta=5, z=4.38 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3450, delta=16, z=9.31 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1759, 2026-09-21T05:45:26.747506Z)
- `FUELINST|fuelType=OTHER|generation` = **1835** (n=1759, 2026-09-21T05:45:26.747506Z)
- `FUELINST|fuelType=PS|generation` = **-128** (n=1759, 2026-09-21T05:45:26.747506Z)
- `FUELINST|fuelType=WIND|generation` = **3544** (n=1759, 2026-09-21T05:45:26.747506Z)
- `IMBALNGC|TOTAL|imbalance` = **-4015** (n=289, 2026-09-21T05:19:58.754386Z)
- `INDDEM|TOTAL|demand` = **-11743** (n=289, 2026-09-21T05:19:58.754386Z)
- `INDGEN|TOTAL|generation` = **16595** (n=289, 2026-09-21T05:19:58.754386Z)
- `MELNGC|TOTAL|margin` = **37533** (n=289, 2026-09-21T05:18:36.808843Z)
- `MID|dataProvider=APXMIDP|price` = **181.97** (n=29, 2026-09-21T05:42:30.662588Z)
- `MID|dataProvider=APXMIDP|volume` = **3042.6** (n=29, 2026-09-21T05:42:30.662588Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=58, 2026-09-21T05:42:30.662588Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=58, 2026-09-21T05:42:30.662588Z)
- `NDF|TOTAL|demand` = **20110** (n=295, 2026-09-21T05:17:16.844589Z)
- `TSDF|TOTAL|demand` = **20610** (n=295, 2026-09-21T05:17:16.844589Z)
- `WINDFOR|TOTAL|generation` = **8794** (n=50, 2026-09-21T05:30:44.368414Z)

## Latest publication events

- `2026-09-21T05:46:15.608198Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:45:45Z`
- `2026-09-21T05:45:26.747506Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:45:00Z`
- `2026-09-21T05:44:23.030206Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:43:45Z`
- `2026-09-21T05:42:30.662588Z` — **MID**: 2 rows; marker `2026-09-21T05:42:03Z`
- `2026-09-21T05:42:30.662588Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:41:45Z`
- `2026-09-21T05:40:25.597709Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:40:00Z`
- `2026-09-21T05:40:10.191805Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:39:45Z`
- `2026-09-21T05:38:18.554700Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:37:45Z`
- `2026-09-21T05:36:26.027530Z` — **MID**: 1 rows; marker `2026-09-21T05:35:00Z`
- `2026-09-21T05:36:10.393869Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:35:45Z`
- `2026-09-21T05:35:38.336116Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:35:00Z`
- `2026-09-21T05:34:18.789868Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:33:45Z`
- `2026-09-21T05:32:04.656778Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:31:45Z`
- `2026-09-21T05:30:44.368414Z` — **WINDFOR**: 73 rows; marker `2026-09-21T05:30:00Z`
- `2026-09-21T05:30:28.571701Z` — **FUELHH**: 20 rows; marker `2026-09-21T05:30:00Z`
