# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T15:52:19.171880Z`  
Current process started UTC: `2026-09-17T15:48:17.406908Z`  
1-second metadata polls in this process: **180**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=1, z=4.14 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-433** (n=772, 2026-09-17T15:50:24.501259Z)
- `FUELINST|fuelType=NPSHYD|generation` = **364** (n=772, 2026-09-17T15:50:24.501259Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3307** (n=772, 2026-09-17T15:50:24.501259Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=772, 2026-09-17T15:50:24.501259Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=772, 2026-09-17T15:50:24.501259Z)
- `FUELINST|fuelType=OTHER|generation` = **847** (n=772, 2026-09-17T15:50:24.501259Z)
- `FUELINST|fuelType=PS|generation` = **-254** (n=772, 2026-09-17T15:50:24.501259Z)
- `FUELINST|fuelType=WIND|generation` = **13863** (n=772, 2026-09-17T15:50:24.501259Z)
- `IMBALNGC|TOTAL|imbalance` = **11656** (n=127, 2026-09-17T15:25:31.201455Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=127, 2026-09-17T15:25:15.240347Z)
- `INDGEN|TOTAL|generation` = **28470** (n=127, 2026-09-17T15:24:58.748219Z)
- `MELNGC|TOTAL|margin` = **36684** (n=128, 2026-09-17T15:51:59.800251Z)
- `NDF|TOTAL|demand` = **16314** (n=131, 2026-09-17T15:48:34.023613Z)
- `TSDF|TOTAL|demand` = **16814** (n=131, 2026-09-17T15:48:34.023613Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T15:52:16.345434Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:52:16.345434Z` — **FREQ**: 5761 rows; marker `2026-09-17T15:51:45Z`
- `2026-09-17T15:52:14.489864Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:52:13.286518Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:52:12.118858Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:52:10.929791Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:52:09.758171Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:52:07.741553Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:52:05.096673Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:52:03.034892Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:51:59.800251Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:51:59.800251Z` — **MELNGC**: 1296 rows; marker `2026-09-17T15:48:00Z`
- `2026-09-17T15:51:58.482503Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:51:57.318568Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:51:56.136707Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
