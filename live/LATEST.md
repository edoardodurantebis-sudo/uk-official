# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T03:04:06.417904Z`  
Current process started UTC: `2026-09-20T03:00:06.275540Z`  
1-second metadata polls in this process: **216**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-6.39 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **288** (n=1438, 2026-09-20T03:00:37.422526Z)
- `FUELINST|fuelType=NPSHYD|generation` = **308** (n=1438, 2026-09-20T03:00:37.422526Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1438, 2026-09-20T03:00:37.422526Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1438, 2026-09-20T03:00:37.422526Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1438, 2026-09-20T03:00:37.422526Z)
- `FUELINST|fuelType=OTHER|generation` = **433** (n=1438, 2026-09-20T03:00:37.422526Z)
- `FUELINST|fuelType=PS|generation` = **-693** (n=1438, 2026-09-20T03:00:37.422526Z)
- `FUELINST|fuelType=WIND|generation` = **15486** (n=1438, 2026-09-20T03:00:37.422526Z)
- `IMBALNGC|TOTAL|imbalance` = **-3749** (n=237, 2026-09-20T02:51:25.319509Z)
- `INDDEM|TOTAL|demand` = **-12278** (n=237, 2026-09-20T02:51:25.319509Z)
- `INDGEN|TOTAL|generation` = **16203** (n=237, 2026-09-20T02:51:25.319509Z)
- `MELNGC|TOTAL|margin` = **37607** (n=237, 2026-09-20T02:49:53.425892Z)
- `NDF|TOTAL|demand` = **19452** (n=242, 2026-09-20T02:47:28.862306Z)
- `TSDF|TOTAL|demand` = **19952** (n=242, 2026-09-20T02:47:28.862306Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T03:04:05.444203Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:04:03.996784Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:04:02.952153Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:04:01.952080Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:04:00.695690Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:03:59.288848Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:03:58.272425Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:03:57.272360Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:03:56.272223Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:03:55.041570Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:03:54.041453Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:03:53.041323Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:03:51.869647Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:03:50.043174Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:03:48.384199Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
