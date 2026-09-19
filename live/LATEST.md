# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T00:13:40.555456Z`  
Current process started UTC: `2026-09-19T00:09:39.799014Z`  
1-second metadata polls in this process: **146**  
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

- `FUELINST|fuelType=INTVKL|generation` = **127** (n=1116, 2026-09-19T00:10:28.302809Z)
- `FUELINST|fuelType=NPSHYD|generation` = **412** (n=1116, 2026-09-19T00:10:28.302809Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1116, 2026-09-19T00:10:28.302809Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1116, 2026-09-19T00:10:28.302809Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1116, 2026-09-19T00:10:28.302809Z)
- `FUELINST|fuelType=OTHER|generation` = **962** (n=1116, 2026-09-19T00:10:28.302809Z)
- `FUELINST|fuelType=PS|generation` = **-767** (n=1116, 2026-09-19T00:10:28.302809Z)
- `FUELINST|fuelType=WIND|generation` = **15849** (n=1116, 2026-09-19T00:10:28.302809Z)
- `IMBALNGC|TOTAL|imbalance` = **9185** (n=184, 2026-09-18T23:52:06.332276Z)
- `INDDEM|TOTAL|demand` = **-10888** (n=184, 2026-09-18T23:52:06.332276Z)
- `INDGEN|TOTAL|generation` = **26379** (n=184, 2026-09-18T23:52:06.332276Z)
- `MELNGC|TOTAL|margin` = **37509** (n=184, 2026-09-18T23:49:39.728322Z)
- `NDF|TOTAL|demand` = **16550** (n=188, 2026-09-18T23:47:38.844646Z)
- `TSDF|TOTAL|demand` = **17194** (n=188, 2026-09-18T23:47:38.844646Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T00:13:38.994608Z` — **MID**: 0 rows; marker `2026-09-19T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:13:37.387535Z` — **MID**: 0 rows; marker `2026-09-19T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:13:35.774100Z` — **MID**: 0 rows; marker `2026-09-19T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:13:34.263677Z` — **MID**: 0 rows; marker `2026-09-19T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:13:32.708703Z` — **MID**: 0 rows; marker `2026-09-19T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:13:31.118728Z` — **MID**: 0 rows; marker `2026-09-19T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:13:29.499752Z` — **MID**: 0 rows; marker `2026-09-19T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:13:27.559622Z` — **MID**: 0 rows; marker `2026-09-19T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:13:26.030147Z` — **MID**: 0 rows; marker `2026-09-19T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:13:24.466017Z` — **MID**: 0 rows; marker `2026-09-19T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:13:22.875037Z` — **MID**: 0 rows; marker `2026-09-19T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:13:21.292289Z` — **MID**: 0 rows; marker `2026-09-19T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:13:19.749403Z` — **MID**: 0 rows; marker `2026-09-19T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:13:18.203457Z` — **MID**: 0 rows; marker `2026-09-19T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:13:16.590066Z` — **MID**: 0 rows; marker `2026-09-19T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
