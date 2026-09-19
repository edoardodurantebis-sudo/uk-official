# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T08:01:30.538413Z`  
Current process started UTC: `2026-09-19T07:57:30.428574Z`  
1-second metadata polls in this process: **219**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1300** (n=1210, 2026-09-19T08:00:28.614968Z)
- `FUELINST|fuelType=NPSHYD|generation` = **372** (n=1210, 2026-09-19T08:00:28.614968Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1210, 2026-09-19T08:00:28.614968Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1210, 2026-09-19T08:00:28.614968Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1210, 2026-09-19T08:00:28.614968Z)
- `FUELINST|fuelType=OTHER|generation` = **701** (n=1210, 2026-09-19T08:00:28.614968Z)
- `FUELINST|fuelType=PS|generation` = **-685** (n=1210, 2026-09-19T08:00:28.614968Z)
- `FUELINST|fuelType=WIND|generation` = **15719** (n=1210, 2026-09-19T08:00:28.614968Z)
- `IMBALNGC|TOTAL|imbalance` = **8458** (n=199, 2026-09-19T07:20:02.514143Z)
- `INDDEM|TOTAL|demand` = **-12078** (n=199, 2026-09-19T07:19:46.165443Z)
- `INDGEN|TOTAL|generation` = **26869** (n=199, 2026-09-19T07:19:46.165443Z)
- `MELNGC|TOTAL|margin` = **37026** (n=199, 2026-09-19T07:19:09.074847Z)
- `NDF|TOTAL|demand` = **19060** (n=204, 2026-09-19T07:45:58.702458Z)
- `TSDF|TOTAL|demand` = **19560** (n=204, 2026-09-19T07:45:58.702458Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T08:01:29.531578Z` — **MID**: 0 rows; marker `2026-09-19T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:01:28.508136Z` — **MID**: 0 rows; marker `2026-09-19T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:01:27.494148Z` — **MID**: 0 rows; marker `2026-09-19T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:01:26.473413Z` — **MID**: 0 rows; marker `2026-09-19T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:01:25.441442Z` — **MID**: 0 rows; marker `2026-09-19T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:01:24.386030Z` — **MID**: 0 rows; marker `2026-09-19T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:01:23.073843Z` — **MID**: 0 rows; marker `2026-09-19T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:01:22.073773Z` — **MID**: 0 rows; marker `2026-09-19T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:01:20.994559Z` — **MID**: 0 rows; marker `2026-09-19T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:01:19.989482Z` — **MID**: 0 rows; marker `2026-09-19T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:01:17.836779Z` — **MID**: 0 rows; marker `2026-09-19T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:01:16.625245Z` — **MID**: 0 rows; marker `2026-09-19T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:01:15.612446Z` — **MID**: 0 rows; marker `2026-09-19T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:01:14.292815Z` — **MID**: 0 rows; marker `2026-09-19T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:01:13.095637Z` — **MID**: 0 rows; marker `2026-09-19T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
