# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T13:25:09.784633Z`  
Current process started UTC: `2026-09-15T13:21:10.007173Z`  
1-second metadata polls in this process: **233**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=197, 2026-09-15T13:20:26.394427Z)
- `FUELINST|fuelType=NPSHYD|generation` = **379** (n=197, 2026-09-15T13:20:26.394427Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=197, 2026-09-15T13:20:26.394427Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=197, 2026-09-15T13:20:26.394427Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=197, 2026-09-15T13:20:26.394427Z)
- `FUELINST|fuelType=OTHER|generation` = **601** (n=197, 2026-09-15T13:20:26.394427Z)
- `FUELINST|fuelType=PS|generation` = **-958** (n=197, 2026-09-15T13:20:26.394427Z)
- `FUELINST|fuelType=WIND|generation` = **10085** (n=197, 2026-09-15T13:20:26.394427Z)
- `IMBALNGC|TOTAL|imbalance` = **5698** (n=33, 2026-09-15T13:23:17.906702Z)
- `INDDEM|TOTAL|demand` = **-11916** (n=33, 2026-09-15T13:23:01.847955Z)
- `INDGEN|TOTAL|generation` = **24819** (n=33, 2026-09-15T13:23:01.847955Z)
- `MELNGC|TOTAL|margin` = **35161** (n=33, 2026-09-15T13:20:10.322251Z)
- `NDF|TOTAL|demand` = **18621** (n=34, 2026-09-15T13:18:17.906032Z)
- `TSDF|TOTAL|demand` = **19121** (n=34, 2026-09-15T13:18:17.906032Z)
- `WINDFOR|TOTAL|generation` = **17848** (n=6, 2026-09-15T12:30:22.163636Z)

## Latest publication events

- `2026-09-15T13:24:06.616432Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:23:45Z`
- `2026-09-15T13:23:17.906702Z` — **IMBALNGC**: 1386 rows; marker `2026-09-15T13:17:00Z`
- `2026-09-15T13:23:01.847955Z` — **INDGEN**: 1386 rows; marker `2026-09-15T13:17:00Z`
- `2026-09-15T13:23:01.847955Z` — **INDDEM**: 1386 rows; marker `2026-09-15T13:17:00Z`
- `2026-09-15T13:22:14.459162Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:21:45Z`
- `2026-09-15T13:20:26.394427Z` — **FUELINST**: 80 rows; marker `2026-09-15T13:20:00Z`
- `2026-09-15T13:20:26.394427Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:19:45Z`
- `2026-09-15T13:20:10.322251Z` — **MELNGC**: 1386 rows; marker `2026-09-15T13:17:00Z`
- `2026-09-15T13:18:17.906032Z` — **TSDF**: 1386 rows; marker `2026-09-15T13:17:00Z`
- `2026-09-15T13:18:17.906032Z` — **NDF**: 77 rows; marker `2026-09-15T13:17:00Z`
- `2026-09-15T13:18:17.906032Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:17:45Z`
- `2026-09-15T13:16:13.517529Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:15:45Z`
- `2026-09-15T13:15:40.028374Z` — **FUELINST**: 80 rows; marker `2026-09-15T13:15:00Z`
- `2026-09-15T13:14:04.333788Z` — **FREQ**: 5761 rows; marker `2026-09-15T13:13:45Z`
- `2026-09-15T13:12:17.257426Z` — **MID**: 0 rows; marker `2026-09-15T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
