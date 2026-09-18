# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T12:10:18.935880Z`  
Current process started UTC: `2026-09-18T12:06:18.213654Z`  
1-second metadata polls in this process: **155**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1399** (n=1015, 2026-09-18T12:05:37.262329Z)
- `FUELINST|fuelType=NPSHYD|generation` = **324** (n=1015, 2026-09-18T12:05:37.262329Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1015, 2026-09-18T12:05:37.262329Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1015, 2026-09-18T12:05:37.262329Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1015, 2026-09-18T12:05:37.262329Z)
- `FUELINST|fuelType=OTHER|generation` = **536** (n=1015, 2026-09-18T12:05:37.262329Z)
- `FUELINST|fuelType=PS|generation` = **-719** (n=1015, 2026-09-18T12:05:37.262329Z)
- `FUELINST|fuelType=WIND|generation` = **13886** (n=1015, 2026-09-18T12:05:37.262329Z)
- `IMBALNGC|TOTAL|imbalance` = **8949** (n=167, 2026-09-18T11:55:35.709657Z)
- `INDDEM|TOTAL|demand` = **-10744** (n=167, 2026-09-18T11:55:20.118979Z)
- `INDGEN|TOTAL|generation` = **25619** (n=167, 2026-09-18T11:55:20.118979Z)
- `MELNGC|TOTAL|margin` = **38104** (n=167, 2026-09-18T11:52:16.190142Z)
- `NDF|TOTAL|demand` = **16170** (n=171, 2026-09-18T11:49:04.559776Z)
- `TSDF|TOTAL|demand` = **16670** (n=171, 2026-09-18T11:49:29.606738Z)
- `WINDFOR|TOTAL|generation` = **7615** (n=29, 2026-09-18T10:30:46.506872Z)

## Latest publication events

- `2026-09-18T12:10:17.487363Z` — **MID**: 0 rows; marker `2026-09-18T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:10:15.997429Z` — **MID**: 0 rows; marker `2026-09-18T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:10:14.530309Z` — **MID**: 0 rows; marker `2026-09-18T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:10:11.331739Z` — **MID**: 0 rows; marker `2026-09-18T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:10:11.331739Z` — **FREQ**: 5761 rows; marker `2026-09-18T12:09:45Z`
- `2026-09-18T12:10:09.856378Z` — **MID**: 0 rows; marker `2026-09-18T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:10:08.350889Z` — **MID**: 0 rows; marker `2026-09-18T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:10:06.934485Z` — **MID**: 0 rows; marker `2026-09-18T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:10:05.355852Z` — **MID**: 0 rows; marker `2026-09-18T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:10:03.895136Z` — **MID**: 0 rows; marker `2026-09-18T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:10:02.454007Z` — **MID**: 0 rows; marker `2026-09-18T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:10:00.945977Z` — **MID**: 0 rows; marker `2026-09-18T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:09:59.441604Z` — **MID**: 0 rows; marker `2026-09-18T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:09:58.000030Z` — **MID**: 0 rows; marker `2026-09-18T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:09:56.539244Z` — **MID**: 0 rows; marker `2026-09-18T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
