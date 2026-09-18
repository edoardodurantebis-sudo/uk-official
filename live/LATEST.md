# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T23:26:34.534328Z`  
Current process started UTC: `2026-09-18T23:22:33.697830Z`  
1-second metadata polls in this process: **135**  
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

- `FUELINST|fuelType=INTVKL|generation` = **747** (n=1107, 2026-09-18T23:25:30.328207Z)
- `FUELINST|fuelType=NPSHYD|generation` = **429** (n=1107, 2026-09-18T23:25:30.328207Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=1107, 2026-09-18T23:25:30.328207Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1107, 2026-09-18T23:25:30.328207Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1107, 2026-09-18T23:25:30.328207Z)
- `FUELINST|fuelType=OTHER|generation` = **872** (n=1107, 2026-09-18T23:25:30.328207Z)
- `FUELINST|fuelType=PS|generation` = **-421** (n=1107, 2026-09-18T23:25:30.328207Z)
- `FUELINST|fuelType=WIND|generation` = **15784** (n=1107, 2026-09-18T23:25:30.328207Z)
- `IMBALNGC|TOTAL|imbalance` = **9193** (n=183, 2026-09-18T23:24:12.299291Z)
- `INDDEM|TOTAL|demand` = **-10889** (n=183, 2026-09-18T23:23:56.569934Z)
- `INDGEN|TOTAL|generation` = **26388** (n=183, 2026-09-18T23:23:56.569934Z)
- `MELNGC|TOTAL|margin` = **37541** (n=183, 2026-09-18T23:22:33.697837Z)
- `NDF|TOTAL|demand` = **16550** (n=187, 2026-09-18T23:19:40.000667Z)
- `TSDF|TOTAL|demand` = **17194** (n=187, 2026-09-18T23:19:40.000667Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T23:26:32.881631Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:26:31.172381Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:26:29.523530Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:26:27.874457Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:26:26.221173Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:26:24.573018Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:26:22.898760Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:26:21.219818Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:26:17.743804Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:26:17.743804Z` — **FREQ**: 5761 rows; marker `2026-09-18T23:25:45Z`
- `2026-09-18T23:26:16.119789Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:26:14.359316Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:26:12.679264Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:26:11.004753Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:26:09.275252Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
