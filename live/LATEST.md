# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T08:21:20.935756Z`  
Current process started UTC: `2026-09-20T08:17:20.299595Z`  
1-second metadata polls in this process: **219**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-986, delta=2, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-983, delta=3, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=-1, z=-3.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.72 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-988, delta=26, z=-3.87 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.79 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.81 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=2, z=-3.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-989, delta=24, z=-3.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.13 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1196** (n=1502, 2026-09-20T08:20:30.547622Z)
- `FUELINST|fuelType=NPSHYD|generation` = **347** (n=1502, 2026-09-20T08:20:30.547622Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1502, 2026-09-20T08:20:30.547622Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1502, 2026-09-20T08:20:30.547622Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1502, 2026-09-20T08:20:30.547622Z)
- `FUELINST|fuelType=OTHER|generation` = **360** (n=1502, 2026-09-20T08:20:30.547622Z)
- `FUELINST|fuelType=PS|generation` = **-936** (n=1502, 2026-09-20T08:20:30.547622Z)
- `FUELINST|fuelType=WIND|generation` = **14902** (n=1502, 2026-09-20T08:20:30.547622Z)
- `IMBALNGC|TOTAL|imbalance` = **-7048** (n=247, 2026-09-20T08:20:30.547622Z)
- `INDDEM|TOTAL|demand` = **-12309** (n=247, 2026-09-20T08:20:30.547622Z)
- `INDGEN|TOTAL|generation` = **13118** (n=247, 2026-09-20T08:20:30.547622Z)
- `MELNGC|TOTAL|margin` = **37453** (n=247, 2026-09-20T08:19:27.585262Z)
- `NDF|TOTAL|demand` = **19666** (n=253, 2026-09-20T08:17:35.777988Z)
- `TSDF|TOTAL|demand` = **20166** (n=253, 2026-09-20T08:17:35.777988Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T08:21:19.987856Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:21:18.987777Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:21:17.788300Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:21:16.788187Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:21:15.788074Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:21:14.787958Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:21:13.746151Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:21:12.746017Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:21:11.727192Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:21:10.727110Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:21:09.726994Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:21:08.726879Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:21:07.726815Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:21:06.726737Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:21:05.726634Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
