# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T17:38:44.715413Z`  
Current process started UTC: `2026-09-21T17:34:44.270600Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3091, delta=123, z=3.96 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=200, delta=76, z=6.93 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3507, delta=-5, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=CCGT` `generation` — instantaneous generation mix [fuelType=CCGT] generation: value=13992, delta=-13, z=3.65 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=2796, delta=1098, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3509, delta=3, z=3.61 -> generation-mix component moved
- **FUELHH** `fuelType=CCGT` `generation` — half-hour generation mix [fuelType=CCGT] generation: value=13661, delta=377, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2968, delta=26, z=3.77 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=124, delta=14, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3512, delta=0, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=CCGT` `generation` — instantaneous generation mix [fuelType=CCGT] generation: value=14005, delta=24, z=3.67 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2942, delta=-55, z=3.74 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=110, delta=0, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3512, delta=4, z=3.65 -> generation-mix component moved
- **FUELINST** `fuelType=CCGT` `generation` — instantaneous generation mix [fuelType=CCGT] generation: value=13981, delta=322, z=3.67 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1898, 2026-09-21T17:35:32.277370Z)
- `FUELINST|fuelType=OTHER|generation` = **3091** (n=1898, 2026-09-21T17:35:32.277370Z)
- `FUELINST|fuelType=PS|generation` = **536** (n=1898, 2026-09-21T17:35:32.277370Z)
- `FUELINST|fuelType=WIND|generation` = **3453** (n=1898, 2026-09-21T17:35:32.277370Z)
- `IMBALNGC|TOTAL|imbalance` = **-3018** (n=312, 2026-09-21T17:23:25.129882Z)
- `INDDEM|TOTAL|demand` = **-12280** (n=312, 2026-09-21T17:23:09.185836Z)
- `INDGEN|TOTAL|generation` = **18441** (n=312, 2026-09-21T17:23:09.185836Z)
- `MELNGC|TOTAL|margin` = **36168** (n=312, 2026-09-21T17:20:29.849386Z)
- `MID|dataProvider=APXMIDP|price` = **207.07** (n=52, 2026-09-21T17:12:20.269195Z)
- `MID|dataProvider=APXMIDP|volume` = **3426** (n=52, 2026-09-21T17:12:20.269195Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=103, 2026-09-21T17:37:24.256333Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=103, 2026-09-21T17:37:24.256333Z)
- `NDF|TOTAL|demand` = **20959** (n=319, 2026-09-21T17:18:22.758203Z)
- `TSDF|TOTAL|demand` = **21459** (n=319, 2026-09-21T17:18:22.758203Z)
- `WINDFOR|TOTAL|generation` = **8620** (n=54, 2026-09-21T16:30:47.714491Z)

## Latest publication events

- `2026-09-21T17:38:27.672474Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:37:45Z`
- `2026-09-21T17:37:24.256333Z` — **MID**: 1 rows; marker `2026-09-21T17:35:00Z`
- `2026-09-21T17:36:19.942577Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:35:45Z`
- `2026-09-21T17:35:32.277370Z` — **FUELINST**: 80 rows; marker `2026-09-21T17:35:00Z`
- `2026-09-21T17:34:15.817303Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:33:45Z`
- `2026-09-21T17:32:23.017823Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:31:45Z`
- `2026-09-21T17:30:30.722887Z` — **FUELHH**: 20 rows; marker `2026-09-21T17:30:00Z`
- `2026-09-21T17:30:30.722887Z` — **FUELINST**: 80 rows; marker `2026-09-21T17:30:00Z`
- `2026-09-21T17:30:30.722887Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:29:45Z`
- `2026-09-21T17:28:26.404450Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:27:45Z`
- `2026-09-21T17:26:18.167198Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:25:45Z`
- `2026-09-21T17:25:33.412031Z` — **FUELINST**: 80 rows; marker `2026-09-21T17:25:00Z`
- `2026-09-21T17:24:29.060516Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:23:45Z`
- `2026-09-21T17:23:25.129882Z` — **IMBALNGC**: 1242 rows; marker `2026-09-21T17:17:00Z`
- `2026-09-21T17:23:09.185836Z` — **INDGEN**: 1242 rows; marker `2026-09-21T17:17:00Z`
