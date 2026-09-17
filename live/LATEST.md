# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T16:55:22.030864Z`  
Current process started UTC: `2026-09-17T16:51:21.354053Z`  
1-second metadata polls in this process: **231**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.55 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=52, delta=-3, z=3.67 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.58 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=-2, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=0, z=4.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=1, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=57, delta=1, z=4.02 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=14, z=4.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.03 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.13 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.18 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **389** (n=784, 2026-09-17T16:50:22.112113Z)
- `FUELINST|fuelType=NPSHYD|generation` = **420** (n=784, 2026-09-17T16:50:22.112113Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=784, 2026-09-17T16:50:22.112113Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=784, 2026-09-17T16:50:22.112113Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=784, 2026-09-17T16:50:22.112113Z)
- `FUELINST|fuelType=OTHER|generation` = **1055** (n=784, 2026-09-17T16:50:22.112113Z)
- `FUELINST|fuelType=PS|generation` = **304** (n=784, 2026-09-17T16:50:22.112113Z)
- `FUELINST|fuelType=WIND|generation` = **14187** (n=784, 2026-09-17T16:50:22.112113Z)
- `IMBALNGC|TOTAL|imbalance` = **11597** (n=130, 2026-09-17T16:54:05.472885Z)
- `INDDEM|TOTAL|demand` = **-11282** (n=130, 2026-09-17T16:53:49.929273Z)
- `INDGEN|TOTAL|generation` = **28411** (n=130, 2026-09-17T16:53:49.929273Z)
- `MELNGC|TOTAL|margin` = **36588** (n=130, 2026-09-17T16:50:53.787200Z)
- `NDF|TOTAL|demand` = **16314** (n=133, 2026-09-17T16:48:29.094169Z)
- `TSDF|TOTAL|demand` = **16814** (n=133, 2026-09-17T16:48:29.094169Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T16:55:21.031471Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:55:20.031361Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:55:19.031247Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:55:18.031132Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:55:16.895526Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:55:15.895456Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:55:14.895375Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:55:13.895262Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:55:12.895148Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:55:11.895066Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:55:10.894984Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:55:09.687178Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:55:08.687065Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:55:07.686995Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:55:06.686884Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
