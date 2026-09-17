# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T21:12:33.064110Z`  
Current process started UTC: `2026-09-17T21:08:32.355601Z`  
1-second metadata polls in this process: **174**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **424** (n=836, 2026-09-17T21:10:27.210728Z)
- `FUELINST|fuelType=NPSHYD|generation` = **529** (n=836, 2026-09-17T21:10:27.210728Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3320** (n=836, 2026-09-17T21:10:27.210728Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=836, 2026-09-17T21:10:27.210728Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=836, 2026-09-17T21:10:27.210728Z)
- `FUELINST|fuelType=OTHER|generation` = **558** (n=836, 2026-09-17T21:10:27.210728Z)
- `FUELINST|fuelType=PS|generation` = **353** (n=836, 2026-09-17T21:10:27.210728Z)
- `FUELINST|fuelType=WIND|generation` = **15132** (n=836, 2026-09-17T21:10:27.210728Z)
- `IMBALNGC|TOTAL|imbalance` = **9702** (n=138, 2026-09-17T20:52:31.535620Z)
- `INDDEM|TOTAL|demand` = **-11159** (n=138, 2026-09-17T20:52:15.731180Z)
- `INDGEN|TOTAL|generation` = **26516** (n=138, 2026-09-17T20:52:15.731180Z)
- `MELNGC|TOTAL|margin` = **36461** (n=138, 2026-09-17T20:50:14.374453Z)
- `NDF|TOTAL|demand` = **16314** (n=141, 2026-09-17T20:47:47.507721Z)
- `TSDF|TOTAL|demand` = **16814** (n=141, 2026-09-17T20:47:47.507721Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T21:12:31.738852Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:12:30.444624Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:12:29.071376Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:12:27.756527Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:12:26.427472Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:12:25.132776Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:12:23.833827Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:12:20.992061Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:12:20.992061Z` — **FREQ**: 5761 rows; marker `2026-09-17T21:11:45Z`
- `2026-09-17T21:12:19.613995Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:12:18.296297Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:12:17.025639Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:12:15.652888Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:12:14.343593Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:12:13.005086Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
