# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T01:38:31.041736Z`  
Current process started UTC: `2026-09-19T01:34:30.684278Z`  
1-second metadata polls in this process: **156**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-604** (n=1133, 2026-09-19T01:35:36.616448Z)
- `FUELINST|fuelType=NPSHYD|generation` = **371** (n=1133, 2026-09-19T01:35:36.616448Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1133, 2026-09-19T01:35:36.616448Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1133, 2026-09-19T01:35:36.616448Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1133, 2026-09-19T01:35:36.616448Z)
- `FUELINST|fuelType=OTHER|generation` = **224** (n=1133, 2026-09-19T01:35:36.616448Z)
- `FUELINST|fuelType=PS|generation` = **-829** (n=1133, 2026-09-19T01:35:36.616448Z)
- `FUELINST|fuelType=WIND|generation` = **16378** (n=1133, 2026-09-19T01:35:36.616448Z)
- `IMBALNGC|TOTAL|imbalance` = **9206** (n=187, 2026-09-19T01:21:41.895741Z)
- `INDDEM|TOTAL|demand` = **-10886** (n=187, 2026-09-19T01:21:41.895741Z)
- `INDGEN|TOTAL|generation` = **26401** (n=187, 2026-09-19T01:21:41.895741Z)
- `MELNGC|TOTAL|margin` = **37117** (n=187, 2026-09-19T01:19:33.784162Z)
- `NDF|TOTAL|demand` = **16550** (n=191, 2026-09-19T01:17:58.768476Z)
- `TSDF|TOTAL|demand` = **17194** (n=191, 2026-09-19T01:17:58.768476Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T01:38:29.597482Z` — **MID**: 0 rows; marker `2026-09-19T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:38:28.134813Z` — **MID**: 0 rows; marker `2026-09-19T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:38:26.626336Z` — **MID**: 0 rows; marker `2026-09-19T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:38:25.185663Z` — **MID**: 0 rows; marker `2026-09-19T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:38:21.738527Z` — **MID**: 0 rows; marker `2026-09-19T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:38:21.738527Z` — **FREQ**: 5761 rows; marker `2026-09-19T01:37:45Z`
- `2026-09-19T01:38:20.263419Z` — **MID**: 0 rows; marker `2026-09-19T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:38:18.799206Z` — **MID**: 0 rows; marker `2026-09-19T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:38:17.324953Z` — **MID**: 0 rows; marker `2026-09-19T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:38:15.854619Z` — **MID**: 0 rows; marker `2026-09-19T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:38:14.358219Z` — **MID**: 0 rows; marker `2026-09-19T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:38:12.918397Z` — **MID**: 0 rows; marker `2026-09-19T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:38:11.462255Z` — **MID**: 0 rows; marker `2026-09-19T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:38:09.982098Z` — **MID**: 0 rows; marker `2026-09-19T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:38:08.519397Z` — **MID**: 0 rows; marker `2026-09-19T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
