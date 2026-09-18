# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T11:07:16.556300Z`  
Current process started UTC: `2026-09-18T11:03:15.234225Z`  
1-second metadata polls in this process: **140**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=1002, 2026-09-18T11:00:24.361355Z)
- `FUELINST|fuelType=NPSHYD|generation` = **328** (n=1002, 2026-09-18T11:00:24.361355Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1002, 2026-09-18T11:00:24.361355Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1002, 2026-09-18T11:00:24.361355Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1002, 2026-09-18T11:00:24.361355Z)
- `FUELINST|fuelType=OTHER|generation` = **1013** (n=1002, 2026-09-18T11:00:24.361355Z)
- `FUELINST|fuelType=PS|generation` = **-425** (n=1002, 2026-09-18T11:00:24.361355Z)
- `FUELINST|fuelType=WIND|generation` = **12147** (n=1002, 2026-09-18T11:00:24.361355Z)
- `IMBALNGC|TOTAL|imbalance` = **8982** (n=165, 2026-09-18T10:55:56.036599Z)
- `INDDEM|TOTAL|demand` = **-10744** (n=165, 2026-09-18T10:55:23.440555Z)
- `INDGEN|TOTAL|generation` = **25652** (n=165, 2026-09-18T10:55:23.440555Z)
- `MELNGC|TOTAL|margin` = **38126** (n=165, 2026-09-18T10:51:27.792376Z)
- `NDF|TOTAL|demand` = **16170** (n=169, 2026-09-18T10:49:05.046376Z)
- `TSDF|TOTAL|demand` = **16670** (n=169, 2026-09-18T10:49:05.046376Z)
- `WINDFOR|TOTAL|generation` = **7615** (n=29, 2026-09-18T10:30:46.506872Z)

## Latest publication events

- `2026-09-18T11:07:15.037947Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:07:13.474725Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:07:11.825195Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:07:10.219891Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:07:07.862416Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:07:06.273621Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:07:04.676906Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:07:03.098254Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:07:01.501999Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:06:59.926080Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:06:58.144806Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:06:56.326062Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:06:54.573670Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:06:52.878761Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:06:50.852939Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
