# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T11:00:26.367353Z`  
Current process started UTC: `2026-09-23T10:56:24.218457Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=COAL` `generation` — half-hour generation mix [fuelType=COAL] generation: value=0, delta=-133, z=-0.05 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3187, delta=-614, z=-1.49 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=772, delta=-9447, z=-0.02 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=0, delta=-871, z=-0.35 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3202, delta=1895, z=-1.32 -> generation-mix component moved
- **FUELINST** `fuelType=COAL` `generation` — instantaneous generation mix [fuelType=COAL] generation: value=0, delta=-795, z=-0.02 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=10219, delta=9339, z=13.89 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=871, delta=871, z=11.02 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=1307, delta=-2493, z=-13.96 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=165, delta=-434, z=1.76 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=437, delta=-153, z=5.21 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3204, delta=-351, z=3.66 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=599, delta=-36, z=7.95 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=0, z=7.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=0, z=7.34 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2395, 2026-09-23T11:00:24.038066Z)
- `FUELINST|fuelType=OTHER|generation` = **959** (n=2395, 2026-09-23T11:00:24.038066Z)
- `FUELINST|fuelType=PS|generation` = **-743** (n=2395, 2026-09-23T11:00:24.038066Z)
- `FUELINST|fuelType=WIND|generation` = **9496** (n=2395, 2026-09-23T11:00:24.038066Z)
- `IMBALNGC|TOTAL|imbalance` = **179** (n=393, 2026-09-23T10:53:33.246798Z)
- `INDDEM|TOTAL|demand` = **-12225** (n=393, 2026-09-23T10:53:17.675971Z)
- `INDGEN|TOTAL|generation` = **20232** (n=393, 2026-09-23T10:53:17.675971Z)
- `MELNGC|TOTAL|margin` = **38936** (n=393, 2026-09-23T10:50:36.303746Z)
- `MID|dataProvider=APXMIDP|price` = **114.86** (n=135, 2026-09-23T10:42:15.276456Z)
- `MID|dataProvider=APXMIDP|volume` = **4109** (n=135, 2026-09-23T10:42:15.276456Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=266, 2026-09-23T10:42:15.276456Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=266, 2026-09-23T10:42:15.276456Z)
- `NDF|TOTAL|demand` = **19553** (n=402, 2026-09-23T10:48:13.307241Z)
- `TSDF|TOTAL|demand` = **20053** (n=402, 2026-09-23T10:48:13.307241Z)
- `WINDFOR|TOTAL|generation` = **7178** (n=68, 2026-09-23T10:30:38.458402Z)

## Latest publication events

- `2026-09-23T11:00:24.038066Z` — **FUELINST**: 80 rows; marker `2026-09-23T11:00:00Z`
- `2026-09-23T11:00:08.486597Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:59:45Z`
- `2026-09-23T10:58:15.663413Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:57:45Z`
- `2026-09-23T10:56:24.218466Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:55:45Z`
- `2026-09-23T10:55:25.216933Z` — **FUELINST**: 80 rows; marker `2026-09-23T10:55:00Z`
- `2026-09-23T10:54:04.915422Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:53:45Z`
- `2026-09-23T10:53:33.246798Z` — **IMBALNGC**: 1476 rows; marker `2026-09-23T10:47:00Z`
- `2026-09-23T10:53:17.675971Z` — **INDGEN**: 1476 rows; marker `2026-09-23T10:47:00Z`
- `2026-09-23T10:53:17.675971Z` — **INDDEM**: 1476 rows; marker `2026-09-23T10:47:00Z`
- `2026-09-23T10:52:12.516548Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:51:45Z`
- `2026-09-23T10:50:36.303746Z` — **MELNGC**: 1476 rows; marker `2026-09-23T10:47:00Z`
- `2026-09-23T10:50:36.303746Z` — **FUELINST**: 80 rows; marker `2026-09-23T10:50:00Z`
- `2026-09-23T10:50:04.748298Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:49:45Z`
- `2026-09-23T10:48:29.268645Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:47:45Z`
- `2026-09-23T10:48:13.307241Z` — **TSDF**: 1476 rows; marker `2026-09-23T10:47:00Z`
