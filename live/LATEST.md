# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T06:03:19.002479Z`  
Current process started UTC: `2026-09-21T05:59:18.593356Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3468, delta=24, z=9.91 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=826, delta=13, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3476, delta=3, z=9.14 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=825, delta=-4, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3473, delta=7, z=9.17 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=829, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3466, delta=1, z=8.93 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=829, delta=3, z=4.32 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3465, delta=-3, z=9.07 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=826, delta=3, z=4.31 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3468, delta=8, z=9.50 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=823, delta=-1, z=4.30 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3460, delta=5, z=9.18 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=824, delta=0, z=4.34 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3444, delta=44, z=9.38 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1762, 2026-09-21T06:00:39.539021Z)
- `FUELINST|fuelType=OTHER|generation` = **2123** (n=1762, 2026-09-21T06:00:39.539021Z)
- `FUELINST|fuelType=PS|generation` = **65** (n=1762, 2026-09-21T06:00:39.539021Z)
- `FUELINST|fuelType=WIND|generation` = **3520** (n=1762, 2026-09-21T06:00:39.539021Z)
- `IMBALNGC|TOTAL|imbalance` = **-3970** (n=290, 2026-09-21T05:50:25.731576Z)
- `INDDEM|TOTAL|demand` = **-11743** (n=290, 2026-09-21T05:50:25.731576Z)
- `INDGEN|TOTAL|generation` = **16640** (n=290, 2026-09-21T05:50:25.731576Z)
- `MELNGC|TOTAL|margin` = **37032** (n=290, 2026-09-21T05:49:21.976604Z)
- `MID|dataProvider=APXMIDP|price` = **181.97** (n=29, 2026-09-21T05:42:30.662588Z)
- `MID|dataProvider=APXMIDP|volume` = **3042.6** (n=29, 2026-09-21T05:42:30.662588Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=58, 2026-09-21T05:42:30.662588Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=58, 2026-09-21T05:42:30.662588Z)
- `NDF|TOTAL|demand` = **20110** (n=296, 2026-09-21T05:47:29.842612Z)
- `TSDF|TOTAL|demand` = **20610** (n=296, 2026-09-21T05:47:29.842612Z)
- `WINDFOR|TOTAL|generation` = **8794** (n=50, 2026-09-21T05:30:44.368414Z)

## Latest publication events

- `2026-09-21T06:02:15.378099Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:01:45Z`
- `2026-09-21T06:00:39.539021Z` — **FUELHH**: 20 rows; marker `2026-09-21T06:00:00Z`
- `2026-09-21T06:00:39.539021Z` — **FUELINST**: 80 rows; marker `2026-09-21T06:00:00Z`
- `2026-09-21T06:00:23.601871Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:59:45Z`
- `2026-09-21T05:58:16.427048Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:57:45Z`
- `2026-09-21T05:56:24.946663Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:55:45Z`
- `2026-09-21T05:55:36.886938Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:55:00Z`
- `2026-09-21T05:54:24.428879Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:53:45Z`
- `2026-09-21T05:52:09.638213Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:51:45Z`
- `2026-09-21T05:50:25.731576Z` — **INDGEN**: 792 rows; marker `2026-09-21T05:47:00Z`
- `2026-09-21T05:50:25.731576Z` — **INDDEM**: 792 rows; marker `2026-09-21T05:47:00Z`
- `2026-09-21T05:50:25.731576Z` — **IMBALNGC**: 792 rows; marker `2026-09-21T05:47:00Z`
- `2026-09-21T05:50:25.731576Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:50:00Z`
- `2026-09-21T05:50:09.863461Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:49:45Z`
- `2026-09-21T05:49:21.976604Z` — **MELNGC**: 792 rows; marker `2026-09-21T05:47:00Z`
