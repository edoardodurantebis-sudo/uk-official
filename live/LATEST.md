# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T20:16:04.226307Z`  
Current process started UTC: `2026-09-14T20:12:04.830437Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

No qualified anomaly yet (series are warming up or no threshold was crossed).

## Latest market values

- `FUELINST|fuelType=INTNSL|generation` = **804** (n=6, 2026-09-14T20:15:45.625680Z)
- `FUELINST|fuelType=INTVKL|generation` = **-1068** (n=6, 2026-09-14T20:15:45.625680Z)
- `FUELINST|fuelType=NPSHYD|generation` = **403** (n=6, 2026-09-14T20:15:45.625680Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3309** (n=6, 2026-09-14T20:15:45.625680Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=6, 2026-09-14T20:15:45.625680Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=6, 2026-09-14T20:15:45.625680Z)
- `FUELINST|fuelType=OTHER|generation` = **876** (n=6, 2026-09-14T20:15:45.625680Z)
- `FUELINST|fuelType=PS|generation` = **-6** (n=6, 2026-09-14T20:15:45.625680Z)
- `FUELINST|fuelType=WIND|generation` = **12312** (n=6, 2026-09-14T20:15:45.625680Z)
- `IMBALNGC|TOTAL|imbalance` = **-277** (n=1, 2026-09-14T17:22:49.776936Z)
- `INDDEM|TOTAL|demand` = **-12258** (n=1, 2026-09-14T17:22:34.309173Z)
- `INDGEN|TOTAL|generation` = **20208** (n=1, 2026-09-14T17:22:34.309173Z)
- `MELNGC|TOTAL|margin` = **32275** (n=1, 2026-09-14T17:19:58.665863Z)
- `NDF|TOTAL|demand` = **19934** (n=1, 2026-09-14T17:17:51.028048Z)
- `TSDF|TOTAL|demand` = **20485** (n=1, 2026-09-14T17:17:51.028048Z)

## Latest publication events

- `2026-09-14T20:15:45.625680Z` — **FUELINST**: 80 rows; marker `2026-09-14T20:15:00Z`
- `2026-09-14T20:14:27.442655Z` — **FREQ**: 5761 rows; marker `2026-09-14T20:13:45Z`
- `2026-09-14T20:12:20.285655Z` — **MID**: 0 rows; marker `2026-09-14T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T20:12:20.285655Z` — **FREQ**: 5761 rows; marker `2026-09-14T20:11:45Z`
- `2026-09-14T20:12:04.830444Z` — **MID**: 0 rows; marker `2026-09-14T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T20:12:04.830444Z` — **MELNGC**: 0 rows; marker `2026-09-14T19:47:00Z`
- `2026-09-14T20:12:04.830444Z` — **INDGEN**: 0 rows; marker `2026-09-14T19:47:00Z`
- `2026-09-14T20:12:04.830444Z` — **INDDEM**: 0 rows; marker `2026-09-14T19:47:00Z`
- `2026-09-14T20:12:04.830444Z` — **IMBALNGC**: 0 rows; marker `2026-09-14T19:47:00Z`
- `2026-09-14T20:12:04.830444Z` — **TSDF**: 0 rows; marker `2026-09-14T19:47:00Z`
- `2026-09-14T20:12:04.830444Z` — **NDF**: 0 rows; marker `2026-09-14T19:47:00Z`
- `2026-09-14T20:12:04.830444Z` — **WINDFOR**: 0 rows; marker `2026-09-14T19:30:00Z`
- `2026-09-14T20:12:04.830444Z` — **FUELHH**: 20 rows; marker `2026-09-14T20:00:00Z`
- `2026-09-14T20:12:04.830444Z` — **FUELINST**: 80 rows; marker `2026-09-14T20:10:00Z`
- `2026-09-14T20:12:04.830444Z` — **FREQ**: 5761 rows; marker `2026-09-14T20:09:45Z`
