# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T13:23:08.726231Z`  
Current process started UTC: `2026-09-21T13:19:08.497011Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=-3, z=4.25 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3507, delta=-2, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=1, z=4.42 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3508, delta=0, z=4.42 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1847, 2026-09-21T13:20:29.934908Z)
- `FUELINST|fuelType=OTHER|generation` = **596** (n=1847, 2026-09-21T13:20:29.934908Z)
- `FUELINST|fuelType=PS|generation` = **222** (n=1847, 2026-09-21T13:20:29.934908Z)
- `FUELINST|fuelType=WIND|generation` = **4021** (n=1847, 2026-09-21T13:20:29.934908Z)
- `IMBALNGC|TOTAL|imbalance` = **-3248** (n=303, 2026-09-21T12:54:01.604416Z)
- `INDDEM|TOTAL|demand` = **-12240** (n=303, 2026-09-21T12:53:45.640615Z)
- `INDGEN|TOTAL|generation` = **18256** (n=303, 2026-09-21T12:53:45.640615Z)
- `MELNGC|TOTAL|margin` = **36270** (n=304, 2026-09-21T13:20:45.333443Z)
- `MID|dataProvider=APXMIDP|price` = **149.28** (n=44, 2026-09-21T13:12:14.660161Z)
- `MID|dataProvider=APXMIDP|volume` = **3942.4** (n=44, 2026-09-21T13:12:14.660161Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=86, 2026-09-21T13:12:14.660161Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=86, 2026-09-21T13:12:14.660161Z)
- `NDF|TOTAL|demand` = **21004** (n=311, 2026-09-21T13:18:22.282779Z)
- `TSDF|TOTAL|demand` = **21504** (n=311, 2026-09-21T13:18:37.721165Z)
- `WINDFOR|TOTAL|generation` = **8616** (n=53, 2026-09-21T12:30:32.614458Z)

## Latest publication events

- `2026-09-21T13:22:05.264421Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:21:45Z`
- `2026-09-21T13:20:45.333443Z` — **MELNGC**: 1386 rows; marker `2026-09-21T13:17:00Z`
- `2026-09-21T13:20:29.934908Z` — **FUELINST**: 80 rows; marker `2026-09-21T13:20:00Z`
- `2026-09-21T13:20:14.003026Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:19:45Z`
- `2026-09-21T13:18:37.721165Z` — **TSDF**: 1386 rows; marker `2026-09-21T13:17:00Z`
- `2026-09-21T13:18:22.282779Z` — **NDF**: 77 rows; marker `2026-09-21T13:17:00Z`
- `2026-09-21T13:18:05.956815Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:17:45Z`
- `2026-09-21T13:16:13.892363Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:15:45Z`
- `2026-09-21T13:15:42.414125Z` — **FUELINST**: 80 rows; marker `2026-09-21T13:15:00Z`
- `2026-09-21T13:14:06.642476Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:13:45Z`
- `2026-09-21T13:12:14.660161Z` — **MID**: 2 rows; marker `2026-09-21T13:12:04Z`
- `2026-09-21T13:12:14.660161Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:11:45Z`
- `2026-09-21T13:10:38.688369Z` — **FUELINST**: 80 rows; marker `2026-09-21T13:10:00Z`
- `2026-09-21T13:10:38.688369Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:09:45Z`
- `2026-09-21T13:08:15.009375Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:07:45Z`
