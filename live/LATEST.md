# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T16:13:19.852529Z`  
Current process started UTC: `2026-09-17T16:09:19.761360Z`  
1-second metadata polls in this process: **136**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=-2, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=0, z=4.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=1, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=57, delta=1, z=4.02 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=14, z=4.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.03 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.13 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.23 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=42, delta=42, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=1, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=2, z=4.25 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **389** (n=776, 2026-09-17T16:10:39.143551Z)
- `FUELINST|fuelType=NPSHYD|generation` = **407** (n=776, 2026-09-17T16:10:39.143551Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3310** (n=776, 2026-09-17T16:10:39.143551Z)
- `FUELINST|fuelType=OCGT|generation` = **51** (n=776, 2026-09-17T16:10:39.143551Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=776, 2026-09-17T16:10:39.143551Z)
- `FUELINST|fuelType=OTHER|generation` = **1034** (n=776, 2026-09-17T16:10:39.143551Z)
- `FUELINST|fuelType=PS|generation` = **-252** (n=776, 2026-09-17T16:10:39.143551Z)
- `FUELINST|fuelType=WIND|generation` = **13902** (n=776, 2026-09-17T16:10:39.143551Z)
- `IMBALNGC|TOTAL|imbalance` = **11642** (n=128, 2026-09-17T15:54:55.997739Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=128, 2026-09-17T15:54:24.168455Z)
- `INDGEN|TOTAL|generation` = **28456** (n=128, 2026-09-17T15:54:40.409047Z)
- `MELNGC|TOTAL|margin` = **36684** (n=128, 2026-09-17T15:51:59.800251Z)
- `NDF|TOTAL|demand` = **16314** (n=131, 2026-09-17T15:48:34.023613Z)
- `TSDF|TOTAL|demand` = **16814** (n=131, 2026-09-17T15:48:34.023613Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T16:13:17.779563Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:13:16.091545Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:13:14.417404Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:13:12.723974Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:13:11.045781Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:13:09.370703Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:13:07.696605Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:13:06.024002Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:13:04.358346Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:13:02.261882Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:13:00.583977Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:12:58.900840Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:12:57.232633Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:12:55.579698Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:12:53.918365Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
