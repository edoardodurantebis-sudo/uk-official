# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T08:17:09.653518Z`  
Current process started UTC: `2026-09-20T08:13:08.329047Z`  
1-second metadata polls in this process: **147**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1196** (n=1501, 2026-09-20T08:15:34.885201Z)
- `FUELINST|fuelType=NPSHYD|generation` = **347** (n=1501, 2026-09-20T08:15:34.885201Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=1501, 2026-09-20T08:15:34.885201Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1501, 2026-09-20T08:15:34.885201Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1501, 2026-09-20T08:15:34.885201Z)
- `FUELINST|fuelType=OTHER|generation` = **361** (n=1501, 2026-09-20T08:15:34.885201Z)
- `FUELINST|fuelType=PS|generation` = **-933** (n=1501, 2026-09-20T08:15:34.885201Z)
- `FUELINST|fuelType=WIND|generation` = **14795** (n=1501, 2026-09-20T08:15:34.885201Z)
- `IMBALNGC|TOTAL|imbalance` = **-6364** (n=246, 2026-09-20T07:20:39.619957Z)
- `INDDEM|TOTAL|demand` = **-12307** (n=246, 2026-09-20T07:20:39.619957Z)
- `INDGEN|TOTAL|generation` = **13588** (n=246, 2026-09-20T07:20:39.619957Z)
- `MELNGC|TOTAL|margin` = **38029** (n=246, 2026-09-20T07:19:35.864933Z)
- `NDF|TOTAL|demand` = **20614** (n=252, 2026-09-20T07:46:13.398324Z)
- `TSDF|TOTAL|demand` = **21114** (n=252, 2026-09-20T07:46:29.490221Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T08:17:07.893430Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:17:06.338467Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:17:04.775059Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:17:03.163100Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:17:01.560432Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:17:00.020838Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:16:58.491726Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:16:56.876301Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:16:55.293530Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:16:53.459853Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:16:51.911221Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:16:50.363210Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:16:48.843692Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:16:47.204528Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:16:45.664805Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
