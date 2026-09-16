# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T06:29:00.660571Z`  
Current process started UTC: `2026-09-16T06:25:00.274424Z`  
1-second metadata polls in this process: **240**  
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

- `FUELINST|fuelType=INTVKL|generation` = **156** (n=402, 2026-09-16T06:25:36.279245Z)
- `FUELINST|fuelType=NPSHYD|generation` = **545** (n=402, 2026-09-16T06:25:36.279245Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=402, 2026-09-16T06:25:36.279245Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=402, 2026-09-16T06:25:36.279245Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=402, 2026-09-16T06:25:36.279245Z)
- `FUELINST|fuelType=OTHER|generation` = **1578** (n=402, 2026-09-16T06:25:36.279245Z)
- `FUELINST|fuelType=PS|generation` = **218** (n=402, 2026-09-16T06:25:36.279245Z)
- `FUELINST|fuelType=WIND|generation` = **7707** (n=402, 2026-09-16T06:25:36.279245Z)
- `IMBALNGC|TOTAL|imbalance` = **7190** (n=67, 2026-09-16T06:19:50.911181Z)
- `INDDEM|TOTAL|demand` = **-12220** (n=67, 2026-09-16T06:19:50.911181Z)
- `INDGEN|TOTAL|generation` = **26311** (n=67, 2026-09-16T06:19:50.911181Z)
- `MELNGC|TOTAL|margin` = **37447** (n=67, 2026-09-16T06:18:47.161225Z)
- `NDF|TOTAL|demand` = **18621** (n=68, 2026-09-16T06:17:27.932668Z)
- `TSDF|TOTAL|demand` = **19121** (n=68, 2026-09-16T06:17:12.191541Z)
- `WINDFOR|TOTAL|generation` = **19006** (n=11, 2026-09-16T05:30:53.425120Z)

## Latest publication events

- `2026-09-16T06:26:08.480978Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:25:45Z`
- `2026-09-16T06:25:36.279245Z` — **FUELINST**: 80 rows; marker `2026-09-16T06:25:00Z`
- `2026-09-16T06:24:16.607191Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:23:45Z`
- `2026-09-16T06:22:08.822888Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:21:45Z`
- `2026-09-16T06:20:22.828055Z` — **FUELINST**: 80 rows; marker `2026-09-16T06:20:00Z`
- `2026-09-16T06:20:06.757376Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:19:45Z`
- `2026-09-16T06:19:50.911181Z` — **INDGEN**: 774 rows; marker `2026-09-16T06:16:00Z`
- `2026-09-16T06:19:50.911181Z` — **INDDEM**: 774 rows; marker `2026-09-16T06:16:00Z`
- `2026-09-16T06:19:50.911181Z` — **IMBALNGC**: 774 rows; marker `2026-09-16T06:16:00Z`
- `2026-09-16T06:18:47.161225Z` — **MELNGC**: 774 rows; marker `2026-09-16T06:16:00Z`
- `2026-09-16T06:18:15.239181Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:17:45Z`
- `2026-09-16T06:17:27.932668Z` — **NDF**: 43 rows; marker `2026-09-16T06:16:00Z`
- `2026-09-16T06:17:12.191541Z` — **TSDF**: 774 rows; marker `2026-09-16T06:16:00Z`
- `2026-09-16T06:16:08.099707Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:15:45Z`
- `2026-09-16T06:15:36.027352Z` — **FUELINST**: 80 rows; marker `2026-09-16T06:15:00Z`
