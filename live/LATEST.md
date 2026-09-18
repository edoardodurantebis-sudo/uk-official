# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T14:29:22.598247Z`  
Current process started UTC: `2026-09-18T14:25:22.453111Z`  
1-second metadata polls in this process: **154**  
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

- `FUELINST|fuelType=INTVKL|generation` = **716** (n=1043, 2026-09-18T14:25:39.422653Z)
- `FUELINST|fuelType=NPSHYD|generation` = **317** (n=1043, 2026-09-18T14:25:39.422653Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1043, 2026-09-18T14:25:39.422653Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1043, 2026-09-18T14:25:39.422653Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1043, 2026-09-18T14:25:39.422653Z)
- `FUELINST|fuelType=OTHER|generation` = **360** (n=1043, 2026-09-18T14:25:39.422653Z)
- `FUELINST|fuelType=PS|generation` = **-468** (n=1043, 2026-09-18T14:25:39.422653Z)
- `FUELINST|fuelType=WIND|generation` = **16091** (n=1043, 2026-09-18T14:25:39.422653Z)
- `IMBALNGC|TOTAL|imbalance` = **8550** (n=172, 2026-09-18T14:24:33.593094Z)
- `INDDEM|TOTAL|demand` = **-10767** (n=172, 2026-09-18T14:24:17.122424Z)
- `INDGEN|TOTAL|generation` = **25600** (n=172, 2026-09-18T14:24:17.122424Z)
- `MELNGC|TOTAL|margin` = **38296** (n=172, 2026-09-18T14:21:10.291729Z)
- `NDF|TOTAL|demand` = **16550** (n=176, 2026-09-18T14:18:53.718876Z)
- `TSDF|TOTAL|demand` = **17050** (n=176, 2026-09-18T14:18:53.718876Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T14:29:21.127411Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:29:19.629636Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:29:18.153379Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:29:16.312790Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:29:14.850331Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:29:13.382118Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:29:11.876006Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:29:10.398281Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:29:08.884584Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:29:07.171475Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:29:05.649288Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:29:04.195340Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:29:02.473291Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:29:00.520869Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:28:59.059593Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
