# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T19:04:23.645774Z`  
Current process started UTC: `2026-09-21T19:00:24.266854Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3738, delta=237, z=4.84 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=230, delta=-14, z=6.75 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3544, delta=-139, z=4.31 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=0, z=6.29 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3683, delta=-137, z=4.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=0, z=6.36 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3820, delta=2, z=4.80 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=0, z=6.42 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3818, delta=30, z=4.83 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=0, z=6.50 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3788, delta=12, z=4.81 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=0, z=6.57 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3776, delta=86, z=4.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=0, z=6.65 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3501, delta=347, z=4.61 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1915, 2026-09-21T19:00:24.266861Z)
- `FUELINST|fuelType=OTHER|generation` = **3544** (n=1915, 2026-09-21T19:00:24.266861Z)
- `FUELINST|fuelType=PS|generation` = **601** (n=1915, 2026-09-21T19:00:24.266861Z)
- `FUELINST|fuelType=WIND|generation` = **3665** (n=1915, 2026-09-21T19:00:24.266861Z)
- `IMBALNGC|TOTAL|imbalance` = **-3084** (n=315, 2026-09-21T18:52:32.457569Z)
- `INDDEM|TOTAL|demand` = **-12280** (n=315, 2026-09-21T18:52:16.710828Z)
- `INDGEN|TOTAL|generation` = **18375** (n=315, 2026-09-21T18:52:16.710828Z)
- `MELNGC|TOTAL|margin` = **36132** (n=315, 2026-09-21T18:49:57.407200Z)
- `MID|dataProvider=APXMIDP|price` = **201.97** (n=55, 2026-09-21T18:42:15.280103Z)
- `MID|dataProvider=APXMIDP|volume` = **3535.5** (n=55, 2026-09-21T18:42:15.280103Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=108, 2026-09-21T18:42:15.280103Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=108, 2026-09-21T18:42:15.280103Z)
- `NDF|TOTAL|demand` = **20959** (n=322, 2026-09-21T18:47:49.021462Z)
- `TSDF|TOTAL|demand` = **21459** (n=322, 2026-09-21T18:47:49.021462Z)
- `WINDFOR|TOTAL|generation` = **8620** (n=54, 2026-09-21T16:30:47.714491Z)

## Latest publication events

- `2026-09-21T19:02:16.810976Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:01:45Z`
- `2026-09-21T19:00:56.173359Z` — **FUELHH**: 20 rows; marker `2026-09-21T19:00:00Z`
- `2026-09-21T19:00:24.266861Z` — **FUELINST**: 80 rows; marker `2026-09-21T19:00:00Z`
- `2026-09-21T19:00:24.266861Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:59:45Z`
- `2026-09-21T18:58:07.371459Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:57:45Z`
- `2026-09-21T18:56:15.810981Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:55:45Z`
- `2026-09-21T18:55:28.184371Z` — **FUELINST**: 80 rows; marker `2026-09-21T18:55:00Z`
- `2026-09-21T18:54:08.544624Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:53:45Z`
- `2026-09-21T18:52:32.457569Z` — **IMBALNGC**: 1188 rows; marker `2026-09-21T18:47:00Z`
- `2026-09-21T18:52:16.710828Z` — **INDGEN**: 1188 rows; marker `2026-09-21T18:47:00Z`
- `2026-09-21T18:52:16.710828Z` — **INDDEM**: 1188 rows; marker `2026-09-21T18:47:00Z`
- `2026-09-21T18:52:16.710828Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:51:45Z`
- `2026-09-21T18:50:29.251144Z` — **FUELINST**: 80 rows; marker `2026-09-21T18:50:00Z`
- `2026-09-21T18:50:29.251144Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:49:45Z`
- `2026-09-21T18:49:57.407200Z` — **MELNGC**: 1188 rows; marker `2026-09-21T18:47:00Z`
