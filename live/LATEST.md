# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T15:33:43.269907Z`  
Current process started UTC: `2026-09-18T15:29:41.802045Z`  
1-second metadata polls in this process: **131**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1051** (n=1056, 2026-09-18T15:30:29.744162Z)
- `FUELINST|fuelType=NPSHYD|generation` = **345** (n=1056, 2026-09-18T15:30:29.744162Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1056, 2026-09-18T15:30:29.744162Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1056, 2026-09-18T15:30:29.744162Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1056, 2026-09-18T15:30:29.744162Z)
- `FUELINST|fuelType=OTHER|generation` = **160** (n=1056, 2026-09-18T15:30:29.744162Z)
- `FUELINST|fuelType=PS|generation` = **226** (n=1056, 2026-09-18T15:30:29.744162Z)
- `FUELINST|fuelType=WIND|generation` = **16619** (n=1056, 2026-09-18T15:30:29.744162Z)
- `IMBALNGC|TOTAL|imbalance` = **8521** (n=174, 2026-09-18T15:23:28.385039Z)
- `INDDEM|TOTAL|demand` = **-10767** (n=174, 2026-09-18T15:23:10.555240Z)
- `INDGEN|TOTAL|generation` = **25571** (n=174, 2026-09-18T15:23:28.385039Z)
- `MELNGC|TOTAL|margin` = **38024** (n=174, 2026-09-18T15:20:56.613821Z)
- `NDF|TOTAL|demand` = **16550** (n=178, 2026-09-18T15:18:18.353381Z)
- `TSDF|TOTAL|demand` = **17050** (n=178, 2026-09-18T15:18:18.353381Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T15:33:41.484643Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:33:39.756639Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:33:38.044829Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:33:36.347549Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:33:34.620157Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:33:32.916121Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:33:30.873441Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:33:29.170939Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:33:27.477653Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:33:25.738482Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:33:24.000331Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:33:22.301451Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:33:20.606904Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:33:18.614391Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:33:16.883416Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
