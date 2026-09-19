# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T11:12:04.757932Z`  
Current process started UTC: `2026-09-19T11:08:04.457453Z`  
1-second metadata polls in this process: **227**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16752, delta=-9313, z=-3.94 -> state changed
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **333** (n=1248, 2026-09-19T11:10:46.116406Z)
- `FUELINST|fuelType=NPSHYD|generation` = **307** (n=1248, 2026-09-19T11:10:46.116406Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1248, 2026-09-19T11:10:46.116406Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1248, 2026-09-19T11:10:46.116406Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1248, 2026-09-19T11:10:46.116406Z)
- `FUELINST|fuelType=OTHER|generation` = **522** (n=1248, 2026-09-19T11:10:46.116406Z)
- `FUELINST|fuelType=PS|generation` = **-809** (n=1248, 2026-09-19T11:10:46.116406Z)
- `FUELINST|fuelType=WIND|generation` = **15778** (n=1248, 2026-09-19T11:10:46.116406Z)
- `IMBALNGC|TOTAL|imbalance` = **-3378** (n=205, 2026-09-19T10:55:05.891910Z)
- `INDDEM|TOTAL|demand` = **-11780** (n=205, 2026-09-19T10:55:05.891910Z)
- `INDGEN|TOTAL|generation` = **16752** (n=205, 2026-09-19T10:55:05.891910Z)
- `MELNGC|TOTAL|margin` = **35551** (n=205, 2026-09-19T10:51:23.218211Z)
- `NDF|TOTAL|demand` = **19631** (n=210, 2026-09-19T10:48:46.270828Z)
- `TSDF|TOTAL|demand` = **20131** (n=210, 2026-09-19T10:49:02.446019Z)
- `WINDFOR|TOTAL|generation` = **6656** (n=36, 2026-09-19T10:30:47.910212Z)

## Latest publication events

- `2026-09-19T11:12:03.788873Z` — **MID**: 0 rows; marker `2026-09-19T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:12:02.779655Z` — **MID**: 0 rows; marker `2026-09-19T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:12:01.779559Z` — **MID**: 0 rows; marker `2026-09-19T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:12:00.765387Z` — **MID**: 0 rows; marker `2026-09-19T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:11:59.765230Z` — **MID**: 0 rows; marker `2026-09-19T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:11:58.765089Z` — **MID**: 0 rows; marker `2026-09-19T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:11:57.764977Z` — **MID**: 0 rows; marker `2026-09-19T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:11:56.662184Z` — **MID**: 0 rows; marker `2026-09-19T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:11:55.662105Z` — **MID**: 0 rows; marker `2026-09-19T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:11:54.550637Z` — **MID**: 0 rows; marker `2026-09-19T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:11:53.550537Z` — **MID**: 0 rows; marker `2026-09-19T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:11:52.550438Z` — **MID**: 0 rows; marker `2026-09-19T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:11:51.038095Z` — **MID**: 0 rows; marker `2026-09-19T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:11:50.038030Z` — **MID**: 0 rows; marker `2026-09-19T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:11:49.037875Z` — **MID**: 0 rows; marker `2026-09-19T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
