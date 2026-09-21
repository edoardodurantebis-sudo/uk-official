# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T13:01:25.790220Z`  
Current process started UTC: `2026-09-21T12:57:24.758198Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3507, delta=-6, z=4.49 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3508, delta=4, z=4.45 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=1, z=4.37 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3503, delta=-6, z=4.36 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1843, 2026-09-21T13:00:35.850154Z)
- `FUELINST|fuelType=OTHER|generation` = **597** (n=1843, 2026-09-21T13:00:35.850154Z)
- `FUELINST|fuelType=PS|generation` = **228** (n=1843, 2026-09-21T13:00:35.850154Z)
- `FUELINST|fuelType=WIND|generation` = **3889** (n=1843, 2026-09-21T13:00:35.850154Z)
- `IMBALNGC|TOTAL|imbalance` = **-3248** (n=303, 2026-09-21T12:54:01.604416Z)
- `INDDEM|TOTAL|demand` = **-12240** (n=303, 2026-09-21T12:53:45.640615Z)
- `INDGEN|TOTAL|generation` = **18256** (n=303, 2026-09-21T12:53:45.640615Z)
- `MELNGC|TOTAL|margin` = **36271** (n=303, 2026-09-21T12:50:38.355172Z)
- `MID|dataProvider=APXMIDP|price` = **158.59** (n=43, 2026-09-21T12:42:12.075590Z)
- `MID|dataProvider=APXMIDP|volume` = **3786.4** (n=43, 2026-09-21T12:42:12.075590Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=84, 2026-09-21T12:42:12.075590Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=84, 2026-09-21T12:42:12.075590Z)
- `NDF|TOTAL|demand` = **21004** (n=310, 2026-09-21T12:48:14.497805Z)
- `TSDF|TOTAL|demand` = **21504** (n=310, 2026-09-21T12:48:30.515388Z)
- `WINDFOR|TOTAL|generation` = **8616** (n=53, 2026-09-21T12:30:32.614458Z)

## Latest publication events

- `2026-09-21T13:00:35.850154Z` — **FUELHH**: 20 rows; marker `2026-09-21T13:00:00Z`
- `2026-09-21T13:00:35.850154Z` — **FUELINST**: 80 rows; marker `2026-09-21T13:00:00Z`
- `2026-09-21T13:00:20.439012Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:59:45Z`
- `2026-09-21T12:58:28.766454Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:57:45Z`
- `2026-09-21T12:56:25.742800Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:55:45Z`
- `2026-09-21T12:55:37.525329Z` — **FUELINST**: 80 rows; marker `2026-09-21T12:55:00Z`
- `2026-09-21T12:54:17.935329Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:53:45Z`
- `2026-09-21T12:54:01.604416Z` — **IMBALNGC**: 1404 rows; marker `2026-09-21T12:47:00Z`
- `2026-09-21T12:53:45.640615Z` — **INDGEN**: 1404 rows; marker `2026-09-21T12:47:00Z`
- `2026-09-21T12:53:45.640615Z` — **INDDEM**: 1404 rows; marker `2026-09-21T12:47:00Z`
- `2026-09-21T12:52:14.641387Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:51:45Z`
- `2026-09-21T12:50:38.355172Z` — **MELNGC**: 1404 rows; marker `2026-09-21T12:47:00Z`
- `2026-09-21T12:50:38.355172Z` — **FUELINST**: 80 rows; marker `2026-09-21T12:50:00Z`
- `2026-09-21T12:50:22.316330Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:49:45Z`
- `2026-09-21T12:48:30.515388Z` — **TSDF**: 1404 rows; marker `2026-09-21T12:47:00Z`
