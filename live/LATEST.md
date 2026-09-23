# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T11:51:08.080577Z`  
Current process started UTC: `2026-09-23T11:47:07.856888Z`  
1-second metadata polls in this process: **232**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2405, 2026-09-23T11:50:21.892852Z)
- `FUELINST|fuelType=OTHER|generation` = **784** (n=2405, 2026-09-23T11:50:21.892852Z)
- `FUELINST|fuelType=PS|generation` = **-738** (n=2405, 2026-09-23T11:50:21.892852Z)
- `FUELINST|fuelType=WIND|generation` = **9591** (n=2405, 2026-09-23T11:50:21.892852Z)
- `IMBALNGC|TOTAL|imbalance` = **139** (n=394, 2026-09-23T11:23:03.248772Z)
- `INDDEM|TOTAL|demand` = **-12229** (n=394, 2026-09-23T11:22:47.078698Z)
- `INDGEN|TOTAL|generation` = **20192** (n=394, 2026-09-23T11:23:03.248772Z)
- `MELNGC|TOTAL|margin` = **39012** (n=395, 2026-09-23T11:49:49.770006Z)
- `MID|dataProvider=APXMIDP|price` = **133.93** (n=137, 2026-09-23T11:42:20.991445Z)
- `MID|dataProvider=APXMIDP|volume` = **4587** (n=137, 2026-09-23T11:42:20.991445Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=270, 2026-09-23T11:42:20.991445Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=270, 2026-09-23T11:42:20.991445Z)
- `NDF|TOTAL|demand` = **19553** (n=404, 2026-09-23T11:47:56.125659Z)
- `TSDF|TOTAL|demand` = **20053** (n=404, 2026-09-23T11:47:56.125659Z)
- `WINDFOR|TOTAL|generation` = **7178** (n=68, 2026-09-23T10:30:38.458402Z)

## Latest publication events

- `2026-09-23T11:50:21.892852Z` — **FUELINST**: 80 rows; marker `2026-09-23T11:50:00Z`
- `2026-09-23T11:50:05.071590Z` — **FREQ**: 5761 rows; marker `2026-09-23T11:49:45Z`
- `2026-09-23T11:49:49.770006Z` — **MELNGC**: 1440 rows; marker `2026-09-23T11:47:00Z`
- `2026-09-23T11:48:11.885987Z` — **FREQ**: 5761 rows; marker `2026-09-23T11:47:45Z`
- `2026-09-23T11:47:56.125659Z` — **TSDF**: 1440 rows; marker `2026-09-23T11:47:00Z`
- `2026-09-23T11:47:56.125659Z` — **NDF**: 80 rows; marker `2026-09-23T11:47:00Z`
- `2026-09-23T11:46:06.098957Z` — **FREQ**: 5761 rows; marker `2026-09-23T11:45:45Z`
- `2026-09-23T11:45:34.895938Z` — **FUELINST**: 80 rows; marker `2026-09-23T11:45:00Z`
- `2026-09-23T11:44:13.848992Z` — **FREQ**: 5761 rows; marker `2026-09-23T11:43:45Z`
- `2026-09-23T11:42:20.991445Z` — **MID**: 2 rows; marker `2026-09-23T11:42:03Z`
- `2026-09-23T11:42:04.802025Z` — **FREQ**: 5761 rows; marker `2026-09-23T11:41:45Z`
- `2026-09-23T11:40:45.158415Z` — **FUELINST**: 80 rows; marker `2026-09-23T11:40:00Z`
- `2026-09-23T11:40:29.670783Z` — **FREQ**: 5761 rows; marker `2026-09-23T11:39:45Z`
- `2026-09-23T11:38:38.100844Z` — **FREQ**: 5761 rows; marker `2026-09-23T11:37:45Z`
- `2026-09-23T11:36:18.416648Z` — **MID**: 1 rows; marker `2026-09-23T11:35:00Z`
