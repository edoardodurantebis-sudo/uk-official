# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T14:34:10.762498Z`  
Current process started UTC: `2026-09-18T14:30:10.681606Z`  
1-second metadata polls in this process: **143**  
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

- `FUELINST|fuelType=INTVKL|generation` = **716** (n=1044, 2026-09-18T14:30:43.028489Z)
- `FUELINST|fuelType=NPSHYD|generation` = **317** (n=1044, 2026-09-18T14:30:43.028489Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3340** (n=1044, 2026-09-18T14:30:43.028489Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1044, 2026-09-18T14:30:43.028489Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1044, 2026-09-18T14:30:43.028489Z)
- `FUELINST|fuelType=OTHER|generation` = **293** (n=1044, 2026-09-18T14:30:43.028489Z)
- `FUELINST|fuelType=PS|generation` = **-468** (n=1044, 2026-09-18T14:30:43.028489Z)
- `FUELINST|fuelType=WIND|generation` = **16222** (n=1044, 2026-09-18T14:30:43.028489Z)
- `IMBALNGC|TOTAL|imbalance` = **8550** (n=172, 2026-09-18T14:24:33.593094Z)
- `INDDEM|TOTAL|demand` = **-10767** (n=172, 2026-09-18T14:24:17.122424Z)
- `INDGEN|TOTAL|generation` = **25600** (n=172, 2026-09-18T14:24:17.122424Z)
- `MELNGC|TOTAL|margin` = **38296** (n=172, 2026-09-18T14:21:10.291729Z)
- `NDF|TOTAL|demand` = **16550** (n=176, 2026-09-18T14:18:53.718876Z)
- `TSDF|TOTAL|demand` = **17050** (n=176, 2026-09-18T14:18:53.718876Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T14:34:09.278665Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:34:07.804545Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:34:06.326875Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:34:04.880629Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:34:03.404735Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:34:01.933283Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:34:00.444132Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:33:58.930882Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:33:56.936463Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:33:55.017687Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:33:53.533082Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:33:52.055967Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:33:50.589913Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:33:49.121612Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:33:47.665921Z` — **MID**: 0 rows; marker `2026-09-18T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
