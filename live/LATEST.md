# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T14:24:12.721515Z`  
Current process started UTC: `2026-09-20T14:20:11.122155Z`  
1-second metadata polls in this process: **231**  
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

- `FUELINST|fuelType=INTVKL|generation` = **286** (n=1574, 2026-09-20T14:20:27.404864Z)
- `FUELINST|fuelType=NPSHYD|generation` = **264** (n=1574, 2026-09-20T14:20:27.404864Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1574, 2026-09-20T14:20:27.404864Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1574, 2026-09-20T14:20:27.404864Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1574, 2026-09-20T14:20:27.404864Z)
- `FUELINST|fuelType=OTHER|generation` = **908** (n=1574, 2026-09-20T14:20:27.404864Z)
- `FUELINST|fuelType=PS|generation` = **-777** (n=1574, 2026-09-20T14:20:27.404864Z)
- `FUELINST|fuelType=WIND|generation` = **9475** (n=1574, 2026-09-20T14:20:27.404864Z)
- `IMBALNGC|TOTAL|imbalance` = **-5731** (n=258, 2026-09-20T13:53:04.012223Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=259, 2026-09-20T14:24:09.197108Z)
- `INDGEN|TOTAL|generation` = **15454** (n=259, 2026-09-20T14:24:09.197108Z)
- `MELNGC|TOTAL|margin` = **35389** (n=259, 2026-09-20T14:20:58.322467Z)
- `NDF|TOTAL|demand` = **20604** (n=265, 2026-09-20T14:18:25.070664Z)
- `TSDF|TOTAL|demand` = **21104** (n=265, 2026-09-20T14:18:25.070664Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T14:24:09.197108Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:24:09.197108Z` — **INDGEN**: 1350 rows; marker `2026-09-20T14:17:00Z`
- `2026-09-20T14:24:09.197108Z` — **INDDEM**: 1350 rows; marker `2026-09-20T14:17:00Z`
- `2026-09-20T14:24:08.196991Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:24:07.196876Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:24:06.196759Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:24:05.196636Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:24:04.196524Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:24:03.196407Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:24:02.196330Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:24:01.196260Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:24:00.196146Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:23:59.196071Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:23:58.195954Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:23:57.195837Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
