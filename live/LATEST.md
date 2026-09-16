# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T23:25:31.139506Z`  
Current process started UTC: `2026-09-16T23:21:31.450222Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.15 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-4, delta=0, z=-3.58 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=3, z=5.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-4, delta=-68, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=29, z=5.10 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.28 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.80 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-464** (n=574, 2026-09-16T23:20:30.636890Z)
- `FUELINST|fuelType=NPSHYD|generation` = **436** (n=574, 2026-09-16T23:20:30.636890Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3313** (n=574, 2026-09-16T23:20:30.636890Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=574, 2026-09-16T23:20:30.636890Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=574, 2026-09-16T23:20:30.636890Z)
- `FUELINST|fuelType=OTHER|generation` = **400** (n=574, 2026-09-16T23:20:30.636890Z)
- `FUELINST|fuelType=PS|generation` = **-249** (n=574, 2026-09-16T23:20:30.636890Z)
- `FUELINST|fuelType=WIND|generation` = **10997** (n=574, 2026-09-16T23:20:30.636890Z)
- `IMBALNGC|TOTAL|imbalance` = **6603** (n=96, 2026-09-16T23:21:18.839440Z)
- `INDDEM|TOTAL|demand` = **-11763** (n=96, 2026-09-16T23:21:18.839440Z)
- `INDGEN|TOTAL|generation` = **25724** (n=96, 2026-09-16T23:21:18.839440Z)
- `MELNGC|TOTAL|margin` = **34485** (n=96, 2026-09-16T23:19:27.229316Z)
- `NDF|TOTAL|demand` = **18621** (n=98, 2026-09-16T23:17:35.862544Z)
- `TSDF|TOTAL|demand` = **19121** (n=98, 2026-09-16T23:17:52.024896Z)
- `WINDFOR|TOTAL|generation` = **19445** (n=16, 2026-09-16T19:30:31.948327Z)

## Latest publication events

- `2026-09-16T23:24:14.321809Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:23:45Z`
- `2026-09-16T23:22:06.454407Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:21:45Z`
- `2026-09-16T23:21:18.839440Z` — **INDGEN**: 1026 rows; marker `2026-09-16T23:17:00Z`
- `2026-09-16T23:21:18.839440Z` — **INDDEM**: 1026 rows; marker `2026-09-16T23:17:00Z`
- `2026-09-16T23:21:18.839440Z` — **IMBALNGC**: 1026 rows; marker `2026-09-16T23:17:00Z`
- `2026-09-16T23:20:30.636890Z` — **FUELINST**: 80 rows; marker `2026-09-16T23:20:00Z`
- `2026-09-16T23:20:14.876300Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:19:45Z`
- `2026-09-16T23:19:27.229316Z` — **MELNGC**: 1026 rows; marker `2026-09-16T23:17:00Z`
- `2026-09-16T23:18:23.409302Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:17:45Z`
- `2026-09-16T23:17:52.024896Z` — **TSDF**: 1026 rows; marker `2026-09-16T23:17:00Z`
- `2026-09-16T23:17:35.862544Z` — **NDF**: 57 rows; marker `2026-09-16T23:17:00Z`
- `2026-09-16T23:16:27.660811Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:15:45Z`
- `2026-09-16T23:15:39.505618Z` — **FUELINST**: 80 rows; marker `2026-09-16T23:15:00Z`
- `2026-09-16T23:14:19.157720Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:13:45Z`
- `2026-09-16T23:12:27.394313Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:11:45Z`
