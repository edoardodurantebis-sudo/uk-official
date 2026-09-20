# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T03:21:25.231435Z`  
Current process started UTC: `2026-09-20T03:17:24.742267Z`  
1-second metadata polls in this process: **147**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-5.00 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.04 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.09 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.14 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.19 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-5.24 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-5.29 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-5.35 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-5.46 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-5.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.58 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.65 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **161** (n=1442, 2026-09-20T03:20:26.665162Z)
- `FUELINST|fuelType=NPSHYD|generation` = **296** (n=1442, 2026-09-20T03:20:26.665162Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1442, 2026-09-20T03:20:26.665162Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1442, 2026-09-20T03:20:26.665162Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1442, 2026-09-20T03:20:26.665162Z)
- `FUELINST|fuelType=OTHER|generation` = **592** (n=1442, 2026-09-20T03:20:26.665162Z)
- `FUELINST|fuelType=PS|generation` = **-697** (n=1442, 2026-09-20T03:20:26.665162Z)
- `FUELINST|fuelType=WIND|generation` = **15214** (n=1442, 2026-09-20T03:20:26.665162Z)
- `IMBALNGC|TOTAL|imbalance` = **-3815** (n=238, 2026-09-20T03:20:58.508066Z)
- `INDDEM|TOTAL|demand` = **-12287** (n=238, 2026-09-20T03:20:58.508066Z)
- `INDGEN|TOTAL|generation` = **16137** (n=238, 2026-09-20T03:20:58.508066Z)
- `MELNGC|TOTAL|margin` = **37545** (n=238, 2026-09-20T03:19:19.206204Z)
- `NDF|TOTAL|demand` = **19452** (n=243, 2026-09-20T03:17:24.742276Z)
- `TSDF|TOTAL|demand` = **19952** (n=243, 2026-09-20T03:17:24.742276Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T03:21:23.788859Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:21:22.333546Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:21:20.918051Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:21:19.433138Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:21:17.997027Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:21:16.492470Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:21:14.697454Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:21:13.163360Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:21:11.670460Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:21:10.120620Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:21:08.648458Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:21:07.162023Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:21:05.714111Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:21:04.297725Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:21:02.804810Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
