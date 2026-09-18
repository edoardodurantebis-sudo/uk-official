# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T14:16:49.333259Z`  
Current process started UTC: `2026-09-18T14:12:48.675182Z`  
1-second metadata polls in this process: **146**  
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

- `FUELINST|fuelType=INTVKL|generation` = **716** (n=1041, 2026-09-18T14:15:37.618007Z)
- `FUELINST|fuelType=NPSHYD|generation` = **316** (n=1041, 2026-09-18T14:15:37.618007Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=1041, 2026-09-18T14:15:37.618007Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1041, 2026-09-18T14:15:37.618007Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1041, 2026-09-18T14:15:37.618007Z)
- `FUELINST|fuelType=OTHER|generation` = **375** (n=1041, 2026-09-18T14:15:37.618007Z)
- `FUELINST|fuelType=PS|generation` = **-474** (n=1041, 2026-09-18T14:15:37.618007Z)
- `FUELINST|fuelType=WIND|generation` = **16051** (n=1041, 2026-09-18T14:15:37.618007Z)
- `IMBALNGC|TOTAL|imbalance` = **8928** (n=171, 2026-09-18T13:54:55.533395Z)
- `INDDEM|TOTAL|demand` = **-10745** (n=171, 2026-09-18T13:54:55.533395Z)
- `INDGEN|TOTAL|generation` = **25598** (n=171, 2026-09-18T13:54:55.533395Z)
- `MELNGC|TOTAL|margin` = **38192** (n=171, 2026-09-18T13:51:42.682305Z)
- `NDF|TOTAL|demand` = **16170** (n=175, 2026-09-18T13:49:24.414005Z)
- `TSDF|TOTAL|demand` = **16670** (n=175, 2026-09-18T13:49:41.459837Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T14:16:46.883120Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:16:45.151179Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:16:42.678569Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:16:40.921297Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:16:39.247694Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:16:37.467826Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:16:35.690881Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:16:34.213111Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:16:32.721640Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:16:30.920180Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:16:26.792624Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:16:26.792624Z` — **FREQ**: 5761 rows; marker `2026-09-18T14:15:45Z`
- `2026-09-18T14:16:24.848719Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:16:23.091473Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:16:21.314664Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
