# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T01:37:32.961779Z`  
Current process started UTC: `2026-09-18T01:33:31.670335Z`  
1-second metadata polls in this process: **169**  
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

- `FUELINST|fuelType=INTVKL|generation` = **781** (n=889, 2026-09-18T01:35:25.845447Z)
- `FUELINST|fuelType=NPSHYD|generation` = **418** (n=889, 2026-09-18T01:35:25.845447Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=889, 2026-09-18T01:35:25.845447Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=889, 2026-09-18T01:35:25.845447Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=889, 2026-09-18T01:35:25.845447Z)
- `FUELINST|fuelType=OTHER|generation` = **252** (n=889, 2026-09-18T01:35:25.845447Z)
- `FUELINST|fuelType=PS|generation` = **533** (n=889, 2026-09-18T01:35:25.845447Z)
- `FUELINST|fuelType=WIND|generation` = **14121** (n=889, 2026-09-18T01:35:25.845447Z)
- `IMBALNGC|TOTAL|imbalance` = **10127** (n=147, 2026-09-18T01:21:58.893655Z)
- `INDDEM|TOTAL|demand` = **-11192** (n=147, 2026-09-18T01:21:42.565092Z)
- `INDGEN|TOTAL|generation` = **26941** (n=147, 2026-09-18T01:21:58.893655Z)
- `MELNGC|TOTAL|margin` = **36704** (n=147, 2026-09-18T01:20:38.557334Z)
- `NDF|TOTAL|demand` = **16314** (n=150, 2026-09-18T01:17:48.779698Z)
- `TSDF|TOTAL|demand` = **16814** (n=150, 2026-09-18T01:17:48.779698Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T01:37:31.593275Z` — **MID**: 0 rows; marker `2026-09-18T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:37:30.273747Z` — **MID**: 0 rows; marker `2026-09-18T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:37:28.999400Z` — **MID**: 0 rows; marker `2026-09-18T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:37:27.587106Z` — **MID**: 0 rows; marker `2026-09-18T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:37:26.236263Z` — **MID**: 0 rows; marker `2026-09-18T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:37:24.938238Z` — **MID**: 0 rows; marker `2026-09-18T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:37:23.608568Z` — **MID**: 0 rows; marker `2026-09-18T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:37:22.286225Z` — **MID**: 0 rows; marker `2026-09-18T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:37:20.943331Z` — **MID**: 0 rows; marker `2026-09-18T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:37:19.220764Z` — **MID**: 0 rows; marker `2026-09-18T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:37:17.931259Z` — **MID**: 0 rows; marker `2026-09-18T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:37:16.633277Z` — **MID**: 0 rows; marker `2026-09-18T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:37:15.292979Z` — **MID**: 0 rows; marker `2026-09-18T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:37:13.943844Z` — **MID**: 0 rows; marker `2026-09-18T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:37:12.621903Z` — **MID**: 0 rows; marker `2026-09-18T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
