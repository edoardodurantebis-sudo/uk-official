# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T14:59:25.792929Z`  
Current process started UTC: `2026-09-18T14:55:25.490141Z`  
1-second metadata polls in this process: **225**  
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

- `FUELINST|fuelType=INTVKL|generation` = **716** (n=1049, 2026-09-18T14:55:25.490152Z)
- `FUELINST|fuelType=NPSHYD|generation` = **318** (n=1049, 2026-09-18T14:55:25.490152Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1049, 2026-09-18T14:55:25.490152Z)
- `FUELINST|fuelType=OCGT|generation` = **2** (n=1049, 2026-09-18T14:55:25.490152Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1049, 2026-09-18T14:55:25.490152Z)
- `FUELINST|fuelType=OTHER|generation` = **467** (n=1049, 2026-09-18T14:55:25.490152Z)
- `FUELINST|fuelType=PS|generation` = **-446** (n=1049, 2026-09-18T14:55:25.490152Z)
- `FUELINST|fuelType=WIND|generation` = **16732** (n=1049, 2026-09-18T14:55:25.490152Z)
- `IMBALNGC|TOTAL|imbalance` = **8537** (n=173, 2026-09-18T14:54:42.837155Z)
- `INDDEM|TOTAL|demand` = **-10767** (n=173, 2026-09-18T14:54:26.655582Z)
- `INDGEN|TOTAL|generation` = **25587** (n=173, 2026-09-18T14:54:26.655582Z)
- `MELNGC|TOTAL|margin` = **38296** (n=173, 2026-09-18T14:51:31.995950Z)
- `NDF|TOTAL|demand` = **16550** (n=177, 2026-09-18T14:48:51.573428Z)
- `TSDF|TOTAL|demand` = **17050** (n=177, 2026-09-18T14:48:51.573428Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T14:59:24.838948Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:59:23.838864Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:59:22.838757Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:59:21.838637Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:59:20.838493Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:59:19.838332Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:59:18.838200Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:59:17.838050Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:59:16.837924Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:59:15.837842Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:59:14.837728Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:59:13.837616Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:59:12.385819Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:59:11.385683Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:59:10.385580Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
