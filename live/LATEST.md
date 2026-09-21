# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T09:13:51.666639Z`  
Current process started UTC: `2026-09-21T09:09:51.734087Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3503, delta=5, z=5.90 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3498, delta=7, z=5.79 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-3, z=6.11 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3491, delta=-2, z=5.59 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3493, delta=0, z=5.72 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3493, delta=-4, z=5.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3497, delta=-3, z=5.97 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3500, delta=-1, z=6.15 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=-4, z=6.25 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3499, delta=-1, z=6.68 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3505, delta=9, z=6.47 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=0, z=6.21 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=0, z=6.28 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-3, z=6.35 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=0, z=6.54 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1800, 2026-09-21T09:10:23.184076Z)
- `FUELINST|fuelType=OTHER|generation` = **642** (n=1800, 2026-09-21T09:10:23.184076Z)
- `FUELINST|fuelType=PS|generation` = **-11** (n=1800, 2026-09-21T09:10:23.184076Z)
- `FUELINST|fuelType=WIND|generation` = **3469** (n=1800, 2026-09-21T09:10:23.184076Z)
- `IMBALNGC|TOTAL|imbalance` = **-2000** (n=295, 2026-09-21T08:49:50.513529Z)
- `INDDEM|TOTAL|demand` = **-12837** (n=295, 2026-09-21T08:49:33.783369Z)
- `INDGEN|TOTAL|generation` = **19269** (n=295, 2026-09-21T08:49:50.513529Z)
- `MELNGC|TOTAL|margin` = **38223** (n=295, 2026-09-21T08:48:46.326673Z)
- `MID|dataProvider=APXMIDP|price` = **186.07** (n=36, 2026-09-21T09:12:15.224778Z)
- `MID|dataProvider=APXMIDP|volume` = **3269.8** (n=36, 2026-09-21T09:12:15.224778Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=72, 2026-09-21T09:12:15.224778Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=72, 2026-09-21T09:12:15.224778Z)
- `NDF|TOTAL|demand` = **20110** (n=302, 2026-09-21T08:47:15.196799Z)
- `TSDF|TOTAL|demand` = **21269** (n=302, 2026-09-21T08:47:15.196799Z)
- `WINDFOR|TOTAL|generation` = **9277** (n=51, 2026-09-21T08:30:33.936824Z)

## Latest publication events

- `2026-09-21T09:12:15.224778Z` — **MID**: 2 rows; marker `2026-09-21T09:12:03Z`
- `2026-09-21T09:12:15.224778Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:11:45Z`
- `2026-09-21T09:10:23.184076Z` — **FUELINST**: 80 rows; marker `2026-09-21T09:10:00Z`
- `2026-09-21T09:10:07.736307Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:09:45Z`
- `2026-09-21T09:08:04.760057Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:07:45Z`
- `2026-09-21T09:06:28.415112Z` — **MID**: 1 rows; marker `2026-09-21T09:05:00Z`
- `2026-09-21T09:06:12.415088Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:05:45Z`
- `2026-09-21T09:05:39.843409Z` — **FUELINST**: 80 rows; marker `2026-09-21T09:05:00Z`
- `2026-09-21T09:04:08.033790Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:03:45Z`
- `2026-09-21T09:02:15.289819Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:01:45Z`
- `2026-09-21T09:00:45.904116Z` — **FUELHH**: 20 rows; marker `2026-09-21T09:00:00Z`
- `2026-09-21T09:00:29.419025Z` — **FUELINST**: 80 rows; marker `2026-09-21T09:00:00Z`
- `2026-09-21T09:00:13.395209Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:59:45Z`
- `2026-09-21T08:58:03.486432Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:57:45Z`
- `2026-09-21T08:56:14.968464Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:55:45Z`
