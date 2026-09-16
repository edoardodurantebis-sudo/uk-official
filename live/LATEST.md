# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T03:07:47.037059Z`  
Current process started UTC: `2026-09-16T03:03:47.307153Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.52 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.55 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.57 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.60 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.63 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.66 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.69 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.73 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.76 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.79 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.83 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.86 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.90 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.94 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.97 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-704** (n=362, 2026-09-16T03:05:40.438710Z)
- `FUELINST|fuelType=NPSHYD|generation` = **398** (n=362, 2026-09-16T03:05:40.438710Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=362, 2026-09-16T03:05:40.438710Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=362, 2026-09-16T03:05:40.438710Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=362, 2026-09-16T03:05:40.438710Z)
- `FUELINST|fuelType=OTHER|generation` = **124** (n=362, 2026-09-16T03:05:40.438710Z)
- `FUELINST|fuelType=PS|generation` = **222** (n=362, 2026-09-16T03:05:40.438710Z)
- `FUELINST|fuelType=WIND|generation` = **9849** (n=362, 2026-09-16T03:05:40.438710Z)
- `IMBALNGC|TOTAL|imbalance` = **6027** (n=60, 2026-09-16T02:51:02.679902Z)
- `INDDEM|TOTAL|demand` = **-12206** (n=60, 2026-09-16T02:51:18.772442Z)
- `INDGEN|TOTAL|generation` = **25148** (n=60, 2026-09-16T02:51:02.679902Z)
- `MELNGC|TOTAL|margin` = **37540** (n=60, 2026-09-16T02:48:55.534436Z)
- `NDF|TOTAL|demand` = **18621** (n=61, 2026-09-16T02:47:20.255278Z)
- `TSDF|TOTAL|demand` = **19121** (n=61, 2026-09-16T02:47:20.255278Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-16T03:07:31.496976Z` — **MID**: 0 rows; marker `2026-09-16T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T03:06:12.048910Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:05:45Z`
- `2026-09-16T03:05:40.438710Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:05:00Z`
- `2026-09-16T03:04:20.223629Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:03:45Z`
- `2026-09-16T03:02:20.251013Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:01:45Z`
- `2026-09-16T03:00:28.332889Z` — **FUELHH**: 20 rows; marker `2026-09-16T03:00:00Z`
- `2026-09-16T03:00:28.332889Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:00:00Z`
- `2026-09-16T03:00:12.881127Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:59:45Z`
- `2026-09-16T02:58:20.620517Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:57:45Z`
- `2026-09-16T02:56:12.523743Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:55:45Z`
- `2026-09-16T02:55:24.973904Z` — **FUELINST**: 80 rows; marker `2026-09-16T02:55:00Z`
- `2026-09-16T02:54:14.706853Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:53:45Z`
- `2026-09-16T02:52:07.240906Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:51:45Z`
- `2026-09-16T02:51:18.772442Z` — **INDDEM**: 900 rows; marker `2026-09-16T02:46:00Z`
- `2026-09-16T02:51:02.679902Z` — **INDGEN**: 900 rows; marker `2026-09-16T02:46:00Z`
