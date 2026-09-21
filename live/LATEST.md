# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T20:11:52.731598Z`  
Current process started UTC: `2026-09-21T20:07:52.702181Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=146, delta=-39, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=0, z=3.62 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1929, 2026-09-21T20:10:31.835970Z)
- `FUELINST|fuelType=OTHER|generation` = **1014** (n=1929, 2026-09-21T20:10:31.835970Z)
- `FUELINST|fuelType=PS|generation` = **568** (n=1929, 2026-09-21T20:10:31.835970Z)
- `FUELINST|fuelType=WIND|generation` = **3716** (n=1929, 2026-09-21T20:10:31.835970Z)
- `IMBALNGC|TOTAL|imbalance` = **-2779** (n=317, 2026-09-21T19:52:52.399287Z)
- `INDDEM|TOTAL|demand` = **-12262** (n=317, 2026-09-21T19:52:36.846403Z)
- `INDGEN|TOTAL|generation` = **18680** (n=317, 2026-09-21T19:52:36.846403Z)
- `MELNGC|TOTAL|margin` = **36039** (n=317, 2026-09-21T19:51:01.311488Z)
- `MID|dataProvider=APXMIDP|price` = **193.44** (n=57, 2026-09-21T19:42:10.036286Z)
- `MID|dataProvider=APXMIDP|volume` = **3317.9** (n=57, 2026-09-21T19:42:10.036286Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=113, 2026-09-21T20:06:21.033069Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=113, 2026-09-21T20:06:21.033069Z)
- `NDF|TOTAL|demand` = **20959** (n=324, 2026-09-21T19:48:08.390110Z)
- `TSDF|TOTAL|demand` = **21459** (n=324, 2026-09-21T19:48:08.390110Z)
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T20:10:31.835970Z` — **FUELINST**: 80 rows; marker `2026-09-21T20:10:00Z`
- `2026-09-21T20:10:16.326486Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:09:45Z`
- `2026-09-21T20:08:08.704184Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:07:45Z`
- `2026-09-21T20:06:21.033069Z` — **MID**: 1 rows; marker `2026-09-21T20:05:00Z`
- `2026-09-21T20:06:05.229658Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:05:45Z`
- `2026-09-21T20:05:33.953541Z` — **FUELINST**: 80 rows; marker `2026-09-21T20:05:00Z`
- `2026-09-21T20:04:13.570086Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:03:45Z`
- `2026-09-21T20:02:20.997784Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:01:45Z`
- `2026-09-21T20:00:45.587599Z` — **FUELHH**: 20 rows; marker `2026-09-21T20:00:00Z`
- `2026-09-21T20:00:45.587599Z` — **FUELINST**: 80 rows; marker `2026-09-21T20:00:00Z`
- `2026-09-21T20:00:13.815080Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:59:45Z`
- `2026-09-21T19:58:11.979232Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:57:45Z`
- `2026-09-21T19:56:20.172685Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:55:45Z`
- `2026-09-21T19:55:31.923713Z` — **FUELINST**: 80 rows; marker `2026-09-21T19:55:00Z`
- `2026-09-21T19:54:12.060264Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:53:45Z`
