# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T10:33:45.226580Z`  
Current process started UTC: `2026-09-21T10:29:44.850734Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3494, delta=3, z=5.14 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3495, delta=2, z=4.96 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3493, delta=-1, z=4.93 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3494, delta=-2, z=5.00 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-1, z=5.10 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3497, delta=6, z=5.17 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3491, delta=-3, z=5.02 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3491, delta=-9, z=5.28 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3494, delta=0, z=5.15 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3494, delta=0, z=5.19 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3494, delta=5, z=5.23 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3489, delta=5, z=5.11 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3484, delta=-4, z=4.98 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3488, delta=-4, z=5.15 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3500, delta=4, z=5.90 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1816, 2026-09-21T10:30:33.931188Z)
- `FUELINST|fuelType=OTHER|generation` = **853** (n=1816, 2026-09-21T10:30:33.931188Z)
- `FUELINST|fuelType=PS|generation` = **-11** (n=1816, 2026-09-21T10:30:33.931188Z)
- `FUELINST|fuelType=WIND|generation` = **3410** (n=1816, 2026-09-21T10:30:33.931188Z)
- `IMBALNGC|TOTAL|imbalance` = **3568** (n=298, 2026-09-21T10:25:10.571552Z)
- `INDDEM|TOTAL|demand` = **-12828** (n=298, 2026-09-21T10:25:10.571552Z)
- `INDGEN|TOTAL|generation` = **24727** (n=298, 2026-09-21T10:25:10.571552Z)
- `MELNGC|TOTAL|margin` = **41012** (n=298, 2026-09-21T10:24:38.321334Z)
- `MID|dataProvider=APXMIDP|price` = **160.64** (n=38, 2026-09-21T10:12:12.217441Z)
- `MID|dataProvider=APXMIDP|volume` = **2813.7** (n=38, 2026-09-21T10:12:12.217441Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=76, 2026-09-21T10:12:12.217441Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=76, 2026-09-21T10:12:12.217441Z)
- `NDF|TOTAL|demand` = **20000** (n=305, 2026-09-21T10:22:13.936734Z)
- `TSDF|TOTAL|demand` = **21159** (n=305, 2026-09-21T10:22:13.936734Z)
- `WINDFOR|TOTAL|generation` = **8923** (n=52, 2026-09-21T10:30:49.343841Z)

## Latest publication events

- `2026-09-21T10:30:49.343841Z` — **WINDFOR**: 73 rows; marker `2026-09-21T10:30:00Z`
- `2026-09-21T10:30:49.343841Z` — **FUELHH**: 20 rows; marker `2026-09-21T10:30:00Z`
- `2026-09-21T10:30:33.931188Z` — **FUELINST**: 80 rows; marker `2026-09-21T10:30:00Z`
- `2026-09-21T10:30:17.618130Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:29:45Z`
- `2026-09-21T10:28:15.773287Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:27:45Z`
- `2026-09-21T10:26:23.617507Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:25:45Z`
- `2026-09-21T10:25:49.756667Z` — **FUELINST**: 80 rows; marker `2026-09-21T10:25:00Z`
- `2026-09-21T10:25:10.571552Z` — **INDGEN**: 630 rows; marker `2026-09-21T10:22:00Z`
- `2026-09-21T10:25:10.571552Z` — **INDDEM**: 630 rows; marker `2026-09-21T10:22:00Z`
- `2026-09-21T10:25:10.571552Z` — **IMBALNGC**: 630 rows; marker `2026-09-21T10:22:00Z`
- `2026-09-21T10:24:38.321334Z` — **MELNGC**: 630 rows; marker `2026-09-21T10:22:00Z`
- `2026-09-21T10:24:22.751239Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:23:45Z`
- `2026-09-21T10:22:13.936734Z` — **TSDF**: 630 rows; marker `2026-09-21T10:22:00Z`
- `2026-09-21T10:22:13.936734Z` — **NDF**: 35 rows; marker `2026-09-21T10:22:00Z`
- `2026-09-21T10:22:13.936734Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:21:45Z`
