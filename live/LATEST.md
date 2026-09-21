# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T05:25:28.187221Z`  
Current process started UTC: `2026-09-21T05:21:28.081952Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3448, delta=-2, z=8.93 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=821, delta=5, z=4.38 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1754, 2026-09-21T05:20:30.241601Z)
- `FUELINST|fuelType=OTHER|generation` = **867** (n=1754, 2026-09-21T05:20:30.241601Z)
- `FUELINST|fuelType=PS|generation` = **-105** (n=1754, 2026-09-21T05:20:30.241601Z)
- `FUELINST|fuelType=WIND|generation` = **3925** (n=1754, 2026-09-21T05:20:30.241601Z)
- `IMBALNGC|TOTAL|imbalance` = **-4015** (n=289, 2026-09-21T05:19:58.754386Z)
- `INDDEM|TOTAL|demand` = **-11743** (n=289, 2026-09-21T05:19:58.754386Z)
- `INDGEN|TOTAL|generation` = **16595** (n=289, 2026-09-21T05:19:58.754386Z)
- `MELNGC|TOTAL|margin` = **37533** (n=289, 2026-09-21T05:18:36.808843Z)
- `MID|dataProvider=APXMIDP|price` = **167.58** (n=28, 2026-09-21T05:12:20.955026Z)
- `MID|dataProvider=APXMIDP|volume` = **2162.7** (n=28, 2026-09-21T05:12:20.955026Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=56, 2026-09-21T05:12:20.955026Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=56, 2026-09-21T05:12:20.955026Z)
- `NDF|TOTAL|demand` = **20110** (n=295, 2026-09-21T05:17:16.844589Z)
- `TSDF|TOTAL|demand` = **20610** (n=295, 2026-09-21T05:17:16.844589Z)
- `WINDFOR|TOTAL|generation` = **8021** (n=49, 2026-09-21T03:30:39.847119Z)

## Latest publication events

- `2026-09-21T05:24:25.500923Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:23:45Z`
- `2026-09-21T05:22:16.087661Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:21:45Z`
- `2026-09-21T05:20:30.241601Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:20:00Z`
- `2026-09-21T05:20:30.241601Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:19:45Z`
- `2026-09-21T05:19:58.754386Z` — **INDGEN**: 810 rows; marker `2026-09-21T05:16:00Z`
- `2026-09-21T05:19:58.754386Z` — **INDDEM**: 810 rows; marker `2026-09-21T05:16:00Z`
- `2026-09-21T05:19:58.754386Z` — **IMBALNGC**: 810 rows; marker `2026-09-21T05:16:00Z`
- `2026-09-21T05:18:36.808843Z` — **MELNGC**: 810 rows; marker `2026-09-21T05:16:00Z`
- `2026-09-21T05:18:20.610704Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:17:45Z`
- `2026-09-21T05:17:16.844589Z` — **TSDF**: 810 rows; marker `2026-09-21T05:16:00Z`
- `2026-09-21T05:17:16.844589Z` — **NDF**: 45 rows; marker `2026-09-21T05:16:00Z`
- `2026-09-21T05:16:16.504168Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:15:45Z`
- `2026-09-21T05:15:29.021274Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:15:00Z`
- `2026-09-21T05:14:24.899442Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:13:45Z`
- `2026-09-21T05:12:20.955026Z` — **MID**: 2 rows; marker `2026-09-21T05:12:04Z`
