# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T16:17:31.227724Z`  
Current process started UTC: `2026-09-17T16:13:30.570051Z`  
1-second metadata polls in this process: **222**  
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

- `FUELINST|fuelType=INTVKL|generation` = **389** (n=777, 2026-09-17T16:15:27.327649Z)
- `FUELINST|fuelType=NPSHYD|generation` = **425** (n=777, 2026-09-17T16:15:27.327649Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3309** (n=777, 2026-09-17T16:15:27.327649Z)
- `FUELINST|fuelType=OCGT|generation` = **51** (n=777, 2026-09-17T16:15:27.327649Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=777, 2026-09-17T16:15:27.327649Z)
- `FUELINST|fuelType=OTHER|generation` = **1120** (n=777, 2026-09-17T16:15:27.327649Z)
- `FUELINST|fuelType=PS|generation` = **-253** (n=777, 2026-09-17T16:15:27.327649Z)
- `FUELINST|fuelType=WIND|generation` = **13879** (n=777, 2026-09-17T16:15:27.327649Z)
- `IMBALNGC|TOTAL|imbalance` = **11642** (n=128, 2026-09-17T15:54:55.997739Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=128, 2026-09-17T15:54:24.168455Z)
- `INDGEN|TOTAL|generation` = **28456** (n=128, 2026-09-17T15:54:40.409047Z)
- `MELNGC|TOTAL|margin` = **36684** (n=128, 2026-09-17T15:51:59.800251Z)
- `NDF|TOTAL|demand` = **16314** (n=131, 2026-09-17T15:48:34.023613Z)
- `TSDF|TOTAL|demand` = **16814** (n=131, 2026-09-17T15:48:34.023613Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T16:17:30.002877Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:17:29.002795Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:17:28.002682Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:17:27.002570Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:17:26.002501Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:17:25.002382Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:17:24.002265Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:17:22.696582Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:17:21.696464Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:17:20.696384Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:17:19.696264Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:17:18.446990Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:17:17.446873Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:17:16.441767Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:17:15.441688Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
