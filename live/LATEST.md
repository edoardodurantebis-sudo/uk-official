# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T01:01:32.435157Z`  
Current process started UTC: `2026-09-16T00:57:32.282440Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.95 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.02 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.11 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.19 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.28 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.38 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.47 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.58 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.69 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.81 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.94 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.07 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.22 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.37 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.54 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **45** (n=337, 2026-09-16T01:00:30.142928Z)
- `FUELINST|fuelType=NPSHYD|generation` = **396** (n=337, 2026-09-16T01:00:30.142928Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=337, 2026-09-16T01:00:30.142928Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=337, 2026-09-16T01:00:30.142928Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=337, 2026-09-16T01:00:30.142928Z)
- `FUELINST|fuelType=OTHER|generation` = **148** (n=337, 2026-09-16T01:00:30.142928Z)
- `FUELINST|fuelType=PS|generation` = **191** (n=337, 2026-09-16T01:00:30.142928Z)
- `FUELINST|fuelType=WIND|generation` = **10622** (n=337, 2026-09-16T01:00:30.142928Z)
- `IMBALNGC|TOTAL|imbalance` = **5999** (n=56, 2026-09-16T00:50:48.850672Z)
- `INDDEM|TOTAL|demand` = **-12159** (n=56, 2026-09-16T00:50:48.850672Z)
- `INDGEN|TOTAL|generation` = **25120** (n=56, 2026-09-16T00:50:32.839782Z)
- `MELNGC|TOTAL|margin` = **35658** (n=56, 2026-09-16T00:48:57.758030Z)
- `NDF|TOTAL|demand` = **18621** (n=57, 2026-09-16T00:47:26.234067Z)
- `TSDF|TOTAL|demand` = **19121** (n=57, 2026-09-16T00:47:26.234067Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-16T01:00:30.142928Z` — **FUELHH**: 20 rows; marker `2026-09-16T01:00:00Z`
- `2026-09-16T01:00:30.142928Z` — **FUELINST**: 80 rows; marker `2026-09-16T01:00:00Z`
- `2026-09-16T01:00:14.252443Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:59:45Z`
- `2026-09-16T00:58:20.288125Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:57:45Z`
- `2026-09-16T00:56:08.790010Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:55:45Z`
- `2026-09-16T00:55:36.695879Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:55:00Z`
- `2026-09-16T00:54:16.959727Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:53:45Z`
- `2026-09-16T00:52:09.113875Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:51:45Z`
- `2026-09-16T00:50:48.850672Z` — **INDDEM**: 972 rows; marker `2026-09-16T00:47:00Z`
- `2026-09-16T00:50:48.850672Z` — **IMBALNGC**: 972 rows; marker `2026-09-16T00:47:00Z`
- `2026-09-16T00:50:32.839782Z` — **INDGEN**: 972 rows; marker `2026-09-16T00:47:00Z`
- `2026-09-16T00:50:32.839782Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:50:00Z`
- `2026-09-16T00:50:17.267268Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:49:45Z`
- `2026-09-16T00:48:57.758030Z` — **MELNGC**: 972 rows; marker `2026-09-16T00:47:00Z`
- `2026-09-16T00:48:13.882929Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:47:45Z`
