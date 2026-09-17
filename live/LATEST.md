# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T18:15:53.228101Z`  
Current process started UTC: `2026-09-17T18:11:52.362537Z`  
1-second metadata polls in this process: **133**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=-1, z=4.71 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=84, delta=7, z=4.84 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=77, delta=66, z=4.46 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=58, delta=2, z=3.72 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.55 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=52, delta=-3, z=3.67 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.58 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=-2, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=0, z=4.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=1, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=57, delta=1, z=4.02 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.99 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=801, 2026-09-17T18:15:34.630577Z)
- `FUELINST|fuelType=NPSHYD|generation` = **620** (n=801, 2026-09-17T18:15:34.630577Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3327** (n=801, 2026-09-17T18:15:34.630577Z)
- `FUELINST|fuelType=OCGT|generation` = **83** (n=801, 2026-09-17T18:15:34.630577Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=801, 2026-09-17T18:15:34.630577Z)
- `FUELINST|fuelType=OTHER|generation` = **1132** (n=801, 2026-09-17T18:15:34.630577Z)
- `FUELINST|fuelType=PS|generation` = **325** (n=801, 2026-09-17T18:15:34.630577Z)
- `FUELINST|fuelType=WIND|generation` = **14899** (n=801, 2026-09-17T18:15:34.630577Z)
- `IMBALNGC|TOTAL|imbalance` = **9672** (n=132, 2026-09-17T17:53:48.152872Z)
- `INDDEM|TOTAL|demand` = **-11283** (n=132, 2026-09-17T17:53:16.406856Z)
- `INDGEN|TOTAL|generation` = **26486** (n=132, 2026-09-17T17:53:16.406856Z)
- `MELNGC|TOTAL|margin` = **36603** (n=132, 2026-09-17T17:50:54.490629Z)
- `NDF|TOTAL|demand` = **16314** (n=135, 2026-09-17T17:48:35.747451Z)
- `TSDF|TOTAL|demand` = **16814** (n=135, 2026-09-17T17:48:35.747451Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T18:15:50.924454Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:15:49.190958Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:15:46.941577Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:15:45.228227Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:15:43.520368Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:15:41.798803Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:15:40.074863Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:15:38.366712Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:15:34.630577Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:15:34.630577Z` — **FUELINST**: 80 rows; marker `2026-09-17T18:15:00Z`
- `2026-09-17T18:15:32.923406Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:15:31.216797Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:15:29.504364Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:15:27.794887Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:15:26.033014Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
