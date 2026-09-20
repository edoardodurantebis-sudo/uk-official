# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T19:34:00.724555Z`  
Current process started UTC: `2026-09-20T19:30:00.595208Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=2793, delta=365, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2736, delta=-158, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2894, delta=-83, z=3.94 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2977, delta=12, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2965, delta=268, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2697, delta=209, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2791, delta=35, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2756, delta=187, z=3.80 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=938, delta=-6, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=-1, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=947, delta=3, z=3.59 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=944, delta=66, z=3.69 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1636, 2026-09-20T19:30:32.161891Z)
- `FUELINST|fuelType=OTHER|generation` = **1822** (n=1636, 2026-09-20T19:30:32.161891Z)
- `FUELINST|fuelType=PS|generation` = **227** (n=1636, 2026-09-20T19:30:32.161891Z)
- `FUELINST|fuelType=WIND|generation` = **5703** (n=1636, 2026-09-20T19:30:32.161891Z)
- `IMBALNGC|TOTAL|imbalance` = **-5338** (n=269, 2026-09-20T19:22:11.796988Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=269, 2026-09-20T19:21:56.156895Z)
- `INDGEN|TOTAL|generation` = **15272** (n=269, 2026-09-20T19:21:40.377483Z)
- `MELNGC|TOTAL|margin` = **35583** (n=269, 2026-09-20T19:20:03.973467Z)
- `MID|dataProvider=APXMIDP|price` = **196.91** (n=8, 2026-09-20T19:12:09.434470Z)
- `MID|dataProvider=APXMIDP|volume` = **2752.7** (n=8, 2026-09-20T19:12:09.434470Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=16, 2026-09-20T19:12:09.434470Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=16, 2026-09-20T19:12:09.434470Z)
- `NDF|TOTAL|demand` = **20110** (n=275, 2026-09-20T19:17:56.651564Z)
- `TSDF|TOTAL|demand` = **20610** (n=275, 2026-09-20T19:17:56.651564Z)
- `WINDFOR|TOTAL|generation` = **1726** (n=47, 2026-09-20T19:30:32.161891Z)

## Latest publication events

- `2026-09-20T19:32:24.347525Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:31:45Z`
- `2026-09-20T19:30:32.161891Z` — **WINDFOR**: 73 rows; marker `2026-09-20T19:30:00Z`
- `2026-09-20T19:30:32.161891Z` — **FUELHH**: 20 rows; marker `2026-09-20T19:30:00Z`
- `2026-09-20T19:30:32.161891Z` — **FUELINST**: 80 rows; marker `2026-09-20T19:30:00Z`
- `2026-09-20T19:30:16.597613Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:29:45Z`
- `2026-09-20T19:28:19.712945Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:27:45Z`
- `2026-09-20T19:26:11.502274Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:25:45Z`
- `2026-09-20T19:25:39.222076Z` — **FUELINST**: 80 rows; marker `2026-09-20T19:25:00Z`
- `2026-09-20T19:24:19.407694Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:23:45Z`
- `2026-09-20T19:22:11.796988Z` — **IMBALNGC**: 1170 rows; marker `2026-09-20T19:17:00Z`
- `2026-09-20T19:22:11.796988Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:21:45Z`
- `2026-09-20T19:21:56.156895Z` — **INDDEM**: 1170 rows; marker `2026-09-20T19:17:00Z`
- `2026-09-20T19:21:40.377483Z` — **INDGEN**: 1170 rows; marker `2026-09-20T19:17:00Z`
- `2026-09-20T19:20:35.493142Z` — **FUELINST**: 80 rows; marker `2026-09-20T19:20:00Z`
- `2026-09-20T19:20:20.157578Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:19:45Z`
