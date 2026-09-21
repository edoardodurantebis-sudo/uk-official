# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T13:31:34.489032Z`  
Current process started UTC: `2026-09-21T13:27:34.205233Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3507, delta=0, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3508, delta=4, z=4.30 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=0, z=4.23 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1849, 2026-09-21T13:30:33.500588Z)
- `FUELINST|fuelType=OTHER|generation` = **489** (n=1849, 2026-09-21T13:30:33.500588Z)
- `FUELINST|fuelType=PS|generation` = **214** (n=1849, 2026-09-21T13:30:33.500588Z)
- `FUELINST|fuelType=WIND|generation` = **4087** (n=1849, 2026-09-21T13:30:33.500588Z)
- `IMBALNGC|TOTAL|imbalance` = **-3231** (n=304, 2026-09-21T13:23:53.188521Z)
- `INDDEM|TOTAL|demand` = **-12240** (n=304, 2026-09-21T13:23:53.188521Z)
- `INDGEN|TOTAL|generation` = **18273** (n=304, 2026-09-21T13:23:37.898078Z)
- `MELNGC|TOTAL|margin` = **36270** (n=304, 2026-09-21T13:20:45.333443Z)
- `MID|dataProvider=APXMIDP|price` = **149.28** (n=44, 2026-09-21T13:12:14.660161Z)
- `MID|dataProvider=APXMIDP|volume` = **3942.4** (n=44, 2026-09-21T13:12:14.660161Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=86, 2026-09-21T13:12:14.660161Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=86, 2026-09-21T13:12:14.660161Z)
- `NDF|TOTAL|demand` = **21004** (n=311, 2026-09-21T13:18:22.282779Z)
- `TSDF|TOTAL|demand` = **21504** (n=311, 2026-09-21T13:18:37.721165Z)
- `WINDFOR|TOTAL|generation` = **8616** (n=53, 2026-09-21T12:30:32.614458Z)

## Latest publication events

- `2026-09-21T13:30:33.500588Z` — **FUELHH**: 20 rows; marker `2026-09-21T13:30:00Z`
- `2026-09-21T13:30:33.500588Z` — **FUELINST**: 80 rows; marker `2026-09-21T13:30:00Z`
- `2026-09-21T13:30:17.160158Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:29:45Z`
- `2026-09-21T13:28:09.209463Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:27:45Z`
- `2026-09-21T13:26:17.253286Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:25:45Z`
- `2026-09-21T13:25:29.120536Z` — **FUELINST**: 80 rows; marker `2026-09-21T13:25:00Z`
- `2026-09-21T13:24:09.319813Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:23:45Z`
- `2026-09-21T13:23:53.188521Z` — **INDDEM**: 1386 rows; marker `2026-09-21T13:17:00Z`
- `2026-09-21T13:23:53.188521Z` — **IMBALNGC**: 1386 rows; marker `2026-09-21T13:18:00Z`
- `2026-09-21T13:23:37.898078Z` — **INDGEN**: 1386 rows; marker `2026-09-21T13:17:00Z`
- `2026-09-21T13:22:05.264421Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:21:45Z`
- `2026-09-21T13:20:45.333443Z` — **MELNGC**: 1386 rows; marker `2026-09-21T13:17:00Z`
- `2026-09-21T13:20:29.934908Z` — **FUELINST**: 80 rows; marker `2026-09-21T13:20:00Z`
- `2026-09-21T13:20:14.003026Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:19:45Z`
- `2026-09-21T13:18:37.721165Z` — **TSDF**: 1386 rows; marker `2026-09-21T13:17:00Z`
