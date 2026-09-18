# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T18:54:36.335312Z`  
Current process started UTC: `2026-09-18T18:50:36.144377Z`  
1-second metadata polls in this process: **158**  
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

- `FUELINST|fuelType=INTVKL|generation` = **943** (n=1073, 2026-09-18T18:50:36.144384Z)
- `FUELINST|fuelType=NPSHYD|generation` = **492** (n=1073, 2026-09-18T18:50:36.144384Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1073, 2026-09-18T18:50:36.144384Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1073, 2026-09-18T18:50:36.144384Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1073, 2026-09-18T18:50:36.144384Z)
- `FUELINST|fuelType=OTHER|generation` = **1479** (n=1073, 2026-09-18T18:50:36.144384Z)
- `FUELINST|fuelType=PS|generation` = **294** (n=1073, 2026-09-18T18:50:36.144384Z)
- `FUELINST|fuelType=WIND|generation` = **16688** (n=1073, 2026-09-18T18:50:36.144384Z)
- `IMBALNGC|TOTAL|imbalance` = **9037** (n=177, 2026-09-18T18:53:19.505898Z)
- `INDDEM|TOTAL|demand` = **-10885** (n=177, 2026-09-18T18:53:19.505898Z)
- `INDGEN|TOTAL|generation` = **26231** (n=177, 2026-09-18T18:53:19.505898Z)
- `MELNGC|TOTAL|margin` = **37526** (n=177, 2026-09-18T18:50:36.144384Z)
- `NDF|TOTAL|demand` = **16550** (n=181, 2026-09-18T18:48:17.389891Z)
- `TSDF|TOTAL|demand` = **17194** (n=181, 2026-09-18T18:48:17.389891Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T18:54:34.294647Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:54:32.994901Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:54:31.373068Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:54:30.056817Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:54:28.297405Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:54:26.699493Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:54:24.285349Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:54:22.981280Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:54:21.029717Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:54:19.742568Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:54:17.523174Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:54:16.168890Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:54:14.468226Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:54:12.443648Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:54:09.016711Z` — **MID**: 0 rows; marker `2026-09-18T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
