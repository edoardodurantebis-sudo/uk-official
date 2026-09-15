# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T15:48:17.716514Z`  
Current process started UTC: `2026-09-15T15:44:17.273531Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=5, delta=0, z=5.44 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=5, delta=3, z=5.86 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **453** (n=226, 2026-09-15T15:45:36.692865Z)
- `FUELINST|fuelType=NPSHYD|generation` = **437** (n=226, 2026-09-15T15:45:36.692865Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3322** (n=226, 2026-09-15T15:45:36.692865Z)
- `FUELINST|fuelType=OCGT|generation` = **5** (n=226, 2026-09-15T15:45:36.692865Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=226, 2026-09-15T15:45:36.692865Z)
- `FUELINST|fuelType=OTHER|generation` = **687** (n=226, 2026-09-15T15:45:36.692865Z)
- `FUELINST|fuelType=PS|generation` = **-136** (n=226, 2026-09-15T15:45:36.692865Z)
- `FUELINST|fuelType=WIND|generation` = **10444** (n=226, 2026-09-15T15:45:36.692865Z)
- `IMBALNGC|TOTAL|imbalance` = **5817** (n=37, 2026-09-15T15:22:46.235102Z)
- `INDDEM|TOTAL|demand` = **-11917** (n=37, 2026-09-15T15:22:30.040692Z)
- `INDGEN|TOTAL|generation` = **24938** (n=37, 2026-09-15T15:22:30.040692Z)
- `MELNGC|TOTAL|margin` = **34648** (n=37, 2026-09-15T15:20:22.556182Z)
- `NDF|TOTAL|demand` = **18621** (n=39, 2026-09-15T15:48:00.289174Z)
- `TSDF|TOTAL|demand` = **19121** (n=39, 2026-09-15T15:48:00.289174Z)
- `WINDFOR|TOTAL|generation` = **17848** (n=6, 2026-09-15T12:30:22.163636Z)

## Latest publication events

- `2026-09-15T15:48:16.082203Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:47:45Z`
- `2026-09-15T15:48:00.289174Z` — **TSDF**: 1296 rows; marker `2026-09-15T15:47:00Z`
- `2026-09-15T15:48:00.289174Z` — **NDF**: 72 rows; marker `2026-09-15T15:47:00Z`
- `2026-09-15T15:46:24.766553Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:45:45Z`
- `2026-09-15T15:45:36.692865Z` — **FUELINST**: 80 rows; marker `2026-09-15T15:45:00Z`
- `2026-09-15T15:44:33.275540Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:43:45Z`
- `2026-09-15T15:42:17.008841Z` — **MID**: 0 rows; marker `2026-09-15T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T15:42:17.008841Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:41:45Z`
- `2026-09-15T15:40:40.891431Z` — **FUELINST**: 80 rows; marker `2026-09-15T15:40:00Z`
- `2026-09-15T15:40:25.387991Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:39:45Z`
- `2026-09-15T15:38:17.726367Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:37:45Z`
- `2026-09-15T15:37:14.467045Z` — **MID**: 0 rows; marker `2026-09-15T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T15:36:10.909072Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:35:45Z`
- `2026-09-15T15:35:27.431183Z` — **FUELINST**: 80 rows; marker `2026-09-15T15:35:00Z`
- `2026-09-15T15:34:23.237791Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:33:45Z`
