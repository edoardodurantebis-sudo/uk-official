# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T11:37:21.496413Z`  
Current process started UTC: `2026-09-19T11:33:20.817586Z`  
1-second metadata polls in this process: **190**  
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

- `FUELINST|fuelType=INTVKL|generation` = **333** (n=1253, 2026-09-19T11:35:30.891655Z)
- `FUELINST|fuelType=NPSHYD|generation` = **305** (n=1253, 2026-09-19T11:35:30.891655Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1253, 2026-09-19T11:35:30.891655Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1253, 2026-09-19T11:35:30.891655Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1253, 2026-09-19T11:35:30.891655Z)
- `FUELINST|fuelType=OTHER|generation` = **630** (n=1253, 2026-09-19T11:35:30.891655Z)
- `FUELINST|fuelType=PS|generation` = **-935** (n=1253, 2026-09-19T11:35:30.891655Z)
- `FUELINST|fuelType=WIND|generation` = **15658** (n=1253, 2026-09-19T11:35:30.891655Z)
- `IMBALNGC|TOTAL|imbalance` = **-3354** (n=206, 2026-09-19T11:25:26.544383Z)
- `INDDEM|TOTAL|demand` = **-11780** (n=206, 2026-09-19T11:25:10.722520Z)
- `INDGEN|TOTAL|generation` = **16777** (n=206, 2026-09-19T11:24:54.717962Z)
- `MELNGC|TOTAL|margin` = **36659** (n=206, 2026-09-19T11:21:14.136124Z)
- `NDF|TOTAL|demand` = **19631** (n=211, 2026-09-19T11:18:50.597516Z)
- `TSDF|TOTAL|demand` = **20131** (n=211, 2026-09-19T11:18:50.597516Z)
- `WINDFOR|TOTAL|generation` = **6656** (n=36, 2026-09-19T10:30:47.910212Z)

## Latest publication events

- `2026-09-19T11:37:20.238868Z` — **MID**: 0 rows; marker `2026-09-19T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:37:19.034104Z` — **MID**: 0 rows; marker `2026-09-19T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:37:17.864225Z` — **MID**: 0 rows; marker `2026-09-19T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:37:16.655394Z` — **MID**: 0 rows; marker `2026-09-19T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:37:15.447742Z` — **MID**: 0 rows; marker `2026-09-19T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:37:14.225478Z` — **MID**: 0 rows; marker `2026-09-19T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:37:13.025481Z` — **MID**: 0 rows; marker `2026-09-19T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:37:11.813913Z` — **MID**: 0 rows; marker `2026-09-19T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:37:10.605973Z` — **MID**: 0 rows; marker `2026-09-19T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:37:09.380067Z` — **MID**: 0 rows; marker `2026-09-19T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:37:07.860491Z` — **MID**: 0 rows; marker `2026-09-19T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:37:06.664988Z` — **MID**: 0 rows; marker `2026-09-19T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:37:05.464389Z` — **MID**: 0 rows; marker `2026-09-19T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:37:04.260652Z` — **MID**: 0 rows; marker `2026-09-19T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:37:03.077835Z` — **MID**: 0 rows; marker `2026-09-19T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
