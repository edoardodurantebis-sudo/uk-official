# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T05:55:16.439857Z`  
Current process started UTC: `2026-09-19T05:51:15.832886Z`  
1-second metadata polls in this process: **149**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-454** (n=1184, 2026-09-19T05:50:19.363803Z)
- `FUELINST|fuelType=NPSHYD|generation` = **372** (n=1184, 2026-09-19T05:50:19.363803Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1184, 2026-09-19T05:50:19.363803Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1184, 2026-09-19T05:50:19.363803Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1184, 2026-09-19T05:50:19.363803Z)
- `FUELINST|fuelType=OTHER|generation` = **950** (n=1184, 2026-09-19T05:50:19.363803Z)
- `FUELINST|fuelType=PS|generation` = **-539** (n=1184, 2026-09-19T05:50:19.363803Z)
- `FUELINST|fuelType=WIND|generation` = **15789** (n=1184, 2026-09-19T05:50:19.363803Z)
- `IMBALNGC|TOTAL|imbalance` = **9697** (n=196, 2026-09-19T05:50:34.942583Z)
- `INDDEM|TOTAL|demand` = **-10865** (n=196, 2026-09-19T05:50:34.942583Z)
- `INDGEN|TOTAL|generation` = **26887** (n=196, 2026-09-19T05:50:50.449260Z)
- `MELNGC|TOTAL|margin` = **38235** (n=196, 2026-09-19T05:49:46.009897Z)
- `NDF|TOTAL|demand` = **16550** (n=200, 2026-09-19T05:47:37.564895Z)
- `TSDF|TOTAL|demand` = **17190** (n=200, 2026-09-19T05:47:37.564895Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T05:55:14.162558Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:55:12.597202Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:55:11.063905Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:55:09.532886Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:55:08.008875Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:55:06.469335Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:55:04.931764Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:55:03.368429Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:55:01.840892Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:55:00.316281Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:54:58.342692Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:54:56.826841Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:54:55.300639Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:54:53.771712Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:54:52.251017Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
