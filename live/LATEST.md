# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T01:42:42.608626Z`  
Current process started UTC: `2026-09-19T01:38:42.530159Z`  
1-second metadata polls in this process: **145**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-604** (n=1134, 2026-09-19T01:40:35.219084Z)
- `FUELINST|fuelType=NPSHYD|generation` = **370** (n=1134, 2026-09-19T01:40:35.219084Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1134, 2026-09-19T01:40:35.219084Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1134, 2026-09-19T01:40:35.219084Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1134, 2026-09-19T01:40:35.219084Z)
- `FUELINST|fuelType=OTHER|generation` = **267** (n=1134, 2026-09-19T01:40:35.219084Z)
- `FUELINST|fuelType=PS|generation` = **-827** (n=1134, 2026-09-19T01:40:35.219084Z)
- `FUELINST|fuelType=WIND|generation` = **16385** (n=1134, 2026-09-19T01:40:35.219084Z)
- `IMBALNGC|TOTAL|imbalance` = **9206** (n=187, 2026-09-19T01:21:41.895741Z)
- `INDDEM|TOTAL|demand` = **-10886** (n=187, 2026-09-19T01:21:41.895741Z)
- `INDGEN|TOTAL|generation` = **26401** (n=187, 2026-09-19T01:21:41.895741Z)
- `MELNGC|TOTAL|margin` = **37117** (n=187, 2026-09-19T01:19:33.784162Z)
- `NDF|TOTAL|demand` = **16550** (n=191, 2026-09-19T01:17:58.768476Z)
- `TSDF|TOTAL|demand` = **17194** (n=191, 2026-09-19T01:17:58.768476Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T01:42:41.056469Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:42:39.486511Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:42:37.920175Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:42:36.383275Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:42:34.711256Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:42:33.174174Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:42:31.644103Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:42:30.097999Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:42:28.179556Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:42:26.628212Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:42:25.053148Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:42:23.526369Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:42:21.983871Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:42:20.399501Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:42:18.864194Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
