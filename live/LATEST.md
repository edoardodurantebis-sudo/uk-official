# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T09:17:10.093700Z`  
Current process started UTC: `2026-09-19T09:13:09.222140Z`  
1-second metadata polls in this process: **134**  
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

- `FUELINST|fuelType=INTVKL|generation` = **560** (n=1225, 2026-09-19T09:15:33.366669Z)
- `FUELINST|fuelType=NPSHYD|generation` = **332** (n=1225, 2026-09-19T09:15:33.366669Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=1225, 2026-09-19T09:15:33.366669Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1225, 2026-09-19T09:15:33.366669Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1225, 2026-09-19T09:15:33.366669Z)
- `FUELINST|fuelType=OTHER|generation` = **605** (n=1225, 2026-09-19T09:15:33.366669Z)
- `FUELINST|fuelType=PS|generation` = **-423** (n=1225, 2026-09-19T09:15:33.366669Z)
- `FUELINST|fuelType=WIND|generation` = **14929** (n=1225, 2026-09-19T09:15:33.366669Z)
- `IMBALNGC|TOTAL|imbalance` = **8932** (n=201, 2026-09-19T08:50:08.297112Z)
- `INDDEM|TOTAL|demand` = **-12086** (n=201, 2026-09-19T08:50:08.297112Z)
- `INDGEN|TOTAL|generation` = **26734** (n=201, 2026-09-19T08:50:08.297112Z)
- `MELNGC|TOTAL|margin` = **37592** (n=201, 2026-09-19T08:49:20.449715Z)
- `NDF|TOTAL|demand` = **15940** (n=206, 2026-09-19T08:47:31.231970Z)
- `TSDF|TOTAL|demand` = **17802** (n=206, 2026-09-19T08:47:59.721944Z)
- `WINDFOR|TOTAL|generation` = **6987** (n=35, 2026-09-19T08:30:39.402179Z)

## Latest publication events

- `2026-09-19T09:17:08.349199Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:17:06.616396Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:17:04.928667Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:17:03.271540Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:17:01.595878Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:16:59.891945Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:16:58.216724Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:16:56.535207Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:16:54.358985Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:16:52.681507Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:16:51.027546Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:16:49.352994Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:16:47.671078Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:16:45.991786Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:16:44.217801Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
