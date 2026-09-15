# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T11:22:30.583584Z`  
Current process started UTC: `2026-09-15T11:18:30.139722Z`  
1-second metadata polls in this process: **233**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=913, delta=181, z=3.84 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=0, z=3.52 -> generation-mix component moved
- **FUELHH** `fuelType=INTNEM` `generation` — half-hour generation mix [fuelType=INTNEM] generation: value=1016, delta=192, z=3.59 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=173, 2026-09-15T11:20:37.187608Z)
- `FUELINST|fuelType=NPSHYD|generation` = **427** (n=173, 2026-09-15T11:20:37.187608Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=173, 2026-09-15T11:20:37.187608Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=173, 2026-09-15T11:20:37.187608Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=173, 2026-09-15T11:20:37.187608Z)
- `FUELINST|fuelType=OTHER|generation` = **976** (n=173, 2026-09-15T11:20:37.187608Z)
- `FUELINST|fuelType=PS|generation` = **-1200** (n=173, 2026-09-15T11:20:37.187608Z)
- `FUELINST|fuelType=WIND|generation` = **11294** (n=173, 2026-09-15T11:20:37.187608Z)
- `IMBALNGC|TOTAL|imbalance` = **5675** (n=28, 2026-09-15T11:04:58.801222Z)
- `INDDEM|TOTAL|demand` = **-11901** (n=28, 2026-09-15T11:04:43.146962Z)
- `INDGEN|TOTAL|generation` = **24779** (n=28, 2026-09-15T11:04:43.146962Z)
- `MELNGC|TOTAL|margin` = **35518** (n=29, 2026-09-15T11:20:21.345799Z)
- `NDF|TOTAL|demand` = **18604** (n=30, 2026-09-15T11:18:07.421422Z)
- `TSDF|TOTAL|demand` = **19104** (n=30, 2026-09-15T11:18:07.421422Z)
- `WINDFOR|TOTAL|generation` = **17599** (n=5, 2026-09-15T10:30:45.227650Z)

## Latest publication events

- `2026-09-15T11:22:13.130396Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:21:45Z`
- `2026-09-15T11:20:37.187608Z` — **FUELINST**: 80 rows; marker `2026-09-15T11:20:00Z`
- `2026-09-15T11:20:21.345799Z` — **MELNGC**: 1458 rows; marker `2026-09-15T11:17:00Z`
- `2026-09-15T11:20:05.980632Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:19:45Z`
- `2026-09-15T11:18:30.139731Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:17:45Z`
- `2026-09-15T11:18:07.421422Z` — **TSDF**: 1458 rows; marker `2026-09-15T11:17:00Z`
- `2026-09-15T11:18:07.421422Z` — **NDF**: 81 rows; marker `2026-09-15T11:17:00Z`
- `2026-09-15T11:16:31.671108Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:15:45Z`
- `2026-09-15T11:15:43.663772Z` — **FUELINST**: 80 rows; marker `2026-09-15T11:15:00Z`
- `2026-09-15T11:14:23.385656Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:13:45Z`
- `2026-09-15T11:12:16.124290Z` — **MID**: 0 rows; marker `2026-09-15T11:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T11:12:16.124290Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:11:45Z`
- `2026-09-15T11:10:40.094332Z` — **FUELINST**: 80 rows; marker `2026-09-15T11:10:00Z`
- `2026-09-15T11:10:23.914086Z` — **FREQ**: 5761 rows; marker `2026-09-15T11:09:45Z`
- `2026-09-15T11:09:25.149863Z` — **MID**: 0 rows; marker `2026-09-15T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
