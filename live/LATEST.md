# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T20:40:13.857527Z`  
Current process started UTC: `2026-09-19T20:36:13.454004Z`  
1-second metadata polls in this process: **145**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1361, 2026-09-19T20:35:34.127437Z)
- `FUELINST|fuelType=NPSHYD|generation` = **476** (n=1361, 2026-09-19T20:35:34.127437Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1361, 2026-09-19T20:35:34.127437Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1361, 2026-09-19T20:35:34.127437Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1361, 2026-09-19T20:35:34.127437Z)
- `FUELINST|fuelType=OTHER|generation` = **770** (n=1361, 2026-09-19T20:35:34.127437Z)
- `FUELINST|fuelType=PS|generation` = **823** (n=1361, 2026-09-19T20:35:34.127437Z)
- `FUELINST|fuelType=WIND|generation` = **14198** (n=1361, 2026-09-19T20:35:34.127437Z)
- `IMBALNGC|TOTAL|imbalance` = **-3820** (n=224, 2026-09-19T20:22:42.485438Z)
- `INDDEM|TOTAL|demand` = **-11873** (n=224, 2026-09-19T20:22:26.195138Z)
- `INDGEN|TOTAL|generation` = **16132** (n=224, 2026-09-19T20:22:26.195138Z)
- `MELNGC|TOTAL|margin` = **36251** (n=224, 2026-09-19T20:20:18.046700Z)
- `NDF|TOTAL|demand` = **19452** (n=229, 2026-09-19T20:17:59.606414Z)
- `TSDF|TOTAL|demand` = **19952** (n=229, 2026-09-19T20:17:59.606414Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T20:40:12.307761Z` — **MID**: 0 rows; marker `2026-09-19T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:40:10.742219Z` — **MID**: 0 rows; marker `2026-09-19T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:40:09.161076Z` — **MID**: 0 rows; marker `2026-09-19T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:40:07.623667Z` — **MID**: 0 rows; marker `2026-09-19T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:40:06.026034Z` — **MID**: 0 rows; marker `2026-09-19T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:40:04.503973Z` — **MID**: 0 rows; marker `2026-09-19T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:40:01.572291Z` — **MID**: 0 rows; marker `2026-09-19T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:40:00.012973Z` — **MID**: 0 rows; marker `2026-09-19T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:39:58.472624Z` — **MID**: 0 rows; marker `2026-09-19T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:39:56.876747Z` — **MID**: 0 rows; marker `2026-09-19T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:39:55.289546Z` — **MID**: 0 rows; marker `2026-09-19T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:39:53.744487Z` — **MID**: 0 rows; marker `2026-09-19T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:39:52.205588Z` — **MID**: 0 rows; marker `2026-09-19T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:39:50.614690Z` — **MID**: 0 rows; marker `2026-09-19T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:39:49.020560Z` — **MID**: 0 rows; marker `2026-09-19T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
