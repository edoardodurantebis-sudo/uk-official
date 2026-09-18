# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T08:38:47.545780Z`  
Current process started UTC: `2026-09-18T08:34:46.458261Z`  
1-second metadata polls in this process: **222**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=973, 2026-09-18T08:35:34.054450Z)
- `FUELINST|fuelType=NPSHYD|generation` = **376** (n=973, 2026-09-18T08:35:34.054450Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=973, 2026-09-18T08:35:34.054450Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=973, 2026-09-18T08:35:34.054450Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=973, 2026-09-18T08:35:34.054450Z)
- `FUELINST|fuelType=OTHER|generation` = **1176** (n=973, 2026-09-18T08:35:34.054450Z)
- `FUELINST|fuelType=PS|generation` = **220** (n=973, 2026-09-18T08:35:34.054450Z)
- `FUELINST|fuelType=WIND|generation` = **12263** (n=973, 2026-09-18T08:35:34.054450Z)
- `IMBALNGC|TOTAL|imbalance` = **9625** (n=160, 2026-09-18T08:20:46.536994Z)
- `INDDEM|TOTAL|demand` = **-11736** (n=160, 2026-09-18T08:20:29.773738Z)
- `INDGEN|TOTAL|generation` = **27269** (n=160, 2026-09-18T08:20:29.773738Z)
- `MELNGC|TOTAL|margin` = **37653** (n=160, 2026-09-18T08:19:40.681819Z)
- `NDF|TOTAL|demand` = **16454** (n=164, 2026-09-18T08:17:38.545846Z)
- `TSDF|TOTAL|demand` = **17644** (n=164, 2026-09-18T08:17:38.545846Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T08:38:45.924952Z` — **MID**: 0 rows; marker `2026-09-18T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:38:44.907301Z` — **MID**: 0 rows; marker `2026-09-18T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:38:43.884716Z` — **MID**: 0 rows; marker `2026-09-18T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:38:42.815935Z` — **MID**: 0 rows; marker `2026-09-18T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:38:41.810049Z` — **MID**: 0 rows; marker `2026-09-18T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:38:40.804841Z` — **MID**: 0 rows; marker `2026-09-18T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:38:39.752055Z` — **MID**: 0 rows; marker `2026-09-18T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:38:38.737361Z` — **MID**: 0 rows; marker `2026-09-18T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:38:37.713440Z` — **MID**: 0 rows; marker `2026-09-18T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:38:36.692075Z` — **MID**: 0 rows; marker `2026-09-18T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:38:35.691979Z` — **MID**: 0 rows; marker `2026-09-18T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:38:34.676883Z` — **MID**: 0 rows; marker `2026-09-18T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:38:33.669798Z` — **MID**: 0 rows; marker `2026-09-18T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:38:32.487396Z` — **MID**: 0 rows; marker `2026-09-18T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:38:30.059433Z` — **MID**: 0 rows; marker `2026-09-18T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
