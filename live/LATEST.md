# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T02:20:35.610417Z`  
Current process started UTC: `2026-09-19T02:16:35.136365Z`  
1-second metadata polls in this process: **133**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-509** (n=1141, 2026-09-19T02:15:22.064443Z)
- `FUELINST|fuelType=NPSHYD|generation` = **345** (n=1141, 2026-09-19T02:15:22.064443Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=1141, 2026-09-19T02:15:22.064443Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1141, 2026-09-19T02:15:22.064443Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1141, 2026-09-19T02:15:22.064443Z)
- `FUELINST|fuelType=OTHER|generation` = **307** (n=1141, 2026-09-19T02:15:22.064443Z)
- `FUELINST|fuelType=PS|generation` = **-379** (n=1141, 2026-09-19T02:15:22.064443Z)
- `FUELINST|fuelType=WIND|generation` = **16187** (n=1141, 2026-09-19T02:15:22.064443Z)
- `IMBALNGC|TOTAL|imbalance` = **9241** (n=188, 2026-09-19T01:51:39.036034Z)
- `INDDEM|TOTAL|demand` = **-10886** (n=188, 2026-09-19T01:51:39.036034Z)
- `INDGEN|TOTAL|generation` = **26435** (n=188, 2026-09-19T01:51:39.036034Z)
- `MELNGC|TOTAL|margin` = **38306** (n=189, 2026-09-19T02:19:37.697156Z)
- `NDF|TOTAL|demand` = **16550** (n=193, 2026-09-19T02:17:41.280152Z)
- `TSDF|TOTAL|demand` = **17194** (n=193, 2026-09-19T02:17:41.280152Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T02:20:33.848522Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:20:32.286193Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:20:30.272651Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:20:28.744694Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:20:26.597331Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:20:24.932015Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:20:23.289809Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:20:21.769320Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:20:19.882610Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:20:18.100955Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:20:16.565972Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:20:14.987517Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:20:13.440524Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:20:10.155889Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:20:10.155889Z` — **FREQ**: 5761 rows; marker `2026-09-19T02:19:45Z`
