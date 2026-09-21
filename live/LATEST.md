# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T12:48:46.857199Z`  
Current process started UTC: `2026-09-21T12:44:46.406969Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=-3, z=4.55 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3512, delta=6, z=4.65 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3506, delta=-6, z=4.52 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3513, delta=1, z=4.83 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3512, delta=-1, z=4.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3513, delta=-3, z=4.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3516, delta=0, z=4.88 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3516, delta=3, z=4.91 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3513, delta=4, z=4.86 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=0, z=4.79 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3512, delta=-3, z=5.00 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=3, z=4.82 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3506, delta=-6, z=4.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3512, delta=-1, z=4.97 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3513, delta=-4, z=5.03 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1840, 2026-09-21T12:45:34.413309Z)
- `FUELINST|fuelType=OTHER|generation` = **622** (n=1840, 2026-09-21T12:45:34.413309Z)
- `FUELINST|fuelType=PS|generation` = **228** (n=1840, 2026-09-21T12:45:34.413309Z)
- `FUELINST|fuelType=WIND|generation` = **3943** (n=1840, 2026-09-21T12:45:34.413309Z)
- `IMBALNGC|TOTAL|imbalance` = **-3333** (n=302, 2026-09-21T12:23:51.221953Z)
- `INDDEM|TOTAL|demand` = **-12237** (n=302, 2026-09-21T12:23:35.101349Z)
- `INDGEN|TOTAL|generation` = **18171** (n=302, 2026-09-21T12:23:35.101349Z)
- `MELNGC|TOTAL|margin` = **36677** (n=302, 2026-09-21T12:20:39.601841Z)
- `MID|dataProvider=APXMIDP|price` = **158.59** (n=43, 2026-09-21T12:42:12.075590Z)
- `MID|dataProvider=APXMIDP|volume` = **3786.4** (n=43, 2026-09-21T12:42:12.075590Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=84, 2026-09-21T12:42:12.075590Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=84, 2026-09-21T12:42:12.075590Z)
- `NDF|TOTAL|demand` = **21004** (n=310, 2026-09-21T12:48:14.497805Z)
- `TSDF|TOTAL|demand` = **21504** (n=310, 2026-09-21T12:48:30.515388Z)
- `WINDFOR|TOTAL|generation` = **8616** (n=53, 2026-09-21T12:30:32.614458Z)

## Latest publication events

- `2026-09-21T12:48:30.515388Z` — **TSDF**: 1404 rows; marker `2026-09-21T12:47:00Z`
- `2026-09-21T12:48:14.497805Z` — **NDF**: 78 rows; marker `2026-09-21T12:47:00Z`
- `2026-09-21T12:48:14.497805Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:47:45Z`
- `2026-09-21T12:46:22.528169Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:45:45Z`
- `2026-09-21T12:45:34.413309Z` — **FUELINST**: 80 rows; marker `2026-09-21T12:45:00Z`
- `2026-09-21T12:44:21.605929Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:43:45Z`
- `2026-09-21T12:42:12.075590Z` — **MID**: 2 rows; marker `2026-09-21T12:42:03Z`
- `2026-09-21T12:42:12.075590Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:41:45Z`
- `2026-09-21T12:40:36.459493Z` — **FUELINST**: 80 rows; marker `2026-09-21T12:40:00Z`
- `2026-09-21T12:40:20.360342Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:39:45Z`
- `2026-09-21T12:38:12.742567Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:37:45Z`
- `2026-09-21T12:36:36.512732Z` — **MID**: 1 rows; marker `2026-09-21T12:35:00Z`
- `2026-09-21T12:36:21.009273Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:35:45Z`
- `2026-09-21T12:35:38.035735Z` — **FUELINST**: 80 rows; marker `2026-09-21T12:35:00Z`
- `2026-09-21T12:34:17.982753Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:33:45Z`
