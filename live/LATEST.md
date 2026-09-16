# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T03:28:46.445407Z`  
Current process started UTC: `2026-09-16T03:24:46.201781Z`  
1-second metadata polls in this process: **239**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-714** (n=366, 2026-09-16T03:25:39.208053Z)
- `FUELINST|fuelType=NPSHYD|generation` = **399** (n=366, 2026-09-16T03:25:39.208053Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3327** (n=366, 2026-09-16T03:25:39.208053Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=366, 2026-09-16T03:25:39.208053Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=366, 2026-09-16T03:25:39.208053Z)
- `FUELINST|fuelType=OTHER|generation` = **126** (n=366, 2026-09-16T03:25:39.208053Z)
- `FUELINST|fuelType=PS|generation` = **224** (n=366, 2026-09-16T03:25:39.208053Z)
- `FUELINST|fuelType=WIND|generation` = **9778** (n=366, 2026-09-16T03:25:39.208053Z)
- `IMBALNGC|TOTAL|imbalance` = **6025** (n=61, 2026-09-16T03:20:52.622308Z)
- `INDDEM|TOTAL|demand` = **-12207** (n=61, 2026-09-16T03:20:52.622308Z)
- `INDGEN|TOTAL|generation` = **25146** (n=61, 2026-09-16T03:20:52.622308Z)
- `MELNGC|TOTAL|margin` = **37540** (n=61, 2026-09-16T03:19:06.803098Z)
- `NDF|TOTAL|demand` = **18621** (n=62, 2026-09-16T03:17:30.975101Z)
- `TSDF|TOTAL|demand` = **19121** (n=62, 2026-09-16T03:17:30.975101Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-16T03:28:03.634717Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:27:45Z`
- `2026-09-16T03:26:11.223710Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:25:45Z`
- `2026-09-16T03:25:39.208053Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:25:00Z`
- `2026-09-16T03:24:04.191033Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:23:45Z`
- `2026-09-16T03:22:28.685225Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:21:45Z`
- `2026-09-16T03:20:52.622308Z` — **INDGEN**: 882 rows; marker `2026-09-16T03:17:00Z`
- `2026-09-16T03:20:52.622308Z` — **INDDEM**: 882 rows; marker `2026-09-16T03:17:00Z`
- `2026-09-16T03:20:52.622308Z` — **IMBALNGC**: 882 rows; marker `2026-09-16T03:17:00Z`
- `2026-09-16T03:20:36.349087Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:20:00Z`
- `2026-09-16T03:20:36.349087Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:19:45Z`
- `2026-09-16T03:19:06.803098Z` — **MELNGC**: 882 rows; marker `2026-09-16T03:17:00Z`
- `2026-09-16T03:18:18.375299Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:17:45Z`
- `2026-09-16T03:17:30.975101Z` — **TSDF**: 882 rows; marker `2026-09-16T03:17:00Z`
- `2026-09-16T03:17:30.975101Z` — **NDF**: 49 rows; marker `2026-09-16T03:17:00Z`
- `2026-09-16T03:16:25.193165Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:15:45Z`
