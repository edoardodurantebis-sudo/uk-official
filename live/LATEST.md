# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T16:09:06.690375Z`  
Current process started UTC: `2026-09-17T16:05:06.242504Z`  
1-second metadata polls in this process: **229**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=-2, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=0, z=4.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=1, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=57, delta=1, z=4.02 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=14, z=4.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.03 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.13 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.23 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=42, delta=42, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=1, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=2, z=4.25 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **176** (n=775, 2026-09-17T16:05:26.074066Z)
- `FUELINST|fuelType=NPSHYD|generation` = **402** (n=775, 2026-09-17T16:05:26.074066Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3309** (n=775, 2026-09-17T16:05:26.074066Z)
- `FUELINST|fuelType=OCGT|generation` = **51** (n=775, 2026-09-17T16:05:26.074066Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=775, 2026-09-17T16:05:26.074066Z)
- `FUELINST|fuelType=OTHER|generation` = **822** (n=775, 2026-09-17T16:05:26.074066Z)
- `FUELINST|fuelType=PS|generation` = **-254** (n=775, 2026-09-17T16:05:26.074066Z)
- `FUELINST|fuelType=WIND|generation` = **13978** (n=775, 2026-09-17T16:05:26.074066Z)
- `IMBALNGC|TOTAL|imbalance` = **11642** (n=128, 2026-09-17T15:54:55.997739Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=128, 2026-09-17T15:54:24.168455Z)
- `INDGEN|TOTAL|generation` = **28456** (n=128, 2026-09-17T15:54:40.409047Z)
- `MELNGC|TOTAL|margin` = **36684** (n=128, 2026-09-17T15:51:59.800251Z)
- `NDF|TOTAL|demand` = **16314** (n=131, 2026-09-17T15:48:34.023613Z)
- `TSDF|TOTAL|demand` = **16814** (n=131, 2026-09-17T15:48:34.023613Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T16:09:05.738008Z` — **MID**: 0 rows; marker `2026-09-17T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:09:04.737885Z` — **MID**: 0 rows; marker `2026-09-17T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:09:03.737764Z` — **MID**: 0 rows; marker `2026-09-17T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:09:02.737620Z` — **MID**: 0 rows; marker `2026-09-17T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:09:01.737519Z` — **MID**: 0 rows; marker `2026-09-17T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:09:00.737371Z` — **MID**: 0 rows; marker `2026-09-17T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:08:59.737245Z` — **MID**: 0 rows; marker `2026-09-17T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:08:58.737129Z` — **MID**: 0 rows; marker `2026-09-17T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:08:57.736999Z` — **MID**: 0 rows; marker `2026-09-17T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:08:56.736872Z` — **MID**: 0 rows; marker `2026-09-17T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:08:55.736746Z` — **MID**: 0 rows; marker `2026-09-17T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:08:54.736607Z` — **MID**: 0 rows; marker `2026-09-17T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:08:53.513452Z` — **MID**: 0 rows; marker `2026-09-17T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:08:52.513315Z` — **MID**: 0 rows; marker `2026-09-17T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:08:51.513169Z` — **MID**: 0 rows; marker `2026-09-17T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
