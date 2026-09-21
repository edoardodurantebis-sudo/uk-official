# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T08:52:46.522212Z`  
Current process started UTC: `2026-09-21T08:48:46.326664Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=0, z=6.62 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3500, delta=1, z=7.30 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=791, delta=-14, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=-2, z=6.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=0, z=6.88 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1796, 2026-09-21T08:50:38.007400Z)
- `FUELINST|fuelType=OTHER|generation` = **1208** (n=1796, 2026-09-21T08:50:38.007400Z)
- `FUELINST|fuelType=PS|generation` = **349** (n=1796, 2026-09-21T08:50:38.007400Z)
- `FUELINST|fuelType=WIND|generation` = **3694** (n=1796, 2026-09-21T08:50:38.007400Z)
- `IMBALNGC|TOTAL|imbalance` = **-2000** (n=295, 2026-09-21T08:49:50.513529Z)
- `INDDEM|TOTAL|demand` = **-12837** (n=295, 2026-09-21T08:49:33.783369Z)
- `INDGEN|TOTAL|generation` = **19269** (n=295, 2026-09-21T08:49:50.513529Z)
- `MELNGC|TOTAL|margin` = **38223** (n=295, 2026-09-21T08:48:46.326673Z)
- `MID|dataProvider=APXMIDP|price` = **190.64** (n=35, 2026-09-21T08:42:15.436154Z)
- `MID|dataProvider=APXMIDP|volume` = **3045.8** (n=35, 2026-09-21T08:42:15.436154Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=70, 2026-09-21T08:42:15.436154Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=70, 2026-09-21T08:42:15.436154Z)
- `NDF|TOTAL|demand` = **20110** (n=302, 2026-09-21T08:47:15.196799Z)
- `TSDF|TOTAL|demand` = **21269** (n=302, 2026-09-21T08:47:15.196799Z)
- `WINDFOR|TOTAL|generation` = **9277** (n=51, 2026-09-21T08:30:33.936824Z)

## Latest publication events

- `2026-09-21T08:52:14.340412Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:51:45Z`
- `2026-09-21T08:50:38.007400Z` — **FUELINST**: 80 rows; marker `2026-09-21T08:50:00Z`
- `2026-09-21T08:50:22.401707Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:49:45Z`
- `2026-09-21T08:49:50.513529Z` — **INDGEN**: 684 rows; marker `2026-09-21T08:46:00Z`
- `2026-09-21T08:49:50.513529Z` — **IMBALNGC**: 684 rows; marker `2026-09-21T08:46:00Z`
- `2026-09-21T08:49:33.783369Z` — **INDDEM**: 684 rows; marker `2026-09-21T08:46:00Z`
- `2026-09-21T08:48:46.326673Z` — **MELNGC**: 684 rows; marker `2026-09-21T08:46:00Z`
- `2026-09-21T08:48:19.577987Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:47:45Z`
- `2026-09-21T08:47:15.196799Z` — **TSDF**: 684 rows; marker `2026-09-21T08:46:00Z`
- `2026-09-21T08:47:15.196799Z` — **NDF**: 38 rows; marker `2026-09-21T08:46:00Z`
- `2026-09-21T08:46:27.727984Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:45:45Z`
- `2026-09-21T08:45:39.552139Z` — **FUELINST**: 80 rows; marker `2026-09-21T08:45:00Z`
- `2026-09-21T08:44:33.748863Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:43:45Z`
- `2026-09-21T08:42:15.436154Z` — **MID**: 2 rows; marker `2026-09-21T08:42:03Z`
- `2026-09-21T08:42:15.436154Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:41:45Z`
