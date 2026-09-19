# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T10:50:54.851966Z`  
Current process started UTC: `2026-09-19T10:46:53.695155Z`  
1-second metadata polls in this process: **163**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1244, 2026-09-19T10:50:39.821602Z)
- `FUELINST|fuelType=NPSHYD|generation` = **301** (n=1244, 2026-09-19T10:50:39.821602Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1244, 2026-09-19T10:50:39.821602Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1244, 2026-09-19T10:50:39.821602Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1244, 2026-09-19T10:50:39.821602Z)
- `FUELINST|fuelType=OTHER|generation` = **304** (n=1244, 2026-09-19T10:50:39.821602Z)
- `FUELINST|fuelType=PS|generation` = **-695** (n=1244, 2026-09-19T10:50:39.821602Z)
- `FUELINST|fuelType=WIND|generation` = **15882** (n=1244, 2026-09-19T10:50:39.821602Z)
- `IMBALNGC|TOTAL|imbalance` = **7134** (n=204, 2026-09-19T10:19:28.234788Z)
- `INDDEM|TOTAL|demand` = **-13222** (n=204, 2026-09-19T10:19:28.234788Z)
- `INDGEN|TOTAL|generation` = **26065** (n=204, 2026-09-19T10:19:28.234788Z)
- `MELNGC|TOTAL|margin` = **36510** (n=204, 2026-09-19T10:18:55.427991Z)
- `NDF|TOTAL|demand` = **19631** (n=210, 2026-09-19T10:48:46.270828Z)
- `TSDF|TOTAL|demand` = **20131** (n=210, 2026-09-19T10:49:02.446019Z)
- `WINDFOR|TOTAL|generation` = **6656** (n=36, 2026-09-19T10:30:47.910212Z)

## Latest publication events

- `2026-09-19T10:50:53.543542Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:50:52.189152Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:50:50.892413Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:50:49.596628Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:50:48.294047Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:50:47.014206Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:50:45.734570Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:50:44.419911Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:50:42.952985Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:50:39.821602Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:50:39.821602Z` — **FUELINST**: 80 rows; marker `2026-09-19T10:50:00Z`
- `2026-09-19T10:50:38.503190Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:50:37.147520Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:50:35.839985Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:50:34.529437Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
