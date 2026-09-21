# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T18:26:30.664270Z`  
Current process started UTC: `2026-09-21T18:22:30.919850Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3684, delta=165, z=4.73 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=0, z=6.81 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3519, delta=91, z=4.49 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=-14, z=6.90 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3428, delta=66, z=4.36 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=244, delta=-24, z=7.47 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3362, delta=41, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=268, delta=8, z=8.42 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3514, delta=4, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3321, delta=-49, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=260, delta=13, z=8.30 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3510, delta=2, z=3.50 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3154, delta=358, z=4.14 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=242, delta=155, z=8.69 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3508, delta=-1, z=3.52 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1908, 2026-09-21T18:25:27.802241Z)
- `FUELINST|fuelType=OTHER|generation` = **3684** (n=1908, 2026-09-21T18:25:27.802241Z)
- `FUELINST|fuelType=PS|generation` = **595** (n=1908, 2026-09-21T18:25:27.802241Z)
- `FUELINST|fuelType=WIND|generation` = **3698** (n=1908, 2026-09-21T18:25:27.802241Z)
- `IMBALNGC|TOTAL|imbalance` = **-3124** (n=314, 2026-09-21T18:22:30.919860Z)
- `INDDEM|TOTAL|demand` = **-12280** (n=314, 2026-09-21T18:22:30.919860Z)
- `INDGEN|TOTAL|generation` = **18335** (n=314, 2026-09-21T18:22:30.919860Z)
- `MELNGC|TOTAL|margin` = **36192** (n=314, 2026-09-21T18:19:48.542412Z)
- `MID|dataProvider=APXMIDP|price` = **205.18** (n=54, 2026-09-21T18:12:21.794388Z)
- `MID|dataProvider=APXMIDP|volume` = **3558.6** (n=54, 2026-09-21T18:12:21.794388Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=106, 2026-09-21T18:12:21.794388Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=106, 2026-09-21T18:12:21.794388Z)
- `NDF|TOTAL|demand` = **20959** (n=321, 2026-09-21T18:17:40.596813Z)
- `TSDF|TOTAL|demand` = **21459** (n=321, 2026-09-21T18:17:40.596813Z)
- `WINDFOR|TOTAL|generation` = **8620** (n=54, 2026-09-21T16:30:47.714491Z)

## Latest publication events

- `2026-09-21T18:26:15.818355Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:25:45Z`
- `2026-09-21T18:25:27.802241Z` — **FUELINST**: 80 rows; marker `2026-09-21T18:25:00Z`
- `2026-09-21T18:24:24.366872Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:23:45Z`
- `2026-09-21T18:22:30.919860Z` — **INDGEN**: 1206 rows; marker `2026-09-21T18:17:00Z`
- `2026-09-21T18:22:30.919860Z` — **INDDEM**: 1206 rows; marker `2026-09-21T18:17:00Z`
- `2026-09-21T18:22:30.919860Z` — **IMBALNGC**: 1206 rows; marker `2026-09-21T18:17:00Z`
- `2026-09-21T18:22:30.919860Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:21:45Z`
- `2026-09-21T18:20:36.707206Z` — **FUELINST**: 80 rows; marker `2026-09-21T18:20:00Z`
- `2026-09-21T18:20:20.446918Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:19:45Z`
- `2026-09-21T18:19:48.542412Z` — **MELNGC**: 1206 rows; marker `2026-09-21T18:17:00Z`
- `2026-09-21T18:18:12.177176Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:17:45Z`
- `2026-09-21T18:17:40.596813Z` — **TSDF**: 1206 rows; marker `2026-09-21T18:17:00Z`
- `2026-09-21T18:17:40.596813Z` — **NDF**: 67 rows; marker `2026-09-21T18:17:00Z`
- `2026-09-21T18:16:24.536063Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:15:45Z`
- `2026-09-21T18:15:37.138430Z` — **FUELINST**: 80 rows; marker `2026-09-21T18:15:00Z`
