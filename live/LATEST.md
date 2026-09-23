# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T11:34:13.878753Z`  
Current process started UTC: `2026-09-23T11:30:13.584920Z`  
1-second metadata polls in this process: **234**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2401, 2026-09-23T11:30:29.330469Z)
- `FUELINST|fuelType=OTHER|generation` = **676** (n=2401, 2026-09-23T11:30:29.330469Z)
- `FUELINST|fuelType=PS|generation` = **-749** (n=2401, 2026-09-23T11:30:29.330469Z)
- `FUELINST|fuelType=WIND|generation` = **9694** (n=2401, 2026-09-23T11:30:29.330469Z)
- `IMBALNGC|TOTAL|imbalance` = **139** (n=394, 2026-09-23T11:23:03.248772Z)
- `INDDEM|TOTAL|demand` = **-12229** (n=394, 2026-09-23T11:22:47.078698Z)
- `INDGEN|TOTAL|generation` = **20192** (n=394, 2026-09-23T11:23:03.248772Z)
- `MELNGC|TOTAL|margin` = **38966** (n=394, 2026-09-23T11:20:22.745782Z)
- `MID|dataProvider=APXMIDP|price` = **129.77** (n=136, 2026-09-23T11:12:18.484872Z)
- `MID|dataProvider=APXMIDP|volume` = **4217.3** (n=136, 2026-09-23T11:12:18.484872Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=268, 2026-09-23T11:12:18.484872Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=268, 2026-09-23T11:12:18.484872Z)
- `NDF|TOTAL|demand` = **19553** (n=403, 2026-09-23T11:18:01.132792Z)
- `TSDF|TOTAL|demand` = **20053** (n=403, 2026-09-23T11:18:01.132792Z)
- `WINDFOR|TOTAL|generation` = **7178** (n=68, 2026-09-23T10:30:38.458402Z)

## Latest publication events

- `2026-09-23T11:32:21.354281Z` — **FREQ**: 5761 rows; marker `2026-09-23T11:31:45Z`
- `2026-09-23T11:30:45.548320Z` — **FUELHH**: 20 rows; marker `2026-09-23T11:30:00Z`
- `2026-09-23T11:30:29.330469Z` — **FUELINST**: 80 rows; marker `2026-09-23T11:30:00Z`
- `2026-09-23T11:30:13.584930Z` — **FREQ**: 5761 rows; marker `2026-09-23T11:29:45Z`
- `2026-09-23T11:28:19.062741Z` — **FREQ**: 5761 rows; marker `2026-09-23T11:27:45Z`
- `2026-09-23T11:26:26.839689Z` — **FREQ**: 5761 rows; marker `2026-09-23T11:25:45Z`
- `2026-09-23T11:25:27.449895Z` — **FUELINST**: 80 rows; marker `2026-09-23T11:25:00Z`
- `2026-09-23T11:24:23.834805Z` — **FREQ**: 5761 rows; marker `2026-09-23T11:23:45Z`
- `2026-09-23T11:23:03.248772Z` — **INDGEN**: 1458 rows; marker `2026-09-23T11:17:00Z`
- `2026-09-23T11:23:03.248772Z` — **IMBALNGC**: 1458 rows; marker `2026-09-23T11:17:00Z`
- `2026-09-23T11:22:47.078698Z` — **INDDEM**: 1458 rows; marker `2026-09-23T11:17:00Z`
- `2026-09-23T11:22:15.428781Z` — **FREQ**: 5761 rows; marker `2026-09-23T11:21:45Z`
- `2026-09-23T11:20:39.250607Z` — **FUELINST**: 80 rows; marker `2026-09-23T11:20:00Z`
- `2026-09-23T11:20:22.745782Z` — **MELNGC**: 1458 rows; marker `2026-09-23T11:17:00Z`
- `2026-09-23T11:20:22.745782Z` — **FREQ**: 5761 rows; marker `2026-09-23T11:19:45Z`
