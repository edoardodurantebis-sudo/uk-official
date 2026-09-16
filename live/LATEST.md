# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T00:40:24.941128Z`  
Current process started UTC: `2026-09-16T00:36:24.923893Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.94 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.07 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.22 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.37 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.54 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.72 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.92 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-7.14 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-7.37 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-7.64 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-7.93 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-8.26 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-8.64 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-9.07 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-9.58 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **65** (n=333, 2026-09-16T00:40:23.613072Z)
- `FUELINST|fuelType=NPSHYD|generation` = **397** (n=333, 2026-09-16T00:40:23.613072Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=333, 2026-09-16T00:40:23.613072Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=333, 2026-09-16T00:40:23.613072Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=333, 2026-09-16T00:40:23.613072Z)
- `FUELINST|fuelType=OTHER|generation` = **234** (n=333, 2026-09-16T00:40:23.613072Z)
- `FUELINST|fuelType=PS|generation` = **104** (n=333, 2026-09-16T00:40:23.613072Z)
- `FUELINST|fuelType=WIND|generation` = **11015** (n=333, 2026-09-16T00:40:23.613072Z)
- `IMBALNGC|TOTAL|imbalance` = **6035** (n=55, 2026-09-16T00:20:47.111437Z)
- `INDDEM|TOTAL|demand` = **-12095** (n=55, 2026-09-16T00:20:30.888031Z)
- `INDGEN|TOTAL|generation` = **25156** (n=55, 2026-09-16T00:20:30.888031Z)
- `MELNGC|TOTAL|margin` = **35662** (n=55, 2026-09-16T00:19:43.131683Z)
- `NDF|TOTAL|demand` = **18621** (n=56, 2026-09-16T00:17:22.904504Z)
- `TSDF|TOTAL|demand` = **19121** (n=56, 2026-09-16T00:17:39.040764Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-16T00:40:23.613072Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:40:00Z`
- `2026-09-16T00:40:08.170756Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:39:45Z`
- `2026-09-16T00:38:16.161996Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:37:45Z`
- `2026-09-16T00:36:24.923901Z` — **MID**: 0 rows; marker `2026-09-16T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T00:36:04.852429Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:35:45Z`
- `2026-09-16T00:35:48.567057Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:35:00Z`
- `2026-09-16T00:34:13.002185Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:33:45Z`
- `2026-09-16T00:32:04.326497Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:31:45Z`
- `2026-09-16T00:30:44.743706Z` — **FUELHH**: 20 rows; marker `2026-09-16T00:30:00Z`
- `2026-09-16T00:30:44.743706Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:30:00Z`
- `2026-09-16T00:30:13.192001Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:29:45Z`
- `2026-09-16T00:28:21.752000Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:27:45Z`
- `2026-09-16T00:26:21.604027Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:25:45Z`
- `2026-09-16T00:25:33.418480Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:25:00Z`
- `2026-09-16T00:24:29.684145Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:23:45Z`
