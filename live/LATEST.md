# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T19:32:46.081029Z`  
Current process started UTC: `2026-09-19T19:28:45.959296Z`  
1-second metadata polls in this process: **142**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=96, delta=93, z=5.31 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=374, delta=374, z=30.30 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.02 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=15.34 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.07 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=-1, z=16.89 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.12 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=404, delta=1, z=19.10 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=-1, z=22.31 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=16, z=5.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=404, delta=175, z=28.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=63, z=4.37 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=229, delta=229, z=17.80 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=0, delta=92, z=-0.01 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1348, 2026-09-19T19:30:45.819998Z)
- `FUELINST|fuelType=NPSHYD|generation` = **525** (n=1348, 2026-09-19T19:30:45.819998Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=1348, 2026-09-19T19:30:45.819998Z)
- `FUELINST|fuelType=OCGT|generation` = **99** (n=1348, 2026-09-19T19:30:45.819998Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1348, 2026-09-19T19:30:45.819998Z)
- `FUELINST|fuelType=OTHER|generation` = **444** (n=1348, 2026-09-19T19:30:45.819998Z)
- `FUELINST|fuelType=PS|generation` = **825** (n=1348, 2026-09-19T19:30:45.819998Z)
- `FUELINST|fuelType=WIND|generation` = **13828** (n=1348, 2026-09-19T19:30:45.819998Z)
- `IMBALNGC|TOTAL|imbalance` = **-3754** (n=222, 2026-09-19T19:22:47.836433Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=222, 2026-09-19T19:22:31.393542Z)
- `INDGEN|TOTAL|generation` = **16198** (n=222, 2026-09-19T19:22:31.393542Z)
- `MELNGC|TOTAL|margin` = **36176** (n=222, 2026-09-19T19:20:20.972192Z)
- `NDF|TOTAL|demand` = **19452** (n=227, 2026-09-19T19:18:02.472274Z)
- `TSDF|TOTAL|demand` = **19952** (n=227, 2026-09-19T19:18:02.472274Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T19:32:44.510122Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:32:42.956684Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:32:40.980031Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:32:39.404694Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:32:37.564904Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:32:35.682733Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:32:34.096408Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:32:32.540242Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:32:30.802370Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:32:29.251366Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:32:27.692132Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:32:24.507047Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:32:24.507047Z` — **FREQ**: 5761 rows; marker `2026-09-19T19:31:45Z`
- `2026-09-19T19:32:22.476042Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:32:20.903941Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
