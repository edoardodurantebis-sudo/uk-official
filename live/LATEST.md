# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T08:14:05.840060Z`  
Current process started UTC: `2026-09-19T08:10:05.287827Z`  
1-second metadata polls in this process: **175**  
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

- `FUELINST|fuelType=INTVKL|generation` = **910** (n=1212, 2026-09-19T08:10:25.656259Z)
- `FUELINST|fuelType=NPSHYD|generation` = **371** (n=1212, 2026-09-19T08:10:25.656259Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1212, 2026-09-19T08:10:25.656259Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1212, 2026-09-19T08:10:25.656259Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1212, 2026-09-19T08:10:25.656259Z)
- `FUELINST|fuelType=OTHER|generation` = **311** (n=1212, 2026-09-19T08:10:25.656259Z)
- `FUELINST|fuelType=PS|generation` = **-592** (n=1212, 2026-09-19T08:10:25.656259Z)
- `FUELINST|fuelType=WIND|generation` = **15428** (n=1212, 2026-09-19T08:10:25.656259Z)
- `IMBALNGC|TOTAL|imbalance` = **8458** (n=199, 2026-09-19T07:20:02.514143Z)
- `INDDEM|TOTAL|demand` = **-12078** (n=199, 2026-09-19T07:19:46.165443Z)
- `INDGEN|TOTAL|generation` = **26869** (n=199, 2026-09-19T07:19:46.165443Z)
- `MELNGC|TOTAL|margin` = **37026** (n=199, 2026-09-19T07:19:09.074847Z)
- `NDF|TOTAL|demand` = **19060** (n=204, 2026-09-19T07:45:58.702458Z)
- `TSDF|TOTAL|demand` = **19560** (n=204, 2026-09-19T07:45:58.702458Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T08:14:04.465939Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:14:03.156494Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:14:01.868260Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:14:00.561598Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:13:59.219421Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:13:57.640427Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:13:56.336677Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:13:55.021355Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:13:53.712071Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:13:52.388411Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:13:51.119857Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:13:49.798487Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:13:48.500394Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:13:47.192628Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:13:45.867950Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
