# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T18:05:21.435253Z`  
Current process started UTC: `2026-09-22T18:01:21.022305Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=635, delta=22, z=10.83 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=832, delta=5, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=636, delta=1, z=9.53 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=832, delta=-1, z=3.50 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=635, delta=0, z=9.72 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=833, delta=1, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=635, delta=0, z=9.94 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=832, delta=1, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=635, delta=0, z=10.18 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=831, delta=0, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=635, delta=0, z=10.43 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=831, delta=0, z=3.54 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=635, delta=1, z=10.70 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=831, delta=0, z=3.55 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=613, delta=26, z=12.48 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2191, 2026-09-22T18:00:38.158941Z)
- `FUELINST|fuelType=OTHER|generation` = **2856** (n=2191, 2026-09-22T18:00:38.158941Z)
- `FUELINST|fuelType=PS|generation` = **1509** (n=2191, 2026-09-22T18:00:38.158941Z)
- `FUELINST|fuelType=WIND|generation` = **1372** (n=2191, 2026-09-22T18:00:38.158941Z)
- `IMBALNGC|TOTAL|imbalance` = **-7940** (n=360, 2026-09-22T17:52:55.340139Z)
- `INDDEM|TOTAL|demand` = **-12478** (n=360, 2026-09-22T17:52:10.596146Z)
- `INDGEN|TOTAL|generation` = **13233** (n=360, 2026-09-22T17:52:10.596146Z)
- `MELNGC|TOTAL|margin` = **37173** (n=360, 2026-09-22T17:49:30.712468Z)
- `MID|dataProvider=APXMIDP|price` = **227.31** (n=101, 2026-09-22T17:42:07.200932Z)
- `MID|dataProvider=APXMIDP|volume` = **3881.3** (n=101, 2026-09-22T17:42:07.200932Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=200, 2026-09-22T17:42:07.200932Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=200, 2026-09-22T17:42:07.200932Z)
- `NDF|TOTAL|demand` = **20673** (n=368, 2026-09-22T17:47:39.575069Z)
- `TSDF|TOTAL|demand` = **21173** (n=368, 2026-09-22T17:47:55.003325Z)
- `WINDFOR|TOTAL|generation` = **13535** (n=62, 2026-09-22T16:30:39.657630Z)

## Latest publication events

- `2026-09-22T18:04:17.268836Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:03:45Z`
- `2026-09-22T18:02:25.029812Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:01:45Z`
- `2026-09-22T18:00:38.158941Z` — **FUELHH**: 20 rows; marker `2026-09-22T18:00:00Z`
- `2026-09-22T18:00:38.158941Z` — **FUELINST**: 80 rows; marker `2026-09-22T18:00:00Z`
- `2026-09-22T18:00:22.413820Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:59:45Z`
- `2026-09-22T17:58:14.996492Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:57:45Z`
- `2026-09-22T17:56:23.307046Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:55:45Z`
- `2026-09-22T17:55:35.709744Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:55:00Z`
- `2026-09-22T17:54:15.489223Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:53:45Z`
- `2026-09-22T17:52:55.340139Z` — **IMBALNGC**: 1224 rows; marker `2026-09-22T17:47:00Z`
- `2026-09-22T17:52:10.596146Z` — **INDGEN**: 1224 rows; marker `2026-09-22T17:47:00Z`
- `2026-09-22T17:52:10.596146Z` — **INDDEM**: 1224 rows; marker `2026-09-22T17:47:00Z`
- `2026-09-22T17:52:10.596146Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:51:45Z`
- `2026-09-22T17:50:34.329913Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:50:00Z`
- `2026-09-22T17:50:34.329913Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:49:45Z`
