# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T11:25:00.791701Z`  
Current process started UTC: `2026-09-22T11:20:59.055349Z`  
1-second metadata polls in this process: **233**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-5, z=3.50 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2111, 2026-09-22T11:20:43.853741Z)
- `FUELINST|fuelType=OTHER|generation` = **662** (n=2111, 2026-09-22T11:20:43.853741Z)
- `FUELINST|fuelType=PS|generation` = **-164** (n=2111, 2026-09-22T11:20:43.853741Z)
- `FUELINST|fuelType=WIND|generation` = **3892** (n=2111, 2026-09-22T11:20:43.853741Z)
- `IMBALNGC|TOTAL|imbalance` = **-6224** (n=347, 2026-09-22T11:23:24.230167Z)
- `INDDEM|TOTAL|demand` = **-12511** (n=347, 2026-09-22T11:23:24.230167Z)
- `INDGEN|TOTAL|generation` = **14934** (n=347, 2026-09-22T11:23:07.676153Z)
- `MELNGC|TOTAL|margin` = **37032** (n=347, 2026-09-22T11:20:43.853741Z)
- `MID|dataProvider=APXMIDP|price` = **123.62** (n=88, 2026-09-22T11:12:31.448643Z)
- `MID|dataProvider=APXMIDP|volume` = **4392.8** (n=88, 2026-09-22T11:12:31.448643Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=174, 2026-09-22T11:12:31.448643Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=174, 2026-09-22T11:12:31.448643Z)
- `NDF|TOTAL|demand` = **20658** (n=355, 2026-09-22T11:18:03.969802Z)
- `TSDF|TOTAL|demand` = **21158** (n=355, 2026-09-22T11:18:03.969802Z)
- `WINDFOR|TOTAL|generation` = **13007** (n=60, 2026-09-22T10:30:42.618958Z)

## Latest publication events

- `2026-09-22T11:24:28.625198Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:23:45Z`
- `2026-09-22T11:23:24.230167Z` — **INDDEM**: 1458 rows; marker `2026-09-22T11:17:00Z`
- `2026-09-22T11:23:24.230167Z` — **IMBALNGC**: 1458 rows; marker `2026-09-22T11:17:00Z`
- `2026-09-22T11:23:07.676153Z` — **INDGEN**: 1458 rows; marker `2026-09-22T11:17:00Z`
- `2026-09-22T11:22:19.389775Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:21:45Z`
- `2026-09-22T11:20:43.853741Z` — **MELNGC**: 1458 rows; marker `2026-09-22T11:17:00Z`
- `2026-09-22T11:20:43.853741Z` — **FUELINST**: 80 rows; marker `2026-09-22T11:20:00Z`
- `2026-09-22T11:20:28.102801Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:19:45Z`
- `2026-09-22T11:18:19.938485Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:17:45Z`
- `2026-09-22T11:18:03.969802Z` — **TSDF**: 1458 rows; marker `2026-09-22T11:17:00Z`
- `2026-09-22T11:18:03.969802Z` — **NDF**: 81 rows; marker `2026-09-22T11:17:00Z`
- `2026-09-22T11:16:44.223861Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:15:45Z`
- `2026-09-22T11:15:44.798615Z` — **FUELINST**: 80 rows; marker `2026-09-22T11:15:00Z`
- `2026-09-22T11:14:24.252209Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:13:45Z`
- `2026-09-22T11:12:31.448643Z` — **MID**: 2 rows; marker `2026-09-22T11:12:04Z`
