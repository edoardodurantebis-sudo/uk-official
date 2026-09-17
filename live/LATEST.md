# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T08:08:23.108432Z`  
Current process started UTC: `2026-09-17T08:04:23.005255Z`  
1-second metadata polls in this process: **134**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16658, delta=-2713, z=-4.41 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16158, delta=-2463, z=-4.57 -> demand pressure easing
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=2, delta=-50, z=-0.16 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=-4, z=3.91 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.36 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=1, z=4.42 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=49, delta=49, z=4.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=3, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=1, z=4.21 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=0, z=4.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=0, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=17, z=4.30 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-1134, delta=10, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1114, delta=62, z=-3.54 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1344** (n=679, 2026-09-17T08:05:28.464902Z)
- `FUELINST|fuelType=NPSHYD|generation` = **420** (n=679, 2026-09-17T08:05:28.464902Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=679, 2026-09-17T08:05:28.464902Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=679, 2026-09-17T08:05:28.464902Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=679, 2026-09-17T08:05:28.464902Z)
- `FUELINST|fuelType=OTHER|generation` = **385** (n=679, 2026-09-17T08:05:28.464902Z)
- `FUELINST|fuelType=PS|generation` = **18** (n=679, 2026-09-17T08:05:28.464902Z)
- `FUELINST|fuelType=WIND|generation` = **15462** (n=679, 2026-09-17T08:05:28.464902Z)
- `IMBALNGC|TOTAL|imbalance` = **7157** (n=112, 2026-09-17T07:19:39.625704Z)
- `INDDEM|TOTAL|demand` = **-12138** (n=112, 2026-09-17T07:19:39.625704Z)
- `INDGEN|TOTAL|generation` = **26528** (n=112, 2026-09-17T07:19:39.625704Z)
- `MELNGC|TOTAL|margin` = **35577** (n=112, 2026-09-17T07:18:19.457722Z)
- `NDF|TOTAL|demand` = **16158** (n=115, 2026-09-17T07:45:46.989663Z)
- `TSDF|TOTAL|demand` = **16658** (n=115, 2026-09-17T07:45:46.989663Z)
- `WINDFOR|TOTAL|generation` = **19265** (n=19, 2026-09-17T05:30:37.912884Z)

## Latest publication events

- `2026-09-17T08:08:21.383666Z` — **MID**: 0 rows; marker `2026-09-17T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:08:19.667099Z` — **MID**: 0 rows; marker `2026-09-17T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:08:17.964182Z` — **MID**: 0 rows; marker `2026-09-17T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:08:16.197830Z` — **MID**: 0 rows; marker `2026-09-17T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:08:14.445709Z` — **MID**: 0 rows; marker `2026-09-17T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:08:12.728888Z` — **MID**: 0 rows; marker `2026-09-17T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:08:10.997876Z` — **MID**: 0 rows; marker `2026-09-17T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:08:07.247919Z` — **MID**: 0 rows; marker `2026-09-17T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:08:07.247919Z` — **FREQ**: 5761 rows; marker `2026-09-17T08:07:45Z`
- `2026-09-17T08:08:05.538057Z` — **MID**: 0 rows; marker `2026-09-17T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:08:03.805413Z` — **MID**: 0 rows; marker `2026-09-17T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:08:02.096118Z` — **MID**: 0 rows; marker `2026-09-17T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:08:00.356315Z` — **MID**: 0 rows; marker `2026-09-17T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:07:58.650053Z` — **MID**: 0 rows; marker `2026-09-17T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:07:56.919739Z` — **MID**: 0 rows; marker `2026-09-17T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
