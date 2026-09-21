# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T19:55:01.617155Z`  
Current process started UTC: `2026-09-21T19:51:01.311476Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=0, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=-12, z=3.66 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=161, delta=-8, z=4.02 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=185, delta=-45, z=4.95 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=169, delta=-2, z=4.27 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=171, delta=-17, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=188, delta=-2, z=4.87 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=190, delta=0, z=4.96 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=190, delta=-12, z=5.00 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=202, delta=-28, z=5.39 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3738, delta=237, z=4.84 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=230, delta=-14, z=6.75 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3544, delta=-139, z=4.31 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=0, z=6.29 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1925, 2026-09-21T19:50:32.932869Z)
- `FUELINST|fuelType=OTHER|generation` = **1559** (n=1925, 2026-09-21T19:50:32.932869Z)
- `FUELINST|fuelType=PS|generation` = **526** (n=1925, 2026-09-21T19:50:32.932869Z)
- `FUELINST|fuelType=WIND|generation` = **3629** (n=1925, 2026-09-21T19:50:32.932869Z)
- `IMBALNGC|TOTAL|imbalance` = **-2779** (n=317, 2026-09-21T19:52:52.399287Z)
- `INDDEM|TOTAL|demand` = **-12262** (n=317, 2026-09-21T19:52:36.846403Z)
- `INDGEN|TOTAL|generation` = **18680** (n=317, 2026-09-21T19:52:36.846403Z)
- `MELNGC|TOTAL|margin` = **36039** (n=317, 2026-09-21T19:51:01.311488Z)
- `MID|dataProvider=APXMIDP|price` = **193.44** (n=57, 2026-09-21T19:42:10.036286Z)
- `MID|dataProvider=APXMIDP|volume` = **3317.9** (n=57, 2026-09-21T19:42:10.036286Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=112, 2026-09-21T19:42:10.036286Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=112, 2026-09-21T19:42:10.036286Z)
- `NDF|TOTAL|demand` = **20959** (n=324, 2026-09-21T19:48:08.390110Z)
- `TSDF|TOTAL|demand` = **21459** (n=324, 2026-09-21T19:48:08.390110Z)
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T19:54:12.060264Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:53:45Z`
- `2026-09-21T19:52:52.399287Z` — **IMBALNGC**: 1152 rows; marker `2026-09-21T19:47:00Z`
- `2026-09-21T19:52:36.846403Z` — **INDGEN**: 1152 rows; marker `2026-09-21T19:47:00Z`
- `2026-09-21T19:52:36.846403Z` — **INDDEM**: 1152 rows; marker `2026-09-21T19:47:00Z`
- `2026-09-21T19:52:20.970180Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:51:45Z`
- `2026-09-21T19:51:01.311488Z` — **MELNGC**: 1152 rows; marker `2026-09-21T19:47:00Z`
- `2026-09-21T19:50:32.932869Z` — **FUELINST**: 80 rows; marker `2026-09-21T19:50:00Z`
- `2026-09-21T19:50:16.931070Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:49:45Z`
- `2026-09-21T19:48:25.112246Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:47:45Z`
- `2026-09-21T19:48:08.390110Z` — **TSDF**: 1152 rows; marker `2026-09-21T19:47:00Z`
- `2026-09-21T19:48:08.390110Z` — **NDF**: 64 rows; marker `2026-09-21T19:47:00Z`
- `2026-09-21T19:46:08.818772Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:45:45Z`
- `2026-09-21T19:45:21.387756Z` — **FUELINST**: 80 rows; marker `2026-09-21T19:45:00Z`
- `2026-09-21T19:44:17.916388Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:43:45Z`
- `2026-09-21T19:42:10.036286Z` — **MID**: 2 rows; marker `2026-09-21T19:42:03Z`
