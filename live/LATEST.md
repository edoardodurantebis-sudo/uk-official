# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T17:55:35.669057Z`  
Current process started UTC: `2026-09-21T17:51:36.183726Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3141, delta=70, z=3.97 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=247, delta=0, z=8.12 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3511, delta=0, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=CCGT` `generation` — instantaneous generation mix [fuelType=CCGT] generation: value=13884, delta=-74, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3071, delta=-54, z=3.87 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=247, delta=0, z=8.27 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3511, delta=3, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=CCGT` `generation` — instantaneous generation mix [fuelType=CCGT] generation: value=13958, delta=-88, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3125, delta=2, z=3.98 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=247, delta=-14, z=8.42 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3508, delta=4, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=CCGT` `generation` — instantaneous generation mix [fuelType=CCGT] generation: value=14046, delta=5, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3123, delta=32, z=3.99 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=261, delta=61, z=9.14 -> generation-mix component moved
- **FUELINST** `fuelType=CCGT` `generation` — instantaneous generation mix [fuelType=CCGT] generation: value=14041, delta=49, z=3.65 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1902, 2026-09-21T17:55:23.623725Z)
- `FUELINST|fuelType=OTHER|generation` = **3141** (n=1902, 2026-09-21T17:55:23.623725Z)
- `FUELINST|fuelType=PS|generation` = **448** (n=1902, 2026-09-21T17:55:23.623725Z)
- `FUELINST|fuelType=WIND|generation` = **3523** (n=1902, 2026-09-21T17:55:23.623725Z)
- `IMBALNGC|TOTAL|imbalance` = **-3042** (n=313, 2026-09-21T17:52:27.042082Z)
- `INDDEM|TOTAL|demand` = **-12280** (n=313, 2026-09-21T17:52:27.042082Z)
- `INDGEN|TOTAL|generation` = **18417** (n=313, 2026-09-21T17:52:27.042082Z)
- `MELNGC|TOTAL|margin` = **36168** (n=313, 2026-09-21T17:49:48.045985Z)
- `MID|dataProvider=APXMIDP|price` = **206.43** (n=53, 2026-09-21T17:42:12.300443Z)
- `MID|dataProvider=APXMIDP|volume` = **3457.9** (n=53, 2026-09-21T17:42:12.300443Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=104, 2026-09-21T17:42:12.300443Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=104, 2026-09-21T17:42:12.300443Z)
- `NDF|TOTAL|demand` = **20959** (n=320, 2026-09-21T17:47:56.600975Z)
- `TSDF|TOTAL|demand` = **21459** (n=320, 2026-09-21T17:47:56.600975Z)
- `WINDFOR|TOTAL|generation` = **8620** (n=54, 2026-09-21T16:30:47.714491Z)

## Latest publication events

- `2026-09-21T17:55:23.623725Z` — **FUELINST**: 80 rows; marker `2026-09-21T17:55:00Z`
- `2026-09-21T17:54:03.215777Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:53:45Z`
- `2026-09-21T17:52:27.042082Z` — **INDGEN**: 1224 rows; marker `2026-09-21T17:47:00Z`
- `2026-09-21T17:52:27.042082Z` — **INDDEM**: 1224 rows; marker `2026-09-21T17:47:00Z`
- `2026-09-21T17:52:27.042082Z` — **IMBALNGC**: 1224 rows; marker `2026-09-21T17:47:00Z`
- `2026-09-21T17:52:11.188284Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:51:45Z`
- `2026-09-21T17:50:19.148312Z` — **FUELINST**: 80 rows; marker `2026-09-21T17:50:00Z`
- `2026-09-21T17:50:03.569969Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:49:45Z`
- `2026-09-21T17:49:48.045985Z` — **MELNGC**: 1224 rows; marker `2026-09-21T17:47:00Z`
- `2026-09-21T17:48:12.270659Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:47:45Z`
- `2026-09-21T17:47:56.600975Z` — **TSDF**: 1224 rows; marker `2026-09-21T17:47:00Z`
- `2026-09-21T17:47:56.600975Z` — **NDF**: 68 rows; marker `2026-09-21T17:47:00Z`
- `2026-09-21T17:46:23.880240Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:45:45Z`
- `2026-09-21T17:45:36.077905Z` — **FUELINST**: 80 rows; marker `2026-09-21T17:45:00Z`
- `2026-09-21T17:44:14.779149Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:43:45Z`
