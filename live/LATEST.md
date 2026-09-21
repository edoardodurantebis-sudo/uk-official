# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T06:15:56.329852Z`  
Current process started UTC: `2026-09-21T06:11:56.048993Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3492, delta=-4, z=9.38 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=837, delta=10, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=9, z=9.87 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=827, delta=7, z=4.21 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3487, delta=11, z=9.59 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=820, delta=-5, z=4.16 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3468, delta=24, z=9.91 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=826, delta=13, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3476, delta=3, z=9.14 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=825, delta=-4, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3473, delta=7, z=9.17 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=829, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3466, delta=1, z=8.93 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=829, delta=3, z=4.32 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3465, delta=-3, z=9.07 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1765, 2026-09-21T06:15:40.677510Z)
- `FUELINST|fuelType=OTHER|generation` = **2164** (n=1765, 2026-09-21T06:15:40.677510Z)
- `FUELINST|fuelType=PS|generation` = **226** (n=1765, 2026-09-21T06:15:40.677510Z)
- `FUELINST|fuelType=WIND|generation` = **3629** (n=1765, 2026-09-21T06:15:40.677510Z)
- `IMBALNGC|TOTAL|imbalance` = **-3970** (n=290, 2026-09-21T05:50:25.731576Z)
- `INDDEM|TOTAL|demand` = **-11743** (n=290, 2026-09-21T05:50:25.731576Z)
- `INDGEN|TOTAL|generation` = **16640** (n=290, 2026-09-21T05:50:25.731576Z)
- `MELNGC|TOTAL|margin` = **37032** (n=290, 2026-09-21T05:49:21.976604Z)
- `MID|dataProvider=APXMIDP|price` = **194.74** (n=30, 2026-09-21T06:12:12.514844Z)
- `MID|dataProvider=APXMIDP|volume` = **2536.8** (n=30, 2026-09-21T06:12:12.514844Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=60, 2026-09-21T06:12:12.514844Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=60, 2026-09-21T06:12:12.514844Z)
- `NDF|TOTAL|demand` = **20110** (n=296, 2026-09-21T05:47:29.842612Z)
- `TSDF|TOTAL|demand` = **20610** (n=296, 2026-09-21T05:47:29.842612Z)
- `WINDFOR|TOTAL|generation` = **8794** (n=50, 2026-09-21T05:30:44.368414Z)

## Latest publication events

- `2026-09-21T06:15:40.677510Z` — **FUELINST**: 80 rows; marker `2026-09-21T06:15:00Z`
- `2026-09-21T06:14:04.315699Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:13:45Z`
- `2026-09-21T06:12:28.649319Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:11:45Z`
- `2026-09-21T06:12:12.514844Z` — **MID**: 2 rows; marker `2026-09-21T06:12:04Z`
- `2026-09-21T06:10:42.044972Z` — **FUELINST**: 80 rows; marker `2026-09-21T06:10:00Z`
- `2026-09-21T06:10:25.677003Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:09:45Z`
- `2026-09-21T06:08:17.395624Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:07:45Z`
- `2026-09-21T06:06:42.334274Z` — **MID**: 1 rows; marker `2026-09-21T06:05:00Z`
- `2026-09-21T06:06:26.098681Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:05:45Z`
- `2026-09-21T06:05:38.597727Z` — **FUELINST**: 80 rows; marker `2026-09-21T06:05:00Z`
- `2026-09-21T06:04:18.796860Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:03:45Z`
- `2026-09-21T06:02:15.378099Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:01:45Z`
- `2026-09-21T06:00:39.539021Z` — **FUELHH**: 20 rows; marker `2026-09-21T06:00:00Z`
- `2026-09-21T06:00:39.539021Z` — **FUELINST**: 80 rows; marker `2026-09-21T06:00:00Z`
- `2026-09-21T06:00:23.601871Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:59:45Z`
