# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T02:37:27.249350Z`  
Current process started UTC: `2026-09-19T02:33:26.948432Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-509** (n=1145, 2026-09-19T02:35:36.475433Z)
- `FUELINST|fuelType=NPSHYD|generation` = **346** (n=1145, 2026-09-19T02:35:36.475433Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1145, 2026-09-19T02:35:36.475433Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1145, 2026-09-19T02:35:36.475433Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1145, 2026-09-19T02:35:36.475433Z)
- `FUELINST|fuelType=OTHER|generation` = **594** (n=1145, 2026-09-19T02:35:36.475433Z)
- `FUELINST|fuelType=PS|generation` = **-667** (n=1145, 2026-09-19T02:35:36.475433Z)
- `FUELINST|fuelType=WIND|generation` = **16242** (n=1145, 2026-09-19T02:35:36.475433Z)
- `IMBALNGC|TOTAL|imbalance` = **9256** (n=189, 2026-09-19T02:21:53.930215Z)
- `INDDEM|TOTAL|demand` = **-10886** (n=189, 2026-09-19T02:21:53.930215Z)
- `INDGEN|TOTAL|generation` = **26451** (n=189, 2026-09-19T02:21:53.930215Z)
- `MELNGC|TOTAL|margin` = **38306** (n=189, 2026-09-19T02:19:37.697156Z)
- `NDF|TOTAL|demand` = **16550** (n=193, 2026-09-19T02:17:41.280152Z)
- `TSDF|TOTAL|demand` = **17194** (n=193, 2026-09-19T02:17:41.280152Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T02:37:26.276123Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:37:25.275996Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:37:24.275881Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:37:23.275768Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:37:22.275653Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:37:21.275527Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:37:20.275410Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:37:19.275288Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:37:18.275180Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:37:17.275053Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:37:16.274990Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:37:15.274858Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:37:13.947472Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:37:12.947342Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:37:11.899217Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
