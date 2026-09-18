# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T11:15:41.363695Z`  
Current process started UTC: `2026-09-18T11:11:40.470421Z`  
1-second metadata polls in this process: **140**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=1003, 2026-09-18T11:15:03.199773Z)
- `FUELINST|fuelType=NPSHYD|generation` = **330** (n=1003, 2026-09-18T11:15:03.199773Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1003, 2026-09-18T11:15:03.199773Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1003, 2026-09-18T11:15:03.199773Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1003, 2026-09-18T11:15:03.199773Z)
- `FUELINST|fuelType=OTHER|generation` = **906** (n=1003, 2026-09-18T11:15:03.199773Z)
- `FUELINST|fuelType=PS|generation` = **-546** (n=1003, 2026-09-18T11:15:03.199773Z)
- `FUELINST|fuelType=WIND|generation` = **12193** (n=1003, 2026-09-18T11:15:03.199773Z)
- `IMBALNGC|TOTAL|imbalance` = **8982** (n=165, 2026-09-18T10:55:56.036599Z)
- `INDDEM|TOTAL|demand` = **-10744** (n=165, 2026-09-18T10:55:23.440555Z)
- `INDGEN|TOTAL|generation` = **25652** (n=165, 2026-09-18T10:55:23.440555Z)
- `MELNGC|TOTAL|margin` = **38126** (n=165, 2026-09-18T10:51:27.792376Z)
- `NDF|TOTAL|demand` = **16170** (n=169, 2026-09-18T10:49:05.046376Z)
- `TSDF|TOTAL|demand` = **16670** (n=169, 2026-09-18T10:49:05.046376Z)
- `WINDFOR|TOTAL|generation` = **7615** (n=29, 2026-09-18T10:30:46.506872Z)

## Latest publication events

- `2026-09-18T11:15:39.686363Z` — **MID**: 0 rows; marker `2026-09-18T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:15:38.021129Z` — **MID**: 0 rows; marker `2026-09-18T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:15:35.268534Z` — **MID**: 0 rows; marker `2026-09-18T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:15:33.699012Z` — **MID**: 0 rows; marker `2026-09-18T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:15:32.039340Z` — **MID**: 0 rows; marker `2026-09-18T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:15:30.371335Z` — **MID**: 0 rows; marker `2026-09-18T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:15:28.713347Z` — **MID**: 0 rows; marker `2026-09-18T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:15:27.094707Z` — **MID**: 0 rows; marker `2026-09-18T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:15:25.414368Z` — **MID**: 0 rows; marker `2026-09-18T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:15:23.793903Z` — **MID**: 0 rows; marker `2026-09-18T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:15:22.176814Z` — **MID**: 0 rows; marker `2026-09-18T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:15:18.813833Z` — **MID**: 0 rows; marker `2026-09-18T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:15:18.813833Z` — **FREQ**: 5761 rows; marker `2026-09-18T11:05:45Z`
- `2026-09-18T11:15:17.194258Z` — **MID**: 0 rows; marker `2026-09-18T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:15:15.619482Z` — **MID**: 0 rows; marker `2026-09-18T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
