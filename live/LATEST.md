# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T10:51:57.810318Z`  
Current process started UTC: `2026-09-23T10:47:57.744430Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2393, 2026-09-23T10:50:36.303746Z)
- `FUELINST|fuelType=OTHER|generation` = **929** (n=2393, 2026-09-23T10:50:36.303746Z)
- `FUELINST|fuelType=PS|generation` = **-860** (n=2393, 2026-09-23T10:50:36.303746Z)
- `FUELINST|fuelType=WIND|generation` = **9573** (n=2393, 2026-09-23T10:50:36.303746Z)
- `IMBALNGC|TOTAL|imbalance` = **-2300** (n=392, 2026-09-23T10:19:00.590799Z)
- `INDDEM|TOTAL|demand` = **-13737** (n=392, 2026-09-23T10:19:00.590799Z)
- `INDGEN|TOTAL|generation` = **18728** (n=392, 2026-09-23T10:19:00.590799Z)
- `MELNGC|TOTAL|margin` = **38936** (n=393, 2026-09-23T10:50:36.303746Z)
- `MID|dataProvider=APXMIDP|price` = **114.86** (n=135, 2026-09-23T10:42:15.276456Z)
- `MID|dataProvider=APXMIDP|volume` = **4109** (n=135, 2026-09-23T10:42:15.276456Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=266, 2026-09-23T10:42:15.276456Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=266, 2026-09-23T10:42:15.276456Z)
- `NDF|TOTAL|demand` = **19553** (n=402, 2026-09-23T10:48:13.307241Z)
- `TSDF|TOTAL|demand` = **20053** (n=402, 2026-09-23T10:48:13.307241Z)
- `WINDFOR|TOTAL|generation` = **7178** (n=68, 2026-09-23T10:30:38.458402Z)

## Latest publication events

- `2026-09-23T10:50:36.303746Z` — **MELNGC**: 1476 rows; marker `2026-09-23T10:47:00Z`
- `2026-09-23T10:50:36.303746Z` — **FUELINST**: 80 rows; marker `2026-09-23T10:50:00Z`
- `2026-09-23T10:50:04.748298Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:49:45Z`
- `2026-09-23T10:48:29.268645Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:47:45Z`
- `2026-09-23T10:48:13.307241Z` — **TSDF**: 1476 rows; marker `2026-09-23T10:47:00Z`
- `2026-09-23T10:48:13.307241Z` — **NDF**: 82 rows; marker `2026-09-23T10:47:00Z`
- `2026-09-23T10:46:26.050379Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:45:45Z`
- `2026-09-23T10:45:38.523605Z` — **FUELINST**: 80 rows; marker `2026-09-23T10:45:00Z`
- `2026-09-23T10:44:18.945263Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:43:45Z`
- `2026-09-23T10:42:15.276456Z` — **MID**: 2 rows; marker `2026-09-23T10:42:03Z`
- `2026-09-23T10:42:15.276456Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:41:45Z`
- `2026-09-23T10:40:39.664193Z` — **FUELINST**: 80 rows; marker `2026-09-23T10:40:00Z`
- `2026-09-23T10:40:23.434020Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:39:45Z`
- `2026-09-23T10:38:15.430543Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:37:45Z`
- `2026-09-23T10:36:23.440055Z` — **MID**: 1 rows; marker `2026-09-23T10:35:00Z`
