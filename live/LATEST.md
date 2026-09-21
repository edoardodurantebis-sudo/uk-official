# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T12:10:42.112188Z`  
Current process started UTC: `2026-09-21T12:06:41.588461Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3513, delta=4, z=4.86 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=0, z=4.79 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3512, delta=-3, z=5.00 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=3, z=4.82 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3506, delta=-6, z=4.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3512, delta=-1, z=4.97 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3513, delta=-4, z=5.03 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3517, delta=2, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3515, delta=0, z=5.16 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3515, delta=13, z=5.33 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3515, delta=-3, z=5.20 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3518, delta=2, z=5.33 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3516, delta=-3, z=5.32 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3519, delta=10, z=5.45 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3502, delta=8, z=5.16 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1833, 2026-09-21T12:10:25.258652Z)
- `FUELINST|fuelType=OTHER|generation` = **630** (n=1833, 2026-09-21T12:10:25.258652Z)
- `FUELINST|fuelType=PS|generation` = **228** (n=1833, 2026-09-21T12:10:25.258652Z)
- `FUELINST|fuelType=WIND|generation` = **3724** (n=1833, 2026-09-21T12:10:25.258652Z)
- `IMBALNGC|TOTAL|imbalance` = **-3014** (n=301, 2026-09-21T11:53:27.219932Z)
- `INDDEM|TOTAL|demand` = **-12241** (n=301, 2026-09-21T11:53:11.216520Z)
- `INDGEN|TOTAL|generation` = **18490** (n=301, 2026-09-21T11:52:55.313730Z)
- `MELNGC|TOTAL|margin` = **36673** (n=301, 2026-09-21T11:49:58.976889Z)
- `MID|dataProvider=APXMIDP|price` = **151.37** (n=41, 2026-09-21T11:42:21.248182Z)
- `MID|dataProvider=APXMIDP|volume` = **3253.6** (n=41, 2026-09-21T11:42:21.248182Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=81, 2026-09-21T12:06:41.588470Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=81, 2026-09-21T12:06:41.588470Z)
- `NDF|TOTAL|demand` = **21004** (n=308, 2026-09-21T11:48:08.614838Z)
- `TSDF|TOTAL|demand` = **21504** (n=308, 2026-09-21T11:48:08.614838Z)
- `WINDFOR|TOTAL|generation` = **8923** (n=52, 2026-09-21T10:30:49.343841Z)

## Latest publication events

- `2026-09-21T12:10:25.258652Z` — **FUELINST**: 80 rows; marker `2026-09-21T12:10:00Z`
- `2026-09-21T12:10:09.762874Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:09:45Z`
- `2026-09-21T12:08:02.226677Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:07:45Z`
- `2026-09-21T12:06:41.588470Z` — **MID**: 1 rows; marker `2026-09-21T12:05:00Z`
- `2026-09-21T12:06:12.203156Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:05:45Z`
- `2026-09-21T12:05:39.354727Z` — **FUELINST**: 80 rows; marker `2026-09-21T12:05:00Z`
- `2026-09-21T12:04:19.526223Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:03:45Z`
- `2026-09-21T12:02:26.376266Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:01:45Z`
- `2026-09-21T12:00:33.688161Z` — **FUELHH**: 20 rows; marker `2026-09-21T12:00:00Z`
- `2026-09-21T12:00:33.688161Z` — **FUELINST**: 80 rows; marker `2026-09-21T12:00:00Z`
- `2026-09-21T12:00:17.399560Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:59:45Z`
- `2026-09-21T11:58:25.116441Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:57:45Z`
- `2026-09-21T11:56:20.852602Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:55:45Z`
- `2026-09-21T11:55:33.407266Z` — **FUELINST**: 80 rows; marker `2026-09-21T11:55:00Z`
- `2026-09-21T11:54:12.328963Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:53:45Z`
