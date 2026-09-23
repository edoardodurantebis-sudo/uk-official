# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T05:59:43.982876Z`  
Current process started UTC: `2026-09-23T05:55:43.557513Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2334, 2026-09-23T05:55:43.557522Z)
- `FUELINST|fuelType=OTHER|generation` = **1694** (n=2334, 2026-09-23T05:55:43.557522Z)
- `FUELINST|fuelType=PS|generation` = **-8** (n=2334, 2026-09-23T05:55:43.557522Z)
- `FUELINST|fuelType=WIND|generation` = **8130** (n=2334, 2026-09-23T05:55:43.557522Z)
- `IMBALNGC|TOTAL|imbalance` = **-7925** (n=384, 2026-09-23T05:49:58.626105Z)
- `INDDEM|TOTAL|demand` = **-12417** (n=384, 2026-09-23T05:50:14.867234Z)
- `INDGEN|TOTAL|generation` = **13248** (n=384, 2026-09-23T05:50:14.867234Z)
- `MELNGC|TOTAL|margin` = **38580** (n=384, 2026-09-23T05:49:10.952491Z)
- `MID|dataProvider=APXMIDP|price` = **151.04** (n=125, 2026-09-23T05:42:21.663201Z)
- `MID|dataProvider=APXMIDP|volume` = **3642.8** (n=125, 2026-09-23T05:42:21.663201Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=246, 2026-09-23T05:42:21.663201Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=246, 2026-09-23T05:42:21.663201Z)
- `NDF|TOTAL|demand` = **20673** (n=392, 2026-09-23T05:47:19.396158Z)
- `TSDF|TOTAL|demand` = **21173** (n=392, 2026-09-23T05:47:19.396158Z)
- `WINDFOR|TOTAL|generation` = **7305** (n=66, 2026-09-23T05:30:43.471788Z)

## Latest publication events

- `2026-09-23T05:58:22.942544Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:57:45Z`
- `2026-09-23T05:56:15.018840Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:55:45Z`
- `2026-09-23T05:55:43.557522Z` — **FUELINST**: 80 rows; marker `2026-09-23T05:55:00Z`
- `2026-09-23T05:54:27.609678Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:53:45Z`
- `2026-09-23T05:52:18.977129Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:51:45Z`
- `2026-09-23T05:50:30.589375Z` — **FUELINST**: 80 rows; marker `2026-09-23T05:50:00Z`
- `2026-09-23T05:50:14.867234Z` — **INDGEN**: 792 rows; marker `2026-09-23T05:46:00Z`
- `2026-09-23T05:50:14.867234Z` — **INDDEM**: 792 rows; marker `2026-09-23T05:46:00Z`
- `2026-09-23T05:50:14.867234Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:49:45Z`
- `2026-09-23T05:49:58.626105Z` — **IMBALNGC**: 792 rows; marker `2026-09-23T05:46:00Z`
- `2026-09-23T05:49:10.952491Z` — **MELNGC**: 792 rows; marker `2026-09-23T05:46:00Z`
- `2026-09-23T05:48:23.086733Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:47:45Z`
- `2026-09-23T05:47:19.396158Z` — **TSDF**: 792 rows; marker `2026-09-23T05:46:00Z`
- `2026-09-23T05:47:19.396158Z` — **NDF**: 44 rows; marker `2026-09-23T05:46:00Z`
- `2026-09-23T05:46:23.002146Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:45:45Z`
