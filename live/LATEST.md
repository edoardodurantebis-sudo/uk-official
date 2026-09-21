# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T22:14:23.573753Z`  
Current process started UTC: `2026-09-21T22:10:22.524501Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3639, delta=0, z=4.98 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3639, delta=-6, z=5.01 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3645, delta=24, z=5.33 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=4, z=5.15 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3641, delta=-1, z=5.12 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3642, delta=-1, z=5.17 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3643, delta=-6, z=5.23 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=1, z=5.37 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=7, z=5.40 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3621, delta=45, z=5.10 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3641, delta=11, z=5.31 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3630, delta=10, z=5.15 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3620, delta=4, z=5.00 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3616, delta=2, z=4.96 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3614, delta=9, z=4.96 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1953, 2026-09-21T22:10:22.524514Z)
- `FUELINST|fuelType=OTHER|generation` = **488** (n=1953, 2026-09-21T22:10:22.524514Z)
- `FUELINST|fuelType=PS|generation` = **-9** (n=1953, 2026-09-21T22:10:22.524514Z)
- `FUELINST|fuelType=WIND|generation` = **3877** (n=1953, 2026-09-21T22:10:22.524514Z)
- `IMBALNGC|TOTAL|imbalance` = **-2513** (n=321, 2026-09-21T21:51:47.142688Z)
- `INDDEM|TOTAL|demand` = **-12258** (n=321, 2026-09-21T21:51:31.174771Z)
- `INDGEN|TOTAL|generation` = **18946** (n=321, 2026-09-21T21:51:31.174771Z)
- `MELNGC|TOTAL|margin` = **36139** (n=321, 2026-09-21T21:49:39.238592Z)
- `MID|dataProvider=APXMIDP|price` = **139.3** (n=62, 2026-09-21T22:12:14.250493Z)
- `MID|dataProvider=APXMIDP|volume` = **1973.2** (n=62, 2026-09-21T22:12:14.250493Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=122, 2026-09-21T22:12:14.250493Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=122, 2026-09-21T22:12:14.250493Z)
- `NDF|TOTAL|demand` = **20959** (n=328, 2026-09-21T21:47:36.336063Z)
- `TSDF|TOTAL|demand` = **21459** (n=328, 2026-09-21T21:47:51.844627Z)
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T22:14:06.157923Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:13:45Z`
- `2026-09-21T22:12:14.250493Z` — **MID**: 2 rows; marker `2026-09-21T22:12:04Z`
- `2026-09-21T22:12:14.250493Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:11:45Z`
- `2026-09-21T22:10:22.524514Z` — **FUELINST**: 80 rows; marker `2026-09-21T22:10:00Z`
- `2026-09-21T22:10:22.524514Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:09:45Z`
- `2026-09-21T22:08:07.495061Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:07:45Z`
- `2026-09-21T22:06:31.208116Z` — **MID**: 1 rows; marker `2026-09-21T22:05:00Z`
- `2026-09-21T22:06:15.204960Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:05:45Z`
- `2026-09-21T22:05:27.041551Z` — **FUELINST**: 80 rows; marker `2026-09-21T22:05:00Z`
- `2026-09-21T22:04:07.493342Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:03:45Z`
- `2026-09-21T22:02:15.519145Z` — **FREQ**: 5761 rows; marker `2026-09-21T22:01:45Z`
- `2026-09-21T22:00:46.782750Z` — **FUELHH**: 20 rows; marker `2026-09-21T22:00:00Z`
- `2026-09-21T22:00:46.782750Z` — **FUELINST**: 80 rows; marker `2026-09-21T22:00:00Z`
- `2026-09-21T22:00:14.262219Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:59:45Z`
- `2026-09-21T21:58:22.050074Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:57:45Z`
