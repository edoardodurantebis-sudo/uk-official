# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T04:56:08.456653Z`  
Current process started UTC: `2026-09-18T04:52:08.068820Z`  
1-second metadata polls in this process: **231**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **WINDFOR** `TOTAL` `generation` — wind forecast [TOTAL] generation: value=7845, delta=-11023, z=-4.38 -> renewable cushion down / residual-load pressure up
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=80, delta=-38, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=97, delta=-21, z=4.20 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.28 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=118, delta=27, z=6.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.70 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=-1, z=5.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=0, z=6.01 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=91, delta=9, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=11, z=6.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=108, delta=29, z=5.66 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **451** (n=929, 2026-09-18T04:55:37.285131Z)
- `FUELINST|fuelType=NPSHYD|generation` = **420** (n=929, 2026-09-18T04:55:37.285131Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=929, 2026-09-18T04:55:37.285131Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=929, 2026-09-18T04:55:37.285131Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=929, 2026-09-18T04:55:37.285131Z)
- `FUELINST|fuelType=OTHER|generation` = **633** (n=929, 2026-09-18T04:55:37.285131Z)
- `FUELINST|fuelType=PS|generation` = **244** (n=929, 2026-09-18T04:55:37.285131Z)
- `FUELINST|fuelType=WIND|generation` = **13654** (n=929, 2026-09-18T04:55:37.285131Z)
- `IMBALNGC|TOTAL|imbalance` = **10765** (n=154, 2026-09-18T04:50:56.245036Z)
- `INDDEM|TOTAL|demand` = **-11169** (n=154, 2026-09-18T04:50:38.189613Z)
- `INDGEN|TOTAL|generation` = **27579** (n=154, 2026-09-18T04:50:56.245036Z)
- `MELNGC|TOTAL|margin` = **38056** (n=154, 2026-09-18T04:49:35.020770Z)
- `NDF|TOTAL|demand` = **16314** (n=157, 2026-09-18T04:47:22.036502Z)
- `TSDF|TOTAL|demand` = **16814** (n=157, 2026-09-18T04:47:22.036502Z)
- `WINDFOR|TOTAL|generation` = **7845** (n=26, 2026-09-18T03:30:37.036559Z)

## Latest publication events

- `2026-09-18T04:56:07.491860Z` — **MID**: 0 rows; marker `2026-09-18T04:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:56:06.491753Z` — **MID**: 0 rows; marker `2026-09-18T04:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:56:05.491643Z` — **MID**: 0 rows; marker `2026-09-18T04:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:56:04.491559Z` — **MID**: 0 rows; marker `2026-09-18T04:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:56:03.491441Z` — **MID**: 0 rows; marker `2026-09-18T04:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:56:02.491321Z` — **MID**: 0 rows; marker `2026-09-18T04:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:56:01.491248Z` — **MID**: 0 rows; marker `2026-09-18T04:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:56:00.491123Z` — **MID**: 0 rows; marker `2026-09-18T04:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:55:59.491053Z` — **MID**: 0 rows; marker `2026-09-18T04:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:55:58.305758Z` — **MID**: 0 rows; marker `2026-09-18T04:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:55:57.305645Z` — **MID**: 0 rows; marker `2026-09-18T04:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:55:56.305521Z` — **MID**: 0 rows; marker `2026-09-18T04:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:55:55.305395Z` — **MID**: 0 rows; marker `2026-09-18T04:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:55:54.305281Z` — **MID**: 0 rows; marker `2026-09-18T04:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:55:53.025815Z` — **MID**: 0 rows; marker `2026-09-18T04:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
