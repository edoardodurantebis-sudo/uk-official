# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T05:28:36.989367Z`  
Current process started UTC: `2026-09-22T05:24:37.224452Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=4, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3646, delta=-1, z=3.58 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2040, 2026-09-22T05:25:25.356641Z)
- `FUELINST|fuelType=OTHER|generation` = **1027** (n=2040, 2026-09-22T05:25:25.356641Z)
- `FUELINST|fuelType=PS|generation` = **-171** (n=2040, 2026-09-22T05:25:25.356641Z)
- `FUELINST|fuelType=WIND|generation` = **3500** (n=2040, 2026-09-22T05:25:25.356641Z)
- `IMBALNGC|TOTAL|imbalance` = **-3262** (n=336, 2026-09-22T05:21:25.826538Z)
- `INDDEM|TOTAL|demand` = **-12475** (n=336, 2026-09-22T05:21:25.826538Z)
- `INDGEN|TOTAL|generation` = **18197** (n=336, 2026-09-22T05:21:25.826538Z)
- `MELNGC|TOTAL|margin` = **37776** (n=336, 2026-09-22T05:20:53.933497Z)
- `MID|dataProvider=APXMIDP|price` = **166** (n=76, 2026-09-22T05:12:07.753775Z)
- `MID|dataProvider=APXMIDP|volume` = **2756.8** (n=76, 2026-09-22T05:12:07.753775Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=150, 2026-09-22T05:12:07.753775Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=150, 2026-09-22T05:12:07.753775Z)
- `NDF|TOTAL|demand` = **20959** (n=343, 2026-09-22T05:17:59.151292Z)
- `TSDF|TOTAL|demand` = **21459** (n=343, 2026-09-22T05:17:42.914630Z)
- `WINDFOR|TOTAL|generation` = **11644** (n=57, 2026-09-22T03:30:45.244161Z)

## Latest publication events

- `2026-09-22T05:28:21.077114Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:27:45Z`
- `2026-09-22T05:26:12.898261Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:25:45Z`
- `2026-09-22T05:25:25.356641Z` — **FUELINST**: 80 rows; marker `2026-09-22T05:25:00Z`
- `2026-09-22T05:24:21.069140Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:23:45Z`
- `2026-09-22T05:22:13.370360Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:21:45Z`
- `2026-09-22T05:21:25.826538Z` — **INDGEN**: 810 rows; marker `2026-09-22T05:17:00Z`
- `2026-09-22T05:21:25.826538Z` — **INDDEM**: 810 rows; marker `2026-09-22T05:17:00Z`
- `2026-09-22T05:21:25.826538Z` — **IMBALNGC**: 810 rows; marker `2026-09-22T05:17:00Z`
- `2026-09-22T05:20:53.933497Z` — **MELNGC**: 810 rows; marker `2026-09-22T05:17:00Z`
- `2026-09-22T05:20:22.250353Z` — **FUELINST**: 80 rows; marker `2026-09-22T05:20:00Z`
- `2026-09-22T05:20:22.250353Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:19:45Z`
- `2026-09-22T05:18:30.996842Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:17:45Z`
- `2026-09-22T05:17:59.151292Z` — **NDF**: 45 rows; marker `2026-09-22T05:17:00Z`
- `2026-09-22T05:17:42.914630Z` — **TSDF**: 810 rows; marker `2026-09-22T05:17:00Z`
- `2026-09-22T05:16:07.789006Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:15:45Z`
