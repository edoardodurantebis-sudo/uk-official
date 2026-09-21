# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T04:55:57.600791Z`  
Current process started UTC: `2026-09-21T04:51:58.242907Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2894, delta=-83, z=3.94 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2977, delta=12, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2965, delta=268, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2697, delta=209, z=3.64 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1749, 2026-09-21T04:55:42.053932Z)
- `FUELINST|fuelType=OTHER|generation` = **282** (n=1749, 2026-09-21T04:55:42.053932Z)
- `FUELINST|fuelType=PS|generation` = **-249** (n=1749, 2026-09-21T04:55:42.053932Z)
- `FUELINST|fuelType=WIND|generation` = **4266** (n=1749, 2026-09-21T04:55:42.053932Z)
- `IMBALNGC|TOTAL|imbalance` = **-4036** (n=288, 2026-09-21T04:50:43.860654Z)
- `INDDEM|TOTAL|demand` = **-11743** (n=288, 2026-09-21T04:50:27.923724Z)
- `INDGEN|TOTAL|generation` = **16574** (n=288, 2026-09-21T04:50:43.860654Z)
- `MELNGC|TOTAL|margin` = **37535** (n=288, 2026-09-21T04:49:24.362460Z)
- `MID|dataProvider=APXMIDP|price` = **157** (n=27, 2026-09-21T04:42:13.305203Z)
- `MID|dataProvider=APXMIDP|volume` = **2759.6** (n=27, 2026-09-21T04:42:13.305203Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=54, 2026-09-21T04:42:13.305203Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=54, 2026-09-21T04:42:13.305203Z)
- `NDF|TOTAL|demand` = **20110** (n=294, 2026-09-21T04:47:47.247919Z)
- `TSDF|TOTAL|demand` = **20610** (n=294, 2026-09-21T04:47:47.247919Z)
- `WINDFOR|TOTAL|generation` = **8021** (n=49, 2026-09-21T03:30:39.847119Z)

## Latest publication events

- `2026-09-21T04:55:42.053932Z` — **FUELINST**: 80 rows; marker `2026-09-21T04:55:00Z`
- `2026-09-21T04:54:22.401253Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:53:45Z`
- `2026-09-21T04:52:14.244974Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:51:45Z`
- `2026-09-21T04:50:43.860654Z` — **INDGEN**: 828 rows; marker `2026-09-21T04:47:00Z`
- `2026-09-21T04:50:43.860654Z` — **IMBALNGC**: 828 rows; marker `2026-09-21T04:47:00Z`
- `2026-09-21T04:50:27.923724Z` — **INDDEM**: 828 rows; marker `2026-09-21T04:47:00Z`
- `2026-09-21T04:50:27.923724Z` — **FUELINST**: 80 rows; marker `2026-09-21T04:50:00Z`
- `2026-09-21T04:50:27.923724Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:49:45Z`
- `2026-09-21T04:49:24.362460Z` — **MELNGC**: 828 rows; marker `2026-09-21T04:47:00Z`
- `2026-09-21T04:48:02.568204Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:47:45Z`
- `2026-09-21T04:47:47.247919Z` — **TSDF**: 828 rows; marker `2026-09-21T04:47:00Z`
- `2026-09-21T04:47:47.247919Z` — **NDF**: 46 rows; marker `2026-09-21T04:47:00Z`
- `2026-09-21T04:46:12.669436Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:45:45Z`
- `2026-09-21T04:45:40.922541Z` — **FUELINST**: 80 rows; marker `2026-09-21T04:45:00Z`
- `2026-09-21T04:44:19.431563Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:43:45Z`
