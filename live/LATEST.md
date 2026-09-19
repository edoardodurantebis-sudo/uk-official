# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T22:12:34.678250Z`  
Current process started UTC: `2026-09-19T22:08:33.585840Z`  
1-second metadata polls in this process: **193**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=100, delta=1, z=4.85 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1228** (n=1380, 2026-09-19T22:10:42.565028Z)
- `FUELINST|fuelType=NPSHYD|generation` = **371** (n=1380, 2026-09-19T22:10:42.565028Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3342** (n=1380, 2026-09-19T22:10:42.565028Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1380, 2026-09-19T22:10:42.565028Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1380, 2026-09-19T22:10:42.565028Z)
- `FUELINST|fuelType=OTHER|generation` = **352** (n=1380, 2026-09-19T22:10:42.565028Z)
- `FUELINST|fuelType=PS|generation` = **-8** (n=1380, 2026-09-19T22:10:42.565028Z)
- `FUELINST|fuelType=WIND|generation` = **15037** (n=1380, 2026-09-19T22:10:42.565028Z)
- `IMBALNGC|TOTAL|imbalance` = **-3893** (n=227, 2026-09-19T21:52:20.831514Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=227, 2026-09-19T21:52:04.466257Z)
- `INDGEN|TOTAL|generation` = **16059** (n=227, 2026-09-19T21:52:20.831514Z)
- `MELNGC|TOTAL|margin` = **36067** (n=227, 2026-09-19T21:50:19.664425Z)
- `NDF|TOTAL|demand` = **19452** (n=232, 2026-09-19T21:48:07.682988Z)
- `TSDF|TOTAL|demand` = **19952** (n=232, 2026-09-19T21:48:07.682988Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T22:12:33.490342Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:12:32.333354Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:12:31.131747Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:12:29.998172Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:12:28.824342Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:12:27.672468Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:12:26.511020Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:12:25.313100Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:12:24.171021Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:12:23.018845Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:12:21.840749Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:12:19.111763Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:12:19.111763Z` — **FREQ**: 5761 rows; marker `2026-09-19T22:11:45Z`
- `2026-09-19T22:12:17.936117Z` — **MID**: 0 rows; marker `2026-09-19T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:12:16.781798Z` — **MID**: 0 rows; marker `2026-09-19T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
