# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T16:21:41.779416Z`  
Current process started UTC: `2026-09-17T16:17:41.597251Z`  
1-second metadata polls in this process: **224**  
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

- `FUELINST|fuelType=INTVKL|generation` = **389** (n=778, 2026-09-17T16:20:37.854083Z)
- `FUELINST|fuelType=NPSHYD|generation` = **422** (n=778, 2026-09-17T16:20:37.854083Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3312** (n=778, 2026-09-17T16:20:37.854083Z)
- `FUELINST|fuelType=OCGT|generation` = **51** (n=778, 2026-09-17T16:20:37.854083Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=778, 2026-09-17T16:20:37.854083Z)
- `FUELINST|fuelType=OTHER|generation` = **1149** (n=778, 2026-09-17T16:20:37.854083Z)
- `FUELINST|fuelType=PS|generation` = **-255** (n=778, 2026-09-17T16:20:37.854083Z)
- `FUELINST|fuelType=WIND|generation` = **13946** (n=778, 2026-09-17T16:20:37.854083Z)
- `IMBALNGC|TOTAL|imbalance` = **11642** (n=128, 2026-09-17T15:54:55.997739Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=128, 2026-09-17T15:54:24.168455Z)
- `INDGEN|TOTAL|generation` = **28456** (n=128, 2026-09-17T15:54:40.409047Z)
- `MELNGC|TOTAL|margin` = **36692** (n=129, 2026-09-17T16:21:11.558898Z)
- `NDF|TOTAL|demand` = **16314** (n=132, 2026-09-17T16:18:29.666995Z)
- `TSDF|TOTAL|demand` = **16814** (n=132, 2026-09-17T16:18:29.666995Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T16:21:40.819096Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:21:39.818981Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:21:38.818871Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:21:37.818761Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:21:36.818634Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:21:35.818556Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:21:34.818426Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:21:33.818305Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:21:32.818166Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:21:31.818080Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:21:30.817955Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:21:29.817861Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:21:28.817732Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:21:27.586571Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:21:26.586479Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
