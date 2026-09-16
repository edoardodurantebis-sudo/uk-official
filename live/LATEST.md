# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T00:32:05.823011Z`  
Current process started UTC: `2026-09-16T00:28:05.750090Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-10.18 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-10.91 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-11.82 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-13.01 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **65** (n=331, 2026-09-16T00:30:44.743706Z)
- `FUELINST|fuelType=NPSHYD|generation` = **400** (n=331, 2026-09-16T00:30:44.743706Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=331, 2026-09-16T00:30:44.743706Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=331, 2026-09-16T00:30:44.743706Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=331, 2026-09-16T00:30:44.743706Z)
- `FUELINST|fuelType=OTHER|generation` = **146** (n=331, 2026-09-16T00:30:44.743706Z)
- `FUELINST|fuelType=PS|generation` = **91** (n=331, 2026-09-16T00:30:44.743706Z)
- `FUELINST|fuelType=WIND|generation` = **10942** (n=331, 2026-09-16T00:30:44.743706Z)
- `IMBALNGC|TOTAL|imbalance` = **6035** (n=55, 2026-09-16T00:20:47.111437Z)
- `INDDEM|TOTAL|demand` = **-12095** (n=55, 2026-09-16T00:20:30.888031Z)
- `INDGEN|TOTAL|generation` = **25156** (n=55, 2026-09-16T00:20:30.888031Z)
- `MELNGC|TOTAL|margin` = **35662** (n=55, 2026-09-16T00:19:43.131683Z)
- `NDF|TOTAL|demand` = **18621** (n=56, 2026-09-16T00:17:22.904504Z)
- `TSDF|TOTAL|demand` = **19121** (n=56, 2026-09-16T00:17:39.040764Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-16T00:32:04.326497Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:31:45Z`
- `2026-09-16T00:30:44.743706Z` — **FUELHH**: 20 rows; marker `2026-09-16T00:30:00Z`
- `2026-09-16T00:30:44.743706Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:30:00Z`
- `2026-09-16T00:30:13.192001Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:29:45Z`
- `2026-09-16T00:28:21.752000Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:27:45Z`
- `2026-09-16T00:26:21.604027Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:25:45Z`
- `2026-09-16T00:25:33.418480Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:25:00Z`
- `2026-09-16T00:24:29.684145Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:23:45Z`
- `2026-09-16T00:22:22.489970Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:21:45Z`
- `2026-09-16T00:20:47.111437Z` — **IMBALNGC**: 990 rows; marker `2026-09-16T00:17:00Z`
- `2026-09-16T00:20:30.888031Z` — **INDGEN**: 990 rows; marker `2026-09-16T00:17:00Z`
- `2026-09-16T00:20:30.888031Z` — **INDDEM**: 990 rows; marker `2026-09-16T00:17:00Z`
- `2026-09-16T00:20:30.888031Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:20:00Z`
- `2026-09-16T00:20:15.384546Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:19:45Z`
- `2026-09-16T00:19:43.131683Z` — **MELNGC**: 990 rows; marker `2026-09-16T00:17:00Z`
