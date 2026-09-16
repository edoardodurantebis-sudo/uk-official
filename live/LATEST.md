# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T23:55:23.289858Z`  
Current process started UTC: `2026-09-16T23:51:22.800808Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=-3, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.63 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.72 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.82 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=50, delta=50, z=5.13 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=40, delta=-418, z=-3.53 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.92 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.03 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-4, delta=0, z=-3.54 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.15 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-4, delta=0, z=-3.58 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=3, z=5.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-4, delta=-68, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=29, z=5.10 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.28 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-464** (n=580, 2026-09-16T23:50:40.700094Z)
- `FUELINST|fuelType=NPSHYD|generation` = **434** (n=580, 2026-09-16T23:50:40.700094Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3312** (n=580, 2026-09-16T23:50:40.700094Z)
- `FUELINST|fuelType=OCGT|generation` = **53** (n=580, 2026-09-16T23:50:40.700094Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=580, 2026-09-16T23:50:40.700094Z)
- `FUELINST|fuelType=OTHER|generation` = **347** (n=580, 2026-09-16T23:50:40.700094Z)
- `FUELINST|fuelType=PS|generation` = **-250** (n=580, 2026-09-16T23:50:40.700094Z)
- `FUELINST|fuelType=WIND|generation` = **11614** (n=580, 2026-09-16T23:50:40.700094Z)
- `IMBALNGC|TOTAL|imbalance` = **6451** (n=97, 2026-09-16T23:51:22.800815Z)
- `INDDEM|TOTAL|demand` = **-11763** (n=97, 2026-09-16T23:51:22.800815Z)
- `INDGEN|TOTAL|generation` = **25572** (n=97, 2026-09-16T23:51:22.800815Z)
- `MELNGC|TOTAL|margin` = **34508** (n=97, 2026-09-16T23:49:04.834499Z)
- `NDF|TOTAL|demand` = **18621** (n=99, 2026-09-16T23:47:28.553408Z)
- `TSDF|TOTAL|demand` = **19121** (n=99, 2026-09-16T23:47:28.553408Z)
- `WINDFOR|TOTAL|generation` = **20102** (n=17, 2026-09-16T23:30:41.101363Z)

## Latest publication events

- `2026-09-16T23:54:18.845762Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:53:45Z`
- `2026-09-16T23:52:27.110241Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:51:45Z`
- `2026-09-16T23:51:22.800815Z` — **INDGEN**: 1008 rows; marker `2026-09-16T23:47:00Z`
- `2026-09-16T23:51:22.800815Z` — **INDDEM**: 1008 rows; marker `2026-09-16T23:47:00Z`
- `2026-09-16T23:51:22.800815Z` — **IMBALNGC**: 1008 rows; marker `2026-09-16T23:47:00Z`
- `2026-09-16T23:50:40.700094Z` — **FUELINST**: 80 rows; marker `2026-09-16T23:50:00Z`
- `2026-09-16T23:50:24.863998Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:49:45Z`
- `2026-09-16T23:49:04.834499Z` — **MELNGC**: 1008 rows; marker `2026-09-16T23:47:00Z`
- `2026-09-16T23:48:16.473417Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:47:45Z`
- `2026-09-16T23:47:28.553408Z` — **TSDF**: 1008 rows; marker `2026-09-16T23:47:00Z`
- `2026-09-16T23:47:28.553408Z` — **NDF**: 56 rows; marker `2026-09-16T23:47:00Z`
- `2026-09-16T23:46:14.728706Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:45:45Z`
- `2026-09-16T23:45:26.660349Z` — **FUELINST**: 80 rows; marker `2026-09-16T23:45:00Z`
- `2026-09-16T23:44:22.301687Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:43:45Z`
- `2026-09-16T23:43:01.251189Z` — **MID**: 0 rows; marker `2026-09-16T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
