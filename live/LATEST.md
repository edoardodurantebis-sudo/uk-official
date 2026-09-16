# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T11:20:30.427627Z`  
Current process started UTC: `2026-09-16T11:16:30.357966Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11768, delta=3343, z=1.00 -> demand pressure up
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-15111, delta=-1226, z=-8.15 -> demand pressure easing
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-13885, delta=0, z=-5.69 -> demand pressure easing
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-13885, delta=-1204, z=-7.82 -> demand pressure easing
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=460, 2026-09-16T11:15:34.359938Z)
- `FUELINST|fuelType=NPSHYD|generation` = **353** (n=460, 2026-09-16T11:15:34.359938Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3318** (n=460, 2026-09-16T11:15:34.359938Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=460, 2026-09-16T11:15:34.359938Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=460, 2026-09-16T11:15:34.359938Z)
- `FUELINST|fuelType=OTHER|generation` = **1314** (n=460, 2026-09-16T11:15:34.359938Z)
- `FUELINST|fuelType=PS|generation` = **-5** (n=460, 2026-09-16T11:15:34.359938Z)
- `FUELINST|fuelType=WIND|generation` = **4463** (n=460, 2026-09-16T11:15:34.359938Z)
- `IMBALNGC|TOTAL|imbalance` = **4364** (n=75, 2026-09-16T10:54:48.693717Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=75, 2026-09-16T10:54:32.710094Z)
- `INDGEN|TOTAL|generation` = **24734** (n=75, 2026-09-16T10:54:32.710094Z)
- `MELNGC|TOTAL|margin` = **33402** (n=75, 2026-09-16T10:51:05.338296Z)
- `NDF|TOTAL|demand` = **18280** (n=78, 2026-09-16T11:18:21.826484Z)
- `TSDF|TOTAL|demand` = **18780** (n=78, 2026-09-16T11:18:37.882202Z)
- `WINDFOR|TOTAL|generation` = **19760** (n=13, 2026-09-16T10:30:36.030367Z)

## Latest publication events

- `2026-09-16T11:20:28.561637Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:19:45Z`
- `2026-09-16T11:18:37.882202Z` — **TSDF**: 1458 rows; marker `2026-09-16T11:18:00Z`
- `2026-09-16T11:18:21.826484Z` — **NDF**: 81 rows; marker `2026-09-16T11:18:00Z`
- `2026-09-16T11:18:06.274683Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:17:45Z`
- `2026-09-16T11:16:30.357977Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:15:45Z`
- `2026-09-16T11:15:34.359938Z` — **FUELINST**: 80 rows; marker `2026-09-16T11:15:00Z`
- `2026-09-16T11:14:14.928674Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:13:45Z`
- `2026-09-16T11:12:22.766784Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:11:45Z`
- `2026-09-16T11:12:06.698975Z` — **MID**: 0 rows; marker `2026-09-16T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T11:10:31.079015Z` — **FUELINST**: 80 rows; marker `2026-09-16T11:10:00Z`
- `2026-09-16T11:10:15.625015Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:09:45Z`
- `2026-09-16T11:08:22.704685Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:07:45Z`
- `2026-09-16T11:07:22.853558Z` — **MID**: 0 rows; marker `2026-09-16T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T11:06:18.377994Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:05:45Z`
- `2026-09-16T11:05:30.769294Z` — **FUELINST**: 80 rows; marker `2026-09-16T11:05:00Z`
