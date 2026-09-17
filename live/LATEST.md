# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T09:11:33.869541Z`  
Current process started UTC: `2026-09-17T09:07:33.604348Z`  
1-second metadata polls in this process: **232**  
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

- `FUELINST|fuelType=INTVKL|generation` = **741** (n=692, 2026-09-17T09:10:32.728448Z)
- `FUELINST|fuelType=NPSHYD|generation` = **363** (n=692, 2026-09-17T09:10:32.728448Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=692, 2026-09-17T09:10:32.728448Z)
- `FUELINST|fuelType=OCGT|generation` = **2** (n=692, 2026-09-17T09:10:32.728448Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=692, 2026-09-17T09:10:32.728448Z)
- `FUELINST|fuelType=OTHER|generation` = **674** (n=692, 2026-09-17T09:10:32.728448Z)
- `FUELINST|fuelType=PS|generation` = **-557** (n=692, 2026-09-17T09:10:32.728448Z)
- `FUELINST|fuelType=WIND|generation` = **15687** (n=692, 2026-09-17T09:10:32.728448Z)
- `IMBALNGC|TOTAL|imbalance` = **7441** (n=114, 2026-09-17T08:49:36.456573Z)
- `INDDEM|TOTAL|demand` = **-12127** (n=114, 2026-09-17T08:49:19.589745Z)
- `INDGEN|TOTAL|generation` = **26447** (n=114, 2026-09-17T08:49:36.456573Z)
- `MELNGC|TOTAL|margin` = **36058** (n=114, 2026-09-17T08:49:03.558387Z)
- `NDF|TOTAL|demand` = **18256** (n=117, 2026-09-17T08:46:53.329886Z)
- `TSDF|TOTAL|demand` = **19006** (n=117, 2026-09-17T08:46:53.329886Z)
- `WINDFOR|TOTAL|generation` = **19255** (n=20, 2026-09-17T08:30:43.563030Z)

## Latest publication events

- `2026-09-17T09:11:32.921776Z` — **MID**: 0 rows; marker `2026-09-17T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:11:31.921639Z` — **MID**: 0 rows; marker `2026-09-17T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:11:30.921554Z` — **MID**: 0 rows; marker `2026-09-17T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:11:29.921474Z` — **MID**: 0 rows; marker `2026-09-17T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:11:28.921373Z` — **MID**: 0 rows; marker `2026-09-17T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:11:27.921299Z` — **MID**: 0 rows; marker `2026-09-17T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:11:26.921203Z` — **MID**: 0 rows; marker `2026-09-17T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:11:25.921077Z` — **MID**: 0 rows; marker `2026-09-17T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:11:24.920975Z` — **MID**: 0 rows; marker `2026-09-17T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:11:23.920841Z` — **MID**: 0 rows; marker `2026-09-17T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:11:22.920752Z` — **MID**: 0 rows; marker `2026-09-17T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:11:21.920647Z` — **MID**: 0 rows; marker `2026-09-17T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:11:20.686598Z` — **MID**: 0 rows; marker `2026-09-17T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:11:19.686466Z` — **MID**: 0 rows; marker `2026-09-17T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:11:18.686373Z` — **MID**: 0 rows; marker `2026-09-17T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
