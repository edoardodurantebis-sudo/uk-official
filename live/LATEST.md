# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T09:30:39.160040Z`  
Current process started UTC: `2026-09-21T09:26:39.067160Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=-4, z=6.25 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3499, delta=-1, z=6.68 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3505, delta=9, z=6.47 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=0, z=6.21 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1803, 2026-09-21T09:25:26.620217Z)
- `FUELINST|fuelType=OTHER|generation` = **762** (n=1803, 2026-09-21T09:25:26.620217Z)
- `FUELINST|fuelType=PS|generation` = **-11** (n=1803, 2026-09-21T09:25:26.620217Z)
- `FUELINST|fuelType=WIND|generation` = **3409** (n=1803, 2026-09-21T09:25:26.620217Z)
- `IMBALNGC|TOTAL|imbalance` = **415** (n=296, 2026-09-21T09:19:19.200312Z)
- `INDDEM|TOTAL|demand` = **-12824** (n=296, 2026-09-21T09:19:19.200312Z)
- `INDGEN|TOTAL|generation` = **21684** (n=296, 2026-09-21T09:19:19.200312Z)
- `MELNGC|TOTAL|margin` = **39679** (n=296, 2026-09-21T09:18:14.929656Z)
- `MID|dataProvider=APXMIDP|price` = **186.07** (n=36, 2026-09-21T09:12:15.224778Z)
- `MID|dataProvider=APXMIDP|volume` = **3269.8** (n=36, 2026-09-21T09:12:15.224778Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=72, 2026-09-21T09:12:15.224778Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=72, 2026-09-21T09:12:15.224778Z)
- `NDF|TOTAL|demand` = **20110** (n=303, 2026-09-21T09:17:02.570418Z)
- `TSDF|TOTAL|demand` = **21269** (n=303, 2026-09-21T09:17:02.570418Z)
- `WINDFOR|TOTAL|generation` = **9277** (n=51, 2026-09-21T08:30:33.936824Z)

## Latest publication events

- `2026-09-21T09:30:24.028234Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:29:45Z`
- `2026-09-21T09:28:16.170699Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:27:45Z`
- `2026-09-21T09:26:14.626588Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:25:45Z`
- `2026-09-21T09:25:26.620217Z` — **FUELINST**: 80 rows; marker `2026-09-21T09:25:00Z`
- `2026-09-21T09:24:22.991045Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:23:45Z`
- `2026-09-21T09:22:14.575508Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:21:45Z`
- `2026-09-21T09:20:22.601413Z` — **FUELINST**: 80 rows; marker `2026-09-21T09:20:00Z`
- `2026-09-21T09:20:22.601413Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:19:45Z`
- `2026-09-21T09:19:19.200312Z` — **INDGEN**: 666 rows; marker `2026-09-21T09:16:00Z`
- `2026-09-21T09:19:19.200312Z` — **INDDEM**: 666 rows; marker `2026-09-21T09:16:00Z`
- `2026-09-21T09:19:19.200312Z` — **IMBALNGC**: 666 rows; marker `2026-09-21T09:16:00Z`
- `2026-09-21T09:18:14.929656Z` — **MELNGC**: 666 rows; marker `2026-09-21T09:16:00Z`
- `2026-09-21T09:18:14.929656Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:17:45Z`
- `2026-09-21T09:17:02.570418Z` — **TSDF**: 666 rows; marker `2026-09-21T09:16:00Z`
- `2026-09-21T09:17:02.570418Z` — **NDF**: 37 rows; marker `2026-09-21T09:16:00Z`
