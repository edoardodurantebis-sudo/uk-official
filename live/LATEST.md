# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T00:43:06.852515Z`  
Current process started UTC: `2026-09-19T00:39:06.383361Z`  
1-second metadata polls in this process: **194**  
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

- `FUELINST|fuelType=INTVKL|generation` = **126** (n=1122, 2026-09-19T00:40:25.210652Z)
- `FUELINST|fuelType=NPSHYD|generation` = **393** (n=1122, 2026-09-19T00:40:25.210652Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1122, 2026-09-19T00:40:25.210652Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1122, 2026-09-19T00:40:25.210652Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1122, 2026-09-19T00:40:25.210652Z)
- `FUELINST|fuelType=OTHER|generation` = **624** (n=1122, 2026-09-19T00:40:25.210652Z)
- `FUELINST|fuelType=PS|generation` = **-824** (n=1122, 2026-09-19T00:40:25.210652Z)
- `FUELINST|fuelType=WIND|generation` = **16184** (n=1122, 2026-09-19T00:40:25.210652Z)
- `IMBALNGC|TOTAL|imbalance` = **9168** (n=185, 2026-09-19T00:21:52.606846Z)
- `INDDEM|TOTAL|demand` = **-10887** (n=185, 2026-09-19T00:21:36.243148Z)
- `INDGEN|TOTAL|generation` = **26362** (n=185, 2026-09-19T00:21:36.243148Z)
- `MELNGC|TOTAL|margin` = **37515** (n=185, 2026-09-19T00:19:43.103653Z)
- `NDF|TOTAL|demand` = **16550** (n=189, 2026-09-19T00:17:41.916697Z)
- `TSDF|TOTAL|demand` = **17194** (n=189, 2026-09-19T00:17:41.916697Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T00:43:04.469986Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:43:03.309298Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:43:02.115510Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:43:00.955099Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:42:59.755387Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:42:58.606285Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:42:57.435712Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:42:56.261613Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:42:55.111312Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:42:53.910875Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:42:52.711623Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:42:51.531551Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:42:50.364588Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:42:47.766599Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:42:46.566569Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
