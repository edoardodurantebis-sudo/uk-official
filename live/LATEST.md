# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T06:45:47.818657Z`  
Current process started UTC: `2026-09-19T06:41:46.789586Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **357** (n=1195, 2026-09-19T06:45:30.221571Z)
- `FUELINST|fuelType=NPSHYD|generation` = **367** (n=1195, 2026-09-19T06:45:30.221571Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1195, 2026-09-19T06:45:30.221571Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1195, 2026-09-19T06:45:30.221571Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1195, 2026-09-19T06:45:30.221571Z)
- `FUELINST|fuelType=OTHER|generation` = **900** (n=1195, 2026-09-19T06:45:30.221571Z)
- `FUELINST|fuelType=PS|generation` = **-301** (n=1195, 2026-09-19T06:45:30.221571Z)
- `FUELINST|fuelType=WIND|generation` = **15886** (n=1195, 2026-09-19T06:45:30.221571Z)
- `IMBALNGC|TOTAL|imbalance` = **9725** (n=197, 2026-09-19T06:21:03.713324Z)
- `INDDEM|TOTAL|demand` = **-10863** (n=197, 2026-09-19T06:20:47.840036Z)
- `INDGEN|TOTAL|generation` = **26914** (n=197, 2026-09-19T06:21:03.713324Z)
- `MELNGC|TOTAL|margin` = **38283** (n=197, 2026-09-19T06:19:39.477513Z)
- `NDF|TOTAL|demand` = **16550** (n=201, 2026-09-19T06:17:40.734662Z)
- `TSDF|TOTAL|demand` = **17190** (n=201, 2026-09-19T06:17:40.734662Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T06:45:45.699173Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:45:43.997946Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:45:42.100858Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:45:40.372164Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:45:38.655388Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:45:36.528494Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:45:34.734152Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:45:33.014865Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:45:30.221571Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:45:30.221571Z` — **FUELINST**: 80 rows; marker `2026-09-19T06:45:00Z`
- `2026-09-19T06:45:28.489781Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:45:26.761244Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:45:24.837070Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:45:23.077619Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:45:21.351125Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
