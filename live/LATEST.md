# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T00:52:57.446457Z`  
Current process started UTC: `2026-09-16T00:48:57.758020Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.72 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.92 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-7.14 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-7.37 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **65** (n=335, 2026-09-16T00:50:32.839782Z)
- `FUELINST|fuelType=NPSHYD|generation` = **395** (n=335, 2026-09-16T00:50:32.839782Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=335, 2026-09-16T00:50:32.839782Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=335, 2026-09-16T00:50:32.839782Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=335, 2026-09-16T00:50:32.839782Z)
- `FUELINST|fuelType=OTHER|generation` = **192** (n=335, 2026-09-16T00:50:32.839782Z)
- `FUELINST|fuelType=PS|generation` = **191** (n=335, 2026-09-16T00:50:32.839782Z)
- `FUELINST|fuelType=WIND|generation` = **10865** (n=335, 2026-09-16T00:50:32.839782Z)
- `IMBALNGC|TOTAL|imbalance` = **5999** (n=56, 2026-09-16T00:50:48.850672Z)
- `INDDEM|TOTAL|demand` = **-12159** (n=56, 2026-09-16T00:50:48.850672Z)
- `INDGEN|TOTAL|generation` = **25120** (n=56, 2026-09-16T00:50:32.839782Z)
- `MELNGC|TOTAL|margin` = **35658** (n=56, 2026-09-16T00:48:57.758030Z)
- `NDF|TOTAL|demand` = **18621** (n=57, 2026-09-16T00:47:26.234067Z)
- `TSDF|TOTAL|demand` = **19121** (n=57, 2026-09-16T00:47:26.234067Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-16T00:52:09.113875Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:51:45Z`
- `2026-09-16T00:50:48.850672Z` — **INDDEM**: 972 rows; marker `2026-09-16T00:47:00Z`
- `2026-09-16T00:50:48.850672Z` — **IMBALNGC**: 972 rows; marker `2026-09-16T00:47:00Z`
- `2026-09-16T00:50:32.839782Z` — **INDGEN**: 972 rows; marker `2026-09-16T00:47:00Z`
- `2026-09-16T00:50:32.839782Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:50:00Z`
- `2026-09-16T00:50:17.267268Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:49:45Z`
- `2026-09-16T00:48:57.758030Z` — **MELNGC**: 972 rows; marker `2026-09-16T00:47:00Z`
- `2026-09-16T00:48:13.882929Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:47:45Z`
- `2026-09-16T00:47:26.234067Z` — **TSDF**: 972 rows; marker `2026-09-16T00:47:00Z`
- `2026-09-16T00:47:26.234067Z` — **NDF**: 54 rows; marker `2026-09-16T00:47:00Z`
- `2026-09-16T00:46:22.004745Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:45:45Z`
- `2026-09-16T00:45:49.916752Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:45:00Z`
- `2026-09-16T00:44:06.649565Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:43:45Z`
- `2026-09-16T00:42:15.008440Z` — **MID**: 0 rows; marker `2026-09-16T00:42:05Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T00:42:15.008440Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:41:45Z`
