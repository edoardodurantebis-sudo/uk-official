# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T23:31:11.416073Z`  
Current process started UTC: `2026-09-17T23:27:10.997378Z`  
1-second metadata polls in this process: **223**  
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

- `FUELINST|fuelType=INTVKL|generation` = **608** (n=864, 2026-09-17T23:30:47.122302Z)
- `FUELINST|fuelType=NPSHYD|generation` = **450** (n=864, 2026-09-17T23:30:47.122302Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3318** (n=864, 2026-09-17T23:30:47.122302Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=864, 2026-09-17T23:30:47.122302Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=864, 2026-09-17T23:30:47.122302Z)
- `FUELINST|fuelType=OTHER|generation` = **267** (n=864, 2026-09-17T23:30:47.122302Z)
- `FUELINST|fuelType=PS|generation` = **52** (n=864, 2026-09-17T23:30:47.122302Z)
- `FUELINST|fuelType=WIND|generation` = **14614** (n=864, 2026-09-17T23:30:47.122302Z)
- `IMBALNGC|TOTAL|imbalance` = **9745** (n=143, 2026-09-17T23:22:08.151476Z)
- `INDDEM|TOTAL|demand` = **-11183** (n=143, 2026-09-17T23:22:08.151476Z)
- `INDGEN|TOTAL|generation` = **26559** (n=143, 2026-09-17T23:22:08.151476Z)
- `MELNGC|TOTAL|margin` = **36572** (n=143, 2026-09-17T23:20:11.082648Z)
- `NDF|TOTAL|demand` = **16314** (n=146, 2026-09-17T23:18:11.234096Z)
- `TSDF|TOTAL|demand` = **16814** (n=146, 2026-09-17T23:18:11.234096Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-17T23:31:10.437506Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:31:09.437425Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:31:08.411859Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:31:07.411733Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:31:06.411603Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:31:04.939292Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:31:03.212556Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:31:01.931171Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:31:00.931097Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:30:59.887797Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:30:58.691520Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:30:57.646776Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:30:56.581389Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:30:55.581261Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:30:54.581128Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
