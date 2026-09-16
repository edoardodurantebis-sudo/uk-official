# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T06:37:20.898630Z`  
Current process started UTC: `2026-09-16T06:33:21.140076Z`  
1-second metadata polls in this process: **235**  
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

- `FUELINST|fuelType=INTVKL|generation` = **156** (n=404, 2026-09-16T06:35:29.943839Z)
- `FUELINST|fuelType=NPSHYD|generation` = **545** (n=404, 2026-09-16T06:35:29.943839Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=404, 2026-09-16T06:35:29.943839Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=404, 2026-09-16T06:35:29.943839Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=404, 2026-09-16T06:35:29.943839Z)
- `FUELINST|fuelType=OTHER|generation` = **1801** (n=404, 2026-09-16T06:35:29.943839Z)
- `FUELINST|fuelType=PS|generation` = **218** (n=404, 2026-09-16T06:35:29.943839Z)
- `FUELINST|fuelType=WIND|generation` = **7599** (n=404, 2026-09-16T06:35:29.943839Z)
- `IMBALNGC|TOTAL|imbalance` = **7190** (n=67, 2026-09-16T06:19:50.911181Z)
- `INDDEM|TOTAL|demand` = **-12220** (n=67, 2026-09-16T06:19:50.911181Z)
- `INDGEN|TOTAL|generation` = **26311** (n=67, 2026-09-16T06:19:50.911181Z)
- `MELNGC|TOTAL|margin` = **37447** (n=67, 2026-09-16T06:18:47.161225Z)
- `NDF|TOTAL|demand` = **18621** (n=68, 2026-09-16T06:17:27.932668Z)
- `TSDF|TOTAL|demand` = **19121** (n=68, 2026-09-16T06:17:12.191541Z)
- `WINDFOR|TOTAL|generation` = **19006** (n=11, 2026-09-16T05:30:53.425120Z)

## Latest publication events

- `2026-09-16T06:36:33.153586Z` — **MID**: 0 rows; marker `2026-09-16T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T06:36:17.584131Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:35:45Z`
- `2026-09-16T06:35:29.943839Z` — **FUELINST**: 80 rows; marker `2026-09-16T06:35:00Z`
- `2026-09-16T06:34:09.575446Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:33:45Z`
- `2026-09-16T06:32:22.150223Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:31:45Z`
- `2026-09-16T06:30:30.164637Z` — **FUELHH**: 20 rows; marker `2026-09-16T06:30:00Z`
- `2026-09-16T06:30:30.164637Z` — **FUELINST**: 80 rows; marker `2026-09-16T06:30:00Z`
- `2026-09-16T06:30:30.164637Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:29:45Z`
- `2026-09-16T06:29:41.702258Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:27:45Z`
- `2026-09-16T06:26:08.480978Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:25:45Z`
- `2026-09-16T06:25:36.279245Z` — **FUELINST**: 80 rows; marker `2026-09-16T06:25:00Z`
- `2026-09-16T06:24:16.607191Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:23:45Z`
- `2026-09-16T06:22:08.822888Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:21:45Z`
- `2026-09-16T06:20:22.828055Z` — **FUELINST**: 80 rows; marker `2026-09-16T06:20:00Z`
- `2026-09-16T06:20:06.757376Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:19:45Z`
