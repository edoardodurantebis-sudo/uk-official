# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T00:13:07.728671Z`  
Current process started UTC: `2026-09-18T00:09:07.274476Z`  
1-second metadata polls in this process: **140**  
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

- `FUELINST|fuelType=INTVKL|generation` = **893** (n=872, 2026-09-18T00:10:31.126956Z)
- `FUELINST|fuelType=NPSHYD|generation` = **448** (n=872, 2026-09-18T00:10:31.126956Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=872, 2026-09-18T00:10:31.126956Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=872, 2026-09-18T00:10:31.126956Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=872, 2026-09-18T00:10:31.126956Z)
- `FUELINST|fuelType=OTHER|generation` = **272** (n=872, 2026-09-18T00:10:31.126956Z)
- `FUELINST|fuelType=PS|generation` = **55** (n=872, 2026-09-18T00:10:31.126956Z)
- `FUELINST|fuelType=WIND|generation` = **14401** (n=872, 2026-09-18T00:10:31.126956Z)
- `IMBALNGC|TOTAL|imbalance` = **10139** (n=144, 2026-09-17T23:53:42.397703Z)
- `INDDEM|TOTAL|demand` = **-11183** (n=144, 2026-09-17T23:53:26.100029Z)
- `INDGEN|TOTAL|generation` = **26953** (n=144, 2026-09-17T23:53:26.100029Z)
- `MELNGC|TOTAL|margin` = **36515** (n=144, 2026-09-17T23:50:34.020814Z)
- `NDF|TOTAL|demand` = **16314** (n=147, 2026-09-17T23:48:05.570317Z)
- `TSDF|TOTAL|demand` = **16814** (n=147, 2026-09-17T23:48:22.184365Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T00:13:06.103117Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:13:04.523185Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:13:02.259090Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:13:00.716206Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:12:59.031029Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:12:57.439490Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:12:55.666095Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:12:53.916151Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:12:52.274086Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:12:50.740938Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:12:49.164694Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:12:47.531794Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:12:44.586133Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:12:43.038507Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:12:41.443834Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
