# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T07:06:54.493008Z`  
Current process started UTC: `2026-09-19T07:02:54.383524Z`  
1-second metadata polls in this process: **219**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-10744, delta=3052, z=1.92 -> demand pressure up
- **WINDFOR** `TOTAL` `generation` — wind forecast [TOTAL] generation: value=7845, delta=-11023, z=-4.38 -> renewable cushion down / residual-load pressure up
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=80, delta=-38, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=97, delta=-21, z=4.20 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.28 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=118, delta=27, z=6.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.70 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=-1, z=5.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=0, z=6.01 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=91, delta=9, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=11, z=6.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=108, delta=29, z=5.66 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1107** (n=1199, 2026-09-19T07:05:33.874196Z)
- `FUELINST|fuelType=NPSHYD|generation` = **369** (n=1199, 2026-09-19T07:05:33.874196Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1199, 2026-09-19T07:05:33.874196Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1199, 2026-09-19T07:05:33.874196Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1199, 2026-09-19T07:05:33.874196Z)
- `FUELINST|fuelType=OTHER|generation` = **416** (n=1199, 2026-09-19T07:05:33.874196Z)
- `FUELINST|fuelType=PS|generation` = **-298** (n=1199, 2026-09-19T07:05:33.874196Z)
- `FUELINST|fuelType=WIND|generation` = **15776** (n=1199, 2026-09-19T07:05:33.874196Z)
- `IMBALNGC|TOTAL|imbalance` = **9478** (n=198, 2026-09-19T06:50:13.925182Z)
- `INDDEM|TOTAL|demand` = **-11352** (n=198, 2026-09-19T06:50:13.925182Z)
- `INDGEN|TOTAL|generation` = **26907** (n=198, 2026-09-19T06:50:13.925182Z)
- `MELNGC|TOTAL|margin` = **38030** (n=198, 2026-09-19T06:49:00.398728Z)
- `NDF|TOTAL|demand` = **16550** (n=202, 2026-09-19T06:47:06.856404Z)
- `TSDF|TOTAL|demand` = **17429** (n=202, 2026-09-19T06:47:06.856404Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T07:06:52.876939Z` — **MID**: 0 rows; marker `2026-09-19T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:06:51.847898Z` — **MID**: 0 rows; marker `2026-09-19T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:06:50.847824Z` — **MID**: 0 rows; marker `2026-09-19T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:06:49.845721Z` — **MID**: 0 rows; marker `2026-09-19T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:06:48.826801Z` — **MID**: 0 rows; marker `2026-09-19T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:06:47.826730Z` — **MID**: 0 rows; marker `2026-09-19T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:06:46.821265Z` — **MID**: 0 rows; marker `2026-09-19T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:06:45.821161Z` — **MID**: 0 rows; marker `2026-09-19T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:06:44.800857Z` — **MID**: 0 rows; marker `2026-09-19T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:06:43.800781Z` — **MID**: 0 rows; marker `2026-09-19T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:06:42.789305Z` — **MID**: 0 rows; marker `2026-09-19T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:06:41.781267Z` — **MID**: 0 rows; marker `2026-09-19T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:06:40.755867Z` — **MID**: 0 rows; marker `2026-09-19T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:06:39.734099Z` — **MID**: 0 rows; marker `2026-09-19T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:06:38.717308Z` — **MID**: 0 rows; marker `2026-09-19T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
