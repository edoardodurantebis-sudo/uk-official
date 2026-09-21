# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T05:54:53.377690Z`  
Current process started UTC: `2026-09-21T05:50:53.736654Z`  
1-second metadata polls in this process: **195**  
HTTP/data errors in this process: **1**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3466, delta=1, z=8.93 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=829, delta=3, z=4.32 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1760, 2026-09-21T05:50:25.731576Z)
- `FUELINST|fuelType=OTHER|generation` = **2053** (n=1760, 2026-09-21T05:50:25.731576Z)
- `FUELINST|fuelType=PS|generation` = **-149** (n=1760, 2026-09-21T05:50:25.731576Z)
- `FUELINST|fuelType=WIND|generation` = **3523** (n=1760, 2026-09-21T05:50:25.731576Z)
- `IMBALNGC|TOTAL|imbalance` = **-3970** (n=290, 2026-09-21T05:50:25.731576Z)
- `INDDEM|TOTAL|demand` = **-11743** (n=290, 2026-09-21T05:50:25.731576Z)
- `INDGEN|TOTAL|generation` = **16640** (n=290, 2026-09-21T05:50:25.731576Z)
- `MELNGC|TOTAL|margin` = **37032** (n=290, 2026-09-21T05:49:21.976604Z)
- `MID|dataProvider=APXMIDP|price` = **181.97** (n=29, 2026-09-21T05:42:30.662588Z)
- `MID|dataProvider=APXMIDP|volume` = **3042.6** (n=29, 2026-09-21T05:42:30.662588Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=58, 2026-09-21T05:42:30.662588Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=58, 2026-09-21T05:42:30.662588Z)
- `NDF|TOTAL|demand` = **20110** (n=296, 2026-09-21T05:47:29.842612Z)
- `TSDF|TOTAL|demand` = **20610** (n=296, 2026-09-21T05:47:29.842612Z)
- `WINDFOR|TOTAL|generation` = **8794** (n=50, 2026-09-21T05:30:44.368414Z)

## Latest publication events

- `2026-09-21T05:54:24.428879Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:53:45Z`
- `2026-09-21T05:52:09.638213Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:51:45Z`
- `2026-09-21T05:50:25.731576Z` — **INDGEN**: 792 rows; marker `2026-09-21T05:47:00Z`
- `2026-09-21T05:50:25.731576Z` — **INDDEM**: 792 rows; marker `2026-09-21T05:47:00Z`
- `2026-09-21T05:50:25.731576Z` — **IMBALNGC**: 792 rows; marker `2026-09-21T05:47:00Z`
- `2026-09-21T05:50:25.731576Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:50:00Z`
- `2026-09-21T05:50:09.863461Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:49:45Z`
- `2026-09-21T05:49:21.976604Z` — **MELNGC**: 792 rows; marker `2026-09-21T05:47:00Z`
- `2026-09-21T05:48:17.701871Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:47:45Z`
- `2026-09-21T05:47:29.842612Z` — **TSDF**: 792 rows; marker `2026-09-21T05:47:00Z`
- `2026-09-21T05:47:29.842612Z` — **NDF**: 44 rows; marker `2026-09-21T05:47:00Z`
- `2026-09-21T05:46:15.608198Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:45:45Z`
- `2026-09-21T05:45:26.747506Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:45:00Z`
- `2026-09-21T05:44:23.030206Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:43:45Z`
- `2026-09-21T05:42:30.662588Z` — **MID**: 2 rows; marker `2026-09-21T05:42:03Z`
