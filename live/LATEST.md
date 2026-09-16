# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T02:17:31.563576Z`  
Current process started UTC: `2026-09-16T02:13:31.251702Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-681** (n=352, 2026-09-16T02:15:38.813456Z)
- `FUELINST|fuelType=NPSHYD|generation` = **391** (n=352, 2026-09-16T02:15:38.813456Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=352, 2026-09-16T02:15:38.813456Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=352, 2026-09-16T02:15:38.813456Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=352, 2026-09-16T02:15:38.813456Z)
- `FUELINST|fuelType=OTHER|generation` = **152** (n=352, 2026-09-16T02:15:38.813456Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=352, 2026-09-16T02:15:38.813456Z)
- `FUELINST|fuelType=WIND|generation` = **10042** (n=352, 2026-09-16T02:15:38.813456Z)
- `IMBALNGC|TOTAL|imbalance` = **5969** (n=58, 2026-09-16T01:50:27.730750Z)
- `INDDEM|TOTAL|demand` = **-12203** (n=58, 2026-09-16T01:50:27.730750Z)
- `INDGEN|TOTAL|generation` = **25090** (n=58, 2026-09-16T01:50:27.730750Z)
- `MELNGC|TOTAL|margin` = **36078** (n=58, 2026-09-16T01:49:07.816417Z)
- `NDF|TOTAL|demand` = **18621** (n=60, 2026-09-16T02:17:14.647012Z)
- `TSDF|TOTAL|demand` = **19121** (n=60, 2026-09-16T02:17:14.647012Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-16T02:17:14.647012Z` — **TSDF**: 918 rows; marker `2026-09-16T02:17:00Z`
- `2026-09-16T02:17:14.647012Z` — **NDF**: 51 rows; marker `2026-09-16T02:17:00Z`
- `2026-09-16T02:16:10.889976Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:15:45Z`
- `2026-09-16T02:15:38.813456Z` — **FUELINST**: 80 rows; marker `2026-09-16T02:15:00Z`
- `2026-09-16T02:14:19.257763Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:13:45Z`
- `2026-09-16T02:12:13.586662Z` — **MID**: 0 rows; marker `2026-09-16T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T02:12:13.586662Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:11:45Z`
- `2026-09-16T02:10:37.566080Z` — **FUELINST**: 80 rows; marker `2026-09-16T02:10:00Z`
- `2026-09-16T02:10:37.566080Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:09:45Z`
- `2026-09-16T02:08:18.294417Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:07:45Z`
- `2026-09-16T02:06:26.105247Z` — **MID**: 0 rows; marker `2026-09-16T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T02:06:09.485756Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:05:45Z`
- `2026-09-16T02:05:21.195701Z` — **FUELINST**: 80 rows; marker `2026-09-16T02:05:00Z`
- `2026-09-16T02:04:33.704987Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:03:45Z`
- `2026-09-16T02:02:14.307675Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:01:45Z`
