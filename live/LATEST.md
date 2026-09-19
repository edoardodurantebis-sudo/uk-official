# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T19:41:11.127464Z`  
Current process started UTC: `2026-09-19T19:37:10.097904Z`  
1-second metadata polls in this process: **157**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=13.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.98 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=14.15 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=96, delta=93, z=5.31 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=374, delta=374, z=30.30 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.02 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=15.34 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.07 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=-1, z=16.89 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.12 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=404, delta=1, z=19.10 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=-1, z=22.31 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=16, z=5.23 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1350, 2026-09-19T19:40:47.794759Z)
- `FUELINST|fuelType=NPSHYD|generation` = **524** (n=1350, 2026-09-19T19:40:47.794759Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1350, 2026-09-19T19:40:47.794759Z)
- `FUELINST|fuelType=OCGT|generation` = **99** (n=1350, 2026-09-19T19:40:47.794759Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1350, 2026-09-19T19:40:47.794759Z)
- `FUELINST|fuelType=OTHER|generation` = **416** (n=1350, 2026-09-19T19:40:47.794759Z)
- `FUELINST|fuelType=PS|generation` = **824** (n=1350, 2026-09-19T19:40:47.794759Z)
- `FUELINST|fuelType=WIND|generation` = **13856** (n=1350, 2026-09-19T19:40:47.794759Z)
- `IMBALNGC|TOTAL|imbalance` = **-3754** (n=222, 2026-09-19T19:22:47.836433Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=222, 2026-09-19T19:22:31.393542Z)
- `INDGEN|TOTAL|generation` = **16198** (n=222, 2026-09-19T19:22:31.393542Z)
- `MELNGC|TOTAL|margin` = **36176** (n=222, 2026-09-19T19:20:20.972192Z)
- `NDF|TOTAL|demand` = **19452** (n=227, 2026-09-19T19:18:02.472274Z)
- `TSDF|TOTAL|demand` = **19952** (n=227, 2026-09-19T19:18:02.472274Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T19:41:09.638828Z` — **MID**: 0 rows; marker `2026-09-19T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:41:08.156669Z` — **MID**: 0 rows; marker `2026-09-19T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:41:06.728511Z` — **MID**: 0 rows; marker `2026-09-19T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:41:05.252820Z` — **MID**: 0 rows; marker `2026-09-19T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:41:03.319798Z` — **MID**: 0 rows; marker `2026-09-19T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:41:01.838891Z` — **MID**: 0 rows; marker `2026-09-19T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:41:00.427607Z` — **MID**: 0 rows; marker `2026-09-19T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:40:58.981595Z` — **MID**: 0 rows; marker `2026-09-19T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:40:57.486619Z` — **MID**: 0 rows; marker `2026-09-19T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:40:56.035310Z` — **MID**: 0 rows; marker `2026-09-19T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:40:54.602447Z` — **MID**: 0 rows; marker `2026-09-19T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:40:53.129991Z` — **MID**: 0 rows; marker `2026-09-19T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:40:51.608208Z` — **MID**: 0 rows; marker `2026-09-19T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:40:50.160586Z` — **MID**: 0 rows; marker `2026-09-19T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:40:47.794759Z` — **MID**: 0 rows; marker `2026-09-19T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
