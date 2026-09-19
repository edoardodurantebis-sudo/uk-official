# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T14:50:38.604371Z`  
Current process started UTC: `2026-09-19T14:46:37.498220Z`  
1-second metadata polls in this process: **180**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.91 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.20 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-102, delta=-202, z=-12.22 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=-15, z=-11.26 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-89, delta=-179, z=-10.03 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=100, delta=26, z=19.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=90, delta=-13, z=10.31 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=12.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=13.38 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1292, 2026-09-19T14:50:29.146102Z)
- `FUELINST|fuelType=NPSHYD|generation` = **265** (n=1292, 2026-09-19T14:50:29.146102Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1292, 2026-09-19T14:50:29.146102Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1292, 2026-09-19T14:50:29.146102Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1292, 2026-09-19T14:50:29.146102Z)
- `FUELINST|fuelType=OTHER|generation` = **1353** (n=1292, 2026-09-19T14:50:29.146102Z)
- `FUELINST|fuelType=PS|generation` = **-257** (n=1292, 2026-09-19T14:50:29.146102Z)
- `FUELINST|fuelType=WIND|generation` = **13410** (n=1292, 2026-09-19T14:50:29.146102Z)
- `IMBALNGC|TOTAL|imbalance` = **-3230** (n=212, 2026-09-19T14:25:35.374558Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=212, 2026-09-19T14:25:35.374558Z)
- `INDGEN|TOTAL|generation` = **16779** (n=212, 2026-09-19T14:25:35.374558Z)
- `MELNGC|TOTAL|margin` = **36925** (n=212, 2026-09-19T14:20:59.619875Z)
- `NDF|TOTAL|demand` = **19452** (n=218, 2026-09-19T14:48:18.199040Z)
- `TSDF|TOTAL|demand` = **19952** (n=218, 2026-09-19T14:48:18.199040Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T14:50:37.405879Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:50:36.246386Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:50:35.081081Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:50:33.872734Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:50:29.146102Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:50:29.146102Z` — **FUELINST**: 80 rows; marker `2026-09-19T14:50:00Z`
- `2026-09-19T14:50:27.888611Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:50:26.695318Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:50:25.490195Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:50:24.305347Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:50:23.123540Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:50:21.941464Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:50:20.746259Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:50:19.361758Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:50:18.003993Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
