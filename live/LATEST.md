# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T07:15:19.605471Z`  
Current process started UTC: `2026-09-19T07:11:19.077129Z`  
1-second metadata polls in this process: **134**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1407** (n=1200, 2026-09-19T07:10:35.803006Z)
- `FUELINST|fuelType=NPSHYD|generation` = **368** (n=1200, 2026-09-19T07:10:35.803006Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1200, 2026-09-19T07:10:35.803006Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1200, 2026-09-19T07:10:35.803006Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1200, 2026-09-19T07:10:35.803006Z)
- `FUELINST|fuelType=OTHER|generation` = **323** (n=1200, 2026-09-19T07:10:35.803006Z)
- `FUELINST|fuelType=PS|generation` = **-192** (n=1200, 2026-09-19T07:10:35.803006Z)
- `FUELINST|fuelType=WIND|generation` = **15707** (n=1200, 2026-09-19T07:10:35.803006Z)
- `IMBALNGC|TOTAL|imbalance` = **9478** (n=198, 2026-09-19T06:50:13.925182Z)
- `INDDEM|TOTAL|demand` = **-11352** (n=198, 2026-09-19T06:50:13.925182Z)
- `INDGEN|TOTAL|generation` = **26907** (n=198, 2026-09-19T06:50:13.925182Z)
- `MELNGC|TOTAL|margin` = **38030** (n=198, 2026-09-19T06:49:00.398728Z)
- `NDF|TOTAL|demand` = **16550** (n=202, 2026-09-19T06:47:06.856404Z)
- `TSDF|TOTAL|demand` = **17429** (n=202, 2026-09-19T06:47:06.856404Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T07:15:17.349992Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:15:15.613760Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:15:13.867448Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:15:12.157471Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:15:10.402040Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:15:08.685956Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:15:06.962359Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:15:05.259747Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:15:03.543376Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:15:01.238874Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:14:59.522100Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:14:57.782060Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:14:56.062707Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:14:54.326420Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:14:52.622201Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
