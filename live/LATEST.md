# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T08:35:12.228379Z`  
Current process started UTC: `2026-09-19T08:31:10.824284Z`  
1-second metadata polls in this process: **156**  
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

- `FUELINST|fuelType=INTVKL|generation` = **910** (n=1216, 2026-09-19T08:30:23.271302Z)
- `FUELINST|fuelType=NPSHYD|generation` = **369** (n=1216, 2026-09-19T08:30:23.271302Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=1216, 2026-09-19T08:30:23.271302Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1216, 2026-09-19T08:30:23.271302Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1216, 2026-09-19T08:30:23.271302Z)
- `FUELINST|fuelType=OTHER|generation` = **322** (n=1216, 2026-09-19T08:30:23.271302Z)
- `FUELINST|fuelType=PS|generation` = **-423** (n=1216, 2026-09-19T08:30:23.271302Z)
- `FUELINST|fuelType=WIND|generation` = **15142** (n=1216, 2026-09-19T08:30:23.271302Z)
- `IMBALNGC|TOTAL|imbalance` = **8998** (n=200, 2026-09-19T08:19:37.431448Z)
- `INDDEM|TOTAL|demand` = **-12081** (n=200, 2026-09-19T08:19:21.440084Z)
- `INDGEN|TOTAL|generation` = **26793** (n=200, 2026-09-19T08:19:21.440084Z)
- `MELNGC|TOTAL|margin` = **37615** (n=200, 2026-09-19T08:18:31.551947Z)
- `NDF|TOTAL|demand` = **15940** (n=205, 2026-09-19T08:17:14.399276Z)
- `TSDF|TOTAL|demand` = **17802** (n=205, 2026-09-19T08:17:14.399276Z)
- `WINDFOR|TOTAL|generation` = **6987** (n=35, 2026-09-19T08:30:39.402179Z)

## Latest publication events

- `2026-09-19T08:35:10.783333Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:35:09.333734Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:35:07.888135Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:35:06.337744Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:35:04.878050Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:35:03.394892Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:35:01.944020Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:35:00.507384Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:34:58.702722Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:34:57.212582Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:34:55.733124Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:34:54.287331Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:34:52.872770Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:34:51.403934Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:34:49.896120Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
