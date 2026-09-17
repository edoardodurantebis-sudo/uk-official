# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T19:06:26.403704Z`  
Current process started UTC: `2026-09-17T19:02:25.651404Z`  
1-second metadata polls in this process: **159**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=0, z=6.01 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1412** (n=811, 2026-09-17T19:05:43.227798Z)
- `FUELINST|fuelType=NPSHYD|generation` = **635** (n=811, 2026-09-17T19:05:43.227798Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=811, 2026-09-17T19:05:43.227798Z)
- `FUELINST|fuelType=OCGT|generation` = **119** (n=811, 2026-09-17T19:05:43.227798Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=811, 2026-09-17T19:05:43.227798Z)
- `FUELINST|fuelType=OTHER|generation` = **879** (n=811, 2026-09-17T19:05:43.227798Z)
- `FUELINST|fuelType=PS|generation` = **278** (n=811, 2026-09-17T19:05:43.227798Z)
- `FUELINST|fuelType=WIND|generation` = **15228** (n=811, 2026-09-17T19:05:43.227798Z)
- `IMBALNGC|TOTAL|imbalance` = **9701** (n=134, 2026-09-17T18:53:56.215839Z)
- `INDDEM|TOTAL|demand` = **-11160** (n=134, 2026-09-17T18:53:56.215839Z)
- `INDGEN|TOTAL|generation` = **26515** (n=134, 2026-09-17T18:53:56.215839Z)
- `MELNGC|TOTAL|margin` = **36584** (n=134, 2026-09-17T18:51:06.144242Z)
- `NDF|TOTAL|demand` = **16314** (n=137, 2026-09-17T18:48:33.698047Z)
- `TSDF|TOTAL|demand` = **16814** (n=137, 2026-09-17T18:48:33.698047Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T19:06:25.080271Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:06:23.747093Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:06:22.340388Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:06:21.011613Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:06:19.698958Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:06:18.350752Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:06:17.000045Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:06:14.063663Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:06:14.063663Z` — **FREQ**: 5761 rows; marker `2026-09-17T19:05:45Z`
- `2026-09-17T19:06:12.652079Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:06:11.275619Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:06:09.966864Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:06:08.656550Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:06:07.291398Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:06:05.668459Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
