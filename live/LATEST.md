# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T20:58:30.297143Z`  
Current process started UTC: `2026-09-21T20:54:29.913447Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3587, delta=7, z=4.54 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3580, delta=8, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3572, delta=9, z=4.31 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3563, delta=6, z=4.16 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3557, delta=8, z=4.06 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3534, delta=22, z=3.69 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3549, delta=2, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3547, delta=8, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3539, delta=7, z=3.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3532, delta=10, z=3.64 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=146, delta=-39, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=0, z=3.62 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=0, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=-12, z=3.66 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1938, 2026-09-21T20:55:18.339226Z)
- `FUELINST|fuelType=OTHER|generation` = **130** (n=1938, 2026-09-21T20:55:18.339226Z)
- `FUELINST|fuelType=PS|generation` = **192** (n=1938, 2026-09-21T20:55:18.339226Z)
- `FUELINST|fuelType=WIND|generation` = **3433** (n=1938, 2026-09-21T20:55:18.339226Z)
- `IMBALNGC|TOTAL|imbalance` = **-2649** (n=319, 2026-09-21T20:52:05.346372Z)
- `INDDEM|TOTAL|demand` = **-12259** (n=319, 2026-09-21T20:52:05.346372Z)
- `INDGEN|TOTAL|generation` = **18810** (n=319, 2026-09-21T20:52:05.346372Z)
- `MELNGC|TOTAL|margin` = **36086** (n=319, 2026-09-21T20:49:58.052949Z)
- `MID|dataProvider=APXMIDP|price` = **162.85** (n=59, 2026-09-21T20:42:18.441146Z)
- `MID|dataProvider=APXMIDP|volume` = **2588.8** (n=59, 2026-09-21T20:42:18.441146Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=116, 2026-09-21T20:42:18.441146Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=116, 2026-09-21T20:42:18.441146Z)
- `NDF|TOTAL|demand` = **20959** (n=326, 2026-09-21T20:47:34.289449Z)
- `TSDF|TOTAL|demand` = **21459** (n=326, 2026-09-21T20:47:34.289449Z)
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T20:58:14.819029Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:57:45Z`
- `2026-09-21T20:56:05.645051Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:55:45Z`
- `2026-09-21T20:55:18.339226Z` — **FUELINST**: 80 rows; marker `2026-09-21T20:55:00Z`
- `2026-09-21T20:54:13.036670Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:53:45Z`
- `2026-09-21T20:52:05.346372Z` — **INDGEN**: 1116 rows; marker `2026-09-21T20:47:00Z`
- `2026-09-21T20:52:05.346372Z` — **INDDEM**: 1116 rows; marker `2026-09-21T20:47:00Z`
- `2026-09-21T20:52:05.346372Z` — **IMBALNGC**: 1116 rows; marker `2026-09-21T20:47:00Z`
- `2026-09-21T20:52:05.346372Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:51:45Z`
- `2026-09-21T20:50:45.930208Z` — **FUELINST**: 80 rows; marker `2026-09-21T20:50:00Z`
- `2026-09-21T20:50:13.821574Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:49:45Z`
- `2026-09-21T20:49:58.052949Z` — **MELNGC**: 1116 rows; marker `2026-09-21T20:47:00Z`
- `2026-09-21T20:48:22.399327Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:47:45Z`
- `2026-09-21T20:47:34.289449Z` — **TSDF**: 1116 rows; marker `2026-09-21T20:47:00Z`
- `2026-09-21T20:47:34.289449Z` — **NDF**: 62 rows; marker `2026-09-21T20:47:00Z`
- `2026-09-21T20:46:30.862170Z` — **FREQ**: 5761 rows; marker `2026-09-21T20:45:45Z`
