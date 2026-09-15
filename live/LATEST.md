# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T15:22:47.714420Z`  
Current process started UTC: `2026-09-15T15:18:47.335227Z`  
1-second metadata polls in this process: **236**  
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

- `FUELINST|fuelType=INTVKL|generation` = **453** (n=221, 2026-09-15T15:20:22.556182Z)
- `FUELINST|fuelType=NPSHYD|generation` = **441** (n=221, 2026-09-15T15:20:22.556182Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=221, 2026-09-15T15:20:22.556182Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=221, 2026-09-15T15:20:22.556182Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=221, 2026-09-15T15:20:22.556182Z)
- `FUELINST|fuelType=OTHER|generation` = **648** (n=221, 2026-09-15T15:20:22.556182Z)
- `FUELINST|fuelType=PS|generation` = **-98** (n=221, 2026-09-15T15:20:22.556182Z)
- `FUELINST|fuelType=WIND|generation` = **10397** (n=221, 2026-09-15T15:20:22.556182Z)
- `IMBALNGC|TOTAL|imbalance` = **5817** (n=37, 2026-09-15T15:22:46.235102Z)
- `INDDEM|TOTAL|demand` = **-11917** (n=37, 2026-09-15T15:22:30.040692Z)
- `INDGEN|TOTAL|generation` = **24938** (n=37, 2026-09-15T15:22:30.040692Z)
- `MELNGC|TOTAL|margin` = **34648** (n=37, 2026-09-15T15:20:22.556182Z)
- `NDF|TOTAL|demand` = **18621** (n=38, 2026-09-15T15:17:52.300887Z)
- `TSDF|TOTAL|demand` = **19121** (n=38, 2026-09-15T15:18:07.533099Z)
- `WINDFOR|TOTAL|generation` = **17848** (n=6, 2026-09-15T12:30:22.163636Z)

## Latest publication events

- `2026-09-15T15:22:46.235102Z` — **IMBALNGC**: 1314 rows; marker `2026-09-15T15:17:00Z`
- `2026-09-15T15:22:30.040692Z` — **INDGEN**: 1314 rows; marker `2026-09-15T15:17:00Z`
- `2026-09-15T15:22:30.040692Z` — **INDDEM**: 1314 rows; marker `2026-09-15T15:17:00Z`
- `2026-09-15T15:22:14.457631Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:21:45Z`
- `2026-09-15T15:20:22.556182Z` — **MELNGC**: 1314 rows; marker `2026-09-15T15:17:00Z`
- `2026-09-15T15:20:22.556182Z` — **FUELINST**: 80 rows; marker `2026-09-15T15:20:00Z`
- `2026-09-15T15:20:06.936814Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:19:45Z`
- `2026-09-15T15:18:07.533099Z` — **TSDF**: 1314 rows; marker `2026-09-15T15:17:00Z`
- `2026-09-15T15:18:07.533099Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:17:45Z`
- `2026-09-15T15:17:52.300887Z` — **NDF**: 73 rows; marker `2026-09-15T15:17:00Z`
- `2026-09-15T15:16:32.298143Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:15:45Z`
- `2026-09-15T15:15:59.994261Z` — **FUELINST**: 80 rows; marker `2026-09-15T15:15:00Z`
- `2026-09-15T15:14:22.354940Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:13:45Z`
- `2026-09-15T15:12:14.298408Z` — **MID**: 0 rows; marker `2026-09-15T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T15:12:14.298408Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:11:45Z`
