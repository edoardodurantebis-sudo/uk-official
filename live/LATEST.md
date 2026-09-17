# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T20:43:05.691352Z`  
Current process started UTC: `2026-09-17T20:39:04.845830Z`  
1-second metadata polls in this process: **232**  
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

- `FUELINST|fuelType=INTVKL|generation` = **728** (n=830, 2026-09-17T20:40:30.951554Z)
- `FUELINST|fuelType=NPSHYD|generation` = **558** (n=830, 2026-09-17T20:40:30.951554Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=830, 2026-09-17T20:40:30.951554Z)
- `FUELINST|fuelType=OCGT|generation` = **38** (n=830, 2026-09-17T20:40:30.951554Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=830, 2026-09-17T20:40:30.951554Z)
- `FUELINST|fuelType=OTHER|generation` = **413** (n=830, 2026-09-17T20:40:30.951554Z)
- `FUELINST|fuelType=PS|generation` = **354** (n=830, 2026-09-17T20:40:30.951554Z)
- `FUELINST|fuelType=WIND|generation` = **15542** (n=830, 2026-09-17T20:40:30.951554Z)
- `IMBALNGC|TOTAL|imbalance` = **9686** (n=137, 2026-09-17T20:23:01.759732Z)
- `INDDEM|TOTAL|demand` = **-11161** (n=137, 2026-09-17T20:22:29.150648Z)
- `INDGEN|TOTAL|generation` = **26500** (n=137, 2026-09-17T20:22:29.150648Z)
- `MELNGC|TOTAL|margin` = **36451** (n=137, 2026-09-17T20:20:13.977200Z)
- `NDF|TOTAL|demand` = **16314** (n=140, 2026-09-17T20:18:03.614644Z)
- `TSDF|TOTAL|demand` = **16814** (n=140, 2026-09-17T20:18:03.614644Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T20:43:04.738836Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:43:03.738705Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:43:02.738633Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:43:01.738537Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:43:00.738409Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:42:59.738299Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:42:58.738166Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:42:57.738092Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:42:56.737969Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:42:55.737833Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:42:54.460692Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:42:53.460612Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:42:52.460516Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:42:51.460422Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:42:50.460283Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
