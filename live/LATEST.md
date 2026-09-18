# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T01:50:42.138661Z`  
Current process started UTC: `2026-09-18T01:46:42.085497Z`  
1-second metadata polls in this process: **142**  
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

- `FUELINST|fuelType=INTVKL|generation` = **781** (n=892, 2026-09-18T01:50:31.739089Z)
- `FUELINST|fuelType=NPSHYD|generation` = **417** (n=892, 2026-09-18T01:50:31.739089Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=892, 2026-09-18T01:50:31.739089Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=892, 2026-09-18T01:50:31.739089Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=892, 2026-09-18T01:50:31.739089Z)
- `FUELINST|fuelType=OTHER|generation` = **160** (n=892, 2026-09-18T01:50:31.739089Z)
- `FUELINST|fuelType=PS|generation` = **532** (n=892, 2026-09-18T01:50:31.739089Z)
- `FUELINST|fuelType=WIND|generation` = **14428** (n=892, 2026-09-18T01:50:31.739089Z)
- `IMBALNGC|TOTAL|imbalance` = **10127** (n=147, 2026-09-18T01:21:58.893655Z)
- `INDDEM|TOTAL|demand` = **-11192** (n=147, 2026-09-18T01:21:42.565092Z)
- `INDGEN|TOTAL|generation` = **26941** (n=147, 2026-09-18T01:21:58.893655Z)
- `MELNGC|TOTAL|margin` = **36705** (n=148, 2026-09-18T01:49:25.897354Z)
- `NDF|TOTAL|demand` = **16314** (n=151, 2026-09-18T01:47:48.325279Z)
- `TSDF|TOTAL|demand` = **16814** (n=151, 2026-09-18T01:47:48.325279Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T01:50:40.597648Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:50:38.973176Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:50:37.431478Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:50:35.915273Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:50:34.352034Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:50:31.739089Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:50:31.739089Z` — **FUELINST**: 80 rows; marker `2026-09-18T01:50:00Z`
- `2026-09-18T01:50:30.214598Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:50:28.695812Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:50:27.070726Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:50:25.518565Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:50:23.905360Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:50:22.311042Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:50:20.556229Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:50:19.029450Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
