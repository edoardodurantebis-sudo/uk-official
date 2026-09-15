# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T12:05:17.664906Z`  
Current process started UTC: `2026-09-15T12:01:17.250696Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=1000, delta=1, z=3.83 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=181, 2026-09-15T12:00:43.048650Z)
- `FUELINST|fuelType=NPSHYD|generation` = **409** (n=181, 2026-09-15T12:00:43.048650Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=181, 2026-09-15T12:00:43.048650Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=181, 2026-09-15T12:00:43.048650Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=181, 2026-09-15T12:00:43.048650Z)
- `FUELINST|fuelType=OTHER|generation` = **462** (n=181, 2026-09-15T12:00:43.048650Z)
- `FUELINST|fuelType=PS|generation` = **-1118** (n=181, 2026-09-15T12:00:43.048650Z)
- `FUELINST|fuelType=WIND|generation` = **10561** (n=181, 2026-09-15T12:00:43.048650Z)
- `IMBALNGC|TOTAL|imbalance` = **5650** (n=30, 2026-09-15T11:53:45.899936Z)
- `INDDEM|TOTAL|demand` = **-11901** (n=30, 2026-09-15T11:53:30.375632Z)
- `INDGEN|TOTAL|generation` = **24753** (n=30, 2026-09-15T11:53:30.375632Z)
- `MELNGC|TOTAL|margin` = **35184** (n=30, 2026-09-15T11:50:38.051324Z)
- `NDF|TOTAL|demand` = **18604** (n=31, 2026-09-15T11:48:29.491494Z)
- `TSDF|TOTAL|demand` = **19104** (n=31, 2026-09-15T11:48:29.491494Z)
- `WINDFOR|TOTAL|generation` = **17599** (n=5, 2026-09-15T10:30:45.227650Z)

## Latest publication events

- `2026-09-15T12:04:14.259958Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:03:45Z`
- `2026-09-15T12:02:21.295964Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:01:45Z`
- `2026-09-15T12:00:43.048650Z` — **FUELHH**: 20 rows; marker `2026-09-15T12:00:00Z`
- `2026-09-15T12:00:43.048650Z` — **FUELINST**: 80 rows; marker `2026-09-15T12:00:00Z`
- `2026-09-15T12:00:26.685028Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:59:45Z`
- `2026-09-15T11:58:18.829795Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:57:45Z`
- `2026-09-15T11:56:25.715261Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:55:45Z`
- `2026-09-15T11:55:37.384479Z` — **FUELINST**: 80 rows; marker `2026-09-15T11:55:00Z`
- `2026-09-15T11:54:17.495455Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:53:45Z`
- `2026-09-15T11:53:45.899936Z` — **IMBALNGC**: 1440 rows; marker `2026-09-15T11:48:00Z`
- `2026-09-15T11:53:30.375632Z` — **INDGEN**: 1440 rows; marker `2026-09-15T11:48:00Z`
- `2026-09-15T11:53:30.375632Z` — **INDDEM**: 1440 rows; marker `2026-09-15T11:48:00Z`
- `2026-09-15T11:52:13.801732Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:51:45Z`
- `2026-09-15T11:50:38.051324Z` — **MELNGC**: 1440 rows; marker `2026-09-15T11:48:00Z`
- `2026-09-15T11:50:38.051324Z` — **FUELINST**: 80 rows; marker `2026-09-15T11:50:00Z`
