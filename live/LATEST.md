# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T14:51:01.818356Z`  
Current process started UTC: `2026-09-18T14:47:00.782860Z`  
1-second metadata polls in this process: **213**  
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

- `FUELINST|fuelType=INTVKL|generation` = **716** (n=1048, 2026-09-18T14:50:28.265584Z)
- `FUELINST|fuelType=NPSHYD|generation` = **318** (n=1048, 2026-09-18T14:50:28.265584Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1048, 2026-09-18T14:50:28.265584Z)
- `FUELINST|fuelType=OCGT|generation` = **1** (n=1048, 2026-09-18T14:50:28.265584Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1048, 2026-09-18T14:50:28.265584Z)
- `FUELINST|fuelType=OTHER|generation` = **309** (n=1048, 2026-09-18T14:50:28.265584Z)
- `FUELINST|fuelType=PS|generation` = **-465** (n=1048, 2026-09-18T14:50:28.265584Z)
- `FUELINST|fuelType=WIND|generation` = **16881** (n=1048, 2026-09-18T14:50:28.265584Z)
- `IMBALNGC|TOTAL|imbalance` = **8550** (n=172, 2026-09-18T14:24:33.593094Z)
- `INDDEM|TOTAL|demand` = **-10767** (n=172, 2026-09-18T14:24:17.122424Z)
- `INDGEN|TOTAL|generation` = **25600** (n=172, 2026-09-18T14:24:17.122424Z)
- `MELNGC|TOTAL|margin` = **38296** (n=172, 2026-09-18T14:21:10.291729Z)
- `NDF|TOTAL|demand` = **16550** (n=177, 2026-09-18T14:48:51.573428Z)
- `TSDF|TOTAL|demand` = **17050** (n=177, 2026-09-18T14:48:51.573428Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T14:51:00.362871Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:50:59.360707Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:50:58.350066Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:50:57.349982Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:50:56.346211Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:50:55.329347Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:50:54.285188Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:50:53.285115Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:50:52.258383Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:50:51.221928Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:50:50.221855Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:50:49.208926Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:50:48.202997Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:50:47.077410Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:50:46.077331Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
