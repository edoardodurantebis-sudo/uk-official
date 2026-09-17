# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T19:02:09.786232Z`  
Current process started UTC: `2026-09-17T18:58:08.029251Z`  
1-second metadata polls in this process: **131**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=91, delta=9, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=11, z=6.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=108, delta=29, z=5.66 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=-2, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=81, delta=-2, z=4.34 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=82, delta=45, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.58 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=-1, z=4.71 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=84, delta=7, z=4.84 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=77, delta=66, z=4.46 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=58, delta=2, z=3.72 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=810, 2026-09-17T19:00:33.505410Z)
- `FUELINST|fuelType=NPSHYD|generation` = **634** (n=810, 2026-09-17T19:00:33.505410Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=810, 2026-09-17T19:00:33.505410Z)
- `FUELINST|fuelType=OCGT|generation` = **119** (n=810, 2026-09-17T19:00:33.505410Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=810, 2026-09-17T19:00:33.505410Z)
- `FUELINST|fuelType=OTHER|generation` = **1234** (n=810, 2026-09-17T19:00:33.505410Z)
- `FUELINST|fuelType=PS|generation` = **277** (n=810, 2026-09-17T19:00:33.505410Z)
- `FUELINST|fuelType=WIND|generation` = **15259** (n=810, 2026-09-17T19:00:33.505410Z)
- `IMBALNGC|TOTAL|imbalance` = **9701** (n=134, 2026-09-17T18:53:56.215839Z)
- `INDDEM|TOTAL|demand` = **-11160** (n=134, 2026-09-17T18:53:56.215839Z)
- `INDGEN|TOTAL|generation` = **26515** (n=134, 2026-09-17T18:53:56.215839Z)
- `MELNGC|TOTAL|margin` = **36584** (n=134, 2026-09-17T18:51:06.144242Z)
- `NDF|TOTAL|demand` = **16314** (n=137, 2026-09-17T18:48:33.698047Z)
- `TSDF|TOTAL|demand` = **16814** (n=137, 2026-09-17T18:48:33.698047Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T19:02:08.001213Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:02:06.180165Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:02:04.446084Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:02:02.619628Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:02:00.882962Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:01:59.081737Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:01:57.351353Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:01:54.999389Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:01:53.248509Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:01:51.453374Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:01:49.684861Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:01:47.912975Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:01:46.192071Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:01:44.462150Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:01:42.713739Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
