# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T03:06:50.483832Z`  
Current process started UTC: `2026-09-18T03:02:49.109032Z`  
1-second metadata polls in this process: **141**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **985** (n=907, 2026-09-18T03:05:32.104783Z)
- `FUELINST|fuelType=NPSHYD|generation` = **405** (n=907, 2026-09-18T03:05:32.104783Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=907, 2026-09-18T03:05:32.104783Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=907, 2026-09-18T03:05:32.104783Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=907, 2026-09-18T03:05:32.104783Z)
- `FUELINST|fuelType=OTHER|generation` = **281** (n=907, 2026-09-18T03:05:32.104783Z)
- `FUELINST|fuelType=PS|generation` = **531** (n=907, 2026-09-18T03:05:32.104783Z)
- `FUELINST|fuelType=WIND|generation` = **13892** (n=907, 2026-09-18T03:05:32.104783Z)
- `IMBALNGC|TOTAL|imbalance` = **10172** (n=150, 2026-09-18T02:52:59.574452Z)
- `INDDEM|TOTAL|demand` = **-11243** (n=150, 2026-09-18T02:52:44.009177Z)
- `INDGEN|TOTAL|generation` = **26986** (n=150, 2026-09-18T02:52:44.009177Z)
- `MELNGC|TOTAL|margin` = **38180** (n=150, 2026-09-18T02:50:47.579617Z)
- `NDF|TOTAL|demand` = **16314** (n=153, 2026-09-18T02:48:27.577132Z)
- `TSDF|TOTAL|demand` = **16814** (n=153, 2026-09-18T02:48:44.860725Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T03:06:48.960138Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:06:47.406122Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:06:45.874373Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:06:44.021196Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:06:42.437297Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:06:40.635061Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:06:38.596537Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:06:37.052140Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:06:35.320509Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:06:33.582054Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:06:31.998503Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:06:30.467265Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:06:28.922267Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:06:27.406369Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:06:25.821045Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
