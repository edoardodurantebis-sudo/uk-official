# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T11:05:46.280261Z`  
Current process started UTC: `2026-09-15T11:01:46.708975Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **IMBALNGC** `TOTAL` `imbalance` — indicated system imbalance [TOTAL] imbalance: value=5675, delta=6507, z=16.70 -> indicated imbalance moved; inspect sign/magnitude
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=24779, delta=5042, z=13.07 -> state changed
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11901, delta=369, z=5.90 -> demand pressure up
- **FUELHH** `fuelType=BIOMASS` `generation` — half-hour generation mix [fuelType=BIOMASS] generation: value=1292, delta=-487, z=-3.55 -> generation-mix component moved
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=19104, delta=-1465, z=-5.53 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=18604, delta=-1465, z=-5.48 -> demand pressure easing
- **FUELHH** `fuelType=INTFR` `generation` — half-hour generation mix [fuelType=INTFR] generation: value=984, delta=278, z=4.11 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=999, delta=-1, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=1000, delta=1, z=3.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=999, delta=86, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=913, delta=181, z=3.84 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=0, z=3.52 -> generation-mix component moved
- **FUELHH** `fuelType=INTNEM` `generation` — half-hour generation mix [fuelType=INTNEM] generation: value=1016, delta=192, z=3.59 -> generation-mix component moved
- **FUELHH** `fuelType=INTIFA2` `generation` — half-hour generation mix [fuelType=INTIFA2] generation: value=828, delta=552, z=3.62 -> generation-mix component moved
- **FUELHH** `fuelType=INTFR` `generation` — half-hour generation mix [fuelType=INTFR] generation: value=674, delta=468, z=4.35 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=170, 2026-09-15T11:05:30.511440Z)
- `FUELINST|fuelType=NPSHYD|generation` = **422** (n=170, 2026-09-15T11:05:30.511440Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=170, 2026-09-15T11:05:30.511440Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=170, 2026-09-15T11:05:30.511440Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=170, 2026-09-15T11:05:30.511440Z)
- `FUELINST|fuelType=OTHER|generation` = **798** (n=170, 2026-09-15T11:05:30.511440Z)
- `FUELINST|fuelType=PS|generation` = **-1209** (n=170, 2026-09-15T11:05:30.511440Z)
- `FUELINST|fuelType=WIND|generation` = **11594** (n=170, 2026-09-15T11:05:30.511440Z)
- `IMBALNGC|TOTAL|imbalance` = **5675** (n=28, 2026-09-15T11:04:58.801222Z)
- `INDDEM|TOTAL|demand` = **-11901** (n=28, 2026-09-15T11:04:43.146962Z)
- `INDGEN|TOTAL|generation` = **24779** (n=28, 2026-09-15T11:04:43.146962Z)
- `MELNGC|TOTAL|margin` = **35212** (n=28, 2026-09-15T10:55:12.649432Z)
- `NDF|TOTAL|demand` = **18604** (n=29, 2026-09-15T10:51:02.252130Z)
- `TSDF|TOTAL|demand` = **19104** (n=29, 2026-09-15T10:51:02.252130Z)
- `WINDFOR|TOTAL|generation` = **17599** (n=5, 2026-09-15T10:30:45.227650Z)

## Latest publication events

- `2026-09-15T11:05:30.511440Z` — **FUELINST**: 80 rows; marker `2026-09-15T11:05:00Z`
- `2026-09-15T11:04:58.801222Z` — **IMBALNGC**: 1476 rows; marker `2026-09-15T10:50:00Z`
- `2026-09-15T11:04:43.146962Z` — **INDGEN**: 1476 rows; marker `2026-09-15T10:50:00Z`
- `2026-09-15T11:04:43.146962Z` — **INDDEM**: 1476 rows; marker `2026-09-15T10:50:00Z`
- `2026-09-15T11:04:27.431549Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:03:45Z`
- `2026-09-15T11:02:18.713268Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:01:45Z`
- `2026-09-15T11:00:46.444783Z` — **FUELHH**: 20 rows; marker `2026-09-15T11:00:00Z`
- `2026-09-15T11:00:30.014168Z` — **FUELINST**: 80 rows; marker `2026-09-15T11:00:00Z`
- `2026-09-15T11:00:14.572046Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:59:45Z`
- `2026-09-15T10:58:22.309791Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:57:45Z`
- `2026-09-15T10:56:16.335274Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:55:45Z`
- `2026-09-15T10:55:28.691177Z` — **FUELINST**: 80 rows; marker `2026-09-15T10:55:00Z`
- `2026-09-15T10:55:12.649432Z` — **MELNGC**: 1476 rows; marker `2026-09-15T10:50:00Z`
- `2026-09-15T10:54:24.246222Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:53:45Z`
- `2026-09-15T10:52:22.195580Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:51:45Z`
