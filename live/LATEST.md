# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T07:36:22.505168Z`  
Current process started UTC: `2026-09-19T07:32:22.256165Z`  
1-second metadata polls in this process: **224**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1421** (n=1205, 2026-09-19T07:35:36.047236Z)
- `FUELINST|fuelType=NPSHYD|generation` = **370** (n=1205, 2026-09-19T07:35:36.047236Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1205, 2026-09-19T07:35:36.047236Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1205, 2026-09-19T07:35:36.047236Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1205, 2026-09-19T07:35:36.047236Z)
- `FUELINST|fuelType=OTHER|generation` = **559** (n=1205, 2026-09-19T07:35:36.047236Z)
- `FUELINST|fuelType=PS|generation` = **-421** (n=1205, 2026-09-19T07:35:36.047236Z)
- `FUELINST|fuelType=WIND|generation` = **15705** (n=1205, 2026-09-19T07:35:36.047236Z)
- `IMBALNGC|TOTAL|imbalance` = **8458** (n=199, 2026-09-19T07:20:02.514143Z)
- `INDDEM|TOTAL|demand` = **-12078** (n=199, 2026-09-19T07:19:46.165443Z)
- `INDGEN|TOTAL|generation` = **26869** (n=199, 2026-09-19T07:19:46.165443Z)
- `MELNGC|TOTAL|margin` = **37026** (n=199, 2026-09-19T07:19:09.074847Z)
- `NDF|TOTAL|demand` = **16550** (n=203, 2026-09-19T07:17:28.186180Z)
- `TSDF|TOTAL|demand` = **18412** (n=203, 2026-09-19T07:17:28.186180Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T07:36:21.531168Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:36:20.531091Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:36:19.530965Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:36:18.530822Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:36:17.530659Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:36:16.530549Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:36:15.530399Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:36:14.530259Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:36:13.530128Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:36:12.529986Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:36:11.529856Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:36:10.529685Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:36:08.086658Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:36:08.086658Z` — **FREQ**: 5761 rows; marker `2026-09-19T07:35:45Z`
- `2026-09-19T07:36:07.086578Z` — **MID**: 0 rows; marker `2026-09-19T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
