# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T05:17:04.185291Z`  
Current process started UTC: `2026-09-21T05:13:04.208811Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3450, delta=16, z=9.31 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=816, delta=5, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3434, delta=8, z=8.26 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=811, delta=28, z=4.33 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3426, delta=4, z=7.77 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=783, delta=279, z=4.05 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3400, delta=39, z=6.25 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3422, delta=13, z=7.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3409, delta=8, z=6.63 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3401, delta=7, z=6.05 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3394, delta=5, z=5.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3389, delta=6, z=5.17 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3383, delta=0, z=4.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3383, delta=-3, z=4.73 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3386, delta=10, z=5.02 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1753, 2026-09-21T05:15:29.021274Z)
- `FUELINST|fuelType=OTHER|generation` = **738** (n=1753, 2026-09-21T05:15:29.021274Z)
- `FUELINST|fuelType=PS|generation` = **-266** (n=1753, 2026-09-21T05:15:29.021274Z)
- `FUELINST|fuelType=WIND|generation` = **3983** (n=1753, 2026-09-21T05:15:29.021274Z)
- `IMBALNGC|TOTAL|imbalance` = **-4036** (n=288, 2026-09-21T04:50:43.860654Z)
- `INDDEM|TOTAL|demand` = **-11743** (n=288, 2026-09-21T04:50:27.923724Z)
- `INDGEN|TOTAL|generation` = **16574** (n=288, 2026-09-21T04:50:43.860654Z)
- `MELNGC|TOTAL|margin` = **37535** (n=288, 2026-09-21T04:49:24.362460Z)
- `MID|dataProvider=APXMIDP|price` = **167.58** (n=28, 2026-09-21T05:12:20.955026Z)
- `MID|dataProvider=APXMIDP|volume` = **2162.7** (n=28, 2026-09-21T05:12:20.955026Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=56, 2026-09-21T05:12:20.955026Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=56, 2026-09-21T05:12:20.955026Z)
- `NDF|TOTAL|demand` = **20110** (n=294, 2026-09-21T04:47:47.247919Z)
- `TSDF|TOTAL|demand` = **20610** (n=294, 2026-09-21T04:47:47.247919Z)
- `WINDFOR|TOTAL|generation` = **8021** (n=49, 2026-09-21T03:30:39.847119Z)

## Latest publication events

- `2026-09-21T05:16:16.504168Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:15:45Z`
- `2026-09-21T05:15:29.021274Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:15:00Z`
- `2026-09-21T05:14:24.899442Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:13:45Z`
- `2026-09-21T05:12:20.955026Z` — **MID**: 2 rows; marker `2026-09-21T05:12:04Z`
- `2026-09-21T05:12:20.955026Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:11:45Z`
- `2026-09-21T05:10:28.280610Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:10:00Z`
- `2026-09-21T05:10:28.280610Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:09:45Z`
- `2026-09-21T05:08:20.297674Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:07:45Z`
- `2026-09-21T05:06:28.264345Z` — **MID**: 1 rows; marker `2026-09-21T05:05:00Z`
- `2026-09-21T05:06:12.670547Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:05:45Z`
- `2026-09-21T05:05:24.615635Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:05:00Z`
- `2026-09-21T05:04:36.990847Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:03:45Z`
- `2026-09-21T05:02:15.989390Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:01:45Z`
- `2026-09-21T05:00:39.946202Z` — **FUELHH**: 20 rows; marker `2026-09-21T05:00:00Z`
- `2026-09-21T05:00:39.946202Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:00:00Z`
