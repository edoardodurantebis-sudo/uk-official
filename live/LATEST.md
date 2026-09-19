# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T01:25:59.139821Z`  
Current process started UTC: `2026-09-19T01:21:58.940630Z`  
1-second metadata polls in this process: **230**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-604** (n=1131, 2026-09-19T01:25:30.425659Z)
- `FUELINST|fuelType=NPSHYD|generation` = **370** (n=1131, 2026-09-19T01:25:30.425659Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1131, 2026-09-19T01:25:30.425659Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1131, 2026-09-19T01:25:30.425659Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1131, 2026-09-19T01:25:30.425659Z)
- `FUELINST|fuelType=OTHER|generation` = **191** (n=1131, 2026-09-19T01:25:30.425659Z)
- `FUELINST|fuelType=PS|generation` = **-832** (n=1131, 2026-09-19T01:25:30.425659Z)
- `FUELINST|fuelType=WIND|generation` = **16357** (n=1131, 2026-09-19T01:25:30.425659Z)
- `IMBALNGC|TOTAL|imbalance` = **9206** (n=187, 2026-09-19T01:21:41.895741Z)
- `INDDEM|TOTAL|demand` = **-10886** (n=187, 2026-09-19T01:21:41.895741Z)
- `INDGEN|TOTAL|generation` = **26401** (n=187, 2026-09-19T01:21:41.895741Z)
- `MELNGC|TOTAL|margin` = **37117** (n=187, 2026-09-19T01:19:33.784162Z)
- `NDF|TOTAL|demand` = **16550** (n=191, 2026-09-19T01:17:58.768476Z)
- `TSDF|TOTAL|demand` = **17194** (n=191, 2026-09-19T01:17:58.768476Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T01:25:58.186984Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:25:57.186845Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:25:56.186721Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:25:55.186586Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:25:54.155104Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:25:53.155019Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:25:52.154887Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:25:51.154746Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:25:50.154601Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:25:49.154444Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:25:48.154321Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:25:46.537833Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:25:45.537697Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:25:44.537574Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:25:43.537445Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
