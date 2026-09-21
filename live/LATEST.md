# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T18:47:34.930015Z`  
Current process started UTC: `2026-09-21T18:43:34.768265Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3818, delta=30, z=4.83 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=0, z=6.50 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3788, delta=12, z=4.81 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=0, z=6.57 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3776, delta=86, z=4.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=0, z=6.65 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3501, delta=347, z=4.61 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=244, delta=2, z=7.87 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3690, delta=6, z=4.71 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=0, z=6.73 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3684, delta=165, z=4.73 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=0, z=6.81 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3519, delta=91, z=4.49 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=-14, z=6.90 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3428, delta=66, z=4.36 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1912, 2026-09-21T18:45:42.272779Z)
- `FUELINST|fuelType=OTHER|generation` = **3818** (n=1912, 2026-09-21T18:45:42.272779Z)
- `FUELINST|fuelType=PS|generation` = **601** (n=1912, 2026-09-21T18:45:42.272779Z)
- `FUELINST|fuelType=WIND|generation` = **3716** (n=1912, 2026-09-21T18:45:42.272779Z)
- `IMBALNGC|TOTAL|imbalance` = **-3124** (n=314, 2026-09-21T18:22:30.919860Z)
- `INDDEM|TOTAL|demand` = **-12280** (n=314, 2026-09-21T18:22:30.919860Z)
- `INDGEN|TOTAL|generation` = **18335** (n=314, 2026-09-21T18:22:30.919860Z)
- `MELNGC|TOTAL|margin` = **36192** (n=314, 2026-09-21T18:19:48.542412Z)
- `MID|dataProvider=APXMIDP|price` = **201.97** (n=55, 2026-09-21T18:42:15.280103Z)
- `MID|dataProvider=APXMIDP|volume` = **3535.5** (n=55, 2026-09-21T18:42:15.280103Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=108, 2026-09-21T18:42:15.280103Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=108, 2026-09-21T18:42:15.280103Z)
- `NDF|TOTAL|demand` = **20959** (n=321, 2026-09-21T18:17:40.596813Z)
- `TSDF|TOTAL|demand` = **21459** (n=321, 2026-09-21T18:17:40.596813Z)
- `WINDFOR|TOTAL|generation` = **8620** (n=54, 2026-09-21T16:30:47.714491Z)

## Latest publication events

- `2026-09-21T18:46:30.028255Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:45:45Z`
- `2026-09-21T18:45:42.272779Z` — **FUELINST**: 80 rows; marker `2026-09-21T18:45:00Z`
- `2026-09-21T18:44:22.829119Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:43:45Z`
- `2026-09-21T18:42:30.724767Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:41:45Z`
- `2026-09-21T18:42:15.280103Z` — **MID**: 2 rows; marker `2026-09-21T18:42:03Z`
- `2026-09-21T18:40:39.638115Z` — **FUELINST**: 80 rows; marker `2026-09-21T18:40:00Z`
- `2026-09-21T18:40:24.147494Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:39:45Z`
- `2026-09-21T18:38:19.689225Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:37:45Z`
- `2026-09-21T18:36:27.606848Z` — **MID**: 1 rows; marker `2026-09-21T18:35:00Z`
- `2026-09-21T18:36:27.606848Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:35:45Z`
- `2026-09-21T18:35:39.428498Z` — **FUELINST**: 80 rows; marker `2026-09-21T18:35:00Z`
- `2026-09-21T18:34:26.182432Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:33:45Z`
- `2026-09-21T18:32:17.430066Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:31:45Z`
- `2026-09-21T18:30:41.934344Z` — **FUELHH**: 20 rows; marker `2026-09-21T18:30:00Z`
- `2026-09-21T18:30:41.934344Z` — **FUELINST**: 80 rows; marker `2026-09-21T18:30:00Z`
