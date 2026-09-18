# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T14:08:23.151272Z`  
Current process started UTC: `2026-09-18T14:04:22.314645Z`  
1-second metadata polls in this process: **137**  
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

- `FUELINST|fuelType=INTVKL|generation` = **890** (n=1039, 2026-09-18T14:05:29.070072Z)
- `FUELINST|fuelType=NPSHYD|generation` = **325** (n=1039, 2026-09-18T14:05:29.070072Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=1039, 2026-09-18T14:05:29.070072Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1039, 2026-09-18T14:05:29.070072Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1039, 2026-09-18T14:05:29.070072Z)
- `FUELINST|fuelType=OTHER|generation` = **381** (n=1039, 2026-09-18T14:05:29.070072Z)
- `FUELINST|fuelType=PS|generation` = **-512** (n=1039, 2026-09-18T14:05:29.070072Z)
- `FUELINST|fuelType=WIND|generation` = **16030** (n=1039, 2026-09-18T14:05:29.070072Z)
- `IMBALNGC|TOTAL|imbalance` = **8928** (n=171, 2026-09-18T13:54:55.533395Z)
- `INDDEM|TOTAL|demand` = **-10745** (n=171, 2026-09-18T13:54:55.533395Z)
- `INDGEN|TOTAL|generation` = **25598** (n=171, 2026-09-18T13:54:55.533395Z)
- `MELNGC|TOTAL|margin` = **38192** (n=171, 2026-09-18T13:51:42.682305Z)
- `NDF|TOTAL|demand` = **16170** (n=175, 2026-09-18T13:49:24.414005Z)
- `TSDF|TOTAL|demand` = **16670** (n=175, 2026-09-18T13:49:41.459837Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T14:08:21.588397Z` — **MID**: 0 rows; marker `2026-09-18T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:08:20.040518Z` — **MID**: 0 rows; marker `2026-09-18T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:08:18.379192Z` — **MID**: 0 rows; marker `2026-09-18T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:08:15.043339Z` — **MID**: 0 rows; marker `2026-09-18T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:08:15.043339Z` — **FREQ**: 5761 rows; marker `2026-09-18T14:07:45Z`
- `2026-09-18T14:08:13.357676Z` — **MID**: 0 rows; marker `2026-09-18T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:08:11.496210Z` — **MID**: 0 rows; marker `2026-09-18T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:08:09.942024Z` — **MID**: 0 rows; marker `2026-09-18T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:08:08.403027Z` — **MID**: 0 rows; marker `2026-09-18T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:08:06.848333Z` — **MID**: 0 rows; marker `2026-09-18T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:08:05.191600Z` — **MID**: 0 rows; marker `2026-09-18T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:08:03.590656Z` — **MID**: 0 rows; marker `2026-09-18T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:08:02.034681Z` — **MID**: 0 rows; marker `2026-09-18T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:08:00.437078Z` — **MID**: 0 rows; marker `2026-09-18T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:07:58.341578Z` — **MID**: 0 rows; marker `2026-09-18T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
