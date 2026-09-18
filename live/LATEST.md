# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T01:46:29.646392Z`  
Current process started UTC: `2026-09-18T01:42:29.314303Z`  
1-second metadata polls in this process: **219**  
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

- `FUELINST|fuelType=INTVKL|generation` = **781** (n=891, 2026-09-18T01:45:25.366785Z)
- `FUELINST|fuelType=NPSHYD|generation` = **418** (n=891, 2026-09-18T01:45:25.366785Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=891, 2026-09-18T01:45:25.366785Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=891, 2026-09-18T01:45:25.366785Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=891, 2026-09-18T01:45:25.366785Z)
- `FUELINST|fuelType=OTHER|generation` = **173** (n=891, 2026-09-18T01:45:25.366785Z)
- `FUELINST|fuelType=PS|generation` = **533** (n=891, 2026-09-18T01:45:25.366785Z)
- `FUELINST|fuelType=WIND|generation` = **14207** (n=891, 2026-09-18T01:45:25.366785Z)
- `IMBALNGC|TOTAL|imbalance` = **10127** (n=147, 2026-09-18T01:21:58.893655Z)
- `INDDEM|TOTAL|demand` = **-11192** (n=147, 2026-09-18T01:21:42.565092Z)
- `INDGEN|TOTAL|generation` = **26941** (n=147, 2026-09-18T01:21:58.893655Z)
- `MELNGC|TOTAL|margin` = **36704** (n=147, 2026-09-18T01:20:38.557334Z)
- `NDF|TOTAL|demand` = **16314** (n=150, 2026-09-18T01:17:48.779698Z)
- `TSDF|TOTAL|demand` = **16814** (n=150, 2026-09-18T01:17:48.779698Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T01:46:28.616999Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:46:27.600689Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:46:26.588115Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:46:25.551872Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:46:24.534349Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:46:23.505034Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:46:22.472682Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:46:21.450455Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:46:20.417287Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:46:19.382383Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:46:18.355579Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:46:17.314565Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:46:16.276334Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:46:13.909027Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:46:13.909027Z` — **FREQ**: 5761 rows; marker `2026-09-18T01:45:45Z`
