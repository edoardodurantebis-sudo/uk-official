# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T13:16:43.889585Z`  
Current process started UTC: `2026-09-15T13:12:44.283461Z`  
1-second metadata polls in this process: **234**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=196, 2026-09-15T13:15:40.028374Z)
- `FUELINST|fuelType=NPSHYD|generation` = **378** (n=196, 2026-09-15T13:15:40.028374Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=196, 2026-09-15T13:15:40.028374Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=196, 2026-09-15T13:15:40.028374Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=196, 2026-09-15T13:15:40.028374Z)
- `FUELINST|fuelType=OTHER|generation` = **612** (n=196, 2026-09-15T13:15:40.028374Z)
- `FUELINST|fuelType=PS|generation` = **-955** (n=196, 2026-09-15T13:15:40.028374Z)
- `FUELINST|fuelType=WIND|generation` = **10070** (n=196, 2026-09-15T13:15:40.028374Z)
- `IMBALNGC|TOTAL|imbalance` = **5698** (n=32, 2026-09-15T12:53:25.162980Z)
- `INDDEM|TOTAL|demand` = **-11920** (n=32, 2026-09-15T12:53:09.844792Z)
- `INDGEN|TOTAL|generation` = **24801** (n=32, 2026-09-15T12:53:09.844792Z)
- `MELNGC|TOTAL|margin` = **35174** (n=32, 2026-09-15T12:50:12.086867Z)
- `NDF|TOTAL|demand` = **18604** (n=33, 2026-09-15T12:48:05.349471Z)
- `TSDF|TOTAL|demand` = **19104** (n=33, 2026-09-15T12:48:05.349471Z)
- `WINDFOR|TOTAL|generation` = **17848** (n=6, 2026-09-15T12:30:22.163636Z)

## Latest publication events

- `2026-09-15T13:16:13.517529Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:15:45Z`
- `2026-09-15T13:15:40.028374Z` — **FUELINST**: 80 rows; marker `2026-09-15T13:15:00Z`
- `2026-09-15T13:14:04.333788Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:13:45Z`
- `2026-09-15T13:12:17.257426Z` — **MID**: 0 rows; marker `2026-09-15T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T13:12:17.257426Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:11:45Z`
- `2026-09-15T13:10:25.712439Z` — **FUELINST**: 80 rows; marker `2026-09-15T13:10:00Z`
- `2026-09-15T13:10:09.277004Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:09:45Z`
- `2026-09-15T13:08:32.043008Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:07:45Z`
- `2026-09-15T13:07:32.170333Z` — **MID**: 0 rows; marker `2026-09-15T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T13:06:11.927080Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:05:45Z`
- `2026-09-15T13:05:40.363281Z` — **FUELINST**: 80 rows; marker `2026-09-15T13:05:00Z`
- `2026-09-15T13:04:19.562366Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:03:45Z`
- `2026-09-15T13:02:20.237502Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:01:45Z`
- `2026-09-15T13:00:44.012653Z` — **FUELHH**: 20 rows; marker `2026-09-15T13:00:00Z`
- `2026-09-15T13:00:44.012653Z` — **FUELINST**: 80 rows; marker `2026-09-15T13:00:00Z`
