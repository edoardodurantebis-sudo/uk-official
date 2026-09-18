# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T06:36:59.578746Z`  
Current process started UTC: `2026-09-18T06:32:58.710663Z`  
1-second metadata polls in this process: **145**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=949, 2026-09-18T06:35:39.597032Z)
- `FUELINST|fuelType=NPSHYD|generation` = **408** (n=949, 2026-09-18T06:35:39.597032Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=949, 2026-09-18T06:35:39.597032Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=949, 2026-09-18T06:35:39.597032Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=949, 2026-09-18T06:35:39.597032Z)
- `FUELINST|fuelType=OTHER|generation` = **1146** (n=949, 2026-09-18T06:35:39.597032Z)
- `FUELINST|fuelType=PS|generation` = **675** (n=949, 2026-09-18T06:35:39.597032Z)
- `FUELINST|fuelType=WIND|generation` = **14414** (n=949, 2026-09-18T06:35:39.597032Z)
- `IMBALNGC|TOTAL|imbalance` = **10652** (n=157, 2026-09-18T06:20:37.859791Z)
- `INDDEM|TOTAL|demand` = **-11168** (n=157, 2026-09-18T06:20:37.859791Z)
- `INDGEN|TOTAL|generation` = **27466** (n=157, 2026-09-18T06:20:37.859791Z)
- `MELNGC|TOTAL|margin` = **37963** (n=157, 2026-09-18T06:19:23.801804Z)
- `NDF|TOTAL|demand` = **16314** (n=160, 2026-09-18T06:17:14.273486Z)
- `TSDF|TOTAL|demand` = **16814** (n=160, 2026-09-18T06:17:14.273486Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T06:36:58.018005Z` — **MID**: 0 rows; marker `2026-09-18T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:36:56.464770Z` — **MID**: 0 rows; marker `2026-09-18T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:36:54.916992Z` — **MID**: 0 rows; marker `2026-09-18T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:36:53.352697Z` — **MID**: 0 rows; marker `2026-09-18T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:36:51.776512Z` — **MID**: 0 rows; marker `2026-09-18T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:36:50.188844Z` — **MID**: 0 rows; marker `2026-09-18T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:36:48.612672Z` — **MID**: 0 rows; marker `2026-09-18T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:36:47.050446Z` — **MID**: 0 rows; marker `2026-09-18T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:36:44.903115Z` — **MID**: 0 rows; marker `2026-09-18T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:36:43.338352Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:36:41.780189Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:36:40.198682Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:36:38.654418Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:36:37.102824Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:36:35.540792Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
