# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T00:29:55.138018Z`  
Current process started UTC: `2026-09-23T00:25:54.954350Z`  
1-second metadata polls in this process: **239**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2268, 2026-09-23T00:25:54.954358Z)
- `FUELINST|fuelType=OTHER|generation` = **178** (n=2268, 2026-09-23T00:25:54.954358Z)
- `FUELINST|fuelType=PS|generation` = **147** (n=2268, 2026-09-23T00:25:54.954358Z)
- `FUELINST|fuelType=WIND|generation` = **4143** (n=2268, 2026-09-23T00:25:54.954358Z)
- `IMBALNGC|TOTAL|imbalance` = **-8007** (n=373, 2026-09-23T00:20:57.638996Z)
- `INDDEM|TOTAL|demand` = **-12484** (n=373, 2026-09-23T00:20:42.260653Z)
- `INDGEN|TOTAL|generation` = **13166** (n=373, 2026-09-23T00:20:42.260653Z)
- `MELNGC|TOTAL|margin` = **37230** (n=373, 2026-09-23T00:19:06.512628Z)
- `MID|dataProvider=APXMIDP|price` = **149.47** (n=114, 2026-09-23T00:12:18.807483Z)
- `MID|dataProvider=APXMIDP|volume` = **2227.9** (n=114, 2026-09-23T00:12:18.807483Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=224, 2026-09-23T00:12:18.807483Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=224, 2026-09-23T00:12:18.807483Z)
- `NDF|TOTAL|demand` = **20673** (n=381, 2026-09-23T00:17:31.420225Z)
- `TSDF|TOTAL|demand` = **21173** (n=381, 2026-09-23T00:17:31.420225Z)
- `WINDFOR|TOTAL|generation` = **13770** (n=64, 2026-09-22T23:30:32.481751Z)

## Latest publication events

- `2026-09-23T00:28:02.507627Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:27:45Z`
- `2026-09-23T00:26:10.972194Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:25:45Z`
- `2026-09-23T00:25:54.954358Z` — **FUELINST**: 80 rows; marker `2026-09-23T00:25:00Z`
- `2026-09-23T00:24:09.899794Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:23:45Z`
- `2026-09-23T00:22:01.895985Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:21:45Z`
- `2026-09-23T00:20:57.638996Z` — **IMBALNGC**: 990 rows; marker `2026-09-23T00:17:00Z`
- `2026-09-23T00:20:42.260653Z` — **INDGEN**: 990 rows; marker `2026-09-23T00:17:00Z`
- `2026-09-23T00:20:42.260653Z` — **INDDEM**: 990 rows; marker `2026-09-23T00:17:00Z`
- `2026-09-23T00:20:42.260653Z` — **FUELINST**: 80 rows; marker `2026-09-23T00:20:00Z`
- `2026-09-23T00:20:26.763365Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:19:45Z`
- `2026-09-23T00:19:06.512628Z` — **MELNGC**: 990 rows; marker `2026-09-23T00:17:00Z`
- `2026-09-23T00:18:19.029763Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:17:45Z`
- `2026-09-23T00:17:31.420225Z` — **TSDF**: 990 rows; marker `2026-09-23T00:17:00Z`
- `2026-09-23T00:17:31.420225Z` — **NDF**: 55 rows; marker `2026-09-23T00:17:00Z`
- `2026-09-23T00:16:19.941729Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:15:45Z`
