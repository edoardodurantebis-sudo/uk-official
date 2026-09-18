# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T18:03:52.864489Z`  
Current process started UTC: `2026-09-18T17:59:52.631954Z`  
1-second metadata polls in this process: **140**  
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

- `FUELINST|fuelType=INTVKL|generation` = **802** (n=1063, 2026-09-18T18:00:40.390215Z)
- `FUELINST|fuelType=NPSHYD|generation` = **475** (n=1063, 2026-09-18T18:00:40.390215Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1063, 2026-09-18T18:00:40.390215Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=1063, 2026-09-18T18:00:40.390215Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1063, 2026-09-18T18:00:40.390215Z)
- `FUELINST|fuelType=OTHER|generation` = **1524** (n=1063, 2026-09-18T18:00:40.390215Z)
- `FUELINST|fuelType=PS|generation` = **579** (n=1063, 2026-09-18T18:00:40.390215Z)
- `FUELINST|fuelType=WIND|generation` = **16788** (n=1063, 2026-09-18T18:00:40.390215Z)
- `IMBALNGC|TOTAL|imbalance` = **9111** (n=175, 2026-09-18T17:53:01.127856Z)
- `INDDEM|TOTAL|demand` = **-10766** (n=175, 2026-09-18T17:53:01.127856Z)
- `INDGEN|TOTAL|generation` = **26161** (n=175, 2026-09-18T17:53:01.127856Z)
- `MELNGC|TOTAL|margin` = **37647** (n=175, 2026-09-18T17:50:25.863831Z)
- `NDF|TOTAL|demand` = **16550** (n=179, 2026-09-18T17:48:14.663667Z)
- `TSDF|TOTAL|demand` = **17050** (n=179, 2026-09-18T17:48:30.574499Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T18:03:51.033294Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:03:49.446089Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:03:47.895047Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:03:46.327037Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:03:44.784928Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:03:43.229861Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:03:40.816178Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:03:39.259666Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:03:37.695537Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:03:36.080626Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:03:34.409050Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:03:32.833946Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:03:31.268161Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:03:29.695163Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:03:27.908845Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
