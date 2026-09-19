# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T08:43:35.382371Z`  
Current process started UTC: `2026-09-19T08:39:35.113297Z`  
1-second metadata polls in this process: **154**  
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

- `FUELINST|fuelType=INTVKL|generation` = **910** (n=1218, 2026-09-19T08:40:27.214195Z)
- `FUELINST|fuelType=NPSHYD|generation` = **358** (n=1218, 2026-09-19T08:40:27.214195Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1218, 2026-09-19T08:40:27.214195Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1218, 2026-09-19T08:40:27.214195Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1218, 2026-09-19T08:40:27.214195Z)
- `FUELINST|fuelType=OTHER|generation` = **366** (n=1218, 2026-09-19T08:40:27.214195Z)
- `FUELINST|fuelType=PS|generation` = **-423** (n=1218, 2026-09-19T08:40:27.214195Z)
- `FUELINST|fuelType=WIND|generation` = **15089** (n=1218, 2026-09-19T08:40:27.214195Z)
- `IMBALNGC|TOTAL|imbalance` = **8998** (n=200, 2026-09-19T08:19:37.431448Z)
- `INDDEM|TOTAL|demand` = **-12081** (n=200, 2026-09-19T08:19:21.440084Z)
- `INDGEN|TOTAL|generation` = **26793** (n=200, 2026-09-19T08:19:21.440084Z)
- `MELNGC|TOTAL|margin` = **37615** (n=200, 2026-09-19T08:18:31.551947Z)
- `NDF|TOTAL|demand` = **15940** (n=205, 2026-09-19T08:17:14.399276Z)
- `TSDF|TOTAL|demand` = **17802** (n=205, 2026-09-19T08:17:14.399276Z)
- `WINDFOR|TOTAL|generation` = **6987** (n=35, 2026-09-19T08:30:39.402179Z)

## Latest publication events

- `2026-09-19T08:43:33.868492Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:43:32.396960Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:43:30.913501Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:43:29.417281Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:43:27.614196Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:43:26.084077Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:43:24.592308Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:43:23.145352Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:43:21.639619Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:43:20.086414Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:43:18.644555Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:43:17.199118Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:43:15.702798Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:43:14.180006Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:43:12.732290Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
