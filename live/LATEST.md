# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T14:07:05.686723Z`  
Current process started UTC: `2026-09-15T14:03:05.316368Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.81 -> generation-mix component moved
- **IMBALNGC** `TOTAL` `imbalance` — indicated system imbalance [TOTAL] imbalance: value=5650, delta=-1, z=3.51 -> indicated imbalance moved; inspect sign/magnitude
- **IMBALNGC** `TOTAL` `imbalance` — indicated system imbalance [TOTAL] imbalance: value=5651, delta=-24, z=4.85 -> indicated imbalance moved; inspect sign/magnitude
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=24755, delta=-24, z=4.72 -> state changed
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11901, delta=0, z=3.83 -> demand pressure easing
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=19104, delta=0, z=-3.76 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=18604, delta=0, z=-3.74 -> demand pressure easing
- **IMBALNGC** `TOTAL` `imbalance` — indicated system imbalance [TOTAL] imbalance: value=5675, delta=6507, z=16.70 -> indicated imbalance moved; inspect sign/magnitude
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=24779, delta=5042, z=13.07 -> state changed
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11901, delta=369, z=5.90 -> demand pressure up
- **FUELHH** `fuelType=BIOMASS` `generation` — half-hour generation mix [fuelType=BIOMASS] generation: value=1292, delta=-487, z=-3.55 -> generation-mix component moved
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=19104, delta=-1465, z=-5.53 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=18604, delta=-1465, z=-5.48 -> demand pressure easing
- **FUELHH** `fuelType=INTFR` `generation` — half-hour generation mix [fuelType=INTFR] generation: value=984, delta=278, z=4.11 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=999, delta=-1, z=3.64 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1260** (n=206, 2026-09-15T14:05:29.371512Z)
- `FUELINST|fuelType=NPSHYD|generation` = **336** (n=206, 2026-09-15T14:05:29.371512Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=206, 2026-09-15T14:05:29.371512Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=206, 2026-09-15T14:05:29.371512Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=206, 2026-09-15T14:05:29.371512Z)
- `FUELINST|fuelType=OTHER|generation` = **637** (n=206, 2026-09-15T14:05:29.371512Z)
- `FUELINST|fuelType=PS|generation` = **-909** (n=206, 2026-09-15T14:05:29.371512Z)
- `FUELINST|fuelType=WIND|generation` = **10067** (n=206, 2026-09-15T14:05:29.371512Z)
- `IMBALNGC|TOTAL|imbalance` = **5710** (n=34, 2026-09-15T13:53:12.812024Z)
- `INDDEM|TOTAL|demand` = **-11915** (n=34, 2026-09-15T13:53:12.812024Z)
- `INDGEN|TOTAL|generation` = **24831** (n=34, 2026-09-15T13:53:12.812024Z)
- `MELNGC|TOTAL|margin` = **35198** (n=34, 2026-09-15T13:50:31.602646Z)
- `NDF|TOTAL|demand` = **18621** (n=35, 2026-09-15T13:47:59.205843Z)
- `TSDF|TOTAL|demand` = **19121** (n=35, 2026-09-15T13:48:15.545762Z)
- `WINDFOR|TOTAL|generation` = **17848** (n=6, 2026-09-15T12:30:22.163636Z)

## Latest publication events

- `2026-09-15T14:06:32.429486Z` — **MID**: 0 rows; marker `2026-09-15T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T14:06:01.104744Z` — **FREQ**: 5761 rows; marker `2026-09-15T14:05:45Z`
- `2026-09-15T14:05:29.371512Z` — **FUELINST**: 80 rows; marker `2026-09-15T14:05:00Z`
- `2026-09-15T14:04:10.035403Z` — **FREQ**: 5761 rows; marker `2026-09-15T14:03:45Z`
- `2026-09-15T14:02:09.309472Z` — **FREQ**: 5761 rows; marker `2026-09-15T14:01:45Z`
- `2026-09-15T14:00:33.830346Z` — **FUELHH**: 20 rows; marker `2026-09-15T14:00:00Z`
- `2026-09-15T14:00:33.830346Z` — **FUELINST**: 80 rows; marker `2026-09-15T14:00:00Z`
- `2026-09-15T14:00:18.377161Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:59:45Z`
- `2026-09-15T13:58:25.993655Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:57:45Z`
- `2026-09-15T13:56:18.100989Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:55:45Z`
- `2026-09-15T13:55:30.812160Z` — **FUELINST**: 80 rows; marker `2026-09-15T13:55:00Z`
- `2026-09-15T13:54:16.606507Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:53:45Z`
- `2026-09-15T13:53:12.812024Z` — **INDGEN**: 1368 rows; marker `2026-09-15T13:47:00Z`
- `2026-09-15T13:53:12.812024Z` — **INDDEM**: 1368 rows; marker `2026-09-15T13:47:00Z`
- `2026-09-15T13:53:12.812024Z` — **IMBALNGC**: 1368 rows; marker `2026-09-15T13:47:00Z`
