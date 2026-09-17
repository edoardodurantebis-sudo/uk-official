# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T20:47:20.553118Z`  
Current process started UTC: `2026-09-17T20:43:20.392898Z`  
1-second metadata polls in this process: **140**  
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

- `FUELINST|fuelType=INTVKL|generation` = **728** (n=831, 2026-09-17T20:45:33.524855Z)
- `FUELINST|fuelType=NPSHYD|generation` = **560** (n=831, 2026-09-17T20:45:33.524855Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=831, 2026-09-17T20:45:33.524855Z)
- `FUELINST|fuelType=OCGT|generation` = **38** (n=831, 2026-09-17T20:45:33.524855Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=831, 2026-09-17T20:45:33.524855Z)
- `FUELINST|fuelType=OTHER|generation` = **340** (n=831, 2026-09-17T20:45:33.524855Z)
- `FUELINST|fuelType=PS|generation` = **356** (n=831, 2026-09-17T20:45:33.524855Z)
- `FUELINST|fuelType=WIND|generation` = **15399** (n=831, 2026-09-17T20:45:33.524855Z)
- `IMBALNGC|TOTAL|imbalance` = **9686** (n=137, 2026-09-17T20:23:01.759732Z)
- `INDDEM|TOTAL|demand` = **-11161** (n=137, 2026-09-17T20:22:29.150648Z)
- `INDGEN|TOTAL|generation` = **26500** (n=137, 2026-09-17T20:22:29.150648Z)
- `MELNGC|TOTAL|margin` = **36451** (n=137, 2026-09-17T20:20:13.977200Z)
- `NDF|TOTAL|demand` = **16314** (n=140, 2026-09-17T20:18:03.614644Z)
- `TSDF|TOTAL|demand` = **16814** (n=140, 2026-09-17T20:18:03.614644Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T20:47:18.989719Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:47:17.364918Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:47:15.780234Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:47:14.186394Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:47:12.494727Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:47:10.505072Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:47:08.767616Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:47:07.183980Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:47:05.505948Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:47:03.880724Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:47:02.027956Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:47:00.392247Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:46:58.603102Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:46:56.998401Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:46:55.044821Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
