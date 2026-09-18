# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T23:22:17.778243Z`  
Current process started UTC: `2026-09-18T23:18:17.354553Z`  
1-second metadata polls in this process: **143**  
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

- `FUELINST|fuelType=INTVKL|generation` = **747** (n=1106, 2026-09-18T23:20:28.776083Z)
- `FUELINST|fuelType=NPSHYD|generation` = **429** (n=1106, 2026-09-18T23:20:28.776083Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=1106, 2026-09-18T23:20:28.776083Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1106, 2026-09-18T23:20:28.776083Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1106, 2026-09-18T23:20:28.776083Z)
- `FUELINST|fuelType=OTHER|generation` = **977** (n=1106, 2026-09-18T23:20:28.776083Z)
- `FUELINST|fuelType=PS|generation` = **-420** (n=1106, 2026-09-18T23:20:28.776083Z)
- `FUELINST|fuelType=WIND|generation` = **15809** (n=1106, 2026-09-18T23:20:28.776083Z)
- `IMBALNGC|TOTAL|imbalance` = **8975** (n=182, 2026-09-18T22:53:01.694251Z)
- `INDDEM|TOTAL|demand` = **-10889** (n=182, 2026-09-18T22:53:01.694251Z)
- `INDGEN|TOTAL|generation` = **26170** (n=182, 2026-09-18T22:53:01.694251Z)
- `MELNGC|TOTAL|margin` = **37610** (n=182, 2026-09-18T22:50:10.642009Z)
- `NDF|TOTAL|demand` = **16550** (n=187, 2026-09-18T23:19:40.000667Z)
- `TSDF|TOTAL|demand` = **17194** (n=187, 2026-09-18T23:19:40.000667Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T23:22:16.198256Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:22:14.624852Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:22:13.072908Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:22:11.480015Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:22:09.883060Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:22:07.811282Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:22:06.248570Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:22:04.673077Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:22:03.036317Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:22:01.454686Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:21:59.867894Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:21:58.304582Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:21:56.740252Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:21:55.125002Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:21:53.553785Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
