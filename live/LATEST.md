# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T17:25:59.901615Z`  
Current process started UTC: `2026-09-14T17:21:14.727783Z`  
1-second metadata polls in this process: **281**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

No qualified anomaly yet (series are warming up or no threshold was crossed).

## Latest market values

- `FUELINST|fuelType=INTNSL|generation` = **959** (n=2, 2026-09-14T17:25:29.203216Z)
- `FUELINST|fuelType=INTVKL|generation` = **-609** (n=2, 2026-09-14T17:25:29.203216Z)
- `FUELINST|fuelType=NPSHYD|generation` = **369** (n=2, 2026-09-14T17:25:29.203216Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3299** (n=2, 2026-09-14T17:25:29.203216Z)
- `FUELINST|fuelType=OCGT|generation` = **6** (n=2, 2026-09-14T17:25:29.203216Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=2, 2026-09-14T17:25:29.203216Z)
- `FUELINST|fuelType=OTHER|generation` = **1954** (n=2, 2026-09-14T17:25:29.203216Z)
- `FUELINST|fuelType=PS|generation` = **979** (n=2, 2026-09-14T17:25:29.203216Z)
- `FUELINST|fuelType=WIND|generation` = **10229** (n=2, 2026-09-14T17:25:29.203216Z)
- `MELNGC|TOTAL|margin` = **32275** (n=1, 2026-09-14T17:19:58.665863Z)
- `NDF|TOTAL|demand` = **19934** (n=1, 2026-09-14T17:17:51.028048Z)
- `TSDF|TOTAL|demand` = **20485** (n=1, 2026-09-14T17:17:51.028048Z)
- `INDDEM|TOTAL|demand` = **-12258** (n=1, 2026-09-14T17:22:34.309173Z)
- `INDGEN|TOTAL|generation` = **20208** (n=1, 2026-09-14T17:22:34.309173Z)
- `IMBALNGC|TOTAL|imbalance` = **-277** (n=1, 2026-09-14T17:22:49.776936Z)

## Latest publication events

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
- `2026-09-14T17:17:51.028048Z` — **TSDF**: 1242 rows; marker `2026-09-14T17:17:00Z`
- `2026-09-14T17:17:51.028048Z` — **NDF**: 69 rows; marker `2026-09-14T17:17:00Z`
- `2026-09-14T17:16:15.602340Z` — **FREQ**: 5761 rows; marker `2026-09-14T17:15:45Z`
