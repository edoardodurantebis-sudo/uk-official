# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T00:21:32.378168Z`  
Current process started UTC: `2026-09-18T00:17:31.433251Z`  
1-second metadata polls in this process: **129**  
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

- `FUELINST|fuelType=INTVKL|generation` = **893** (n=874, 2026-09-18T00:20:47.452329Z)
- `FUELINST|fuelType=NPSHYD|generation` = **447** (n=874, 2026-09-18T00:20:47.452329Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3323** (n=874, 2026-09-18T00:20:47.452329Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=874, 2026-09-18T00:20:47.452329Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=874, 2026-09-18T00:20:47.452329Z)
- `FUELINST|fuelType=OTHER|generation` = **249** (n=874, 2026-09-18T00:20:47.452329Z)
- `FUELINST|fuelType=PS|generation` = **175** (n=874, 2026-09-18T00:20:47.452329Z)
- `FUELINST|fuelType=WIND|generation` = **14270** (n=874, 2026-09-18T00:20:47.452329Z)
- `IMBALNGC|TOTAL|imbalance` = **10139** (n=144, 2026-09-17T23:53:42.397703Z)
- `INDDEM|TOTAL|demand` = **-11183** (n=144, 2026-09-17T23:53:26.100029Z)
- `INDGEN|TOTAL|generation` = **26953** (n=144, 2026-09-17T23:53:26.100029Z)
- `MELNGC|TOTAL|margin` = **36542** (n=145, 2026-09-18T00:20:30.506045Z)
- `NDF|TOTAL|demand` = **16314** (n=148, 2026-09-18T00:17:48.242066Z)
- `TSDF|TOTAL|demand` = **16814** (n=148, 2026-09-18T00:17:48.242066Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T00:21:30.680086Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:21:28.975004Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:21:27.265666Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:21:25.569410Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:21:23.860328Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:21:21.639031Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:21:19.932773Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:21:18.240145Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:21:16.542520Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:21:14.846098Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:21:13.129514Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:21:11.393470Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:21:09.661634Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:21:07.927189Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:21:05.412925Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
