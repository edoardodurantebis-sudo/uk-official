# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T19:15:57.662092Z`  
Current process started UTC: `2026-09-19T19:11:56.309964Z`  
1-second metadata polls in this process: **134**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=-1, z=22.31 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=16, z=5.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=404, delta=175, z=28.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=63, z=4.37 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=229, delta=229, z=17.80 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=0, delta=92, z=-0.01 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-92, delta=10, z=-8.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-31, delta=73, z=-2.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.91 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.20 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-102, delta=-202, z=-12.22 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1345, 2026-09-19T19:15:40.689562Z)
- `FUELINST|fuelType=NPSHYD|generation` = **507** (n=1345, 2026-09-19T19:15:40.689562Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=1345, 2026-09-19T19:15:40.689562Z)
- `FUELINST|fuelType=OCGT|generation` = **99** (n=1345, 2026-09-19T19:15:40.689562Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1345, 2026-09-19T19:15:40.689562Z)
- `FUELINST|fuelType=OTHER|generation` = **516** (n=1345, 2026-09-19T19:15:40.689562Z)
- `FUELINST|fuelType=PS|generation` = **825** (n=1345, 2026-09-19T19:15:40.689562Z)
- `FUELINST|fuelType=WIND|generation` = **13883** (n=1345, 2026-09-19T19:15:40.689562Z)
- `IMBALNGC|TOTAL|imbalance` = **-3742** (n=221, 2026-09-19T18:54:47.042884Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=221, 2026-09-19T18:54:31.530560Z)
- `INDGEN|TOTAL|generation` = **16210** (n=221, 2026-09-19T18:54:31.530560Z)
- `MELNGC|TOTAL|margin` = **36202** (n=221, 2026-09-19T18:51:13.295596Z)
- `NDF|TOTAL|demand` = **19452** (n=226, 2026-09-19T18:48:41.702714Z)
- `TSDF|TOTAL|demand` = **19952** (n=226, 2026-09-19T18:48:41.702714Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T19:15:55.909791Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:15:54.010862Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:15:52.319520Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:15:50.572025Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:15:48.575376Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:15:46.881103Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:15:45.193626Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:15:43.484490Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:15:40.689562Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:15:40.689562Z` — **FUELINST**: 80 rows; marker `2026-09-19T19:15:00Z`
- `2026-09-19T19:15:38.962590Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:15:37.254954Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:15:35.542958Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:15:33.839935Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:15:32.118206Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
