# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T03:49:41.886406Z`  
Current process started UTC: `2026-09-16T03:45:41.282883Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-714** (n=370, 2026-09-16T03:45:41.282892Z)
- `FUELINST|fuelType=NPSHYD|generation` = **399** (n=370, 2026-09-16T03:45:41.282892Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=370, 2026-09-16T03:45:41.282892Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=370, 2026-09-16T03:45:41.282892Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=370, 2026-09-16T03:45:41.282892Z)
- `FUELINST|fuelType=OTHER|generation` = **196** (n=370, 2026-09-16T03:45:41.282892Z)
- `FUELINST|fuelType=PS|generation` = **-58** (n=370, 2026-09-16T03:45:41.282892Z)
- `FUELINST|fuelType=WIND|generation` = **9635** (n=370, 2026-09-16T03:45:41.282892Z)
- `IMBALNGC|TOTAL|imbalance` = **6025** (n=61, 2026-09-16T03:20:52.622308Z)
- `INDDEM|TOTAL|demand` = **-12207** (n=61, 2026-09-16T03:20:52.622308Z)
- `INDGEN|TOTAL|generation` = **25146** (n=61, 2026-09-16T03:20:52.622308Z)
- `MELNGC|TOTAL|margin` = **37540** (n=62, 2026-09-16T03:49:25.287483Z)
- `NDF|TOTAL|demand` = **18621** (n=63, 2026-09-16T03:47:17.385316Z)
- `TSDF|TOTAL|demand` = **19121** (n=63, 2026-09-16T03:47:32.908810Z)
- `WINDFOR|TOTAL|generation` = **18849** (n=10, 2026-09-16T03:30:50.299289Z)

## Latest publication events

- `2026-09-16T03:49:25.287483Z` — **MELNGC**: 864 rows; marker `2026-09-16T03:47:00Z`
- `2026-09-16T03:48:20.987084Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:47:45Z`
- `2026-09-16T03:47:32.908810Z` — **TSDF**: 864 rows; marker `2026-09-16T03:47:00Z`
- `2026-09-16T03:47:17.385316Z` — **NDF**: 48 rows; marker `2026-09-16T03:47:00Z`
- `2026-09-16T03:46:13.037990Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:45:45Z`
- `2026-09-16T03:45:41.282892Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:45:00Z`
- `2026-09-16T03:44:15.107495Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:43:45Z`
- `2026-09-16T03:42:06.719365Z` — **MID**: 0 rows; marker `2026-09-16T03:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T03:42:06.719365Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:41:45Z`
- `2026-09-16T03:40:30.882022Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:40:00Z`
- `2026-09-16T03:40:15.360922Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:39:45Z`
- `2026-09-16T03:38:23.858796Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:37:45Z`
- `2026-09-16T03:36:26.742777Z` — **MID**: 0 rows; marker `2026-09-16T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T03:36:11.027276Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:35:45Z`
- `2026-09-16T03:35:54.877424Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:35:00Z`
