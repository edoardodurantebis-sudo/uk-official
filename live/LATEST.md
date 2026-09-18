# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T08:17:51.594175Z`  
Current process started UTC: `2026-09-18T08:13:50.373185Z`  
1-second metadata polls in this process: **165**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=969, 2026-09-18T08:15:29.671959Z)
- `FUELINST|fuelType=NPSHYD|generation` = **378** (n=969, 2026-09-18T08:15:29.671959Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=969, 2026-09-18T08:15:29.671959Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=969, 2026-09-18T08:15:29.671959Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=969, 2026-09-18T08:15:29.671959Z)
- `FUELINST|fuelType=OTHER|generation` = **1607** (n=969, 2026-09-18T08:15:29.671959Z)
- `FUELINST|fuelType=PS|generation` = **381** (n=969, 2026-09-18T08:15:29.671959Z)
- `FUELINST|fuelType=WIND|generation` = **12421** (n=969, 2026-09-18T08:15:29.671959Z)
- `IMBALNGC|TOTAL|imbalance` = **10218** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDDEM|TOTAL|demand` = **-11739** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDGEN|TOTAL|generation` = **27722** (n=159, 2026-09-18T07:19:58.374346Z)
- `MELNGC|TOTAL|margin` = **37765** (n=159, 2026-09-18T07:19:09.419948Z)
- `NDF|TOTAL|demand` = **16454** (n=164, 2026-09-18T08:17:38.545846Z)
- `TSDF|TOTAL|demand` = **17644** (n=164, 2026-09-18T08:17:38.545846Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T08:17:49.957839Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:17:48.614624Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:17:47.331098Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:17:46.039527Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:17:44.654904Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:17:43.230390Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:17:41.931740Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:17:38.545846Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:17:38.545846Z` — **TSDF**: 702 rows; marker `2026-09-18T08:17:00Z`
- `2026-09-18T08:17:38.545846Z` — **NDF**: 39 rows; marker `2026-09-18T08:17:00Z`
- `2026-09-18T08:17:36.005218Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:17:34.489079Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:17:33.140282Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:17:31.825498Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:17:30.471808Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
