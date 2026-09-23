# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T07:07:06.316107Z`  
Current process started UTC: `2026-09-23T07:03:06.333493Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=165, delta=-434, z=1.76 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=437, delta=-153, z=5.21 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3204, delta=-351, z=3.66 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=599, delta=-36, z=7.95 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=0, z=7.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=0, z=7.34 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3238, delta=-72, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=0, z=7.43 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3310, delta=62, z=3.73 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=-2, z=7.53 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3248, delta=-217, z=3.65 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=592, delta=-48, z=7.65 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3465, delta=-220, z=3.99 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=640, delta=7, z=8.44 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3555, delta=892, z=4.30 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2348, 2026-09-23T07:05:30.189594Z)
- `FUELINST|fuelType=OTHER|generation` = **1047** (n=2348, 2026-09-23T07:05:30.189594Z)
- `FUELINST|fuelType=PS|generation` = **-133** (n=2348, 2026-09-23T07:05:30.189594Z)
- `FUELINST|fuelType=WIND|generation` = **10049** (n=2348, 2026-09-23T07:05:30.189594Z)
- `IMBALNGC|TOTAL|imbalance` = **-7468** (n=386, 2026-09-23T06:50:26.293824Z)
- `INDDEM|TOTAL|demand` = **-12407** (n=386, 2026-09-23T06:49:58.508820Z)
- `INDGEN|TOTAL|generation` = **13705** (n=386, 2026-09-23T06:49:58.508820Z)
- `MELNGC|TOTAL|margin` = **38785** (n=386, 2026-09-23T06:49:10.291588Z)
- `MID|dataProvider=APXMIDP|price` = **177** (n=127, 2026-09-23T06:42:20.420957Z)
- `MID|dataProvider=APXMIDP|volume` = **4199.6** (n=127, 2026-09-23T06:42:20.420957Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=251, 2026-09-23T07:06:17.344544Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=251, 2026-09-23T07:06:17.344544Z)
- `NDF|TOTAL|demand` = **20673** (n=394, 2026-09-23T06:47:18.229649Z)
- `TSDF|TOTAL|demand` = **21173** (n=394, 2026-09-23T06:47:18.229649Z)
- `WINDFOR|TOTAL|generation` = **7305** (n=66, 2026-09-23T05:30:43.471788Z)

## Latest publication events

- `2026-09-23T07:06:17.344544Z` — **MID**: 1 rows; marker `2026-09-23T07:05:00Z`
- `2026-09-23T07:06:01.718522Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:05:45Z`
- `2026-09-23T07:05:30.189594Z` — **FUELINST**: 80 rows; marker `2026-09-23T07:05:00Z`
- `2026-09-23T07:04:10.610480Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:03:45Z`
- `2026-09-23T07:02:06.570234Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:01:45Z`
- `2026-09-23T07:00:45.591966Z` — **FUELHH**: 20 rows; marker `2026-09-23T07:00:00Z`
- `2026-09-23T07:00:45.591966Z` — **FUELINST**: 80 rows; marker `2026-09-23T07:00:00Z`
- `2026-09-23T07:00:13.380531Z` — **FREQ**: 5761 rows; marker `2026-09-23T06:59:45Z`
- `2026-09-23T06:58:25.376627Z` — **FREQ**: 5761 rows; marker `2026-09-23T06:57:45Z`
- `2026-09-23T06:56:17.475635Z` — **FREQ**: 5761 rows; marker `2026-09-23T06:55:45Z`
- `2026-09-23T06:55:45.167911Z` — **FUELINST**: 80 rows; marker `2026-09-23T06:55:00Z`
- `2026-09-23T06:54:24.906615Z` — **FREQ**: 5761 rows; marker `2026-09-23T06:53:45Z`
- `2026-09-23T06:52:17.315704Z` — **FREQ**: 5761 rows; marker `2026-09-23T06:51:45Z`
- `2026-09-23T06:50:41.879662Z` — **FUELINST**: 80 rows; marker `2026-09-23T06:50:00Z`
- `2026-09-23T06:50:26.293824Z` — **IMBALNGC**: 756 rows; marker `2026-09-23T06:46:00Z`
