# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T03:58:05.006293Z`  
Current process started UTC: `2026-09-16T03:54:05.231916Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-714** (n=372, 2026-09-16T03:55:41.041545Z)
- `FUELINST|fuelType=NPSHYD|generation` = **399** (n=372, 2026-09-16T03:55:41.041545Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=372, 2026-09-16T03:55:41.041545Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=372, 2026-09-16T03:55:41.041545Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=372, 2026-09-16T03:55:41.041545Z)
- `FUELINST|fuelType=OTHER|generation` = **225** (n=372, 2026-09-16T03:55:41.041545Z)
- `FUELINST|fuelType=PS|generation` = **-329** (n=372, 2026-09-16T03:55:41.041545Z)
- `FUELINST|fuelType=WIND|generation` = **9612** (n=372, 2026-09-16T03:55:41.041545Z)
- `IMBALNGC|TOTAL|imbalance` = **7021** (n=62, 2026-09-16T03:50:43.848366Z)
- `INDDEM|TOTAL|demand` = **-12202** (n=62, 2026-09-16T03:50:43.848366Z)
- `INDGEN|TOTAL|generation` = **26142** (n=62, 2026-09-16T03:50:43.848366Z)
- `MELNGC|TOTAL|margin` = **37540** (n=62, 2026-09-16T03:49:25.287483Z)
- `NDF|TOTAL|demand` = **18621** (n=63, 2026-09-16T03:47:17.385316Z)
- `TSDF|TOTAL|demand` = **19121** (n=63, 2026-09-16T03:47:32.908810Z)
- `WINDFOR|TOTAL|generation` = **18849** (n=10, 2026-09-16T03:30:50.299289Z)

## Latest publication events

- `2026-09-16T03:56:13.605990Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:55:45Z`
- `2026-09-16T03:55:41.041545Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:55:00Z`
- `2026-09-16T03:54:21.234027Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:53:45Z`
- `2026-09-16T03:52:20.073190Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:51:45Z`
- `2026-09-16T03:50:43.848366Z` — **INDGEN**: 864 rows; marker `2026-09-16T03:46:00Z`
- `2026-09-16T03:50:43.848366Z` — **INDDEM**: 864 rows; marker `2026-09-16T03:46:00Z`
- `2026-09-16T03:50:43.848366Z` — **IMBALNGC**: 864 rows; marker `2026-09-16T03:47:00Z`
- `2026-09-16T03:50:28.384980Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:50:00Z`
- `2026-09-16T03:50:12.914860Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:49:45Z`
- `2026-09-16T03:49:25.287483Z` — **MELNGC**: 864 rows; marker `2026-09-16T03:47:00Z`
- `2026-09-16T03:48:20.987084Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:47:45Z`
- `2026-09-16T03:47:32.908810Z` — **TSDF**: 864 rows; marker `2026-09-16T03:47:00Z`
- `2026-09-16T03:47:17.385316Z` — **NDF**: 48 rows; marker `2026-09-16T03:47:00Z`
- `2026-09-16T03:46:13.037990Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:45:45Z`
- `2026-09-16T03:45:41.282892Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:45:00Z`
