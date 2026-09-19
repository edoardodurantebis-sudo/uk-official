# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T21:30:37.102246Z`  
Current process started UTC: `2026-09-19T21:26:36.097662Z`  
1-second metadata polls in this process: **135**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=94, delta=-6, z=4.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=0, delta=-378, z=-0.09 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=92, delta=-14, z=4.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=4.92 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=4.97 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=5.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=1, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=1, delta=-250, z=-0.07 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=100, delta=4, z=5.22 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=378, delta=4, z=13.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=105, delta=5, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=251, delta=-152, z=6.63 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=100, delta=1, z=4.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=11.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.84 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1372, 2026-09-19T21:30:34.172377Z)
- `FUELINST|fuelType=NPSHYD|generation` = **453** (n=1372, 2026-09-19T21:30:34.172377Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1372, 2026-09-19T21:30:34.172377Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1372, 2026-09-19T21:30:34.172377Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1372, 2026-09-19T21:30:34.172377Z)
- `FUELINST|fuelType=OTHER|generation` = **452** (n=1372, 2026-09-19T21:30:34.172377Z)
- `FUELINST|fuelType=PS|generation` = **674** (n=1372, 2026-09-19T21:30:34.172377Z)
- `FUELINST|fuelType=WIND|generation` = **14462** (n=1372, 2026-09-19T21:30:34.172377Z)
- `IMBALNGC|TOTAL|imbalance` = **-3899** (n=226, 2026-09-19T21:22:23.160034Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=226, 2026-09-19T21:22:23.160034Z)
- `INDGEN|TOTAL|generation` = **16053** (n=226, 2026-09-19T21:22:23.160034Z)
- `MELNGC|TOTAL|margin` = **36062** (n=226, 2026-09-19T21:19:49.749521Z)
- `NDF|TOTAL|demand` = **19452** (n=231, 2026-09-19T21:18:12.331486Z)
- `TSDF|TOTAL|demand` = **19952** (n=231, 2026-09-19T21:18:12.331486Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T21:30:34.172377Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:30:34.172377Z` — **FUELINST**: 80 rows; marker `2026-09-19T21:30:00Z`
- `2026-09-19T21:30:32.415871Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:30:30.720329Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:30:28.998742Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:30:27.304406Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:30:25.601420Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:30:23.868340Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:30:22.151558Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:30:20.451221Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:30:16.922842Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:30:16.922842Z` — **FREQ**: 5761 rows; marker `2026-09-19T21:29:45Z`
- `2026-09-19T21:30:15.237346Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:30:13.529651Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:30:11.782208Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
