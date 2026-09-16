# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T02:04:21.560629Z`  
Current process started UTC: `2026-09-16T02:00:21.810496Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.01 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-168** (n=349, 2026-09-16T02:00:38.033922Z)
- `FUELINST|fuelType=NPSHYD|generation` = **390** (n=349, 2026-09-16T02:00:38.033922Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=349, 2026-09-16T02:00:38.033922Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=349, 2026-09-16T02:00:38.033922Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=349, 2026-09-16T02:00:38.033922Z)
- `FUELINST|fuelType=OTHER|generation` = **141** (n=349, 2026-09-16T02:00:38.033922Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=349, 2026-09-16T02:00:38.033922Z)
- `FUELINST|fuelType=WIND|generation` = **10190** (n=349, 2026-09-16T02:00:38.033922Z)
- `IMBALNGC|TOTAL|imbalance` = **5969** (n=58, 2026-09-16T01:50:27.730750Z)
- `INDDEM|TOTAL|demand` = **-12203** (n=58, 2026-09-16T01:50:27.730750Z)
- `INDGEN|TOTAL|generation` = **25090** (n=58, 2026-09-16T01:50:27.730750Z)
- `MELNGC|TOTAL|margin` = **36078** (n=58, 2026-09-16T01:49:07.816417Z)
- `NDF|TOTAL|demand` = **18621** (n=59, 2026-09-16T01:47:16.954243Z)
- `TSDF|TOTAL|demand` = **19121** (n=59, 2026-09-16T01:47:32.569044Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-16T02:02:14.307675Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:01:45Z`
- `2026-09-16T02:00:38.033922Z` — **FUELHH**: 20 rows; marker `2026-09-16T02:00:00Z`
- `2026-09-16T02:00:38.033922Z` — **FUELINST**: 80 rows; marker `2026-09-16T02:00:00Z`
- `2026-09-16T02:00:21.810506Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:59:45Z`
- `2026-09-16T01:58:03.381442Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:57:45Z`
- `2026-09-16T01:56:10.765426Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:55:45Z`
- `2026-09-16T01:55:47.191807Z` — **FUELINST**: 80 rows; marker `2026-09-16T01:55:00Z`
- `2026-09-16T01:54:27.425634Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:53:45Z`
- `2026-09-16T01:52:18.479369Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:51:45Z`
- `2026-09-16T01:50:43.093605Z` — **FUELINST**: 80 rows; marker `2026-09-16T01:50:00Z`
- `2026-09-16T01:50:27.730750Z` — **INDGEN**: 936 rows; marker `2026-09-16T01:46:00Z`
- `2026-09-16T01:50:27.730750Z` — **INDDEM**: 936 rows; marker `2026-09-16T01:46:00Z`
- `2026-09-16T01:50:27.730750Z` — **IMBALNGC**: 936 rows; marker `2026-09-16T01:46:00Z`
- `2026-09-16T01:50:27.730750Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:49:45Z`
- `2026-09-16T01:49:07.816417Z` — **MELNGC**: 936 rows; marker `2026-09-16T01:46:00Z`
