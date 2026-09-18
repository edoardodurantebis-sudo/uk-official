# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T14:21:00.095068Z`  
Current process started UTC: `2026-09-18T14:16:59.412602Z`  
1-second metadata polls in this process: **205**  
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

- `FUELINST|fuelType=INTVKL|generation` = **716** (n=1042, 2026-09-18T14:20:28.819414Z)
- `FUELINST|fuelType=NPSHYD|generation` = **317** (n=1042, 2026-09-18T14:20:28.819414Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1042, 2026-09-18T14:20:28.819414Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1042, 2026-09-18T14:20:28.819414Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1042, 2026-09-18T14:20:28.819414Z)
- `FUELINST|fuelType=OTHER|generation` = **368** (n=1042, 2026-09-18T14:20:28.819414Z)
- `FUELINST|fuelType=PS|generation` = **-468** (n=1042, 2026-09-18T14:20:28.819414Z)
- `FUELINST|fuelType=WIND|generation` = **16027** (n=1042, 2026-09-18T14:20:28.819414Z)
- `IMBALNGC|TOTAL|imbalance` = **8928** (n=171, 2026-09-18T13:54:55.533395Z)
- `INDDEM|TOTAL|demand` = **-10745** (n=171, 2026-09-18T13:54:55.533395Z)
- `INDGEN|TOTAL|generation` = **25598** (n=171, 2026-09-18T13:54:55.533395Z)
- `MELNGC|TOTAL|margin` = **38192** (n=171, 2026-09-18T13:51:42.682305Z)
- `NDF|TOTAL|demand` = **16550** (n=176, 2026-09-18T14:18:53.718876Z)
- `TSDF|TOTAL|demand` = **17050** (n=176, 2026-09-18T14:18:53.718876Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T14:20:59.144184Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:20:58.144070Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:20:57.143953Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:20:56.143836Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:20:55.143722Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:20:54.143654Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:20:53.143540Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:20:52.143424Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:20:51.143308Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:20:50.143199Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:20:49.143087Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:20:48.142987Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:20:47.142871Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:20:46.142753Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:20:44.580410Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
