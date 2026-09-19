# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T08:09:55.185956Z`  
Current process started UTC: `2026-09-19T08:05:54.259855Z`  
1-second metadata polls in this process: **224**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1042** (n=1211, 2026-09-19T08:05:54.259864Z)
- `FUELINST|fuelType=NPSHYD|generation` = **372** (n=1211, 2026-09-19T08:05:54.259864Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1211, 2026-09-19T08:05:54.259864Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1211, 2026-09-19T08:05:54.259864Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1211, 2026-09-19T08:05:54.259864Z)
- `FUELINST|fuelType=OTHER|generation` = **412** (n=1211, 2026-09-19T08:05:54.259864Z)
- `FUELINST|fuelType=PS|generation` = **-689** (n=1211, 2026-09-19T08:05:54.259864Z)
- `FUELINST|fuelType=WIND|generation` = **15537** (n=1211, 2026-09-19T08:05:54.259864Z)
- `IMBALNGC|TOTAL|imbalance` = **8458** (n=199, 2026-09-19T07:20:02.514143Z)
- `INDDEM|TOTAL|demand` = **-12078** (n=199, 2026-09-19T07:19:46.165443Z)
- `INDGEN|TOTAL|generation` = **26869** (n=199, 2026-09-19T07:19:46.165443Z)
- `MELNGC|TOTAL|margin` = **37026** (n=199, 2026-09-19T07:19:09.074847Z)
- `NDF|TOTAL|demand` = **19060** (n=204, 2026-09-19T07:45:58.702458Z)
- `TSDF|TOTAL|demand` = **19560** (n=204, 2026-09-19T07:45:58.702458Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T08:09:53.630650Z` — **MID**: 0 rows; marker `2026-09-19T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:09:52.629973Z` — **MID**: 0 rows; marker `2026-09-19T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:09:51.602169Z` — **MID**: 0 rows; marker `2026-09-19T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:09:50.559840Z` — **MID**: 0 rows; marker `2026-09-19T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:09:49.549499Z` — **MID**: 0 rows; marker `2026-09-19T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:09:48.541599Z` — **MID**: 0 rows; marker `2026-09-19T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:09:47.541504Z` — **MID**: 0 rows; marker `2026-09-19T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:09:46.513739Z` — **MID**: 0 rows; marker `2026-09-19T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:09:45.511305Z` — **MID**: 0 rows; marker `2026-09-19T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:09:44.509141Z` — **MID**: 0 rows; marker `2026-09-19T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:09:43.466613Z` — **MID**: 0 rows; marker `2026-09-19T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:09:42.448184Z` — **MID**: 0 rows; marker `2026-09-19T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:09:41.448099Z` — **MID**: 0 rows; marker `2026-09-19T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:09:40.429286Z` — **MID**: 0 rows; marker `2026-09-19T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:09:39.416287Z` — **MID**: 0 rows; marker `2026-09-19T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
