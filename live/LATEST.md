# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T17:01:43.530958Z`  
Current process started UTC: `2026-09-22T16:57:43.957833Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=587, delta=286, z=15.29 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=596, delta=1, z=12.35 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=595, delta=1, z=12.79 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=594, delta=1, z=13.28 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=593, delta=0, z=13.83 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=593, delta=45, z=14.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=548, delta=67, z=13.93 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=301, delta=202, z=8.27 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=481, delta=100, z=12.60 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=381, delta=82, z=10.10 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=299, delta=62, z=7.92 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=237, delta=23, z=6.22 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=214, delta=19, z=5.60 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=195, delta=18, z=5.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=177, delta=84, z=4.58 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2179, 2026-09-22T17:00:40.169642Z)
- `FUELINST|fuelType=OTHER|generation` = **1935** (n=2179, 2026-09-22T17:00:40.169642Z)
- `FUELINST|fuelType=PS|generation` = **1509** (n=2179, 2026-09-22T17:00:40.169642Z)
- `FUELINST|fuelType=WIND|generation` = **1349** (n=2179, 2026-09-22T17:00:40.169642Z)
- `IMBALNGC|TOTAL|imbalance` = **-7954** (n=358, 2026-09-22T16:53:45.809507Z)
- `INDDEM|TOTAL|demand` = **-12476** (n=358, 2026-09-22T16:53:29.392532Z)
- `INDGEN|TOTAL|generation` = **13219** (n=358, 2026-09-22T16:53:45.809507Z)
- `MELNGC|TOTAL|margin` = **37151** (n=358, 2026-09-22T16:50:03.584874Z)
- `MID|dataProvider=APXMIDP|price` = **224.84** (n=99, 2026-09-22T16:42:18.479088Z)
- `MID|dataProvider=APXMIDP|volume` = **4488** (n=99, 2026-09-22T16:42:18.479088Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=196, 2026-09-22T16:42:18.479088Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=196, 2026-09-22T16:42:18.479088Z)
- `NDF|TOTAL|demand` = **20673** (n=366, 2026-09-22T16:47:42.402614Z)
- `TSDF|TOTAL|demand` = **21173** (n=366, 2026-09-22T16:47:42.402614Z)
- `WINDFOR|TOTAL|generation` = **13535** (n=62, 2026-09-22T16:30:39.657630Z)

## Latest publication events

- `2026-09-22T17:00:40.169642Z` — **FUELHH**: 20 rows; marker `2026-09-22T17:00:00Z`
- `2026-09-22T17:00:40.169642Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:00:00Z`
- `2026-09-22T17:00:40.169642Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:59:45Z`
- `2026-09-22T16:58:15.961825Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:57:45Z`
- `2026-09-22T16:56:11.282212Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:55:45Z`
- `2026-09-22T16:55:39.662230Z` — **FUELINST**: 80 rows; marker `2026-09-22T16:55:00Z`
- `2026-09-22T16:54:19.211737Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:53:45Z`
- `2026-09-22T16:53:45.809507Z` — **INDGEN**: 1260 rows; marker `2026-09-22T16:47:00Z`
- `2026-09-22T16:53:45.809507Z` — **IMBALNGC**: 1260 rows; marker `2026-09-22T16:47:00Z`
- `2026-09-22T16:53:29.392532Z` — **INDDEM**: 1260 rows; marker `2026-09-22T16:47:00Z`
- `2026-09-22T16:52:26.033554Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:51:45Z`
- `2026-09-22T16:50:34.484290Z` — **FUELINST**: 80 rows; marker `2026-09-22T16:50:00Z`
- `2026-09-22T16:50:18.962260Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:49:45Z`
- `2026-09-22T16:50:03.584874Z` — **MELNGC**: 1260 rows; marker `2026-09-22T16:47:00Z`
- `2026-09-22T16:48:14.752232Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:47:45Z`
