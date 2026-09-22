# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T13:28:27.728280Z`  
Current process started UTC: `2026-09-22T13:24:27.866709Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3729, delta=7, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3732, delta=1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3731, delta=9, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3737, delta=0, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3722, delta=43, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3737, delta=4, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3733, delta=3, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3730, delta=10, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3136, delta=-128, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3264, delta=142, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3122, delta=169, z=3.61 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=-1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3662, delta=5, z=3.53 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3659, delta=11, z=3.61 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2136, 2026-09-22T13:25:18.873072Z)
- `FUELINST|fuelType=OTHER|generation` = **833** (n=2136, 2026-09-22T13:25:18.873072Z)
- `FUELINST|fuelType=PS|generation` = **-6** (n=2136, 2026-09-22T13:25:18.873072Z)
- `FUELINST|fuelType=WIND|generation` = **2335** (n=2136, 2026-09-22T13:25:18.873072Z)
- `IMBALNGC|TOTAL|imbalance` = **-7101** (n=351, 2026-09-22T13:23:27.914109Z)
- `INDDEM|TOTAL|demand` = **-12489** (n=351, 2026-09-22T13:23:11.544375Z)
- `INDGEN|TOTAL|generation` = **14057** (n=351, 2026-09-22T13:23:11.544375Z)
- `MELNGC|TOTAL|margin` = **37210** (n=351, 2026-09-22T13:20:32.064206Z)
- `MID|dataProvider=APXMIDP|price` = **123.86** (n=92, 2026-09-22T13:12:19.089418Z)
- `MID|dataProvider=APXMIDP|volume` = **4159.4** (n=92, 2026-09-22T13:12:19.089418Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=182, 2026-09-22T13:12:19.089418Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=182, 2026-09-22T13:12:19.089418Z)
- `NDF|TOTAL|demand` = **20658** (n=359, 2026-09-22T13:18:11.209895Z)
- `TSDF|TOTAL|demand` = **21158** (n=359, 2026-09-22T13:18:11.209895Z)
- `WINDFOR|TOTAL|generation` = **13082** (n=61, 2026-09-22T12:30:43.630179Z)

## Latest publication events

- `2026-09-22T13:28:14.835564Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:27:45Z`
- `2026-09-22T13:26:07.209895Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:25:45Z`
- `2026-09-22T13:25:18.873072Z` — **FUELINST**: 80 rows; marker `2026-09-22T13:25:00Z`
- `2026-09-22T13:24:15.253181Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:23:45Z`
- `2026-09-22T13:23:27.914109Z` — **IMBALNGC**: 1386 rows; marker `2026-09-22T13:17:00Z`
- `2026-09-22T13:23:11.544375Z` — **INDGEN**: 1386 rows; marker `2026-09-22T13:17:00Z`
- `2026-09-22T13:23:11.544375Z` — **INDDEM**: 1386 rows; marker `2026-09-22T13:17:00Z`
- `2026-09-22T13:22:07.883835Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:21:45Z`
- `2026-09-22T13:20:32.064206Z` — **MELNGC**: 1386 rows; marker `2026-09-22T13:17:00Z`
- `2026-09-22T13:20:32.064206Z` — **FUELINST**: 80 rows; marker `2026-09-22T13:20:00Z`
- `2026-09-22T13:20:16.490375Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:19:45Z`
- `2026-09-22T13:18:11.209895Z` — **TSDF**: 1386 rows; marker `2026-09-22T13:17:00Z`
- `2026-09-22T13:18:11.209895Z` — **NDF**: 77 rows; marker `2026-09-22T13:17:00Z`
- `2026-09-22T13:18:11.209895Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:17:45Z`
- `2026-09-22T13:16:17.787236Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:15:45Z`
