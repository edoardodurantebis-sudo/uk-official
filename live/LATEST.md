# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T07:00:51.550793Z`  
Current process started UTC: `2026-09-17T06:56:51.987249Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=49, delta=49, z=4.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=3, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=1, z=4.21 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=0, z=4.18 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **393** (n=666, 2026-09-17T07:00:42.220355Z)
- `FUELINST|fuelType=NPSHYD|generation` = **437** (n=666, 2026-09-17T07:00:42.220355Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3314** (n=666, 2026-09-17T07:00:42.220355Z)
- `FUELINST|fuelType=OCGT|generation` = **55** (n=666, 2026-09-17T07:00:42.220355Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=666, 2026-09-17T07:00:42.220355Z)
- `FUELINST|fuelType=OTHER|generation` = **1753** (n=666, 2026-09-17T07:00:42.220355Z)
- `FUELINST|fuelType=PS|generation` = **226** (n=666, 2026-09-17T07:00:42.220355Z)
- `FUELINST|fuelType=WIND|generation` = **14004** (n=666, 2026-09-17T07:00:42.220355Z)
- `IMBALNGC|TOTAL|imbalance` = **7338** (n=111, 2026-09-17T06:49:53.327366Z)
- `INDDEM|TOTAL|demand` = **-12129** (n=111, 2026-09-17T06:49:37.422907Z)
- `INDGEN|TOTAL|generation` = **26459** (n=111, 2026-09-17T06:49:37.422907Z)
- `MELNGC|TOTAL|margin` = **35731** (n=111, 2026-09-17T06:48:49.093378Z)
- `NDF|TOTAL|demand` = **18621** (n=113, 2026-09-17T06:46:58.264612Z)
- `TSDF|TOTAL|demand` = **19121** (n=113, 2026-09-17T06:46:58.264612Z)
- `WINDFOR|TOTAL|generation` = **19265** (n=19, 2026-09-17T05:30:37.912884Z)

## Latest publication events

- `2026-09-17T07:00:42.220355Z` — **FUELHH**: 20 rows; marker `2026-09-17T07:00:00Z`
- `2026-09-17T07:00:42.220355Z` — **FUELINST**: 80 rows; marker `2026-09-17T07:00:00Z`
- `2026-09-17T07:00:26.023010Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:59:45Z`
- `2026-09-17T06:58:18.206286Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:57:45Z`
- `2026-09-17T06:56:26.030891Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:55:45Z`
- `2026-09-17T06:55:37.876934Z` — **FUELINST**: 80 rows; marker `2026-09-17T06:55:00Z`
- `2026-09-17T06:54:18.386811Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:53:45Z`
- `2026-09-17T06:52:17.114532Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:51:45Z`
- `2026-09-17T06:50:41.013694Z` — **FUELINST**: 80 rows; marker `2026-09-17T06:50:00Z`
- `2026-09-17T06:50:25.599826Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:49:45Z`
- `2026-09-17T06:49:53.327366Z` — **IMBALNGC**: 756 rows; marker `2026-09-17T06:46:00Z`
- `2026-09-17T06:49:37.422907Z` — **INDGEN**: 756 rows; marker `2026-09-17T06:46:00Z`
- `2026-09-17T06:49:37.422907Z` — **INDDEM**: 756 rows; marker `2026-09-17T06:46:00Z`
- `2026-09-17T06:48:49.093378Z` — **MELNGC**: 756 rows; marker `2026-09-17T06:46:00Z`
- `2026-09-17T06:48:17.846218Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:47:45Z`
