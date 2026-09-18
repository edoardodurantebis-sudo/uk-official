# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T18:16:31.102996Z`  
Current process started UTC: `2026-09-18T18:12:30.891264Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **939** (n=1066, 2026-09-18T18:15:32.325200Z)
- `FUELINST|fuelType=NPSHYD|generation` = **495** (n=1066, 2026-09-18T18:15:32.325200Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1066, 2026-09-18T18:15:32.325200Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=1066, 2026-09-18T18:15:32.325200Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1066, 2026-09-18T18:15:32.325200Z)
- `FUELINST|fuelType=OTHER|generation` = **1812** (n=1066, 2026-09-18T18:15:32.325200Z)
- `FUELINST|fuelType=PS|generation` = **513** (n=1066, 2026-09-18T18:15:32.325200Z)
- `FUELINST|fuelType=WIND|generation` = **16779** (n=1066, 2026-09-18T18:15:32.325200Z)
- `IMBALNGC|TOTAL|imbalance` = **9111** (n=175, 2026-09-18T17:53:01.127856Z)
- `INDDEM|TOTAL|demand` = **-10766** (n=175, 2026-09-18T17:53:01.127856Z)
- `INDGEN|TOTAL|generation` = **26161** (n=175, 2026-09-18T17:53:01.127856Z)
- `MELNGC|TOTAL|margin` = **37647** (n=175, 2026-09-18T17:50:25.863831Z)
- `NDF|TOTAL|demand` = **16550** (n=179, 2026-09-18T17:48:14.663667Z)
- `TSDF|TOTAL|demand` = **17050** (n=179, 2026-09-18T17:48:30.574499Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T18:16:29.762371Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:16:27.994382Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:16:26.369414Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:16:24.517935Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:16:23.154628Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:16:20.287879Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:16:20.287879Z` — **FREQ**: 5761 rows; marker `2026-09-18T18:15:45Z`
- `2026-09-18T18:16:18.642991Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:16:16.683775Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:16:14.864212Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:16:13.494538Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:16:12.095709Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:16:10.777424Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:16:09.193535Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:16:07.802610Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
