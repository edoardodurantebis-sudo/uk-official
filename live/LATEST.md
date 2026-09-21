# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T09:43:12.889839Z`  
Current process started UTC: `2026-09-21T09:39:13.575435Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3484, delta=-4, z=4.98 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3488, delta=-4, z=5.15 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3500, delta=4, z=5.90 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3492, delta=-7, z=5.32 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=0, z=5.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=-2, z=5.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=-2, z=5.78 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3503, delta=5, z=5.90 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3498, delta=7, z=5.79 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-3, z=6.11 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3491, delta=-2, z=5.59 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3493, delta=0, z=5.72 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3493, delta=-4, z=5.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3497, delta=-3, z=5.97 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3500, delta=-1, z=6.15 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1806, 2026-09-21T09:40:37.222245Z)
- `FUELINST|fuelType=OTHER|generation` = **841** (n=1806, 2026-09-21T09:40:37.222245Z)
- `FUELINST|fuelType=PS|generation` = **-11** (n=1806, 2026-09-21T09:40:37.222245Z)
- `FUELINST|fuelType=WIND|generation` = **3300** (n=1806, 2026-09-21T09:40:37.222245Z)
- `IMBALNGC|TOTAL|imbalance` = **415** (n=296, 2026-09-21T09:19:19.200312Z)
- `INDDEM|TOTAL|demand` = **-12824** (n=296, 2026-09-21T09:19:19.200312Z)
- `INDGEN|TOTAL|generation` = **21684** (n=296, 2026-09-21T09:19:19.200312Z)
- `MELNGC|TOTAL|margin` = **39679** (n=296, 2026-09-21T09:18:14.929656Z)
- `MID|dataProvider=APXMIDP|price` = **185.3** (n=37, 2026-09-21T09:42:14.042386Z)
- `MID|dataProvider=APXMIDP|volume` = **3412.1** (n=37, 2026-09-21T09:42:14.042386Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=74, 2026-09-21T09:42:14.042386Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=74, 2026-09-21T09:42:14.042386Z)
- `NDF|TOTAL|demand` = **20110** (n=303, 2026-09-21T09:17:02.570418Z)
- `TSDF|TOTAL|demand` = **21269** (n=303, 2026-09-21T09:17:02.570418Z)
- `WINDFOR|TOTAL|generation` = **9277** (n=51, 2026-09-21T08:30:33.936824Z)

## Latest publication events

- `2026-09-21T09:42:30.082947Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:41:45Z`
- `2026-09-21T09:42:14.042386Z` — **MID**: 2 rows; marker `2026-09-21T09:42:03Z`
- `2026-09-21T09:40:37.222245Z` — **FUELINST**: 80 rows; marker `2026-09-21T09:40:00Z`
- `2026-09-21T09:40:21.583749Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:39:45Z`
- `2026-09-21T09:38:14.057929Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:37:45Z`
- `2026-09-21T09:36:22.100071Z` — **MID**: 1 rows; marker `2026-09-21T09:35:00Z`
- `2026-09-21T09:36:22.100071Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:35:45Z`
- `2026-09-21T09:35:34.070061Z` — **FUELINST**: 80 rows; marker `2026-09-21T09:35:00Z`
- `2026-09-21T09:34:18.495533Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:33:45Z`
- `2026-09-21T09:32:25.669472Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:31:45Z`
- `2026-09-21T09:30:50.080679Z` — **FUELHH**: 20 rows; marker `2026-09-21T09:30:00Z`
- `2026-09-21T09:30:50.080679Z` — **FUELINST**: 80 rows; marker `2026-09-21T09:30:00Z`
- `2026-09-21T09:30:24.028234Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:29:45Z`
- `2026-09-21T09:28:16.170699Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:27:45Z`
- `2026-09-21T09:26:14.626588Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:25:45Z`
