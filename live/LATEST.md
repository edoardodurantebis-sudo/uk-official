# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T21:33:27.652952Z`  
Current process started UTC: `2026-09-17T21:29:26.340242Z`  
1-second metadata polls in this process: **141**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **424** (n=840, 2026-09-17T21:30:31.051450Z)
- `FUELINST|fuelType=NPSHYD|generation` = **492** (n=840, 2026-09-17T21:30:31.051450Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=840, 2026-09-17T21:30:31.051450Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=840, 2026-09-17T21:30:31.051450Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=840, 2026-09-17T21:30:31.051450Z)
- `FUELINST|fuelType=OTHER|generation` = **741** (n=840, 2026-09-17T21:30:31.051450Z)
- `FUELINST|fuelType=PS|generation` = **355** (n=840, 2026-09-17T21:30:31.051450Z)
- `FUELINST|fuelType=WIND|generation` = **14912** (n=840, 2026-09-17T21:30:31.051450Z)
- `IMBALNGC|TOTAL|imbalance` = **9702** (n=139, 2026-09-17T21:23:13.923147Z)
- `INDDEM|TOTAL|demand` = **-11159** (n=139, 2026-09-17T21:23:13.923147Z)
- `INDGEN|TOTAL|generation` = **26516** (n=139, 2026-09-17T21:23:13.923147Z)
- `MELNGC|TOTAL|margin` = **36445** (n=139, 2026-09-17T21:20:23.938551Z)
- `NDF|TOTAL|demand` = **16314** (n=142, 2026-09-17T21:17:59.034802Z)
- `TSDF|TOTAL|demand` = **16814** (n=142, 2026-09-17T21:17:59.034802Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T21:33:25.979020Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:33:24.254903Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:33:22.681981Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:33:21.050158Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:33:19.434039Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:33:17.834222Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:33:16.254789Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:33:14.323763Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:33:12.581809Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:33:10.742890Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:33:08.979382Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:33:07.396290Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:33:05.724751Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:33:04.028066Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:33:02.429240Z` — **MID**: 0 rows; marker `2026-09-17T21:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
