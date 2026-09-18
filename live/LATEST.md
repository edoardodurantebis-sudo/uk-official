# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T07:10:34.908287Z`  
Current process started UTC: `2026-09-18T07:06:33.826305Z`  
1-second metadata polls in this process: **169**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=956, 2026-09-18T07:10:22.157448Z)
- `FUELINST|fuelType=NPSHYD|generation` = **377** (n=956, 2026-09-18T07:10:22.157448Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=956, 2026-09-18T07:10:22.157448Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=956, 2026-09-18T07:10:22.157448Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=956, 2026-09-18T07:10:22.157448Z)
- `FUELINST|fuelType=OTHER|generation` = **1331** (n=956, 2026-09-18T07:10:22.157448Z)
- `FUELINST|fuelType=PS|generation` = **820** (n=956, 2026-09-18T07:10:22.157448Z)
- `FUELINST|fuelType=WIND|generation` = **12812** (n=956, 2026-09-18T07:10:22.157448Z)
- `IMBALNGC|TOTAL|imbalance` = **10565** (n=158, 2026-09-18T06:50:20.667031Z)
- `INDDEM|TOTAL|demand` = **-11405** (n=158, 2026-09-18T06:50:04.574079Z)
- `INDGEN|TOTAL|generation` = **27379** (n=158, 2026-09-18T06:50:04.574079Z)
- `MELNGC|TOTAL|margin` = **37954** (n=158, 2026-09-18T06:49:07.667660Z)
- `NDF|TOTAL|demand` = **16314** (n=161, 2026-09-18T06:47:15.091718Z)
- `TSDF|TOTAL|demand` = **16814** (n=161, 2026-09-18T06:47:15.091718Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T07:10:33.532129Z` — **MID**: 0 rows; marker `2026-09-18T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:10:32.218817Z` — **MID**: 0 rows; marker `2026-09-18T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:10:30.838152Z` — **MID**: 0 rows; marker `2026-09-18T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:10:29.501630Z` — **MID**: 0 rows; marker `2026-09-18T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:10:28.146549Z` — **MID**: 0 rows; marker `2026-09-18T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:10:26.765873Z` — **MID**: 0 rows; marker `2026-09-18T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:10:25.475441Z` — **MID**: 0 rows; marker `2026-09-18T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:10:22.157448Z` — **MID**: 0 rows; marker `2026-09-18T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:10:22.157448Z` — **FUELINST**: 80 rows; marker `2026-09-18T07:10:00Z`
- `2026-09-18T07:10:22.157448Z` — **FREQ**: 5761 rows; marker `2026-09-18T07:09:45Z`
- `2026-09-18T07:10:20.714881Z` — **MID**: 0 rows; marker `2026-09-18T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:10:19.368329Z` — **MID**: 0 rows; marker `2026-09-18T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:10:17.994510Z` — **MID**: 0 rows; marker `2026-09-18T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:10:16.676773Z` — **MID**: 0 rows; marker `2026-09-18T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:10:15.250715Z` — **MID**: 0 rows; marker `2026-09-18T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
