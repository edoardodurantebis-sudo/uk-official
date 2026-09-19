# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T06:41:34.144580Z`  
Current process started UTC: `2026-09-19T06:37:33.356226Z`  
1-second metadata polls in this process: **174**  
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

- `FUELINST|fuelType=INTVKL|generation` = **357** (n=1194, 2026-09-19T06:40:18.113470Z)
- `FUELINST|fuelType=NPSHYD|generation` = **368** (n=1194, 2026-09-19T06:40:18.113470Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1194, 2026-09-19T06:40:18.113470Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1194, 2026-09-19T06:40:18.113470Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1194, 2026-09-19T06:40:18.113470Z)
- `FUELINST|fuelType=OTHER|generation` = **1058** (n=1194, 2026-09-19T06:40:18.113470Z)
- `FUELINST|fuelType=PS|generation` = **-430** (n=1194, 2026-09-19T06:40:18.113470Z)
- `FUELINST|fuelType=WIND|generation` = **15842** (n=1194, 2026-09-19T06:40:18.113470Z)
- `IMBALNGC|TOTAL|imbalance` = **9725** (n=197, 2026-09-19T06:21:03.713324Z)
- `INDDEM|TOTAL|demand` = **-10863** (n=197, 2026-09-19T06:20:47.840036Z)
- `INDGEN|TOTAL|generation` = **26914** (n=197, 2026-09-19T06:21:03.713324Z)
- `MELNGC|TOTAL|margin` = **38283** (n=197, 2026-09-19T06:19:39.477513Z)
- `NDF|TOTAL|demand` = **16550** (n=201, 2026-09-19T06:17:40.734662Z)
- `TSDF|TOTAL|demand` = **17190** (n=201, 2026-09-19T06:17:40.734662Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T06:41:32.854467Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:41:31.543615Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:41:30.263746Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:41:29.004238Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:41:27.557198Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:41:26.226139Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:41:24.938502Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:41:23.283696Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:41:21.995428Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:41:20.682379Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:41:19.399904Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:41:18.121111Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:41:16.796713Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:41:15.513660Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:41:14.214309Z` — **MID**: 0 rows; marker `2026-09-19T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
