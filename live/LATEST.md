# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T13:13:45.562808Z`  
Current process started UTC: `2026-09-18T13:09:45.422955Z`  
1-second metadata polls in this process: **225**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1389** (n=1028, 2026-09-18T13:10:38.221744Z)
- `FUELINST|fuelType=NPSHYD|generation` = **319** (n=1028, 2026-09-18T13:10:38.221744Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3340** (n=1028, 2026-09-18T13:10:38.221744Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1028, 2026-09-18T13:10:38.221744Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1028, 2026-09-18T13:10:38.221744Z)
- `FUELINST|fuelType=OTHER|generation` = **676** (n=1028, 2026-09-18T13:10:38.221744Z)
- `FUELINST|fuelType=PS|generation` = **-703** (n=1028, 2026-09-18T13:10:38.221744Z)
- `FUELINST|fuelType=WIND|generation` = **14940** (n=1028, 2026-09-18T13:10:38.221744Z)
- `IMBALNGC|TOTAL|imbalance` = **8939** (n=169, 2026-09-18T12:54:54.509238Z)
- `INDDEM|TOTAL|demand` = **-10745** (n=169, 2026-09-18T12:54:38.671500Z)
- `INDGEN|TOTAL|generation` = **25609** (n=169, 2026-09-18T12:54:38.671500Z)
- `MELNGC|TOTAL|margin` = **38104** (n=169, 2026-09-18T12:51:19.340925Z)
- `NDF|TOTAL|demand` = **16170** (n=173, 2026-09-18T12:48:33.598652Z)
- `TSDF|TOTAL|demand` = **16670** (n=173, 2026-09-18T12:48:33.598652Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T13:13:44.571717Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:13:43.558125Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:13:42.550059Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:13:41.549988Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:13:40.540167Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:13:39.500717Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:13:38.500649Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:13:37.485724Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:13:36.475491Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:13:35.464264Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:13:34.444087Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:13:33.143238Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:13:32.140981Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:13:31.132331Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:13:30.073350Z` — **MID**: 0 rows; marker `2026-09-18T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
