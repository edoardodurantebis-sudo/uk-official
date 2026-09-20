# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T03:08:52.964554Z`  
Current process started UTC: `2026-09-20T03:04:52.239505Z`  
1-second metadata polls in this process: **218**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.85 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **204** (n=1439, 2026-09-20T03:05:41.446172Z)
- `FUELINST|fuelType=NPSHYD|generation` = **298** (n=1439, 2026-09-20T03:05:41.446172Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=1439, 2026-09-20T03:05:41.446172Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1439, 2026-09-20T03:05:41.446172Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1439, 2026-09-20T03:05:41.446172Z)
- `FUELINST|fuelType=OTHER|generation` = **436** (n=1439, 2026-09-20T03:05:41.446172Z)
- `FUELINST|fuelType=PS|generation` = **-693** (n=1439, 2026-09-20T03:05:41.446172Z)
- `FUELINST|fuelType=WIND|generation` = **15357** (n=1439, 2026-09-20T03:05:41.446172Z)
- `IMBALNGC|TOTAL|imbalance` = **-3749** (n=237, 2026-09-20T02:51:25.319509Z)
- `INDDEM|TOTAL|demand` = **-12278** (n=237, 2026-09-20T02:51:25.319509Z)
- `INDGEN|TOTAL|generation` = **16203** (n=237, 2026-09-20T02:51:25.319509Z)
- `MELNGC|TOTAL|margin` = **37607** (n=237, 2026-09-20T02:49:53.425892Z)
- `NDF|TOTAL|demand` = **19452** (n=242, 2026-09-20T02:47:28.862306Z)
- `TSDF|TOTAL|demand` = **19952** (n=242, 2026-09-20T02:47:28.862306Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T03:08:51.936821Z` — **MID**: 0 rows; marker `2026-09-20T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:08:50.917595Z` — **MID**: 0 rows; marker `2026-09-20T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:08:49.910807Z` — **MID**: 0 rows; marker `2026-09-20T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:08:48.606003Z` — **MID**: 0 rows; marker `2026-09-20T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:08:47.605935Z` — **MID**: 0 rows; marker `2026-09-20T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:08:46.561375Z` — **MID**: 0 rows; marker `2026-09-20T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:08:45.522585Z` — **MID**: 0 rows; marker `2026-09-20T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:08:44.521471Z` — **MID**: 0 rows; marker `2026-09-20T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:08:43.497094Z` — **MID**: 0 rows; marker `2026-09-20T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:08:42.440892Z` — **MID**: 0 rows; marker `2026-09-20T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:08:41.440824Z` — **MID**: 0 rows; marker `2026-09-20T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:08:40.413707Z` — **MID**: 0 rows; marker `2026-09-20T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:08:39.395306Z` — **MID**: 0 rows; marker `2026-09-20T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:08:38.395238Z` — **MID**: 0 rows; marker `2026-09-20T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:08:37.367882Z` — **MID**: 0 rows; marker `2026-09-20T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
