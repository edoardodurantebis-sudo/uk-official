# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T17:20:58.282604Z`  
Current process started UTC: `2026-09-14T17:16:13.602070Z`  
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

- `FUELINST|fuelType=INTFR|generation` = **302** (n=1, 2026-09-14T17:20:29.840002Z)
- `FUELINST|fuelType=INTGRNL|generation` = **-52** (n=1, 2026-09-14T17:20:29.840002Z)
- `FUELINST|fuelType=INTIFA2|generation` = **-721** (n=1, 2026-09-14T17:20:29.840002Z)
- `FUELINST|fuelType=INTIRL|generation` = **15** (n=1, 2026-09-14T17:20:29.840002Z)
- `FUELINST|fuelType=INTNED|generation` = **1** (n=1, 2026-09-14T17:20:29.840002Z)
- `FUELINST|fuelType=INTNEM|generation` = **-395** (n=1, 2026-09-14T17:20:29.840002Z)
- `FUELINST|fuelType=INTNSL|generation` = **959** (n=1, 2026-09-14T17:20:29.840002Z)
- `FUELINST|fuelType=INTVKL|generation` = **-609** (n=1, 2026-09-14T17:20:29.840002Z)
- `FUELINST|fuelType=NPSHYD|generation` = **370** (n=1, 2026-09-14T17:20:29.840002Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3297** (n=1, 2026-09-14T17:20:29.840002Z)
- `FUELINST|fuelType=OCGT|generation` = **6** (n=1, 2026-09-14T17:20:29.840002Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1, 2026-09-14T17:20:29.840002Z)
- `FUELINST|fuelType=OTHER|generation` = **1816** (n=1, 2026-09-14T17:20:29.840002Z)
- `FUELINST|fuelType=PS|generation` = **980** (n=1, 2026-09-14T17:20:29.840002Z)
- `FUELINST|fuelType=WIND|generation` = **10210** (n=1, 2026-09-14T17:20:29.840002Z)

## Latest publication events

- `2026-09-14T17:20:29.840002Z` — **FUELINST**: 80 rows; marker `2026-09-14T17:20:00Z`
- `2026-09-14T17:20:13.999784Z` — **FREQ**: 5761 rows; marker `2026-09-14T17:19:45Z`
- `2026-09-14T17:19:58.665863Z` — **MELNGC**: 1242 rows; marker `2026-09-14T17:17:00Z`
- `2026-09-14T17:18:23.019266Z` — **FREQ**: 5761 rows; marker `2026-09-14T17:17:45Z`
- `2026-09-14T17:17:51.028048Z` — **TSDF**: 1242 rows; marker `2026-09-14T17:17:00Z`
- `2026-09-14T17:17:51.028048Z` — **NDF**: 69 rows; marker `2026-09-14T17:17:00Z`
- `2026-09-14T17:16:15.602340Z` — **FREQ**: 5761 rows; marker `2026-09-14T17:15:45Z`
