# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T02:45:51.158083Z`  
Current process started UTC: `2026-09-19T02:41:50.677285Z`  
1-second metadata polls in this process: **198**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-509** (n=1147, 2026-09-19T02:45:34.730491Z)
- `FUELINST|fuelType=NPSHYD|generation` = **346** (n=1147, 2026-09-19T02:45:34.730491Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3343** (n=1147, 2026-09-19T02:45:34.730491Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1147, 2026-09-19T02:45:34.730491Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1147, 2026-09-19T02:45:34.730491Z)
- `FUELINST|fuelType=OTHER|generation` = **497** (n=1147, 2026-09-19T02:45:34.730491Z)
- `FUELINST|fuelType=PS|generation` = **-543** (n=1147, 2026-09-19T02:45:34.730491Z)
- `FUELINST|fuelType=WIND|generation` = **16205** (n=1147, 2026-09-19T02:45:34.730491Z)
- `IMBALNGC|TOTAL|imbalance` = **9256** (n=189, 2026-09-19T02:21:53.930215Z)
- `INDDEM|TOTAL|demand` = **-10886** (n=189, 2026-09-19T02:21:53.930215Z)
- `INDGEN|TOTAL|generation` = **26451** (n=189, 2026-09-19T02:21:53.930215Z)
- `MELNGC|TOTAL|margin` = **38306** (n=189, 2026-09-19T02:19:37.697156Z)
- `NDF|TOTAL|demand` = **16550** (n=193, 2026-09-19T02:17:41.280152Z)
- `TSDF|TOTAL|demand` = **17194** (n=193, 2026-09-19T02:17:41.280152Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T02:45:50.001630Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:45:48.772387Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:45:47.615481Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:45:46.420473Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:45:45.237980Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:45:44.080295Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:45:42.955784Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:45:41.807962Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:45:40.622718Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:45:39.476497Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:45:38.317319Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:45:37.137863Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:45:34.730491Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:45:34.730491Z` — **FUELINST**: 80 rows; marker `2026-09-19T02:45:00Z`
- `2026-09-19T02:45:33.561691Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
