# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T10:38:13.907248Z`  
Current process started UTC: `2026-09-19T10:34:13.125242Z`  
1-second metadata polls in this process: **148**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1241, 2026-09-19T10:35:33.067876Z)
- `FUELINST|fuelType=NPSHYD|generation` = **301** (n=1241, 2026-09-19T10:35:33.067876Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1241, 2026-09-19T10:35:33.067876Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1241, 2026-09-19T10:35:33.067876Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1241, 2026-09-19T10:35:33.067876Z)
- `FUELINST|fuelType=OTHER|generation` = **321** (n=1241, 2026-09-19T10:35:33.067876Z)
- `FUELINST|fuelType=PS|generation` = **-694** (n=1241, 2026-09-19T10:35:33.067876Z)
- `FUELINST|fuelType=WIND|generation` = **15899** (n=1241, 2026-09-19T10:35:33.067876Z)
- `IMBALNGC|TOTAL|imbalance` = **7134** (n=204, 2026-09-19T10:19:28.234788Z)
- `INDDEM|TOTAL|demand` = **-13222** (n=204, 2026-09-19T10:19:28.234788Z)
- `INDGEN|TOTAL|generation` = **26065** (n=204, 2026-09-19T10:19:28.234788Z)
- `MELNGC|TOTAL|margin` = **36510** (n=204, 2026-09-19T10:18:55.427991Z)
- `NDF|TOTAL|demand` = **15940** (n=209, 2026-09-19T10:16:50.751867Z)
- `TSDF|TOTAL|demand` = **18932** (n=209, 2026-09-19T10:16:50.751867Z)
- `WINDFOR|TOTAL|generation` = **6656** (n=36, 2026-09-19T10:30:47.910212Z)

## Latest publication events

- `2026-09-19T10:38:12.367934Z` — **MID**: 0 rows; marker `2026-09-19T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:38:10.838526Z` — **MID**: 0 rows; marker `2026-09-19T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:38:09.301852Z` — **MID**: 0 rows; marker `2026-09-19T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:38:07.754564Z` — **MID**: 0 rows; marker `2026-09-19T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:38:06.215799Z` — **MID**: 0 rows; marker `2026-09-19T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:38:04.678471Z` — **MID**: 0 rows; marker `2026-09-19T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:38:03.141086Z` — **MID**: 0 rows; marker `2026-09-19T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:38:01.589508Z` — **MID**: 0 rows; marker `2026-09-19T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:38:00.047237Z` — **MID**: 0 rows; marker `2026-09-19T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:37:57.672929Z` — **MID**: 0 rows; marker `2026-09-19T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:37:56.116322Z` — **MID**: 0 rows; marker `2026-09-19T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:37:54.580857Z` — **MID**: 0 rows; marker `2026-09-19T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:37:53.053315Z` — **MID**: 0 rows; marker `2026-09-19T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:37:51.522458Z` — **MID**: 0 rows; marker `2026-09-19T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:37:49.969111Z` — **MID**: 0 rows; marker `2026-09-19T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
