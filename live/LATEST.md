# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T15:14:24.814350Z`  
Current process started UTC: `2026-09-15T15:10:22.526884Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **453** (n=219, 2026-09-15T15:10:22.526891Z)
- `FUELINST|fuelType=NPSHYD|generation` = **419** (n=219, 2026-09-15T15:10:22.526891Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=219, 2026-09-15T15:10:22.526891Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=219, 2026-09-15T15:10:22.526891Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=219, 2026-09-15T15:10:22.526891Z)
- `FUELINST|fuelType=OTHER|generation` = **546** (n=219, 2026-09-15T15:10:22.526891Z)
- `FUELINST|fuelType=PS|generation` = **-163** (n=219, 2026-09-15T15:10:22.526891Z)
- `FUELINST|fuelType=WIND|generation` = **10520** (n=219, 2026-09-15T15:10:22.526891Z)
- `IMBALNGC|TOTAL|imbalance` = **5818** (n=36, 2026-09-15T14:53:27.847430Z)
- `INDDEM|TOTAL|demand` = **-11918** (n=36, 2026-09-15T14:53:27.847430Z)
- `INDGEN|TOTAL|generation` = **24939** (n=36, 2026-09-15T14:53:12.545007Z)
- `MELNGC|TOTAL|margin` = **34624** (n=36, 2026-09-15T14:50:32.815739Z)
- `NDF|TOTAL|demand` = **18621** (n=37, 2026-09-15T14:48:14.836485Z)
- `TSDF|TOTAL|demand` = **19121** (n=37, 2026-09-15T14:48:14.836485Z)
- `WINDFOR|TOTAL|generation` = **17848** (n=6, 2026-09-15T12:30:22.163636Z)

## Latest publication events

- `2026-09-15T15:14:22.354940Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:13:45Z`
- `2026-09-15T15:12:14.298408Z` — **MID**: 0 rows; marker `2026-09-15T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T15:12:14.298408Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:11:45Z`
- `2026-09-15T15:10:22.526891Z` — **FUELINST**: 80 rows; marker `2026-09-15T15:10:00Z`
- `2026-09-15T15:10:22.526891Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:09:45Z`
- `2026-09-15T15:08:03.762970Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:07:45Z`
- `2026-09-15T15:06:28.346017Z` — **MID**: 0 rows; marker `2026-09-15T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T15:06:28.346017Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:05:45Z`
- `2026-09-15T15:05:33.230682Z` — **FUELINST**: 80 rows; marker `2026-09-15T15:05:00Z`
- `2026-09-15T15:04:13.990943Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:03:45Z`
- `2026-09-15T15:02:06.361945Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:01:45Z`
- `2026-09-15T15:00:46.403732Z` — **FUELINST**: 80 rows; marker `2026-09-15T15:00:00Z`
- `2026-09-15T15:00:30.401903Z` — **FUELHH**: 20 rows; marker `2026-09-15T15:00:00Z`
- `2026-09-15T15:00:14.846980Z` — **FREQ**: 5761 rows; marker `2026-09-15T14:59:45Z`
- `2026-09-15T14:58:23.283087Z` — **FREQ**: 5761 rows; marker `2026-09-15T14:57:45Z`
