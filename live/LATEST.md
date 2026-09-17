# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T17:42:19.124501Z`  
Current process started UTC: `2026-09-17T17:38:17.009003Z`  
1-second metadata polls in this process: **134**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=58, delta=2, z=3.72 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.55 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=52, delta=-3, z=3.67 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.58 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=-2, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=0, z=4.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=1, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=57, delta=1, z=4.02 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=14, z=4.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.03 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.08 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1407** (n=794, 2026-09-17T17:40:24.651342Z)
- `FUELINST|fuelType=NPSHYD|generation` = **572** (n=794, 2026-09-17T17:40:24.651342Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3319** (n=794, 2026-09-17T17:40:24.651342Z)
- `FUELINST|fuelType=OCGT|generation` = **58** (n=794, 2026-09-17T17:40:24.651342Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=794, 2026-09-17T17:40:24.651342Z)
- `FUELINST|fuelType=OTHER|generation` = **1088** (n=794, 2026-09-17T17:40:24.651342Z)
- `FUELINST|fuelType=PS|generation` = **356** (n=794, 2026-09-17T17:40:24.651342Z)
- `FUELINST|fuelType=WIND|generation` = **14621** (n=794, 2026-09-17T17:40:24.651342Z)
- `IMBALNGC|TOTAL|imbalance` = **9664** (n=131, 2026-09-17T17:23:21.966440Z)
- `INDDEM|TOTAL|demand` = **-11283** (n=131, 2026-09-17T17:23:21.966440Z)
- `INDGEN|TOTAL|generation` = **26478** (n=131, 2026-09-17T17:23:21.966440Z)
- `MELNGC|TOTAL|margin` = **36582** (n=131, 2026-09-17T17:20:41.323525Z)
- `NDF|TOTAL|demand` = **16314** (n=134, 2026-09-17T17:18:17.399296Z)
- `TSDF|TOTAL|demand` = **16814** (n=134, 2026-09-17T17:18:17.399296Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T17:42:15.779929Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:42:15.779929Z` — **FREQ**: 5761 rows; marker `2026-09-17T17:41:45Z`
- `2026-09-17T17:42:14.087812Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:42:12.402699Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:42:10.667046Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:42:08.892372Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:42:07.201318Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:42:05.502869Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:42:03.792694Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:42:02.097316Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:41:59.089905Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:41:57.395093Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:41:55.658384Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:41:53.941697Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:41:52.242233Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
