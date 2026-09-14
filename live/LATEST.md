# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T17:36:06.029242Z`  
Current process started UTC: `2026-09-14T17:31:20.548518Z`  
1-second metadata polls in this process: **282**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

No qualified anomaly yet (series are warming up or no threshold was crossed).

## Latest market values

- `FUELINST|fuelType=INTNSL|generation` = **959** (n=4, 2026-09-14T17:35:22.011002Z)
- `FUELINST|fuelType=INTVKL|generation` = **-609** (n=4, 2026-09-14T17:35:22.011002Z)
- `FUELINST|fuelType=NPSHYD|generation` = **390** (n=4, 2026-09-14T17:35:22.011002Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3296** (n=4, 2026-09-14T17:35:22.011002Z)
- `FUELINST|fuelType=OCGT|generation` = **6** (n=4, 2026-09-14T17:35:22.011002Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=4, 2026-09-14T17:35:22.011002Z)
- `FUELINST|fuelType=OTHER|generation` = **2221** (n=4, 2026-09-14T17:35:22.011002Z)
- `FUELINST|fuelType=PS|generation` = **817** (n=4, 2026-09-14T17:35:22.011002Z)
- `FUELINST|fuelType=WIND|generation` = **10344** (n=4, 2026-09-14T17:35:22.011002Z)
- `IMBALNGC|TOTAL|imbalance` = **-277** (n=1, 2026-09-14T17:22:49.776936Z)
- `INDDEM|TOTAL|demand` = **-12258** (n=1, 2026-09-14T17:22:34.309173Z)
- `INDGEN|TOTAL|generation` = **20208** (n=1, 2026-09-14T17:22:34.309173Z)
- `MELNGC|TOTAL|margin` = **32275** (n=1, 2026-09-14T17:19:58.665863Z)
- `NDF|TOTAL|demand` = **19934** (n=1, 2026-09-14T17:17:51.028048Z)
- `TSDF|TOTAL|demand` = **20485** (n=1, 2026-09-14T17:17:51.028048Z)

## Latest publication events

- `2026-09-14T17:35:22.011002Z` — **FUELINST**: 80 rows; marker `2026-09-14T17:35:00Z`
- `2026-09-14T17:34:17.600947Z` — **FREQ**: 5761 rows; marker `2026-09-14T17:33:45Z`
- `2026-09-14T17:32:25.351956Z` — **FREQ**: 5761 rows; marker `2026-09-14T17:31:45Z`
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
