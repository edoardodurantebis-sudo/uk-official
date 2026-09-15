# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T12:34:47.590663Z`  
Current process started UTC: `2026-09-15T12:30:48.140734Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=187, 2026-09-15T12:30:22.163636Z)
- `FUELINST|fuelType=NPSHYD|generation` = **356** (n=187, 2026-09-15T12:30:22.163636Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=187, 2026-09-15T12:30:22.163636Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=187, 2026-09-15T12:30:22.163636Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=187, 2026-09-15T12:30:22.163636Z)
- `FUELINST|fuelType=OTHER|generation` = **586** (n=187, 2026-09-15T12:30:22.163636Z)
- `FUELINST|fuelType=PS|generation` = **-1079** (n=187, 2026-09-15T12:30:22.163636Z)
- `FUELINST|fuelType=WIND|generation` = **10795** (n=187, 2026-09-15T12:30:22.163636Z)
- `IMBALNGC|TOTAL|imbalance` = **5650** (n=31, 2026-09-15T12:23:27.061734Z)
- `INDDEM|TOTAL|demand` = **-11898** (n=31, 2026-09-15T12:23:27.061734Z)
- `INDGEN|TOTAL|generation` = **24754** (n=31, 2026-09-15T12:23:11.180817Z)
- `MELNGC|TOTAL|margin` = **35178** (n=31, 2026-09-15T12:20:35.294204Z)
- `NDF|TOTAL|demand` = **18604** (n=32, 2026-09-15T12:18:26.250837Z)
- `TSDF|TOTAL|demand` = **19104** (n=32, 2026-09-15T12:18:26.250837Z)
- `WINDFOR|TOTAL|generation` = **17848** (n=6, 2026-09-15T12:30:22.163636Z)

## Latest publication events

- `2026-09-15T12:34:18.955836Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:33:45Z`
- `2026-09-15T12:32:11.087027Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:31:45Z`
- `2026-09-15T12:30:48.140744Z` — **FUELHH**: 20 rows; marker `2026-09-15T12:30:00Z`
- `2026-09-15T12:30:22.163636Z` — **WINDFOR**: 73 rows; marker `2026-09-15T12:30:00Z`
- `2026-09-15T12:30:22.163636Z` — **FUELINST**: 80 rows; marker `2026-09-15T12:30:00Z`
- `2026-09-15T12:30:22.163636Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:29:45Z`
- `2026-09-15T12:28:12.429079Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:27:45Z`
- `2026-09-15T12:26:07.126362Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:25:45Z`
- `2026-09-15T12:25:35.608981Z` — **FUELINST**: 80 rows; marker `2026-09-15T12:25:00Z`
- `2026-09-15T12:24:15.284753Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:23:45Z`
- `2026-09-15T12:23:27.061734Z` — **INDDEM**: 1422 rows; marker `2026-09-15T12:17:00Z`
- `2026-09-15T12:23:27.061734Z` — **IMBALNGC**: 1422 rows; marker `2026-09-15T12:17:00Z`
- `2026-09-15T12:23:11.180817Z` — **INDGEN**: 1422 rows; marker `2026-09-15T12:17:00Z`
- `2026-09-15T12:22:22.940814Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:21:45Z`
- `2026-09-15T12:20:35.294204Z` — **MELNGC**: 1422 rows; marker `2026-09-15T12:17:00Z`
