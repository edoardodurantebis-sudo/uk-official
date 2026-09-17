# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T20:13:38.561149Z`  
Current process started UTC: `2026-09-17T20:09:37.055050Z`  
1-second metadata polls in this process: **143**  
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

- `FUELINST|fuelType=INTVKL|generation` = **728** (n=824, 2026-09-17T20:10:26.608985Z)
- `FUELINST|fuelType=NPSHYD|generation` = **576** (n=824, 2026-09-17T20:10:26.608985Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3317** (n=824, 2026-09-17T20:10:26.608985Z)
- `FUELINST|fuelType=OCGT|generation` = **38** (n=824, 2026-09-17T20:10:26.608985Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=824, 2026-09-17T20:10:26.608985Z)
- `FUELINST|fuelType=OTHER|generation` = **644** (n=824, 2026-09-17T20:10:26.608985Z)
- `FUELINST|fuelType=PS|generation` = **502** (n=824, 2026-09-17T20:10:26.608985Z)
- `FUELINST|fuelType=WIND|generation` = **15991** (n=824, 2026-09-17T20:10:26.608985Z)
- `IMBALNGC|TOTAL|imbalance` = **9708** (n=136, 2026-09-17T19:53:01.099555Z)
- `INDDEM|TOTAL|demand` = **-11160** (n=136, 2026-09-17T19:52:45.276545Z)
- `INDGEN|TOTAL|generation` = **26522** (n=136, 2026-09-17T19:52:45.276545Z)
- `MELNGC|TOTAL|margin` = **36519** (n=136, 2026-09-17T19:50:44.130170Z)
- `NDF|TOTAL|demand` = **16314** (n=139, 2026-09-17T19:48:10.710850Z)
- `TSDF|TOTAL|demand` = **16814** (n=139, 2026-09-17T19:48:10.710850Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T20:13:36.992820Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:13:35.404258Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:13:33.832342Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:13:32.224384Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:13:30.652480Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:13:28.784068Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:13:27.130590Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:13:25.576356Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:13:24.012573Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:13:22.443283Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:13:20.852072Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:13:19.254277Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:13:17.703408Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:13:16.152579Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:13:14.586749Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
