# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T12:51:33.315634Z`  
Current process started UTC: `2026-09-15T12:47:33.345461Z`  
1-second metadata polls in this process: **232**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=191, 2026-09-15T12:50:28.143978Z)
- `FUELINST|fuelType=NPSHYD|generation` = **385** (n=191, 2026-09-15T12:50:28.143978Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=191, 2026-09-15T12:50:28.143978Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=191, 2026-09-15T12:50:28.143978Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=191, 2026-09-15T12:50:28.143978Z)
- `FUELINST|fuelType=OTHER|generation` = **387** (n=191, 2026-09-15T12:50:28.143978Z)
- `FUELINST|fuelType=PS|generation` = **-1082** (n=191, 2026-09-15T12:50:28.143978Z)
- `FUELINST|fuelType=WIND|generation` = **10425** (n=191, 2026-09-15T12:50:28.143978Z)
- `IMBALNGC|TOTAL|imbalance` = **5650** (n=31, 2026-09-15T12:23:27.061734Z)
- `INDDEM|TOTAL|demand` = **-11898** (n=31, 2026-09-15T12:23:27.061734Z)
- `INDGEN|TOTAL|generation` = **24754** (n=31, 2026-09-15T12:23:11.180817Z)
- `MELNGC|TOTAL|margin` = **35174** (n=32, 2026-09-15T12:50:12.086867Z)
- `NDF|TOTAL|demand` = **18604** (n=33, 2026-09-15T12:48:05.349471Z)
- `TSDF|TOTAL|demand` = **19104** (n=33, 2026-09-15T12:48:05.349471Z)
- `WINDFOR|TOTAL|generation` = **17848** (n=6, 2026-09-15T12:30:22.163636Z)

## Latest publication events

- `2026-09-15T12:50:28.143978Z` — **FUELINST**: 80 rows; marker `2026-09-15T12:50:00Z`
- `2026-09-15T12:50:12.086867Z` — **MELNGC**: 1404 rows; marker `2026-09-15T12:47:00Z`
- `2026-09-15T12:50:12.086867Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:49:45Z`
- `2026-09-15T12:48:21.248291Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:47:45Z`
- `2026-09-15T12:48:05.349471Z` — **TSDF**: 1404 rows; marker `2026-09-15T12:47:00Z`
- `2026-09-15T12:48:05.349471Z` — **NDF**: 78 rows; marker `2026-09-15T12:47:00Z`
- `2026-09-15T12:46:16.362246Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:45:45Z`
- `2026-09-15T12:45:28.692638Z` — **FUELINST**: 80 rows; marker `2026-09-15T12:45:00Z`
- `2026-09-15T12:44:24.697926Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:43:45Z`
- `2026-09-15T12:42:22.286249Z` — **MID**: 0 rows; marker `2026-09-15T12:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T12:42:22.286249Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:41:45Z`
- `2026-09-15T12:40:29.318105Z` — **FUELINST**: 80 rows; marker `2026-09-15T12:40:00Z`
- `2026-09-15T12:40:13.390089Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:39:45Z`
- `2026-09-15T12:38:12.149902Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:37:45Z`
- `2026-09-15T12:36:35.949120Z` — **MID**: 0 rows; marker `2026-09-15T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
