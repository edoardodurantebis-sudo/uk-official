# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T12:36:29.390150Z`  
Current process started UTC: `2026-09-16T12:32:28.238867Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3295, delta=-5, z=-3.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3297, delta=3, z=-3.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3294, delta=-4, z=-4.20 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3298, delta=-3, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3290, delta=-7, z=-5.03 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3297, delta=-24, z=-4.07 -> generation-mix component moved
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11768, delta=3343, z=1.00 -> demand pressure up
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-15111, delta=-1226, z=-8.15 -> demand pressure easing
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-13885, delta=0, z=-5.69 -> demand pressure easing
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-13885, delta=-1204, z=-7.82 -> demand pressure easing
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.27 -> generation-mix component moved
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.52 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.55 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.57 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.60 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=476, 2026-09-16T12:35:39.857057Z)
- `FUELINST|fuelType=NPSHYD|generation` = **353** (n=476, 2026-09-16T12:35:39.857057Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3295** (n=476, 2026-09-16T12:35:39.857057Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=476, 2026-09-16T12:35:39.857057Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=476, 2026-09-16T12:35:39.857057Z)
- `FUELINST|fuelType=OTHER|generation` = **506** (n=476, 2026-09-16T12:35:39.857057Z)
- `FUELINST|fuelType=PS|generation` = **-5** (n=476, 2026-09-16T12:35:39.857057Z)
- `FUELINST|fuelType=WIND|generation` = **3883** (n=476, 2026-09-16T12:35:39.857057Z)
- `IMBALNGC|TOTAL|imbalance` = **6066** (n=78, 2026-09-16T12:23:48.551845Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=78, 2026-09-16T12:23:32.543133Z)
- `INDGEN|TOTAL|generation` = **24846** (n=78, 2026-09-16T12:23:32.543133Z)
- `MELNGC|TOTAL|margin` = **35500** (n=78, 2026-09-16T12:20:37.764961Z)
- `NDF|TOTAL|demand` = **18280** (n=80, 2026-09-16T12:18:18.459111Z)
- `TSDF|TOTAL|demand` = **18780** (n=80, 2026-09-16T12:18:18.459111Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T12:36:27.714221Z` — **MID**: 0 rows; marker `2026-09-16T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T12:36:12.010604Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:35:45Z`
- `2026-09-16T12:35:39.857057Z` — **FUELINST**: 80 rows; marker `2026-09-16T12:35:00Z`
- `2026-09-16T12:34:19.972961Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:33:45Z`
- `2026-09-16T12:32:28.238878Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:31:45Z`
- `2026-09-16T12:30:41.513478Z` — **FUELHH**: 20 rows; marker `2026-09-16T12:30:00Z`
- `2026-09-16T12:30:41.513478Z` — **FUELINST**: 80 rows; marker `2026-09-16T12:30:00Z`
- `2026-09-16T12:30:25.126294Z` — **WINDFOR**: 73 rows; marker `2026-09-16T12:30:00Z`
- `2026-09-16T12:30:09.338004Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:29:45Z`
- `2026-09-16T12:28:17.403199Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:27:45Z`
- `2026-09-16T12:26:11.749139Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:25:45Z`
- `2026-09-16T12:25:23.732227Z` — **FUELINST**: 80 rows; marker `2026-09-16T12:25:00Z`
- `2026-09-16T12:24:20.274803Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:23:45Z`
- `2026-09-16T12:23:48.551845Z` — **IMBALNGC**: 1422 rows; marker `2026-09-16T12:17:00Z`
- `2026-09-16T12:23:32.543133Z` — **INDGEN**: 1422 rows; marker `2026-09-16T12:17:00Z`
