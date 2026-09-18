# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T12:01:54.591031Z`  
Current process started UTC: `2026-09-18T11:57:52.966133Z`  
1-second metadata polls in this process: **129**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1418** (n=1014, 2026-09-18T12:00:36.360974Z)
- `FUELINST|fuelType=NPSHYD|generation` = **331** (n=1014, 2026-09-18T12:00:36.360974Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1014, 2026-09-18T12:00:36.360974Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1014, 2026-09-18T12:00:36.360974Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1014, 2026-09-18T12:00:36.360974Z)
- `FUELINST|fuelType=OTHER|generation` = **654** (n=1014, 2026-09-18T12:00:36.360974Z)
- `FUELINST|fuelType=PS|generation` = **-722** (n=1014, 2026-09-18T12:00:36.360974Z)
- `FUELINST|fuelType=WIND|generation` = **13572** (n=1014, 2026-09-18T12:00:36.360974Z)
- `IMBALNGC|TOTAL|imbalance` = **8949** (n=167, 2026-09-18T11:55:35.709657Z)
- `INDDEM|TOTAL|demand` = **-10744** (n=167, 2026-09-18T11:55:20.118979Z)
- `INDGEN|TOTAL|generation` = **25619** (n=167, 2026-09-18T11:55:20.118979Z)
- `MELNGC|TOTAL|margin` = **38104** (n=167, 2026-09-18T11:52:16.190142Z)
- `NDF|TOTAL|demand` = **16170** (n=171, 2026-09-18T11:49:04.559776Z)
- `TSDF|TOTAL|demand` = **16670** (n=171, 2026-09-18T11:49:29.606738Z)
- `WINDFOR|TOTAL|generation` = **7615** (n=29, 2026-09-18T10:30:46.506872Z)

## Latest publication events

- `2026-09-18T12:01:52.683538Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:01:51.019597Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:01:49.015287Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:01:47.314128Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:01:45.062244Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:01:42.100575Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:01:40.383140Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:01:38.571356Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:01:36.645113Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:01:34.956810Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:01:33.265653Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:01:31.341545Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:01:29.620214Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:01:27.918757Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:01:25.487730Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
