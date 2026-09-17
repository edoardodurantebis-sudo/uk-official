# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T08:16:49.690300Z`  
Current process started UTC: `2026-09-17T08:12:48.163985Z`  
1-second metadata polls in this process: **164**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1334** (n=681, 2026-09-17T08:15:32.340871Z)
- `FUELINST|fuelType=NPSHYD|generation` = **419** (n=681, 2026-09-17T08:15:32.340871Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3316** (n=681, 2026-09-17T08:15:32.340871Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=681, 2026-09-17T08:15:32.340871Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=681, 2026-09-17T08:15:32.340871Z)
- `FUELINST|fuelType=OTHER|generation` = **409** (n=681, 2026-09-17T08:15:32.340871Z)
- `FUELINST|fuelType=PS|generation` = **-147** (n=681, 2026-09-17T08:15:32.340871Z)
- `FUELINST|fuelType=WIND|generation` = **15520** (n=681, 2026-09-17T08:15:32.340871Z)
- `IMBALNGC|TOTAL|imbalance` = **7157** (n=112, 2026-09-17T07:19:39.625704Z)
- `INDDEM|TOTAL|demand` = **-12138** (n=112, 2026-09-17T07:19:39.625704Z)
- `INDGEN|TOTAL|generation` = **26528** (n=112, 2026-09-17T07:19:39.625704Z)
- `MELNGC|TOTAL|margin` = **35577** (n=112, 2026-09-17T07:18:19.457722Z)
- `NDF|TOTAL|demand` = **16158** (n=115, 2026-09-17T07:45:46.989663Z)
- `TSDF|TOTAL|demand` = **16658** (n=115, 2026-09-17T07:45:46.989663Z)
- `WINDFOR|TOTAL|generation` = **19265** (n=19, 2026-09-17T05:30:37.912884Z)

## Latest publication events

- `2026-09-17T08:16:48.146717Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:16:46.785717Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:16:45.361372Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:16:44.016394Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:16:42.660719Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:16:41.283166Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:16:39.921710Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:16:38.544403Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:16:36.856901Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:16:34.836887Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:16:33.466794Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:16:32.061042Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:16:30.695420Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:16:29.332668Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:16:27.976507Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
