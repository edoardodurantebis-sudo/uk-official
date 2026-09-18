# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T12:57:04.110283Z`  
Current process started UTC: `2026-09-18T12:53:03.775547Z`  
1-second metadata polls in this process: **224**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1389** (n=1025, 2026-09-18T12:55:28.366188Z)
- `FUELINST|fuelType=NPSHYD|generation` = **317** (n=1025, 2026-09-18T12:55:28.366188Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3342** (n=1025, 2026-09-18T12:55:28.366188Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1025, 2026-09-18T12:55:28.366188Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1025, 2026-09-18T12:55:28.366188Z)
- `FUELINST|fuelType=OTHER|generation` = **497** (n=1025, 2026-09-18T12:55:28.366188Z)
- `FUELINST|fuelType=PS|generation` = **-716** (n=1025, 2026-09-18T12:55:28.366188Z)
- `FUELINST|fuelType=WIND|generation` = **14949** (n=1025, 2026-09-18T12:55:28.366188Z)
- `IMBALNGC|TOTAL|imbalance` = **8939** (n=169, 2026-09-18T12:54:54.509238Z)
- `INDDEM|TOTAL|demand` = **-10745** (n=169, 2026-09-18T12:54:38.671500Z)
- `INDGEN|TOTAL|generation` = **25609** (n=169, 2026-09-18T12:54:38.671500Z)
- `MELNGC|TOTAL|margin` = **38104** (n=169, 2026-09-18T12:51:19.340925Z)
- `NDF|TOTAL|demand` = **16170** (n=173, 2026-09-18T12:48:33.598652Z)
- `TSDF|TOTAL|demand` = **16670** (n=173, 2026-09-18T12:48:33.598652Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T12:57:03.144548Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:57:02.144435Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:57:01.144182Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:57:00.144109Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:56:59.143979Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:56:58.143884Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:56:57.143765Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:56:56.143636Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:56:55.143518Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:56:54.143411Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:56:53.143267Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:56:52.143116Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:56:51.143002Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:56:50.142906Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:56:48.757977Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
