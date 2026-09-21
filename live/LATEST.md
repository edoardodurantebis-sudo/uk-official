# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T11:15:50.742436Z`  
Current process started UTC: `2026-09-21T11:11:50.983684Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3516, delta=-3, z=5.32 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3519, delta=10, z=5.45 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3502, delta=8, z=5.16 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=6, z=5.19 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3503, delta=-2, z=5.05 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3505, delta=5, z=5.15 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3500, delta=1, z=5.04 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=4, z=5.05 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3494, delta=3, z=5.14 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3495, delta=2, z=4.96 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3493, delta=-1, z=4.93 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3494, delta=-2, z=5.00 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-1, z=5.10 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3497, delta=6, z=5.17 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3491, delta=-3, z=5.02 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1823, 2026-09-21T11:10:36.296471Z)
- `FUELINST|fuelType=OTHER|generation` = **687** (n=1823, 2026-09-21T11:10:36.296471Z)
- `FUELINST|fuelType=PS|generation` = **-9** (n=1823, 2026-09-21T11:10:36.296471Z)
- `FUELINST|fuelType=WIND|generation` = **3321** (n=1823, 2026-09-21T11:10:36.296471Z)
- `IMBALNGC|TOTAL|imbalance` = **-3871** (n=299, 2026-09-21T10:54:28.824712Z)
- `INDDEM|TOTAL|demand` = **-12243** (n=299, 2026-09-21T10:54:28.824712Z)
- `INDGEN|TOTAL|generation` = **17737** (n=299, 2026-09-21T10:54:28.824712Z)
- `MELNGC|TOTAL|margin` = **36495** (n=299, 2026-09-21T10:54:28.824712Z)
- `MID|dataProvider=APXMIDP|price` = **148.23** (n=40, 2026-09-21T11:12:23.227186Z)
- `MID|dataProvider=APXMIDP|volume` = **2804.1** (n=40, 2026-09-21T11:12:23.227186Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=78, 2026-09-21T11:12:23.227186Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=78, 2026-09-21T11:12:23.227186Z)
- `NDF|TOTAL|demand` = **21108** (n=306, 2026-09-21T10:53:55.939064Z)
- `TSDF|TOTAL|demand` = **21608** (n=306, 2026-09-21T10:54:11.637875Z)
- `WINDFOR|TOTAL|generation` = **8923** (n=52, 2026-09-21T10:30:49.343841Z)

## Latest publication events

- `2026-09-21T11:12:23.227186Z` — **MID**: 2 rows; marker `2026-09-21T11:12:05Z`
- `2026-09-21T11:12:23.227186Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:11:45Z`
- `2026-09-21T11:10:36.296471Z` — **FUELINST**: 80 rows; marker `2026-09-21T11:10:00Z`
- `2026-09-21T11:10:20.912605Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:09:45Z`
- `2026-09-21T11:08:12.644592Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:07:45Z`
- `2026-09-21T11:06:37.050810Z` — **MID**: 1 rows; marker `2026-09-21T11:05:00Z`
- `2026-09-21T11:06:21.579291Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:05:45Z`
- `2026-09-21T11:05:33.528943Z` — **FUELINST**: 80 rows; marker `2026-09-21T11:05:00Z`
- `2026-09-21T11:02:12.673882Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:01:45Z`
- `2026-09-21T11:00:34.414314Z` — **FUELHH**: 20 rows; marker `2026-09-21T11:00:00Z`
- `2026-09-21T11:00:34.414314Z` — **FUELINST**: 80 rows; marker `2026-09-21T11:00:00Z`
- `2026-09-21T11:00:18.112313Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:59:45Z`
- `2026-09-21T10:58:08.203536Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:57:45Z`
- `2026-09-21T10:56:16.057918Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:55:45Z`
- `2026-09-21T10:55:28.290975Z` — **FUELINST**: 80 rows; marker `2026-09-21T10:55:00Z`
