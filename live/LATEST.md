# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T18:12:37.942551Z`  
Current process started UTC: `2026-09-21T18:08:37.754990Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3362, delta=41, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=268, delta=8, z=8.42 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3514, delta=4, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3321, delta=-49, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=260, delta=13, z=8.30 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3510, delta=2, z=3.50 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3154, delta=358, z=4.14 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=242, delta=155, z=8.69 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3508, delta=-1, z=3.52 -> generation-mix component moved
- **FUELHH** `fuelType=CCGT` `generation` — half-hour generation mix [fuelType=CCGT] generation: value=13950, delta=289, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3370, delta=229, z=4.33 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=247, delta=0, z=7.98 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3141, delta=70, z=3.97 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=247, delta=0, z=8.12 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3511, delta=0, z=3.55 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1905, 2026-09-21T18:10:29.801736Z)
- `FUELINST|fuelType=OTHER|generation` = **3362** (n=1905, 2026-09-21T18:10:29.801736Z)
- `FUELINST|fuelType=PS|generation` = **631** (n=1905, 2026-09-21T18:10:29.801736Z)
- `FUELINST|fuelType=WIND|generation` = **3508** (n=1905, 2026-09-21T18:10:29.801736Z)
- `IMBALNGC|TOTAL|imbalance` = **-3042** (n=313, 2026-09-21T17:52:27.042082Z)
- `INDDEM|TOTAL|demand` = **-12280** (n=313, 2026-09-21T17:52:27.042082Z)
- `INDGEN|TOTAL|generation` = **18417** (n=313, 2026-09-21T17:52:27.042082Z)
- `MELNGC|TOTAL|margin` = **36168** (n=313, 2026-09-21T17:49:48.045985Z)
- `MID|dataProvider=APXMIDP|price` = **205.18** (n=54, 2026-09-21T18:12:21.794388Z)
- `MID|dataProvider=APXMIDP|volume` = **3558.6** (n=54, 2026-09-21T18:12:21.794388Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=106, 2026-09-21T18:12:21.794388Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=106, 2026-09-21T18:12:21.794388Z)
- `NDF|TOTAL|demand` = **20959** (n=320, 2026-09-21T17:47:56.600975Z)
- `TSDF|TOTAL|demand` = **21459** (n=320, 2026-09-21T17:47:56.600975Z)
- `WINDFOR|TOTAL|generation` = **8620** (n=54, 2026-09-21T16:30:47.714491Z)

## Latest publication events

- `2026-09-21T18:12:21.794388Z` — **MID**: 2 rows; marker `2026-09-21T18:12:04Z`
- `2026-09-21T18:12:21.794388Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:11:45Z`
- `2026-09-21T18:10:29.801736Z` — **FUELINST**: 80 rows; marker `2026-09-21T18:10:00Z`
- `2026-09-21T18:10:13.806114Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:09:45Z`
- `2026-09-21T18:08:21.988035Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:07:45Z`
- `2026-09-21T18:06:29.968320Z` — **MID**: 1 rows; marker `2026-09-21T18:05:00Z`
- `2026-09-21T18:06:14.612523Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:05:45Z`
- `2026-09-21T18:05:26.955894Z` — **FUELINST**: 80 rows; marker `2026-09-21T18:05:00Z`
- `2026-09-21T18:04:23.266057Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:03:45Z`
- `2026-09-21T18:02:15.196020Z` — **FREQ**: 5761 rows; marker `2026-09-21T18:01:45Z`
- `2026-09-21T18:00:55.599571Z` — **FUELHH**: 20 rows; marker `2026-09-21T18:00:00Z`
- `2026-09-21T18:00:23.927933Z` — **FUELINST**: 80 rows; marker `2026-09-21T18:00:00Z`
- `2026-09-21T18:00:07.529753Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:59:45Z`
- `2026-09-21T17:58:11.652337Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:57:45Z`
- `2026-09-21T17:56:04.078931Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:55:45Z`
