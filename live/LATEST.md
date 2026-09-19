# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T05:59:28.965118Z`  
Current process started UTC: `2026-09-19T05:55:28.059211Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-454** (n=1185, 2026-09-19T05:55:30.125095Z)
- `FUELINST|fuelType=NPSHYD|generation` = **372** (n=1185, 2026-09-19T05:55:30.125095Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1185, 2026-09-19T05:55:30.125095Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1185, 2026-09-19T05:55:30.125095Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1185, 2026-09-19T05:55:30.125095Z)
- `FUELINST|fuelType=OTHER|generation` = **981** (n=1185, 2026-09-19T05:55:30.125095Z)
- `FUELINST|fuelType=PS|generation` = **-540** (n=1185, 2026-09-19T05:55:30.125095Z)
- `FUELINST|fuelType=WIND|generation` = **15810** (n=1185, 2026-09-19T05:55:30.125095Z)
- `IMBALNGC|TOTAL|imbalance` = **9697** (n=196, 2026-09-19T05:50:34.942583Z)
- `INDDEM|TOTAL|demand` = **-10865** (n=196, 2026-09-19T05:50:34.942583Z)
- `INDGEN|TOTAL|generation` = **26887** (n=196, 2026-09-19T05:50:50.449260Z)
- `MELNGC|TOTAL|margin` = **38235** (n=196, 2026-09-19T05:49:46.009897Z)
- `NDF|TOTAL|demand` = **16550** (n=200, 2026-09-19T05:47:37.564895Z)
- `TSDF|TOTAL|demand` = **17190** (n=200, 2026-09-19T05:47:37.564895Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T05:59:27.938997Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:59:26.895742Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:59:25.847065Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:59:24.794530Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:59:23.779329Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:59:22.730432Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:59:21.685666Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:59:20.659683Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:59:19.632991Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:59:18.586498Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:59:17.560898Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:59:16.513479Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:59:15.483983Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:59:14.444331Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:59:12.845711Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
