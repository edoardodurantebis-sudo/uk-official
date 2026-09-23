# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T06:29:10.568704Z`  
Current process started UTC: `2026-09-23T06:25:09.596645Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2340, 2026-09-23T06:25:25.599087Z)
- `FUELINST|fuelType=OTHER|generation` = **2063** (n=2340, 2026-09-23T06:25:25.599087Z)
- `FUELINST|fuelType=PS|generation` = **144** (n=2340, 2026-09-23T06:25:25.599087Z)
- `FUELINST|fuelType=WIND|generation` = **9160** (n=2340, 2026-09-23T06:25:25.599087Z)
- `IMBALNGC|TOTAL|imbalance` = **-7911** (n=385, 2026-09-23T06:20:29.662447Z)
- `INDDEM|TOTAL|demand` = **-12408** (n=385, 2026-09-23T06:20:29.662447Z)
- `INDGEN|TOTAL|generation` = **13260** (n=385, 2026-09-23T06:20:13.501628Z)
- `MELNGC|TOTAL|margin` = **38871** (n=385, 2026-09-23T06:19:09.497492Z)
- `MID|dataProvider=APXMIDP|price` = **165.32** (n=126, 2026-09-23T06:12:32.893369Z)
- `MID|dataProvider=APXMIDP|volume` = **4104.4** (n=126, 2026-09-23T06:12:32.893369Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=248, 2026-09-23T06:12:32.893369Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=248, 2026-09-23T06:12:32.893369Z)
- `NDF|TOTAL|demand` = **20673** (n=393, 2026-09-23T06:17:18.149964Z)
- `TSDF|TOTAL|demand` = **21173** (n=393, 2026-09-23T06:17:18.149964Z)
- `WINDFOR|TOTAL|generation` = **7305** (n=66, 2026-09-23T05:30:43.471788Z)

## Latest publication events

- `2026-09-23T06:28:21.492955Z` — **FREQ**: 5761 rows; marker `2026-09-23T06:27:45Z`
- `2026-09-23T06:26:13.326706Z` — **FREQ**: 5761 rows; marker `2026-09-23T06:25:45Z`
- `2026-09-23T06:25:25.599087Z` — **FUELINST**: 80 rows; marker `2026-09-23T06:25:00Z`
- `2026-09-23T06:24:14.004841Z` — **FREQ**: 5761 rows; marker `2026-09-23T06:23:45Z`
- `2026-09-23T06:22:06.196498Z` — **FREQ**: 5761 rows; marker `2026-09-23T06:21:45Z`
- `2026-09-23T06:20:29.662447Z` — **INDDEM**: 774 rows; marker `2026-09-23T06:16:00Z`
- `2026-09-23T06:20:29.662447Z` — **IMBALNGC**: 774 rows; marker `2026-09-23T06:16:00Z`
- `2026-09-23T06:20:29.662447Z` — **FUELINST**: 80 rows; marker `2026-09-23T06:20:00Z`
- `2026-09-23T06:20:13.501628Z` — **INDGEN**: 774 rows; marker `2026-09-23T06:16:00Z`
- `2026-09-23T06:20:13.501628Z` — **FREQ**: 5761 rows; marker `2026-09-23T06:19:45Z`
- `2026-09-23T06:19:09.497492Z` — **MELNGC**: 774 rows; marker `2026-09-23T06:16:00Z`
- `2026-09-23T06:18:05.848758Z` — **FREQ**: 5761 rows; marker `2026-09-23T06:17:45Z`
- `2026-09-23T06:17:18.149964Z` — **TSDF**: 774 rows; marker `2026-09-23T06:16:00Z`
- `2026-09-23T06:17:18.149964Z` — **NDF**: 43 rows; marker `2026-09-23T06:16:00Z`
- `2026-09-23T06:16:17.725759Z` — **FREQ**: 5761 rows; marker `2026-09-23T06:15:45Z`
