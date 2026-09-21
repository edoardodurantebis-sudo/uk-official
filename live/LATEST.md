# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T10:16:57.686357Z`  
Current process started UTC: `2026-09-21T10:12:57.715147Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3492, delta=-7, z=5.32 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=0, z=5.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=-2, z=5.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=-2, z=5.78 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1813, 2026-09-21T10:15:56.661656Z)
- `FUELINST|fuelType=OTHER|generation` = **782** (n=1813, 2026-09-21T10:15:56.661656Z)
- `FUELINST|fuelType=PS|generation` = **-11** (n=1813, 2026-09-21T10:15:56.661656Z)
- `FUELINST|fuelType=WIND|generation` = **3290** (n=1813, 2026-09-21T10:15:56.661656Z)
- `IMBALNGC|TOTAL|imbalance` = **569** (n=297, 2026-09-21T09:49:16.952337Z)
- `INDDEM|TOTAL|demand` = **-12811** (n=297, 2026-09-21T09:49:16.952337Z)
- `INDGEN|TOTAL|generation` = **21728** (n=297, 2026-09-21T09:49:16.952337Z)
- `MELNGC|TOTAL|margin` = **39819** (n=297, 2026-09-21T09:48:45.225710Z)
- `MID|dataProvider=APXMIDP|price` = **160.64** (n=38, 2026-09-21T10:12:12.217441Z)
- `MID|dataProvider=APXMIDP|volume` = **2813.7** (n=38, 2026-09-21T10:12:12.217441Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=76, 2026-09-21T10:12:12.217441Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=76, 2026-09-21T10:12:12.217441Z)
- `NDF|TOTAL|demand` = **20000** (n=304, 2026-09-21T09:46:53.428239Z)
- `TSDF|TOTAL|demand` = **21159** (n=304, 2026-09-21T09:46:53.428239Z)
- `WINDFOR|TOTAL|generation` = **9277** (n=51, 2026-09-21T08:30:33.936824Z)

## Latest publication events

- `2026-09-21T10:16:12.208188Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:15:45Z`
- `2026-09-21T10:15:56.661656Z` — **FUELINST**: 80 rows; marker `2026-09-21T10:15:00Z`
- `2026-09-21T10:14:17.725523Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:13:45Z`
- `2026-09-21T10:12:12.217441Z` — **MID**: 2 rows; marker `2026-09-21T10:12:03Z`
- `2026-09-21T10:12:12.217441Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:11:45Z`
- `2026-09-21T10:10:35.161240Z` — **FUELINST**: 80 rows; marker `2026-09-21T10:10:00Z`
- `2026-09-21T10:10:19.121688Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:09:45Z`
- `2026-09-21T10:08:13.151529Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:07:45Z`
- `2026-09-21T10:06:52.221572Z` — **MID**: 1 rows; marker `2026-09-21T10:05:00Z`
- `2026-09-21T10:06:20.929406Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:05:45Z`
- `2026-09-21T10:05:32.523147Z` — **FUELINST**: 80 rows; marker `2026-09-21T10:05:00Z`
- `2026-09-21T10:04:28.566901Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:03:45Z`
- `2026-09-21T10:02:07.353899Z` — **FREQ**: 5761 rows; marker `2026-09-21T10:01:45Z`
- `2026-09-21T10:00:47.696570Z` — **FUELHH**: 20 rows; marker `2026-09-21T10:00:00Z`
- `2026-09-21T10:00:31.664859Z` — **FUELINST**: 80 rows; marker `2026-09-21T10:00:00Z`
