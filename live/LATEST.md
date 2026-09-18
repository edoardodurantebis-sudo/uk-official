# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T19:32:42.523449Z`  
Current process started UTC: `2026-09-18T19:28:41.153658Z`  
1-second metadata polls in this process: **169**  
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

- `FUELINST|fuelType=INTVKL|generation` = **943** (n=1081, 2026-09-18T19:30:34.296062Z)
- `FUELINST|fuelType=NPSHYD|generation` = **487** (n=1081, 2026-09-18T19:30:34.296062Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1081, 2026-09-18T19:30:34.296062Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1081, 2026-09-18T19:30:34.296062Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1081, 2026-09-18T19:30:34.296062Z)
- `FUELINST|fuelType=OTHER|generation` = **1237** (n=1081, 2026-09-18T19:30:34.296062Z)
- `FUELINST|fuelType=PS|generation` = **446** (n=1081, 2026-09-18T19:30:34.296062Z)
- `FUELINST|fuelType=WIND|generation` = **16635** (n=1081, 2026-09-18T19:30:34.296062Z)
- `IMBALNGC|TOTAL|imbalance` = **9032** (n=178, 2026-09-18T19:22:27.550765Z)
- `INDDEM|TOTAL|demand` = **-10891** (n=178, 2026-09-18T19:22:12.034913Z)
- `INDGEN|TOTAL|generation` = **26226** (n=178, 2026-09-18T19:22:12.034913Z)
- `MELNGC|TOTAL|margin` = **37505** (n=178, 2026-09-18T19:20:16.544424Z)
- `NDF|TOTAL|demand` = **16550** (n=182, 2026-09-18T19:17:43.952660Z)
- `TSDF|TOTAL|demand` = **17194** (n=182, 2026-09-18T19:17:43.952660Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T19:32:40.980375Z` — **MID**: 0 rows; marker `2026-09-18T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:32:39.557518Z` — **MID**: 0 rows; marker `2026-09-18T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:32:38.071285Z` — **MID**: 0 rows; marker `2026-09-18T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:32:36.731036Z` — **MID**: 0 rows; marker `2026-09-18T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:32:35.432893Z` — **MID**: 0 rows; marker `2026-09-18T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:32:34.112835Z` — **MID**: 0 rows; marker `2026-09-18T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:32:32.777629Z` — **MID**: 0 rows; marker `2026-09-18T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:32:31.467871Z` — **MID**: 0 rows; marker `2026-09-18T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:32:30.103484Z` — **MID**: 0 rows; marker `2026-09-18T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:32:28.745731Z` — **MID**: 0 rows; marker `2026-09-18T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:32:25.842824Z` — **MID**: 0 rows; marker `2026-09-18T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:32:25.842824Z` — **FREQ**: 5761 rows; marker `2026-09-18T19:31:45Z`
- `2026-09-18T19:32:24.443378Z` — **MID**: 0 rows; marker `2026-09-18T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:32:23.091361Z` — **MID**: 0 rows; marker `2026-09-18T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:32:21.738400Z` — **MID**: 0 rows; marker `2026-09-18T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
