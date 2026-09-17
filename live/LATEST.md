# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T23:43:44.918701Z`  
Current process started UTC: `2026-09-17T23:39:44.542706Z`  
1-second metadata polls in this process: **230**  
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

- `FUELINST|fuelType=INTVKL|generation` = **608** (n=866, 2026-09-17T23:40:33.399921Z)
- `FUELINST|fuelType=NPSHYD|generation` = **453** (n=866, 2026-09-17T23:40:33.399921Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3320** (n=866, 2026-09-17T23:40:33.399921Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=866, 2026-09-17T23:40:33.399921Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=866, 2026-09-17T23:40:33.399921Z)
- `FUELINST|fuelType=OTHER|generation` = **586** (n=866, 2026-09-17T23:40:33.399921Z)
- `FUELINST|fuelType=PS|generation` = **24** (n=866, 2026-09-17T23:40:33.399921Z)
- `FUELINST|fuelType=WIND|generation` = **14577** (n=866, 2026-09-17T23:40:33.399921Z)
- `IMBALNGC|TOTAL|imbalance` = **9745** (n=143, 2026-09-17T23:22:08.151476Z)
- `INDDEM|TOTAL|demand` = **-11183** (n=143, 2026-09-17T23:22:08.151476Z)
- `INDGEN|TOTAL|generation` = **26559** (n=143, 2026-09-17T23:22:08.151476Z)
- `MELNGC|TOTAL|margin` = **36572** (n=143, 2026-09-17T23:20:11.082648Z)
- `NDF|TOTAL|demand` = **16314** (n=146, 2026-09-17T23:18:11.234096Z)
- `TSDF|TOTAL|demand` = **16814** (n=146, 2026-09-17T23:18:11.234096Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-17T23:43:43.966379Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:43:42.966260Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:43:41.966178Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:43:40.966062Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:43:39.965945Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:43:38.965837Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:43:37.965720Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:43:36.965610Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:43:35.965435Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:43:34.965273Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:43:33.965175Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:43:32.359867Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:43:31.359746Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:43:30.359611Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:43:29.359514Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
