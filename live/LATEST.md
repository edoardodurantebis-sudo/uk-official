# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T11:52:26.540031Z`  
Current process started UTC: `2026-09-20T11:48:26.533044Z`  
1-second metadata polls in this process: **180**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1544, 2026-09-20T11:50:35.344079Z)
- `FUELINST|fuelType=NPSHYD|generation` = **285** (n=1544, 2026-09-20T11:50:35.344079Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1544, 2026-09-20T11:50:35.344079Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1544, 2026-09-20T11:50:35.344079Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1544, 2026-09-20T11:50:35.344079Z)
- `FUELINST|fuelType=OTHER|generation` = **450** (n=1544, 2026-09-20T11:50:35.344079Z)
- `FUELINST|fuelType=PS|generation` = **-667** (n=1544, 2026-09-20T11:50:35.344079Z)
- `FUELINST|fuelType=WIND|generation` = **12765** (n=1544, 2026-09-20T11:50:35.344079Z)
- `IMBALNGC|TOTAL|imbalance` = **-5732** (n=253, 2026-09-20T11:24:21.965190Z)
- `INDDEM|TOTAL|demand` = **-11813** (n=253, 2026-09-20T11:23:50.776605Z)
- `INDGEN|TOTAL|generation` = **15372** (n=253, 2026-09-20T11:23:50.776605Z)
- `MELNGC|TOTAL|margin` = **35780** (n=254, 2026-09-20T11:50:51.530998Z)
- `NDF|TOTAL|demand` = **20604** (n=260, 2026-09-20T11:48:14.448744Z)
- `TSDF|TOTAL|demand` = **21104** (n=260, 2026-09-20T11:48:14.448744Z)
- `WINDFOR|TOTAL|generation` = **2360** (n=44, 2026-09-20T10:30:44.491768Z)

## Latest publication events

- `2026-09-20T11:52:25.306397Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:52:24.016415Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:52:22.666525Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:52:21.366773Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:52:19.747260Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:52:18.455571Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:52:17.162139Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:52:15.937394Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:52:14.631503Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:52:13.335558Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:52:11.602087Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:52:10.342984Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:52:09.091126Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:52:07.851616Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:52:06.233834Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
