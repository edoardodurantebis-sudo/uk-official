# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T06:48:19.285779Z`  
Current process started UTC: `2026-09-17T06:44:18.741956Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=0, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=17, z=4.30 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-1134, delta=10, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1114, delta=62, z=-3.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.73 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.82 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-1144, delta=-306, z=-4.09 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.87 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.92 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.98 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=-48, z=-4.03 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1128, delta=-92, z=-4.00 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1036, delta=-93, z=-3.88 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-113** (n=663, 2026-09-17T06:45:38.345079Z)
- `FUELINST|fuelType=NPSHYD|generation` = **438** (n=663, 2026-09-17T06:45:38.345079Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3307** (n=663, 2026-09-17T06:45:38.345079Z)
- `FUELINST|fuelType=OCGT|generation` = **51** (n=663, 2026-09-17T06:45:38.345079Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=663, 2026-09-17T06:45:38.345079Z)
- `FUELINST|fuelType=OTHER|generation` = **2264** (n=663, 2026-09-17T06:45:38.345079Z)
- `FUELINST|fuelType=PS|generation` = **226** (n=663, 2026-09-17T06:45:38.345079Z)
- `FUELINST|fuelType=WIND|generation` = **14010** (n=663, 2026-09-17T06:45:38.345079Z)
- `IMBALNGC|TOTAL|imbalance` = **7359** (n=110, 2026-09-17T06:20:20.000035Z)
- `INDDEM|TOTAL|demand` = **-11818** (n=110, 2026-09-17T06:19:48.949687Z)
- `INDGEN|TOTAL|generation` = **26480** (n=110, 2026-09-17T06:20:04.422650Z)
- `MELNGC|TOTAL|margin` = **35773** (n=110, 2026-09-17T06:19:01.245120Z)
- `NDF|TOTAL|demand` = **18621** (n=113, 2026-09-17T06:46:58.264612Z)
- `TSDF|TOTAL|demand` = **19121** (n=113, 2026-09-17T06:46:58.264612Z)
- `WINDFOR|TOTAL|generation` = **19265** (n=19, 2026-09-17T05:30:37.912884Z)

## Latest publication events

- `2026-09-17T06:48:17.846218Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:47:45Z`
- `2026-09-17T06:46:58.264612Z` — **TSDF**: 756 rows; marker `2026-09-17T06:46:00Z`
- `2026-09-17T06:46:58.264612Z` — **NDF**: 42 rows; marker `2026-09-17T06:46:00Z`
- `2026-09-17T06:46:10.517352Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:45:45Z`
- `2026-09-17T06:45:38.345079Z` — **FUELINST**: 80 rows; marker `2026-09-17T06:45:00Z`
- `2026-09-17T06:44:18.741964Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:43:45Z`
- `2026-09-17T06:42:20.738258Z` — **MID**: 0 rows; marker `2026-09-17T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T06:42:20.738258Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:41:45Z`
- `2026-09-17T06:40:28.516289Z` — **FUELINST**: 80 rows; marker `2026-09-17T06:40:00Z`
- `2026-09-17T06:40:12.768676Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:39:45Z`
- `2026-09-17T06:38:20.729910Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:37:45Z`
- `2026-09-17T06:37:48.457038Z` — **MID**: 0 rows; marker `2026-09-17T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T06:36:13.037449Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:35:45Z`
- `2026-09-17T06:35:31.655447Z` — **FUELINST**: 80 rows; marker `2026-09-17T06:35:00Z`
- `2026-09-17T06:34:12.080428Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:33:45Z`
