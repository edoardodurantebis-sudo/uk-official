# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T11:39:18.573405Z`  
Current process started UTC: `2026-09-15T11:35:18.196364Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=1000, delta=1, z=3.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=999, delta=86, z=4.05 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=176, 2026-09-15T11:35:34.198276Z)
- `FUELINST|fuelType=NPSHYD|generation` = **434** (n=176, 2026-09-15T11:35:34.198276Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=176, 2026-09-15T11:35:34.198276Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=176, 2026-09-15T11:35:34.198276Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=176, 2026-09-15T11:35:34.198276Z)
- `FUELINST|fuelType=OTHER|generation` = **690** (n=176, 2026-09-15T11:35:34.198276Z)
- `FUELINST|fuelType=PS|generation` = **-1212** (n=176, 2026-09-15T11:35:34.198276Z)
- `FUELINST|fuelType=WIND|generation` = **11212** (n=176, 2026-09-15T11:35:34.198276Z)
- `IMBALNGC|TOTAL|imbalance` = **5651** (n=29, 2026-09-15T11:24:04.689154Z)
- `INDDEM|TOTAL|demand` = **-11901** (n=29, 2026-09-15T11:23:49.076924Z)
- `INDGEN|TOTAL|generation` = **24755** (n=29, 2026-09-15T11:23:49.076924Z)
- `MELNGC|TOTAL|margin` = **35518** (n=29, 2026-09-15T11:20:21.345799Z)
- `NDF|TOTAL|demand` = **18604** (n=30, 2026-09-15T11:18:07.421422Z)
- `TSDF|TOTAL|demand` = **19104** (n=30, 2026-09-15T11:18:07.421422Z)
- `WINDFOR|TOTAL|generation` = **17599** (n=5, 2026-09-15T10:30:45.227650Z)

## Latest publication events

- `2026-09-15T11:38:13.460282Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:37:45Z`
- `2026-09-15T11:36:21.983734Z` — **MID**: 0 rows; marker `2026-09-15T11:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T11:36:06.340387Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:35:45Z`
- `2026-09-15T11:35:34.198276Z` — **FUELINST**: 80 rows; marker `2026-09-15T11:35:00Z`
- `2026-09-15T11:34:08.159070Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:33:45Z`
- `2026-09-15T11:32:15.203887Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:31:45Z`
- `2026-09-15T11:30:54.139807Z` — **FUELHH**: 20 rows; marker `2026-09-15T11:30:00Z`
- `2026-09-15T11:30:38.680892Z` — **FUELINST**: 80 rows; marker `2026-09-15T11:30:00Z`
- `2026-09-15T11:30:07.070594Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:29:45Z`
- `2026-09-15T11:28:14.931339Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:27:45Z`
- `2026-09-15T11:26:12.685666Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:25:45Z`
- `2026-09-15T11:25:25.203779Z` — **FUELINST**: 80 rows; marker `2026-09-15T11:25:00Z`
- `2026-09-15T11:24:04.689154Z` — **IMBALNGC**: 1458 rows; marker `2026-09-15T11:17:00Z`
- `2026-09-15T11:24:04.689154Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:23:45Z`
- `2026-09-15T11:23:49.076924Z` — **INDGEN**: 1458 rows; marker `2026-09-15T11:17:00Z`
