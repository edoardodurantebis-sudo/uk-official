# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T00:05:15.771675Z`  
Current process started UTC: `2026-09-19T00:01:14.619274Z`  
1-second metadata polls in this process: **132**  
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

- `FUELINST|fuelType=INTVKL|generation` = **601** (n=1114, 2026-09-19T00:00:46.210855Z)
- `FUELINST|fuelType=NPSHYD|generation` = **428** (n=1114, 2026-09-19T00:00:46.210855Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1114, 2026-09-19T00:00:46.210855Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1114, 2026-09-19T00:00:46.210855Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1114, 2026-09-19T00:00:46.210855Z)
- `FUELINST|fuelType=OTHER|generation` = **794** (n=1114, 2026-09-19T00:00:46.210855Z)
- `FUELINST|fuelType=PS|generation` = **-438** (n=1114, 2026-09-19T00:00:46.210855Z)
- `FUELINST|fuelType=WIND|generation` = **15895** (n=1114, 2026-09-19T00:00:46.210855Z)
- `IMBALNGC|TOTAL|imbalance` = **9185** (n=184, 2026-09-18T23:52:06.332276Z)
- `INDDEM|TOTAL|demand` = **-10888** (n=184, 2026-09-18T23:52:06.332276Z)
- `INDGEN|TOTAL|generation` = **26379** (n=184, 2026-09-18T23:52:06.332276Z)
- `MELNGC|TOTAL|margin` = **37509** (n=184, 2026-09-18T23:49:39.728322Z)
- `NDF|TOTAL|demand` = **16550** (n=188, 2026-09-18T23:47:38.844646Z)
- `TSDF|TOTAL|demand` = **17194** (n=188, 2026-09-18T23:47:38.844646Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T00:05:14.076243Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:05:12.373509Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:05:10.610655Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:05:08.911448Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:05:07.163600Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:05:05.474922Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:05:03.751171Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:05:01.526162Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:04:59.775945Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:04:58.061666Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:04:56.343141Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:04:54.638023Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:04:52.936562Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:04:51.232870Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:04:49.478393Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
