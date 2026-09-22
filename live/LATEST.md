# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T04:20:42.397938Z`  
Current process started UTC: `2026-09-22T04:16:42.008603Z`  
1-second metadata polls in this process: **231**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=6, z=3.67 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=4, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3646, delta=-1, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3647, delta=-3, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-1, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=0, z=3.65 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=-4, z=3.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-3, z=3.73 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-1, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3658, delta=1, z=3.81 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3657, delta=7, z=3.81 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3655, delta=1, z=3.88 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=2, z=3.73 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-9, z=3.72 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-3, z=3.85 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2027, 2026-09-22T04:20:26.160081Z)
- `FUELINST|fuelType=OTHER|generation` = **531** (n=2027, 2026-09-22T04:20:26.160081Z)
- `FUELINST|fuelType=PS|generation` = **-705** (n=2027, 2026-09-22T04:20:26.160081Z)
- `FUELINST|fuelType=WIND|generation` = **3476** (n=2027, 2026-09-22T04:20:26.160081Z)
- `IMBALNGC|TOTAL|imbalance` = **-3324** (n=334, 2026-09-22T04:20:26.160081Z)
- `INDDEM|TOTAL|demand` = **-12520** (n=334, 2026-09-22T04:20:26.160081Z)
- `INDGEN|TOTAL|generation` = **18135** (n=334, 2026-09-22T04:20:26.160081Z)
- `MELNGC|TOTAL|margin` = **37794** (n=334, 2026-09-22T04:19:22.013813Z)
- `MID|dataProvider=APXMIDP|price` = **161.73** (n=74, 2026-09-22T04:12:29.072816Z)
- `MID|dataProvider=APXMIDP|volume` = **2587.8** (n=74, 2026-09-22T04:12:29.072816Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=146, 2026-09-22T04:12:29.072816Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=146, 2026-09-22T04:12:29.072816Z)
- `NDF|TOTAL|demand` = **20959** (n=341, 2026-09-22T04:17:30.952649Z)
- `TSDF|TOTAL|demand` = **21459** (n=341, 2026-09-22T04:17:30.952649Z)
- `WINDFOR|TOTAL|generation` = **11644** (n=57, 2026-09-22T03:30:45.244161Z)

## Latest publication events

- `2026-09-22T04:20:26.160081Z` — **INDGEN**: 846 rows; marker `2026-09-22T04:17:00Z`
- `2026-09-22T04:20:26.160081Z` — **INDDEM**: 846 rows; marker `2026-09-22T04:16:00Z`
- `2026-09-22T04:20:26.160081Z` — **IMBALNGC**: 846 rows; marker `2026-09-22T04:17:00Z`
- `2026-09-22T04:20:26.160081Z` — **FUELINST**: 80 rows; marker `2026-09-22T04:20:00Z`
- `2026-09-22T04:20:09.951832Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:19:45Z`
- `2026-09-22T04:19:22.013813Z` — **MELNGC**: 846 rows; marker `2026-09-22T04:17:00Z`
- `2026-09-22T04:18:02.637993Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:17:45Z`
- `2026-09-22T04:17:30.952649Z` — **TSDF**: 846 rows; marker `2026-09-22T04:17:00Z`
- `2026-09-22T04:17:30.952649Z` — **NDF**: 47 rows; marker `2026-09-22T04:17:00Z`
- `2026-09-22T04:16:12.906208Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:15:45Z`
- `2026-09-22T04:15:41.405461Z` — **FUELINST**: 80 rows; marker `2026-09-22T04:15:00Z`
- `2026-09-22T04:14:05.466616Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:13:45Z`
- `2026-09-22T04:12:29.072816Z` — **MID**: 2 rows; marker `2026-09-22T04:12:03Z`
- `2026-09-22T04:12:01.440961Z` — **FREQ**: 5761 rows; marker `2026-09-22T04:11:45Z`
- `2026-09-22T04:10:41.810060Z` — **FUELINST**: 80 rows; marker `2026-09-22T04:10:00Z`
