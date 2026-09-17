# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T18:32:46.899748Z`  
Current process started UTC: `2026-09-17T18:28:45.880878Z`  
1-second metadata polls in this process: **144**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=82, delta=45, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.58 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=-1, z=4.71 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=84, delta=7, z=4.84 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=77, delta=66, z=4.46 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=58, delta=2, z=3.72 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.55 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=52, delta=-3, z=3.67 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.58 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=-2, z=3.82 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=804, 2026-09-17T18:30:23.263617Z)
- `FUELINST|fuelType=NPSHYD|generation` = **620** (n=804, 2026-09-17T18:30:23.263617Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3323** (n=804, 2026-09-17T18:30:23.263617Z)
- `FUELINST|fuelType=OCGT|generation` = **83** (n=804, 2026-09-17T18:30:23.263617Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=804, 2026-09-17T18:30:23.263617Z)
- `FUELINST|fuelType=OTHER|generation` = **1304** (n=804, 2026-09-17T18:30:23.263617Z)
- `FUELINST|fuelType=PS|generation` = **279** (n=804, 2026-09-17T18:30:23.263617Z)
- `FUELINST|fuelType=WIND|generation` = **15007** (n=804, 2026-09-17T18:30:23.263617Z)
- `IMBALNGC|TOTAL|imbalance` = **9682** (n=133, 2026-09-17T18:24:32.722523Z)
- `INDDEM|TOTAL|demand` = **-11254** (n=133, 2026-09-17T18:24:12.670545Z)
- `INDGEN|TOTAL|generation` = **26496** (n=133, 2026-09-17T18:24:12.670545Z)
- `MELNGC|TOTAL|margin` = **36584** (n=133, 2026-09-17T18:21:20.240550Z)
- `NDF|TOTAL|demand` = **16314** (n=136, 2026-09-17T18:18:46.937615Z)
- `TSDF|TOTAL|demand` = **16814** (n=136, 2026-09-17T18:18:46.937615Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T18:32:45.356542Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:32:43.787290Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:32:42.183523Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:32:40.603713Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:32:39.036368Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:32:37.439601Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:32:35.786961Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:32:33.761379Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:32:32.159790Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:32:30.459778Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:32:28.885133Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:32:27.350176Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:32:25.767933Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:32:24.170100Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:32:22.558189Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
