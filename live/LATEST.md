# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T03:20:25.024501Z`  
Current process started UTC: `2026-09-16T03:16:25.193159Z`  
1-second metadata polls in this process: **232**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-713** (n=364, 2026-09-16T03:15:29.833137Z)
- `FUELINST|fuelType=NPSHYD|generation` = **399** (n=364, 2026-09-16T03:15:29.833137Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=364, 2026-09-16T03:15:29.833137Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=364, 2026-09-16T03:15:29.833137Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=364, 2026-09-16T03:15:29.833137Z)
- `FUELINST|fuelType=OTHER|generation` = **336** (n=364, 2026-09-16T03:15:29.833137Z)
- `FUELINST|fuelType=PS|generation` = **224** (n=364, 2026-09-16T03:15:29.833137Z)
- `FUELINST|fuelType=WIND|generation` = **9751** (n=364, 2026-09-16T03:15:29.833137Z)
- `IMBALNGC|TOTAL|imbalance` = **6027** (n=60, 2026-09-16T02:51:02.679902Z)
- `INDDEM|TOTAL|demand` = **-12206** (n=60, 2026-09-16T02:51:18.772442Z)
- `INDGEN|TOTAL|generation` = **25148** (n=60, 2026-09-16T02:51:02.679902Z)
- `MELNGC|TOTAL|margin` = **37540** (n=61, 2026-09-16T03:19:06.803098Z)
- `NDF|TOTAL|demand` = **18621** (n=62, 2026-09-16T03:17:30.975101Z)
- `TSDF|TOTAL|demand` = **19121** (n=62, 2026-09-16T03:17:30.975101Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-16T03:19:06.803098Z` — **MELNGC**: 882 rows; marker `2026-09-16T03:17:00Z`
- `2026-09-16T03:18:18.375299Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:17:45Z`
- `2026-09-16T03:17:30.975101Z` — **TSDF**: 882 rows; marker `2026-09-16T03:17:00Z`
- `2026-09-16T03:17:30.975101Z` — **NDF**: 49 rows; marker `2026-09-16T03:17:00Z`
- `2026-09-16T03:16:25.193165Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:15:45Z`
- `2026-09-16T03:15:29.833137Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:15:00Z`
- `2026-09-16T03:14:26.142941Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:13:45Z`
- `2026-09-16T03:12:17.717549Z` — **MID**: 0 rows; marker `2026-09-16T03:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T03:12:17.717549Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:11:45Z`
- `2026-09-16T03:10:26.673034Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:10:00Z`
- `2026-09-16T03:10:26.673034Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:09:45Z`
- `2026-09-16T03:08:18.773701Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:07:45Z`
- `2026-09-16T03:07:31.496976Z` — **MID**: 0 rows; marker `2026-09-16T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T03:06:12.048910Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:05:45Z`
- `2026-09-16T03:05:40.438710Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:05:00Z`
