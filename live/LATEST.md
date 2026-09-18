# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T14:38:23.972183Z`  
Current process started UTC: `2026-09-18T14:34:23.904166Z`  
1-second metadata polls in this process: **164**  
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

- `FUELINST|fuelType=INTVKL|generation` = **716** (n=1045, 2026-09-18T14:35:30.848536Z)
- `FUELINST|fuelType=NPSHYD|generation` = **317** (n=1045, 2026-09-18T14:35:30.848536Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1045, 2026-09-18T14:35:30.848536Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1045, 2026-09-18T14:35:30.848536Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1045, 2026-09-18T14:35:30.848536Z)
- `FUELINST|fuelType=OTHER|generation` = **239** (n=1045, 2026-09-18T14:35:30.848536Z)
- `FUELINST|fuelType=PS|generation` = **-473** (n=1045, 2026-09-18T14:35:30.848536Z)
- `FUELINST|fuelType=WIND|generation` = **16492** (n=1045, 2026-09-18T14:35:30.848536Z)
- `IMBALNGC|TOTAL|imbalance` = **8550** (n=172, 2026-09-18T14:24:33.593094Z)
- `INDDEM|TOTAL|demand` = **-10767** (n=172, 2026-09-18T14:24:17.122424Z)
- `INDGEN|TOTAL|generation` = **25600** (n=172, 2026-09-18T14:24:17.122424Z)
- `MELNGC|TOTAL|margin` = **38296** (n=172, 2026-09-18T14:21:10.291729Z)
- `NDF|TOTAL|demand` = **16550** (n=176, 2026-09-18T14:18:53.718876Z)
- `TSDF|TOTAL|demand` = **17050** (n=176, 2026-09-18T14:18:53.718876Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T14:38:22.643438Z` — **MID**: 0 rows; marker `2026-09-18T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:38:21.253097Z` — **MID**: 0 rows; marker `2026-09-18T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:38:19.965543Z` — **MID**: 0 rows; marker `2026-09-18T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:38:18.635733Z` — **MID**: 0 rows; marker `2026-09-18T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:38:15.748532Z` — **MID**: 0 rows; marker `2026-09-18T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:38:15.748532Z` — **FREQ**: 5761 rows; marker `2026-09-18T14:37:45Z`
- `2026-09-18T14:38:14.304182Z` — **MID**: 0 rows; marker `2026-09-18T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:38:12.985369Z` — **MID**: 0 rows; marker `2026-09-18T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:38:11.647124Z` — **MID**: 0 rows; marker `2026-09-18T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:38:10.293786Z` — **MID**: 0 rows; marker `2026-09-18T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:38:08.781622Z` — **MID**: 0 rows; marker `2026-09-18T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:38:07.497251Z` — **MID**: 0 rows; marker `2026-09-18T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:38:05.890393Z` — **MID**: 0 rows; marker `2026-09-18T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:38:04.539391Z` — **MID**: 0 rows; marker `2026-09-18T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:38:03.178768Z` — **MID**: 0 rows; marker `2026-09-18T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
