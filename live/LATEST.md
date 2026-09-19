# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T11:54:18.197604Z`  
Current process started UTC: `2026-09-19T11:50:17.702824Z`  
1-second metadata polls in this process: **230**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16777, delta=25, z=-3.78 -> state changed
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16752, delta=-9313, z=-3.94 -> state changed
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **333** (n=1256, 2026-09-19T11:50:35.128307Z)
- `FUELINST|fuelType=NPSHYD|generation` = **303** (n=1256, 2026-09-19T11:50:35.128307Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1256, 2026-09-19T11:50:35.128307Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1256, 2026-09-19T11:50:35.128307Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1256, 2026-09-19T11:50:35.128307Z)
- `FUELINST|fuelType=OTHER|generation` = **653** (n=1256, 2026-09-19T11:50:35.128307Z)
- `FUELINST|fuelType=PS|generation` = **-939** (n=1256, 2026-09-19T11:50:35.128307Z)
- `FUELINST|fuelType=WIND|generation` = **15745** (n=1256, 2026-09-19T11:50:35.128307Z)
- `IMBALNGC|TOTAL|imbalance` = **-3354** (n=206, 2026-09-19T11:25:26.544383Z)
- `INDDEM|TOTAL|demand` = **-11780** (n=206, 2026-09-19T11:25:10.722520Z)
- `INDGEN|TOTAL|generation` = **16777** (n=206, 2026-09-19T11:24:54.717962Z)
- `MELNGC|TOTAL|margin` = **36781** (n=207, 2026-09-19T11:51:22.558353Z)
- `NDF|TOTAL|demand` = **19509** (n=212, 2026-09-19T11:48:28.385634Z)
- `TSDF|TOTAL|demand` = **20009** (n=212, 2026-09-19T11:48:28.385634Z)
- `WINDFOR|TOTAL|generation` = **6656** (n=36, 2026-09-19T10:30:47.910212Z)

## Latest publication events

- `2026-09-19T11:54:17.141972Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:54:16.141832Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:54:15.141733Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:54:14.141562Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:54:13.141475Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:54:12.128245Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:54:11.128130Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:54:10.128007Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:54:09.127866Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:54:08.127732Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:54:07.127649Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:54:06.114039Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:54:05.113920Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:54:03.790761Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:54:02.790656Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
