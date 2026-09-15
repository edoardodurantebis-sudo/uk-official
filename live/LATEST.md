# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T12:55:46.067543Z`  
Current process started UTC: `2026-09-15T12:51:45.783172Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=192, 2026-09-15T12:55:32.339481Z)
- `FUELINST|fuelType=NPSHYD|generation` = **384** (n=192, 2026-09-15T12:55:32.339481Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=192, 2026-09-15T12:55:32.339481Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=192, 2026-09-15T12:55:32.339481Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=192, 2026-09-15T12:55:32.339481Z)
- `FUELINST|fuelType=OTHER|generation` = **567** (n=192, 2026-09-15T12:55:32.339481Z)
- `FUELINST|fuelType=PS|generation` = **-1070** (n=192, 2026-09-15T12:55:32.339481Z)
- `FUELINST|fuelType=WIND|generation` = **10228** (n=192, 2026-09-15T12:55:32.339481Z)
- `IMBALNGC|TOTAL|imbalance` = **5698** (n=32, 2026-09-15T12:53:25.162980Z)
- `INDDEM|TOTAL|demand` = **-11920** (n=32, 2026-09-15T12:53:09.844792Z)
- `INDGEN|TOTAL|generation` = **24801** (n=32, 2026-09-15T12:53:09.844792Z)
- `MELNGC|TOTAL|margin` = **35174** (n=32, 2026-09-15T12:50:12.086867Z)
- `NDF|TOTAL|demand` = **18604** (n=33, 2026-09-15T12:48:05.349471Z)
- `TSDF|TOTAL|demand` = **19104** (n=33, 2026-09-15T12:48:05.349471Z)
- `WINDFOR|TOTAL|generation` = **17848** (n=6, 2026-09-15T12:30:22.163636Z)

## Latest publication events

- `2026-09-15T12:55:32.339481Z` — **FUELINST**: 80 rows; marker `2026-09-15T12:55:00Z`
- `2026-09-15T12:54:12.578672Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:53:45Z`
- `2026-09-15T12:53:25.162980Z` — **IMBALNGC**: 1404 rows; marker `2026-09-15T12:47:00Z`
- `2026-09-15T12:53:09.844792Z` — **INDGEN**: 1404 rows; marker `2026-09-15T12:47:00Z`
- `2026-09-15T12:53:09.844792Z` — **INDDEM**: 1404 rows; marker `2026-09-15T12:47:00Z`
- `2026-09-15T12:52:20.788068Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:51:45Z`
- `2026-09-15T12:50:28.143978Z` — **FUELINST**: 80 rows; marker `2026-09-15T12:50:00Z`
- `2026-09-15T12:50:12.086867Z` — **MELNGC**: 1404 rows; marker `2026-09-15T12:47:00Z`
- `2026-09-15T12:50:12.086867Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:49:45Z`
- `2026-09-15T12:48:21.248291Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:47:45Z`
- `2026-09-15T12:48:05.349471Z` — **TSDF**: 1404 rows; marker `2026-09-15T12:47:00Z`
- `2026-09-15T12:48:05.349471Z` — **NDF**: 78 rows; marker `2026-09-15T12:47:00Z`
- `2026-09-15T12:46:16.362246Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:45:45Z`
- `2026-09-15T12:45:28.692638Z` — **FUELINST**: 80 rows; marker `2026-09-15T12:45:00Z`
- `2026-09-15T12:44:24.697926Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:43:45Z`
