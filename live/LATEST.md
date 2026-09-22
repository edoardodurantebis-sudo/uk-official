# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T05:37:02.871454Z`  
Current process started UTC: `2026-09-22T05:33:02.575040Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3659, delta=11, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3659, delta=-2, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=1, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=-3, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3663, delta=14, z=3.65 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-2, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-5, z=3.50 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=6, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3647, delta=3, z=3.52 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3650, delta=-4, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3646, delta=-9, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3655, delta=-1, z=3.65 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=6, z=3.67 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2042, 2026-09-22T05:35:28.174218Z)
- `FUELINST|fuelType=OTHER|generation` = **1217** (n=2042, 2026-09-22T05:35:28.174218Z)
- `FUELINST|fuelType=PS|generation` = **-18** (n=2042, 2026-09-22T05:35:28.174218Z)
- `FUELINST|fuelType=WIND|generation` = **3451** (n=2042, 2026-09-22T05:35:28.174218Z)
- `IMBALNGC|TOTAL|imbalance` = **-3262** (n=336, 2026-09-22T05:21:25.826538Z)
- `INDDEM|TOTAL|demand` = **-12475** (n=336, 2026-09-22T05:21:25.826538Z)
- `INDGEN|TOTAL|generation` = **18197** (n=336, 2026-09-22T05:21:25.826538Z)
- `MELNGC|TOTAL|margin` = **37776** (n=336, 2026-09-22T05:20:53.933497Z)
- `MID|dataProvider=APXMIDP|price` = **166** (n=76, 2026-09-22T05:12:07.753775Z)
- `MID|dataProvider=APXMIDP|volume` = **2756.8** (n=76, 2026-09-22T05:12:07.753775Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=151, 2026-09-22T05:36:33.524532Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=151, 2026-09-22T05:36:33.524532Z)
- `NDF|TOTAL|demand` = **20959** (n=343, 2026-09-22T05:17:59.151292Z)
- `TSDF|TOTAL|demand` = **21459** (n=343, 2026-09-22T05:17:42.914630Z)
- `WINDFOR|TOTAL|generation` = **12340** (n=58, 2026-09-22T05:30:40.954997Z)

## Latest publication events

- `2026-09-22T05:36:33.524532Z` — **MID**: 1 rows; marker `2026-09-22T05:35:00Z`
- `2026-09-22T05:36:17.994723Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:35:45Z`
- `2026-09-22T05:35:28.174218Z` — **FUELINST**: 80 rows; marker `2026-09-22T05:35:00Z`
- `2026-09-22T05:34:24.584800Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:33:45Z`
- `2026-09-22T05:32:17.543330Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:31:45Z`
- `2026-09-22T05:30:40.954997Z` — **WINDFOR**: 73 rows; marker `2026-09-22T05:30:00Z`
- `2026-09-22T05:30:40.954997Z` — **FUELHH**: 20 rows; marker `2026-09-22T05:30:00Z`
- `2026-09-22T05:30:40.954997Z` — **FUELINST**: 80 rows; marker `2026-09-22T05:30:00Z`
- `2026-09-22T05:30:09.318117Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:29:45Z`
- `2026-09-22T05:28:21.077114Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:27:45Z`
- `2026-09-22T05:26:12.898261Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:25:45Z`
- `2026-09-22T05:25:25.356641Z` — **FUELINST**: 80 rows; marker `2026-09-22T05:25:00Z`
- `2026-09-22T05:24:21.069140Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:23:45Z`
- `2026-09-22T05:22:13.370360Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:21:45Z`
- `2026-09-22T05:21:25.826538Z` — **INDGEN**: 810 rows; marker `2026-09-22T05:17:00Z`
