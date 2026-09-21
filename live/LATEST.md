# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T08:35:54.596727Z`  
Current process started UTC: `2026-09-21T08:31:54.158331Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=-4, z=6.25 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3499, delta=-1, z=6.68 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3505, delta=9, z=6.47 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=0, z=6.21 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=0, z=6.28 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-3, z=6.35 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=0, z=6.54 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=0, z=6.62 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3500, delta=1, z=7.30 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=791, delta=-14, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=-2, z=6.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=0, z=6.88 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=-3, z=6.98 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=3, z=7.20 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=5, z=7.18 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1793, 2026-09-21T08:35:39.251537Z)
- `FUELINST|fuelType=OTHER|generation` = **1222** (n=1793, 2026-09-21T08:35:39.251537Z)
- `FUELINST|fuelType=PS|generation` = **103** (n=1793, 2026-09-21T08:35:39.251537Z)
- `FUELINST|fuelType=WIND|generation` = **3969** (n=1793, 2026-09-21T08:35:39.251537Z)
- `IMBALNGC|TOTAL|imbalance` = **-2271** (n=294, 2026-09-21T08:19:28.892313Z)
- `INDDEM|TOTAL|demand` = **-12835** (n=294, 2026-09-21T08:19:13.069003Z)
- `INDGEN|TOTAL|generation` = **18998** (n=294, 2026-09-21T08:19:28.892313Z)
- `MELNGC|TOTAL|margin` = **38252** (n=294, 2026-09-21T08:18:56.991927Z)
- `MID|dataProvider=APXMIDP|price` = **201.31** (n=34, 2026-09-21T08:12:09.816775Z)
- `MID|dataProvider=APXMIDP|volume` = **2941.7** (n=34, 2026-09-21T08:12:09.816775Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=68, 2026-09-21T08:12:09.816775Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=68, 2026-09-21T08:12:09.816775Z)
- `NDF|TOTAL|demand` = **20110** (n=301, 2026-09-21T08:17:02.430587Z)
- `TSDF|TOTAL|demand` = **21269** (n=301, 2026-09-21T08:17:02.430587Z)
- `WINDFOR|TOTAL|generation` = **9277** (n=51, 2026-09-21T08:30:33.936824Z)

## Latest publication events

- `2026-09-21T08:35:39.251537Z` — **FUELINST**: 80 rows; marker `2026-09-21T08:35:00Z`
- `2026-09-21T08:34:18.614350Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:33:45Z`
- `2026-09-21T08:32:10.206564Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:31:45Z`
- `2026-09-21T08:30:33.936824Z` — **WINDFOR**: 73 rows; marker `2026-09-21T08:30:00Z`
- `2026-09-21T08:30:33.936824Z` — **FUELHH**: 20 rows; marker `2026-09-21T08:30:00Z`
- `2026-09-21T08:30:33.936824Z` — **FUELINST**: 80 rows; marker `2026-09-21T08:30:00Z`
- `2026-09-21T08:30:17.653079Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:29:45Z`
- `2026-09-21T08:28:09.176384Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:27:45Z`
- `2026-09-21T08:26:21.436535Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:25:45Z`
- `2026-09-21T08:25:33.633328Z` — **FUELINST**: 80 rows; marker `2026-09-21T08:25:00Z`
- `2026-09-21T08:24:13.422111Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:23:45Z`
- `2026-09-21T08:22:08.887308Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:21:45Z`
- `2026-09-21T08:20:32.864774Z` — **FUELINST**: 80 rows; marker `2026-09-21T08:20:00Z`
- `2026-09-21T08:20:16.785468Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:19:45Z`
- `2026-09-21T08:19:28.892313Z` — **INDGEN**: 702 rows; marker `2026-09-21T08:16:00Z`
