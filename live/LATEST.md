# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T09:05:27.340072Z`  
Current process started UTC: `2026-09-21T09:01:26.962481Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=0, z=6.62 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3500, delta=1, z=7.30 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1798, 2026-09-21T09:00:29.419025Z)
- `FUELINST|fuelType=OTHER|generation` = **1056** (n=1798, 2026-09-21T09:00:29.419025Z)
- `FUELINST|fuelType=PS|generation` = **204** (n=1798, 2026-09-21T09:00:29.419025Z)
- `FUELINST|fuelType=WIND|generation` = **3543** (n=1798, 2026-09-21T09:00:29.419025Z)
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

- `2026-09-21T09:04:08.033790Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:03:45Z`
- `2026-09-21T09:02:15.289819Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:01:45Z`
- `2026-09-21T09:00:45.904116Z` — **FUELHH**: 20 rows; marker `2026-09-21T09:00:00Z`
- `2026-09-21T09:00:29.419025Z` — **FUELINST**: 80 rows; marker `2026-09-21T09:00:00Z`
- `2026-09-21T09:00:13.395209Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:59:45Z`
- `2026-09-21T08:58:03.486432Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:57:45Z`
- `2026-09-21T08:56:14.968464Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:55:45Z`
- `2026-09-21T08:55:43.552732Z` — **FUELINST**: 80 rows; marker `2026-09-21T08:55:00Z`
- `2026-09-21T08:54:05.133438Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:53:45Z`
- `2026-09-21T08:52:14.340412Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:51:45Z`
- `2026-09-21T08:50:38.007400Z` — **FUELINST**: 80 rows; marker `2026-09-21T08:50:00Z`
- `2026-09-21T08:50:22.401707Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:49:45Z`
- `2026-09-21T08:49:50.513529Z` — **INDGEN**: 684 rows; marker `2026-09-21T08:46:00Z`
- `2026-09-21T08:49:50.513529Z` — **IMBALNGC**: 684 rows; marker `2026-09-21T08:46:00Z`
- `2026-09-21T08:49:33.783369Z` — **INDDEM**: 684 rows; marker `2026-09-21T08:46:00Z`
