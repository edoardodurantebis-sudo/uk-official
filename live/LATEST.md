# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T00:09:28.870583Z`  
Current process started UTC: `2026-09-19T00:05:28.310841Z`  
1-second metadata polls in this process: **227**  
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

- `FUELINST|fuelType=INTVKL|generation` = **289** (n=1115, 2026-09-19T00:05:28.310850Z)
- `FUELINST|fuelType=NPSHYD|generation` = **428** (n=1115, 2026-09-19T00:05:28.310850Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1115, 2026-09-19T00:05:28.310850Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1115, 2026-09-19T00:05:28.310850Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1115, 2026-09-19T00:05:28.310850Z)
- `FUELINST|fuelType=OTHER|generation` = **697** (n=1115, 2026-09-19T00:05:28.310850Z)
- `FUELINST|fuelType=PS|generation` = **-545** (n=1115, 2026-09-19T00:05:28.310850Z)
- `FUELINST|fuelType=WIND|generation` = **15877** (n=1115, 2026-09-19T00:05:28.310850Z)
- `IMBALNGC|TOTAL|imbalance` = **9185** (n=184, 2026-09-18T23:52:06.332276Z)
- `INDDEM|TOTAL|demand` = **-10888** (n=184, 2026-09-18T23:52:06.332276Z)
- `INDGEN|TOTAL|generation` = **26379** (n=184, 2026-09-18T23:52:06.332276Z)
- `MELNGC|TOTAL|margin` = **37509** (n=184, 2026-09-18T23:49:39.728322Z)
- `NDF|TOTAL|demand` = **16550** (n=188, 2026-09-18T23:47:38.844646Z)
- `TSDF|TOTAL|demand` = **17194** (n=188, 2026-09-18T23:47:38.844646Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T00:09:27.898531Z` — **MID**: 0 rows; marker `2026-09-19T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:09:26.898396Z` — **MID**: 0 rows; marker `2026-09-19T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:09:25.898285Z` — **MID**: 0 rows; marker `2026-09-19T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:09:24.898173Z` — **MID**: 0 rows; marker `2026-09-19T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:09:23.898061Z` — **MID**: 0 rows; marker `2026-09-19T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:09:22.897918Z` — **MID**: 0 rows; marker `2026-09-19T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:09:21.897796Z` — **MID**: 0 rows; marker `2026-09-19T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:09:20.897679Z` — **MID**: 0 rows; marker `2026-09-19T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:09:17.881512Z` — **MID**: 0 rows; marker `2026-09-19T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:09:16.881380Z` — **MID**: 0 rows; marker `2026-09-19T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:09:15.881264Z` — **MID**: 0 rows; marker `2026-09-19T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:09:14.881185Z` — **MID**: 0 rows; marker `2026-09-19T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:09:13.881069Z` — **MID**: 0 rows; marker `2026-09-19T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:09:12.880952Z` — **MID**: 0 rows; marker `2026-09-19T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:09:11.880841Z` — **MID**: 0 rows; marker `2026-09-19T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
