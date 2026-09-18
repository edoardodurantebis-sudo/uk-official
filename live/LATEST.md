# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T15:03:36.700348Z`  
Current process started UTC: `2026-09-18T14:59:36.399779Z`  
1-second metadata polls in this process: **136**  
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

- `FUELINST|fuelType=INTVKL|generation` = **797** (n=1050, 2026-09-18T15:00:25.820386Z)
- `FUELINST|fuelType=NPSHYD|generation` = **320** (n=1050, 2026-09-18T15:00:25.820386Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1050, 2026-09-18T15:00:25.820386Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1050, 2026-09-18T15:00:25.820386Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1050, 2026-09-18T15:00:25.820386Z)
- `FUELINST|fuelType=OTHER|generation` = **417** (n=1050, 2026-09-18T15:00:25.820386Z)
- `FUELINST|fuelType=PS|generation` = **-176** (n=1050, 2026-09-18T15:00:25.820386Z)
- `FUELINST|fuelType=WIND|generation` = **16562** (n=1050, 2026-09-18T15:00:25.820386Z)
- `IMBALNGC|TOTAL|imbalance` = **8537** (n=173, 2026-09-18T14:54:42.837155Z)
- `INDDEM|TOTAL|demand` = **-10767** (n=173, 2026-09-18T14:54:26.655582Z)
- `INDGEN|TOTAL|generation` = **25587** (n=173, 2026-09-18T14:54:26.655582Z)
- `MELNGC|TOTAL|margin` = **38296** (n=173, 2026-09-18T14:51:31.995950Z)
- `NDF|TOTAL|demand` = **16550** (n=177, 2026-09-18T14:48:51.573428Z)
- `TSDF|TOTAL|demand` = **17050** (n=177, 2026-09-18T14:48:51.573428Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T15:03:34.751518Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:03:32.887309Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:03:31.237245Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:03:29.640268Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:03:28.061143Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:03:25.656762Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:03:24.048408Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:03:22.159658Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:03:20.180831Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:03:18.631838Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:03:17.084149Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:03:14.700585Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:03:12.206500Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:03:10.148928Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:03:08.604432Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
