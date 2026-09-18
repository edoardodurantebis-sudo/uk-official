# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T03:40:35.456172Z`  
Current process started UTC: `2026-09-18T03:36:34.993082Z`  
1-second metadata polls in this process: **193**  
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

- `FUELINST|fuelType=INTVKL|generation` = **990** (n=914, 2026-09-18T03:40:33.462466Z)
- `FUELINST|fuelType=NPSHYD|generation` = **405** (n=914, 2026-09-18T03:40:33.462466Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=914, 2026-09-18T03:40:33.462466Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=914, 2026-09-18T03:40:33.462466Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=914, 2026-09-18T03:40:33.462466Z)
- `FUELINST|fuelType=OTHER|generation` = **168** (n=914, 2026-09-18T03:40:33.462466Z)
- `FUELINST|fuelType=PS|generation` = **166** (n=914, 2026-09-18T03:40:33.462466Z)
- `FUELINST|fuelType=WIND|generation` = **13726** (n=914, 2026-09-18T03:40:33.462466Z)
- `IMBALNGC|TOTAL|imbalance` = **10169** (n=151, 2026-09-18T03:21:23.504107Z)
- `INDDEM|TOTAL|demand` = **-11249** (n=151, 2026-09-18T03:21:23.504107Z)
- `INDGEN|TOTAL|generation` = **26983** (n=151, 2026-09-18T03:21:23.504107Z)
- `MELNGC|TOTAL|margin` = **38166** (n=151, 2026-09-18T03:19:45.452751Z)
- `NDF|TOTAL|demand` = **16314** (n=154, 2026-09-18T03:17:28.449836Z)
- `TSDF|TOTAL|demand` = **16814** (n=154, 2026-09-18T03:17:28.449836Z)
- `WINDFOR|TOTAL|generation` = **7845** (n=26, 2026-09-18T03:30:37.036559Z)

## Latest publication events

- `2026-09-18T03:40:33.462466Z` — **MID**: 0 rows; marker `2026-09-18T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:40:33.462466Z` — **FUELINST**: 80 rows; marker `2026-09-18T03:40:00Z`
- `2026-09-18T03:40:32.296598Z` — **MID**: 0 rows; marker `2026-09-18T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:40:31.109999Z` — **MID**: 0 rows; marker `2026-09-18T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:40:29.924618Z` — **MID**: 0 rows; marker `2026-09-18T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:40:28.774286Z` — **MID**: 0 rows; marker `2026-09-18T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:40:27.603281Z` — **MID**: 0 rows; marker `2026-09-18T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:40:26.419554Z` — **MID**: 0 rows; marker `2026-09-18T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:40:25.253971Z` — **MID**: 0 rows; marker `2026-09-18T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:40:23.984505Z` — **MID**: 0 rows; marker `2026-09-18T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:40:22.826158Z` — **MID**: 0 rows; marker `2026-09-18T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:40:21.614890Z` — **MID**: 0 rows; marker `2026-09-18T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:40:20.455530Z` — **MID**: 0 rows; marker `2026-09-18T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:40:17.874102Z` — **MID**: 0 rows; marker `2026-09-18T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:40:17.874102Z` — **FREQ**: 5761 rows; marker `2026-09-18T03:39:45Z`
