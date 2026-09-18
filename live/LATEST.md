# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T10:58:51.815853Z`  
Current process started UTC: `2026-09-18T10:54:51.328724Z`  
1-second metadata polls in this process: **220**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=1001, 2026-09-18T10:55:56.036599Z)
- `FUELINST|fuelType=NPSHYD|generation` = **326** (n=1001, 2026-09-18T10:55:56.036599Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1001, 2026-09-18T10:55:56.036599Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1001, 2026-09-18T10:55:56.036599Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1001, 2026-09-18T10:55:56.036599Z)
- `FUELINST|fuelType=OTHER|generation` = **968** (n=1001, 2026-09-18T10:55:56.036599Z)
- `FUELINST|fuelType=PS|generation` = **-698** (n=1001, 2026-09-18T10:55:56.036599Z)
- `FUELINST|fuelType=WIND|generation` = **12119** (n=1001, 2026-09-18T10:55:56.036599Z)
- `IMBALNGC|TOTAL|imbalance` = **8982** (n=165, 2026-09-18T10:55:56.036599Z)
- `INDDEM|TOTAL|demand` = **-10744** (n=165, 2026-09-18T10:55:23.440555Z)
- `INDGEN|TOTAL|generation` = **25652** (n=165, 2026-09-18T10:55:23.440555Z)
- `MELNGC|TOTAL|margin` = **38126** (n=165, 2026-09-18T10:51:27.792376Z)
- `NDF|TOTAL|demand` = **16170** (n=169, 2026-09-18T10:49:05.046376Z)
- `TSDF|TOTAL|demand` = **16670** (n=169, 2026-09-18T10:49:05.046376Z)
- `WINDFOR|TOTAL|generation` = **7615** (n=29, 2026-09-18T10:30:46.506872Z)

## Latest publication events

- `2026-09-18T10:58:50.782095Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:58:49.781961Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:58:48.781892Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:58:47.745284Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:58:46.728761Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:58:45.700517Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:58:44.629814Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:58:43.580517Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:58:42.572340Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:58:41.532822Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:58:40.532749Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:58:39.514069Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:58:38.499578Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:58:35.257987Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:58:34.200201Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
