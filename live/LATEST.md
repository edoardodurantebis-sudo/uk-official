# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T20:42:31.710079Z`  
Current process started UTC: `2026-09-22T20:38:31.449608Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2223, 2026-09-22T20:40:26.980826Z)
- `FUELINST|fuelType=OTHER|generation` = **737** (n=2223, 2026-09-22T20:40:26.980826Z)
- `FUELINST|fuelType=PS|generation` = **139** (n=2223, 2026-09-22T20:40:26.980826Z)
- `FUELINST|fuelType=WIND|generation` = **2252** (n=2223, 2026-09-22T20:40:26.980826Z)
- `IMBALNGC|TOTAL|imbalance` = **-8038** (n=365, 2026-09-22T20:21:48.728628Z)
- `INDDEM|TOTAL|demand` = **-12478** (n=365, 2026-09-22T20:21:32.613808Z)
- `INDGEN|TOTAL|generation` = **13135** (n=365, 2026-09-22T20:21:32.613808Z)
- `MELNGC|TOTAL|margin` = **37132** (n=365, 2026-09-22T20:19:30.714418Z)
- `MID|dataProvider=APXMIDP|price` = **172.15** (n=107, 2026-09-22T20:42:19.623301Z)
- `MID|dataProvider=APXMIDP|volume` = **4165.1** (n=107, 2026-09-22T20:42:19.623301Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=212, 2026-09-22T20:42:19.623301Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=212, 2026-09-22T20:42:19.623301Z)
- `NDF|TOTAL|demand` = **20673** (n=373, 2026-09-22T20:17:39.195882Z)
- `TSDF|TOTAL|demand` = **21173** (n=373, 2026-09-22T20:17:39.195882Z)
- `WINDFOR|TOTAL|generation` = **13612** (n=63, 2026-09-22T19:30:53.095849Z)

## Latest publication events

- `2026-09-22T20:42:19.623301Z` — **MID**: 2 rows; marker `2026-09-22T20:42:03Z`
- `2026-09-22T20:42:19.623301Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:41:45Z`
- `2026-09-22T20:40:26.980826Z` — **FUELINST**: 80 rows; marker `2026-09-22T20:40:00Z`
- `2026-09-22T20:40:11.462085Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:39:45Z`
- `2026-09-22T20:38:19.986640Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:37:45Z`
- `2026-09-22T20:36:28.051746Z` — **MID**: 1 rows; marker `2026-09-22T20:35:00Z`
- `2026-09-22T20:36:12.139215Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:35:45Z`
- `2026-09-22T20:35:24.000811Z` — **FUELINST**: 80 rows; marker `2026-09-22T20:35:00Z`
- `2026-09-22T20:34:20.060155Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:33:45Z`
- `2026-09-22T20:32:14.568750Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:31:45Z`
- `2026-09-22T20:30:38.110004Z` — **FUELHH**: 20 rows; marker `2026-09-22T20:30:00Z`
- `2026-09-22T20:30:21.822699Z` — **FUELINST**: 80 rows; marker `2026-09-22T20:30:00Z`
- `2026-09-22T20:30:06.013591Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:29:45Z`
- `2026-09-22T20:28:13.197021Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:27:45Z`
- `2026-09-22T20:26:05.347179Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:25:45Z`
