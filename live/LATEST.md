# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T22:16:44.566606Z`  
Current process started UTC: `2026-09-19T22:12:44.093861Z`  
1-second metadata polls in this process: **220**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=-10, z=-15.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-675, delta=-337, z=-16.96 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-338, delta=-235, z=-8.76 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1226** (n=1381, 2026-09-19T22:15:40.330311Z)
- `FUELINST|fuelType=NPSHYD|generation` = **372** (n=1381, 2026-09-19T22:15:40.330311Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1381, 2026-09-19T22:15:40.330311Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1381, 2026-09-19T22:15:40.330311Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1381, 2026-09-19T22:15:40.330311Z)
- `FUELINST|fuelType=OTHER|generation` = **350** (n=1381, 2026-09-19T22:15:40.330311Z)
- `FUELINST|fuelType=PS|generation` = **-8** (n=1381, 2026-09-19T22:15:40.330311Z)
- `FUELINST|fuelType=WIND|generation` = **15044** (n=1381, 2026-09-19T22:15:40.330311Z)
- `IMBALNGC|TOTAL|imbalance` = **-3893** (n=227, 2026-09-19T21:52:20.831514Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=227, 2026-09-19T21:52:04.466257Z)
- `INDGEN|TOTAL|generation` = **16059** (n=227, 2026-09-19T21:52:20.831514Z)
- `MELNGC|TOTAL|margin` = **36067** (n=227, 2026-09-19T21:50:19.664425Z)
- `NDF|TOTAL|demand` = **19452** (n=232, 2026-09-19T21:48:07.682988Z)
- `TSDF|TOTAL|demand` = **19952** (n=232, 2026-09-19T21:48:07.682988Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T22:16:43.530142Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:16:42.062394Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:16:40.569693Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:16:39.569618Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:16:38.523405Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:16:37.113797Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:16:36.113724Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:16:35.076538Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:16:34.073500Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:16:33.050849Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:16:32.050766Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:16:31.043301Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:16:28.245447Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:16:28.245447Z` — **FREQ**: 5761 rows; marker `2026-09-19T22:15:45Z`
- `2026-09-19T22:16:27.213986Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
