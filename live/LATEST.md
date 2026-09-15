# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T11:01:34.134558Z`  
Current process started UTC: `2026-09-15T10:57:34.123329Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELHH** `fuelType=INTIFA2` `generation` — half-hour generation mix [fuelType=INTIFA2] generation: value=828, delta=552, z=3.62 -> generation-mix component moved
- **FUELHH** `fuelType=INTFR` `generation` — half-hour generation mix [fuelType=INTFR] generation: value=674, delta=468, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=0, z=3.70 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=0, z=3.92 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=0, z=4.18 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=169, 2026-09-15T11:00:30.014168Z)
- `FUELINST|fuelType=NPSHYD|generation` = **410** (n=169, 2026-09-15T11:00:30.014168Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=169, 2026-09-15T11:00:30.014168Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=169, 2026-09-15T11:00:30.014168Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=169, 2026-09-15T11:00:30.014168Z)
- `FUELINST|fuelType=OTHER|generation` = **912** (n=169, 2026-09-15T11:00:30.014168Z)
- `FUELINST|fuelType=PS|generation` = **-1200** (n=169, 2026-09-15T11:00:30.014168Z)
- `FUELINST|fuelType=WIND|generation` = **11495** (n=169, 2026-09-15T11:00:30.014168Z)
- `IMBALNGC|TOTAL|imbalance` = **-832** (n=27, 2026-09-15T10:19:25.748675Z)
- `INDDEM|TOTAL|demand` = **-12270** (n=27, 2026-09-15T10:19:25.748675Z)
- `INDGEN|TOTAL|generation` = **19737** (n=27, 2026-09-15T10:19:25.748675Z)
- `MELNGC|TOTAL|margin` = **35212** (n=28, 2026-09-15T10:55:12.649432Z)
- `NDF|TOTAL|demand` = **18604** (n=29, 2026-09-15T10:51:02.252130Z)
- `TSDF|TOTAL|demand` = **19104** (n=29, 2026-09-15T10:51:02.252130Z)
- `WINDFOR|TOTAL|generation` = **17599** (n=5, 2026-09-15T10:30:45.227650Z)

## Latest publication events

- `2026-09-15T11:00:46.444783Z` — **FUELHH**: 20 rows; marker `2026-09-15T11:00:00Z`
- `2026-09-15T11:00:30.014168Z` — **FUELINST**: 80 rows; marker `2026-09-15T11:00:00Z`
- `2026-09-15T11:00:14.572046Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:59:45Z`
- `2026-09-15T10:58:22.309791Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:57:45Z`
- `2026-09-15T10:56:16.335274Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:55:45Z`
- `2026-09-15T10:55:28.691177Z` — **FUELINST**: 80 rows; marker `2026-09-15T10:55:00Z`
- `2026-09-15T10:55:12.649432Z` — **MELNGC**: 1476 rows; marker `2026-09-15T10:50:00Z`
- `2026-09-15T10:54:24.246222Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:53:45Z`
- `2026-09-15T10:52:22.195580Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:51:45Z`
- `2026-09-15T10:51:02.252130Z` — **TSDF**: 1476 rows; marker `2026-09-15T10:50:00Z`
- `2026-09-15T10:51:02.252130Z` — **NDF**: 82 rows; marker `2026-09-15T10:50:00Z`
- `2026-09-15T10:50:29.025353Z` — **FUELINST**: 80 rows; marker `2026-09-15T10:50:00Z`
- `2026-09-15T10:50:12.479255Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:49:45Z`
- `2026-09-15T10:48:21.547975Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:47:45Z`
- `2026-09-15T10:46:12.929596Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:45:45Z`
