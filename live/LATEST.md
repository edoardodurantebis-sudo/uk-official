# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T03:13:03.999605Z`  
Current process started UTC: `2026-09-20T03:09:03.929922Z`  
1-second metadata polls in this process: **183**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.09 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.14 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.19 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-5.24 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-5.29 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-5.35 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-5.46 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-5.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.58 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-5.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-5.78 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **161** (n=1440, 2026-09-20T03:10:37.430999Z)
- `FUELINST|fuelType=NPSHYD|generation` = **297** (n=1440, 2026-09-20T03:10:37.430999Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=1440, 2026-09-20T03:10:37.430999Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1440, 2026-09-20T03:10:37.430999Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1440, 2026-09-20T03:10:37.430999Z)
- `FUELINST|fuelType=OTHER|generation` = **578** (n=1440, 2026-09-20T03:10:37.430999Z)
- `FUELINST|fuelType=PS|generation` = **-693** (n=1440, 2026-09-20T03:10:37.430999Z)
- `FUELINST|fuelType=WIND|generation` = **15254** (n=1440, 2026-09-20T03:10:37.430999Z)
- `IMBALNGC|TOTAL|imbalance` = **-3749** (n=237, 2026-09-20T02:51:25.319509Z)
- `INDDEM|TOTAL|demand` = **-12278** (n=237, 2026-09-20T02:51:25.319509Z)
- `INDGEN|TOTAL|generation` = **16203** (n=237, 2026-09-20T02:51:25.319509Z)
- `MELNGC|TOTAL|margin` = **37607** (n=237, 2026-09-20T02:49:53.425892Z)
- `NDF|TOTAL|demand` = **19452** (n=242, 2026-09-20T02:47:28.862306Z)
- `TSDF|TOTAL|demand` = **19952** (n=242, 2026-09-20T02:47:28.862306Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T03:13:02.732978Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:13:01.448143Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:13:00.141383Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:12:58.883562Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:12:57.409362Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:12:56.156947Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:12:54.903312Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:12:53.659551Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:12:52.398946Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:12:51.055959Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:12:49.845471Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:12:48.556735Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:12:47.314113Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:12:46.106927Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:12:44.779769Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
