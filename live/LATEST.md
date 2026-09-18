# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T13:51:29.192400Z`  
Current process started UTC: `2026-09-18T13:47:28.248552Z`  
1-second metadata polls in this process: **128**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-10744, delta=3052, z=1.92 -> demand pressure up
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1389** (n=1036, 2026-09-18T13:50:46.543296Z)
- `FUELINST|fuelType=NPSHYD|generation` = **318** (n=1036, 2026-09-18T13:50:46.543296Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1036, 2026-09-18T13:50:46.543296Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1036, 2026-09-18T13:50:46.543296Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1036, 2026-09-18T13:50:46.543296Z)
- `FUELINST|fuelType=OTHER|generation` = **516** (n=1036, 2026-09-18T13:50:46.543296Z)
- `FUELINST|fuelType=PS|generation` = **-704** (n=1036, 2026-09-18T13:50:46.543296Z)
- `FUELINST|fuelType=WIND|generation` = **15624** (n=1036, 2026-09-18T13:50:46.543296Z)
- `IMBALNGC|TOTAL|imbalance` = **8935** (n=170, 2026-09-18T13:25:04.803083Z)
- `INDDEM|TOTAL|demand` = **-10745** (n=170, 2026-09-18T13:25:04.803083Z)
- `INDGEN|TOTAL|generation` = **25605** (n=170, 2026-09-18T13:25:04.803083Z)
- `MELNGC|TOTAL|margin` = **38174** (n=170, 2026-09-18T13:21:37.459648Z)
- `NDF|TOTAL|demand` = **16170** (n=175, 2026-09-18T13:49:24.414005Z)
- `TSDF|TOTAL|demand` = **16670** (n=175, 2026-09-18T13:49:41.459837Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T13:51:27.444550Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:51:25.701917Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:51:23.942249Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:51:21.942507Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:51:19.859374Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:51:18.076185Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:51:16.363377Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:51:14.623648Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:51:12.871561Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:51:11.067824Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:51:09.350585Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:51:07.636080Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:51:05.857239Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:51:03.337028Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:51:01.569018Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
