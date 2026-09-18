# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T23:18:02.537599Z`  
Current process started UTC: `2026-09-18T23:14:01.860739Z`  
1-second metadata polls in this process: **228**  
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

- `FUELINST|fuelType=INTVKL|generation` = **747** (n=1105, 2026-09-18T23:15:21.937616Z)
- `FUELINST|fuelType=NPSHYD|generation` = **429** (n=1105, 2026-09-18T23:15:21.937616Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=1105, 2026-09-18T23:15:21.937616Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1105, 2026-09-18T23:15:21.937616Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1105, 2026-09-18T23:15:21.937616Z)
- `FUELINST|fuelType=OTHER|generation` = **1099** (n=1105, 2026-09-18T23:15:21.937616Z)
- `FUELINST|fuelType=PS|generation` = **-420** (n=1105, 2026-09-18T23:15:21.937616Z)
- `FUELINST|fuelType=WIND|generation` = **15809** (n=1105, 2026-09-18T23:15:21.937616Z)
- `IMBALNGC|TOTAL|imbalance` = **8975** (n=182, 2026-09-18T22:53:01.694251Z)
- `INDDEM|TOTAL|demand` = **-10889** (n=182, 2026-09-18T22:53:01.694251Z)
- `INDGEN|TOTAL|generation` = **26170** (n=182, 2026-09-18T22:53:01.694251Z)
- `MELNGC|TOTAL|margin` = **37610** (n=182, 2026-09-18T22:50:10.642009Z)
- `NDF|TOTAL|demand` = **16550** (n=186, 2026-09-18T22:48:26.880797Z)
- `TSDF|TOTAL|demand` = **17194** (n=186, 2026-09-18T22:48:26.880797Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T23:18:01.576727Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:18:00.225740Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:17:59.225615Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:17:58.225511Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:17:57.225399Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:17:56.225283Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:17:55.225163Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:17:54.225121Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:17:53.224994Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:17:51.876852Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:17:50.876736Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:17:49.876619Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:17:48.876502Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:17:47.876396Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:17:46.719250Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
