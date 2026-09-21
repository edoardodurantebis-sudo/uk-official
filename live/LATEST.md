# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T05:08:37.184218Z`  
Current process started UTC: `2026-09-21T05:04:36.990838Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3376, delta=22, z=4.20 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=994, delta=146, z=3.51 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=2793, delta=365, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2736, delta=-158, z=3.64 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1751, 2026-09-21T05:05:24.615635Z)
- `FUELINST|fuelType=OTHER|generation` = **324** (n=1751, 2026-09-21T05:05:24.615635Z)
- `FUELINST|fuelType=PS|generation` = **-193** (n=1751, 2026-09-21T05:05:24.615635Z)
- `FUELINST|fuelType=WIND|generation` = **4181** (n=1751, 2026-09-21T05:05:24.615635Z)
- `IMBALNGC|TOTAL|imbalance` = **-4036** (n=288, 2026-09-21T04:50:43.860654Z)
- `INDDEM|TOTAL|demand` = **-11743** (n=288, 2026-09-21T04:50:27.923724Z)
- `INDGEN|TOTAL|generation` = **16574** (n=288, 2026-09-21T04:50:43.860654Z)
- `MELNGC|TOTAL|margin` = **37535** (n=288, 2026-09-21T04:49:24.362460Z)
- `MID|dataProvider=APXMIDP|price` = **157** (n=27, 2026-09-21T04:42:13.305203Z)
- `MID|dataProvider=APXMIDP|volume` = **2759.6** (n=27, 2026-09-21T04:42:13.305203Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=55, 2026-09-21T05:06:28.264345Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=55, 2026-09-21T05:06:28.264345Z)
- `NDF|TOTAL|demand` = **20110** (n=294, 2026-09-21T04:47:47.247919Z)
- `TSDF|TOTAL|demand` = **20610** (n=294, 2026-09-21T04:47:47.247919Z)
- `WINDFOR|TOTAL|generation` = **8021** (n=49, 2026-09-21T03:30:39.847119Z)

## Latest publication events

- `2026-09-21T05:08:20.297674Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:07:45Z`
- `2026-09-21T05:06:28.264345Z` — **MID**: 1 rows; marker `2026-09-21T05:05:00Z`
- `2026-09-21T05:06:12.670547Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:05:45Z`
- `2026-09-21T05:05:24.615635Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:05:00Z`
- `2026-09-21T05:04:36.990847Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:03:45Z`
- `2026-09-21T05:02:15.989390Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:01:45Z`
- `2026-09-21T05:00:39.946202Z` — **FUELHH**: 20 rows; marker `2026-09-21T05:00:00Z`
- `2026-09-21T05:00:39.946202Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:00:00Z`
- `2026-09-21T05:00:08.151881Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:59:45Z`
- `2026-09-21T04:58:16.572104Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:57:45Z`
- `2026-09-21T04:56:09.129578Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:55:45Z`
- `2026-09-21T04:55:42.053932Z` — **FUELINST**: 80 rows; marker `2026-09-21T04:55:00Z`
- `2026-09-21T04:54:22.401253Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:53:45Z`
- `2026-09-21T04:52:14.244974Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:51:45Z`
- `2026-09-21T04:50:43.860654Z` — **INDGEN**: 828 rows; marker `2026-09-21T04:47:00Z`
