# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T06:37:23.292694Z`  
Current process started UTC: `2026-09-19T06:33:23.095174Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **357** (n=1193, 2026-09-19T06:35:48.026786Z)
- `FUELINST|fuelType=NPSHYD|generation` = **368** (n=1193, 2026-09-19T06:35:48.026786Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1193, 2026-09-19T06:35:48.026786Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1193, 2026-09-19T06:35:48.026786Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1193, 2026-09-19T06:35:48.026786Z)
- `FUELINST|fuelType=OTHER|generation` = **1071** (n=1193, 2026-09-19T06:35:48.026786Z)
- `FUELINST|fuelType=PS|generation` = **-481** (n=1193, 2026-09-19T06:35:48.026786Z)
- `FUELINST|fuelType=WIND|generation` = **15804** (n=1193, 2026-09-19T06:35:48.026786Z)
- `IMBALNGC|TOTAL|imbalance` = **9725** (n=197, 2026-09-19T06:21:03.713324Z)
- `INDDEM|TOTAL|demand` = **-10863** (n=197, 2026-09-19T06:20:47.840036Z)
- `INDGEN|TOTAL|generation` = **26914** (n=197, 2026-09-19T06:21:03.713324Z)
- `MELNGC|TOTAL|margin` = **38283** (n=197, 2026-09-19T06:19:39.477513Z)
- `NDF|TOTAL|demand` = **16550** (n=201, 2026-09-19T06:17:40.734662Z)
- `TSDF|TOTAL|demand` = **17190** (n=201, 2026-09-19T06:17:40.734662Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T06:37:22.317171Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:37:21.317055Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:37:20.316939Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:37:19.316820Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:37:18.316701Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:37:17.316583Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:37:16.316467Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:37:15.316384Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:37:14.316270Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:37:13.316152Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:37:12.316066Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:37:11.315949Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:37:10.276539Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:37:09.276420Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:37:07.691720Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
