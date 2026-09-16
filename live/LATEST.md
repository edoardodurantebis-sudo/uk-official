# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T08:17:56.655220Z`  
Current process started UTC: `2026-09-16T08:13:57.076629Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.27 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=424, 2026-09-16T08:15:38.215629Z)
- `FUELINST|fuelType=NPSHYD|generation` = **426** (n=424, 2026-09-16T08:15:38.215629Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=424, 2026-09-16T08:15:38.215629Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=424, 2026-09-16T08:15:38.215629Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=424, 2026-09-16T08:15:38.215629Z)
- `FUELINST|fuelType=OTHER|generation` = **396** (n=424, 2026-09-16T08:15:38.215629Z)
- `FUELINST|fuelType=PS|generation` = **230** (n=424, 2026-09-16T08:15:38.215629Z)
- `FUELINST|fuelType=WIND|generation` = **6995** (n=424, 2026-09-16T08:15:38.215629Z)
- `IMBALNGC|TOTAL|imbalance` = **6872** (n=69, 2026-09-16T07:20:10.341890Z)
- `INDDEM|TOTAL|demand` = **-12664** (n=69, 2026-09-16T07:19:53.371027Z)
- `INDGEN|TOTAL|generation` = **26437** (n=69, 2026-09-16T07:19:53.371027Z)
- `MELNGC|TOTAL|margin` = **36325** (n=69, 2026-09-16T07:18:39.087802Z)
- `NDF|TOTAL|demand` = **18514** (n=72, 2026-09-16T08:16:58.262307Z)
- `TSDF|TOTAL|demand` = **19458** (n=72, 2026-09-16T08:16:58.262307Z)
- `WINDFOR|TOTAL|generation` = **19006** (n=11, 2026-09-16T05:30:53.425120Z)

## Latest publication events

- `2026-09-16T08:16:58.262307Z` — **TSDF**: 702 rows; marker `2026-09-16T08:16:00Z`
- `2026-09-16T08:16:58.262307Z` — **NDF**: 39 rows; marker `2026-09-16T08:16:00Z`
- `2026-09-16T08:16:26.278784Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:15:45Z`
- `2026-09-16T08:15:38.215629Z` — **FUELINST**: 80 rows; marker `2026-09-16T08:15:00Z`
- `2026-09-16T08:14:34.080833Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:13:45Z`
- `2026-09-16T08:12:26.483883Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:11:45Z`
- `2026-09-16T08:12:10.249655Z` — **MID**: 0 rows; marker `2026-09-16T08:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T08:10:34.440211Z` — **FUELINST**: 80 rows; marker `2026-09-16T08:10:00Z`
- `2026-09-16T08:10:34.440211Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:09:45Z`
- `2026-09-16T08:08:29.060475Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:07:45Z`
- `2026-09-16T08:06:22.299921Z` — **MID**: 0 rows; marker `2026-09-16T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T08:06:22.299921Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:05:45Z`
- `2026-09-16T08:05:34.341079Z` — **FUELINST**: 80 rows; marker `2026-09-16T08:05:00Z`
- `2026-09-16T08:04:06.137263Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:03:45Z`
- `2026-09-16T08:02:12.741609Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:01:45Z`
