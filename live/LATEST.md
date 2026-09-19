# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T07:27:59.734595Z`  
Current process started UTC: `2026-09-19T07:23:58.953813Z`  
1-second metadata polls in this process: **136**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1421** (n=1203, 2026-09-19T07:25:34.306989Z)
- `FUELINST|fuelType=NPSHYD|generation` = **375** (n=1203, 2026-09-19T07:25:34.306989Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1203, 2026-09-19T07:25:34.306989Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1203, 2026-09-19T07:25:34.306989Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1203, 2026-09-19T07:25:34.306989Z)
- `FUELINST|fuelType=OTHER|generation` = **524** (n=1203, 2026-09-19T07:25:34.306989Z)
- `FUELINST|fuelType=PS|generation` = **-420** (n=1203, 2026-09-19T07:25:34.306989Z)
- `FUELINST|fuelType=WIND|generation` = **15754** (n=1203, 2026-09-19T07:25:34.306989Z)
- `IMBALNGC|TOTAL|imbalance` = **8458** (n=199, 2026-09-19T07:20:02.514143Z)
- `INDDEM|TOTAL|demand` = **-12078** (n=199, 2026-09-19T07:19:46.165443Z)
- `INDGEN|TOTAL|generation` = **26869** (n=199, 2026-09-19T07:19:46.165443Z)
- `MELNGC|TOTAL|margin` = **37026** (n=199, 2026-09-19T07:19:09.074847Z)
- `NDF|TOTAL|demand` = **16550** (n=203, 2026-09-19T07:17:28.186180Z)
- `TSDF|TOTAL|demand` = **18412** (n=203, 2026-09-19T07:17:28.186180Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T07:27:58.051303Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:27:55.650392Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:27:53.970961Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:27:52.330674Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:27:50.630282Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:27:48.916011Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:27:47.224020Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:27:45.525164Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:27:43.859920Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:27:42.183119Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:27:40.133368Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:27:38.350733Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:27:36.665070Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:27:34.977899Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:27:33.280079Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
