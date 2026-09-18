# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T15:16:12.631344Z`  
Current process started UTC: `2026-09-18T15:12:12.493457Z`  
1-second metadata polls in this process: **226**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1051** (n=1053, 2026-09-18T15:15:40.228890Z)
- `FUELINST|fuelType=NPSHYD|generation` = **346** (n=1053, 2026-09-18T15:15:40.228890Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1053, 2026-09-18T15:15:40.228890Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1053, 2026-09-18T15:15:40.228890Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1053, 2026-09-18T15:15:40.228890Z)
- `FUELINST|fuelType=OTHER|generation` = **363** (n=1053, 2026-09-18T15:15:40.228890Z)
- `FUELINST|fuelType=PS|generation` = **-173** (n=1053, 2026-09-18T15:15:40.228890Z)
- `FUELINST|fuelType=WIND|generation` = **16423** (n=1053, 2026-09-18T15:15:40.228890Z)
- `IMBALNGC|TOTAL|imbalance` = **8537** (n=173, 2026-09-18T14:54:42.837155Z)
- `INDDEM|TOTAL|demand` = **-10767** (n=173, 2026-09-18T14:54:26.655582Z)
- `INDGEN|TOTAL|generation` = **25587** (n=173, 2026-09-18T14:54:26.655582Z)
- `MELNGC|TOTAL|margin` = **38296** (n=173, 2026-09-18T14:51:31.995950Z)
- `NDF|TOTAL|demand` = **16550** (n=177, 2026-09-18T14:48:51.573428Z)
- `TSDF|TOTAL|demand` = **17050** (n=177, 2026-09-18T14:48:51.573428Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T15:16:11.679909Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:16:10.679826Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:16:09.679759Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:16:08.679678Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:16:07.319754Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:16:06.204501Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:16:05.204416Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:16:03.528689Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:16:02.522309Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:16:01.522242Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:16:00.522172Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:15:59.472947Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:15:56.964322Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:15:55.964205Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:15:54.964128Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
