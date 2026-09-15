# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T14:19:39.877060Z`  
Current process started UTC: `2026-09-15T14:15:40.468555Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1202** (n=208, 2026-09-15T14:15:40.468567Z)
- `FUELINST|fuelType=NPSHYD|generation` = **334** (n=208, 2026-09-15T14:15:40.468567Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3327** (n=208, 2026-09-15T14:15:40.468567Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=208, 2026-09-15T14:15:40.468567Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=208, 2026-09-15T14:15:40.468567Z)
- `FUELINST|fuelType=OTHER|generation` = **393** (n=208, 2026-09-15T14:15:40.468567Z)
- `FUELINST|fuelType=PS|generation` = **-609** (n=208, 2026-09-15T14:15:40.468567Z)
- `FUELINST|fuelType=WIND|generation` = **10484** (n=208, 2026-09-15T14:15:40.468567Z)
- `IMBALNGC|TOTAL|imbalance` = **5710** (n=34, 2026-09-15T13:53:12.812024Z)
- `INDDEM|TOTAL|demand` = **-11915** (n=34, 2026-09-15T13:53:12.812024Z)
- `INDGEN|TOTAL|generation` = **24831** (n=34, 2026-09-15T13:53:12.812024Z)
- `MELNGC|TOTAL|margin` = **35198** (n=34, 2026-09-15T13:50:31.602646Z)
- `NDF|TOTAL|demand` = **18621** (n=36, 2026-09-15T14:18:04.242685Z)
- `TSDF|TOTAL|demand` = **19121** (n=36, 2026-09-15T14:18:04.242685Z)
- `WINDFOR|TOTAL|generation` = **17848** (n=6, 2026-09-15T12:30:22.163636Z)

## Latest publication events

- `2026-09-15T14:18:19.885489Z` — **FREQ**: 5761 rows; marker `2026-09-15T14:17:45Z`
- `2026-09-15T14:18:04.242685Z` — **TSDF**: 1350 rows; marker `2026-09-15T14:17:00Z`
- `2026-09-15T14:18:04.242685Z` — **NDF**: 75 rows; marker `2026-09-15T14:17:00Z`
- `2026-09-15T14:16:12.589051Z` — **FREQ**: 5761 rows; marker `2026-09-15T14:15:45Z`
- `2026-09-15T14:15:40.468567Z` — **FUELINST**: 80 rows; marker `2026-09-15T14:15:00Z`
- `2026-09-15T14:14:08.846555Z` — **FREQ**: 5761 rows; marker `2026-09-15T14:13:45Z`
- `2026-09-15T14:12:17.026896Z` — **MID**: 0 rows; marker `2026-09-15T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T14:12:17.026896Z` — **FREQ**: 5761 rows; marker `2026-09-15T14:11:45Z`
- `2026-09-15T14:10:32.638215Z` — **FUELINST**: 80 rows; marker `2026-09-15T14:10:00Z`
- `2026-09-15T14:10:16.912368Z` — **FREQ**: 5761 rows; marker `2026-09-15T14:09:45Z`
- `2026-09-15T14:08:09.032429Z` — **FREQ**: 5761 rows; marker `2026-09-15T14:07:45Z`
- `2026-09-15T14:06:32.429486Z` — **MID**: 0 rows; marker `2026-09-15T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T14:06:01.104744Z` — **FREQ**: 5761 rows; marker `2026-09-15T14:05:45Z`
- `2026-09-15T14:05:29.371512Z` — **FUELINST**: 80 rows; marker `2026-09-15T14:05:00Z`
- `2026-09-15T14:04:10.035403Z` — **FREQ**: 5761 rows; marker `2026-09-15T14:03:45Z`
