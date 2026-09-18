# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T19:45:21.125821Z`  
Current process started UTC: `2026-09-18T19:41:21.093213Z`  
1-second metadata polls in this process: **176**  
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

- `FUELINST|fuelType=INTVKL|generation` = **943** (n=1083, 2026-09-18T19:40:40.786631Z)
- `FUELINST|fuelType=NPSHYD|generation` = **485** (n=1083, 2026-09-18T19:40:40.786631Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1083, 2026-09-18T19:40:40.786631Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1083, 2026-09-18T19:40:40.786631Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1083, 2026-09-18T19:40:40.786631Z)
- `FUELINST|fuelType=OTHER|generation` = **919** (n=1083, 2026-09-18T19:40:40.786631Z)
- `FUELINST|fuelType=PS|generation` = **464** (n=1083, 2026-09-18T19:40:40.786631Z)
- `FUELINST|fuelType=WIND|generation` = **16813** (n=1083, 2026-09-18T19:40:40.786631Z)
- `IMBALNGC|TOTAL|imbalance` = **9032** (n=178, 2026-09-18T19:22:27.550765Z)
- `INDDEM|TOTAL|demand` = **-10891** (n=178, 2026-09-18T19:22:12.034913Z)
- `INDGEN|TOTAL|generation` = **26226** (n=178, 2026-09-18T19:22:12.034913Z)
- `MELNGC|TOTAL|margin` = **37505** (n=178, 2026-09-18T19:20:16.544424Z)
- `NDF|TOTAL|demand` = **16550** (n=182, 2026-09-18T19:17:43.952660Z)
- `TSDF|TOTAL|demand` = **17194** (n=182, 2026-09-18T19:17:43.952660Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T19:45:19.824003Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:45:18.520719Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:45:17.208104Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:45:15.842927Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:45:14.527610Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:45:13.270761Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:45:11.979824Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:45:10.658984Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:45:09.374637Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:45:06.792215Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:45:05.424548Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:45:04.080075Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:45:02.824119Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:45:01.531763Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:45:00.184311Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
