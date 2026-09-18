# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T05:46:35.499351Z`  
Current process started UTC: `2026-09-18T05:42:34.634242Z`  
1-second metadata polls in this process: **131**  
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

- `FUELINST|fuelType=INTVKL|generation` = **954** (n=939, 2026-09-18T05:45:31.422962Z)
- `FUELINST|fuelType=NPSHYD|generation` = **486** (n=939, 2026-09-18T05:45:31.422962Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=939, 2026-09-18T05:45:31.422962Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=939, 2026-09-18T05:45:31.422962Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=939, 2026-09-18T05:45:31.422962Z)
- `FUELINST|fuelType=OTHER|generation` = **1240** (n=939, 2026-09-18T05:45:31.422962Z)
- `FUELINST|fuelType=PS|generation` = **419** (n=939, 2026-09-18T05:45:31.422962Z)
- `FUELINST|fuelType=WIND|generation` = **14046** (n=939, 2026-09-18T05:45:31.422962Z)
- `IMBALNGC|TOTAL|imbalance` = **10704** (n=155, 2026-09-18T05:20:21.081324Z)
- `INDDEM|TOTAL|demand` = **-11169** (n=155, 2026-09-18T05:20:21.081324Z)
- `INDGEN|TOTAL|generation` = **27518** (n=155, 2026-09-18T05:20:21.081324Z)
- `MELNGC|TOTAL|margin` = **38019** (n=155, 2026-09-18T05:19:16.747972Z)
- `NDF|TOTAL|demand` = **16314** (n=158, 2026-09-18T05:17:26.772425Z)
- `TSDF|TOTAL|demand` = **16814** (n=158, 2026-09-18T05:17:26.772425Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T05:46:33.783519Z` — **MID**: 0 rows; marker `2026-09-18T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:46:32.050018Z` — **MID**: 0 rows; marker `2026-09-18T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:46:30.219610Z` — **MID**: 0 rows; marker `2026-09-18T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:46:28.492093Z` — **MID**: 0 rows; marker `2026-09-18T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:46:26.568064Z` — **MID**: 0 rows; marker `2026-09-18T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:46:22.509901Z` — **MID**: 0 rows; marker `2026-09-18T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:46:22.509901Z` — **FREQ**: 5761 rows; marker `2026-09-18T05:45:45Z`
- `2026-09-18T05:46:20.793758Z` — **MID**: 0 rows; marker `2026-09-18T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:46:18.720807Z` — **MID**: 0 rows; marker `2026-09-18T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:46:16.984233Z` — **MID**: 0 rows; marker `2026-09-18T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:46:15.251559Z` — **MID**: 0 rows; marker `2026-09-18T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:46:13.525043Z` — **MID**: 0 rows; marker `2026-09-18T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:46:11.818694Z` — **MID**: 0 rows; marker `2026-09-18T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:46:10.105102Z` — **MID**: 0 rows; marker `2026-09-18T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:46:08.315685Z` — **MID**: 0 rows; marker `2026-09-18T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
