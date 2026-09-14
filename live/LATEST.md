# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T17:31:03.204230Z`  
Current process started UTC: `2026-09-14T17:26:18.085197Z`  
1-second metadata polls in this process: **280**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

No qualified anomaly yet (series are warming up or no threshold was crossed).

## Latest market values

- `FUELHH|fuelType=INTFR|generation` = **324** (n=1, 2026-09-14T17:30:48.094966Z)
- `FUELHH|fuelType=INTGRNL|generation` = **-54** (n=1, 2026-09-14T17:30:48.094966Z)
- `FUELHH|fuelType=INTIFA2|generation` = **-678** (n=1, 2026-09-14T17:30:48.094966Z)
- `FUELHH|fuelType=INTIRL|generation` = **14** (n=1, 2026-09-14T17:30:48.094966Z)
- `FUELHH|fuelType=INTNED|generation` = **0** (n=1, 2026-09-14T17:30:48.094966Z)
- `FUELHH|fuelType=INTNEM|generation` = **-394** (n=1, 2026-09-14T17:30:48.094966Z)
- `FUELHH|fuelType=INTNSL|generation` = **988** (n=1, 2026-09-14T17:30:48.094966Z)
- `FUELHH|fuelType=INTVKL|generation` = **-646** (n=1, 2026-09-14T17:30:48.094966Z)
- `FUELHH|fuelType=NPSHYD|generation` = **369** (n=1, 2026-09-14T17:30:48.094966Z)
- `FUELHH|fuelType=NUCLEAR|generation` = **3306** (n=1, 2026-09-14T17:30:48.094966Z)
- `FUELHH|fuelType=OCGT|generation` = **6** (n=1, 2026-09-14T17:30:48.094966Z)
- `FUELHH|fuelType=OIL|generation` = **0** (n=1, 2026-09-14T17:30:48.094966Z)
- `FUELHH|fuelType=OTHER|generation` = **1805** (n=1, 2026-09-14T17:30:48.094966Z)
- `FUELHH|fuelType=PS|generation` = **980** (n=1, 2026-09-14T17:30:48.094966Z)
- `FUELHH|fuelType=WIND|generation` = **10216** (n=1, 2026-09-14T17:30:48.094966Z)

## Latest publication events

- `2026-09-14T17:30:48.094966Z` — **FUELHH**: 20 rows; marker `2026-09-14T17:30:00Z`
- `2026-09-14T17:30:32.573753Z` — **FUELINST**: 80 rows; marker `2026-09-14T17:30:00Z`
- `2026-09-14T17:30:17.209063Z` — **FREQ**: 5761 rows; marker `2026-09-14T17:29:45Z`
- `2026-09-14T17:28:25.733844Z` — **FREQ**: 5761 rows; marker `2026-09-14T17:27:45Z`
- `2026-09-14T17:26:18.085212Z` — **FREQ**: 5761 rows; marker `2026-09-14T17:25:45Z`
- `2026-09-14T17:25:29.203216Z` — **FUELINST**: 80 rows; marker `2026-09-14T17:25:00Z`
- `2026-09-14T17:24:25.334977Z` — **FREQ**: 5761 rows; marker `2026-09-14T17:23:45Z`
- `2026-09-14T17:22:49.776936Z` — **IMBALNGC**: 1242 rows; marker `2026-09-14T17:17:00Z`
- `2026-09-14T17:22:34.309173Z` — **INDGEN**: 1242 rows; marker `2026-09-14T17:17:00Z`
- `2026-09-14T17:22:34.309173Z` — **INDDEM**: 1242 rows; marker `2026-09-14T17:17:00Z`
- `2026-09-14T17:22:18.495787Z` — **FREQ**: 5761 rows; marker `2026-09-14T17:21:45Z`
- `2026-09-14T17:20:29.840002Z` — **FUELINST**: 80 rows; marker `2026-09-14T17:20:00Z`
- `2026-09-14T17:20:13.999784Z` — **FREQ**: 5761 rows; marker `2026-09-14T17:19:45Z`
- `2026-09-14T17:19:58.665863Z` — **MELNGC**: 1242 rows; marker `2026-09-14T17:17:00Z`
- `2026-09-14T17:18:23.019266Z` — **FREQ**: 5761 rows; marker `2026-09-14T17:17:45Z`
