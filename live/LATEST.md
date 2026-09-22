# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T12:29:09.665549Z`  
Current process started UTC: `2026-09-22T12:25:09.674760Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3733, delta=3, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3730, delta=10, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3136, delta=-128, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3264, delta=142, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3122, delta=169, z=3.61 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=-1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3662, delta=5, z=3.53 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3659, delta=11, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3659, delta=-2, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=1, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=-3, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3663, delta=14, z=3.65 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-2, z=3.55 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2124, 2026-09-22T12:25:29.676914Z)
- `FUELINST|fuelType=OTHER|generation` = **666** (n=2124, 2026-09-22T12:25:29.676914Z)
- `FUELINST|fuelType=PS|generation` = **-126** (n=2124, 2026-09-22T12:25:29.676914Z)
- `FUELINST|fuelType=WIND|generation` = **2750** (n=2124, 2026-09-22T12:25:29.676914Z)
- `IMBALNGC|TOTAL|imbalance` = **-7075** (n=349, 2026-09-22T12:23:54.131907Z)
- `INDDEM|TOTAL|demand` = **-12511** (n=349, 2026-09-22T12:23:38.146172Z)
- `INDGEN|TOTAL|generation` = **14083** (n=349, 2026-09-22T12:23:38.146172Z)
- `MELNGC|TOTAL|margin` = **37065** (n=349, 2026-09-22T12:20:42.277962Z)
- `MID|dataProvider=APXMIDP|price` = **122.04** (n=90, 2026-09-22T12:12:28.586866Z)
- `MID|dataProvider=APXMIDP|volume` = **4318.9** (n=90, 2026-09-22T12:12:28.586866Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=178, 2026-09-22T12:12:28.586866Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=178, 2026-09-22T12:12:28.586866Z)
- `NDF|TOTAL|demand` = **20658** (n=357, 2026-09-22T12:18:18.895814Z)
- `TSDF|TOTAL|demand` = **21158** (n=357, 2026-09-22T12:18:18.895814Z)
- `WINDFOR|TOTAL|generation` = **13007** (n=60, 2026-09-22T10:30:42.618958Z)

## Latest publication events

- `2026-09-22T12:28:09.273733Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:27:45Z`
- `2026-09-22T12:26:17.049885Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:25:45Z`
- `2026-09-22T12:25:29.676914Z` — **FUELINST**: 80 rows; marker `2026-09-22T12:25:00Z`
- `2026-09-22T12:24:09.834774Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:23:45Z`
- `2026-09-22T12:23:54.131907Z` — **IMBALNGC**: 1422 rows; marker `2026-09-22T12:18:00Z`
- `2026-09-22T12:23:38.146172Z` — **INDGEN**: 1422 rows; marker `2026-09-22T12:17:00Z`
- `2026-09-22T12:23:38.146172Z` — **INDDEM**: 1422 rows; marker `2026-09-22T12:17:00Z`
- `2026-09-22T12:22:01.882360Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:21:45Z`
- `2026-09-22T12:20:42.277962Z` — **MELNGC**: 1422 rows; marker `2026-09-22T12:18:00Z`
- `2026-09-22T12:20:42.277962Z` — **FUELINST**: 80 rows; marker `2026-09-22T12:20:00Z`
- `2026-09-22T12:20:10.933486Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:19:45Z`
- `2026-09-22T12:18:18.895814Z` — **TSDF**: 1422 rows; marker `2026-09-22T12:18:00Z`
- `2026-09-22T12:18:18.895814Z` — **NDF**: 79 rows; marker `2026-09-22T12:18:00Z`
- `2026-09-22T12:18:03.511568Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:17:45Z`
- `2026-09-22T12:16:44.248026Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:15:45Z`
