# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T09:19:04.464084Z`  
Current process started UTC: `2026-09-15T09:15:04.136631Z`  
1-second metadata polls in this process: **231**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=20619, delta=1396, z=0.72 -> demand pressure up
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=20069, delta=1346, z=0.74 -> demand pressure up
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=0, z=4.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=162, z=4.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=538, delta=280, z=3.81 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=148, 2026-09-15T09:15:36.208421Z)
- `FUELINST|fuelType=NPSHYD|generation` = **418** (n=148, 2026-09-15T09:15:36.208421Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3317** (n=148, 2026-09-15T09:15:36.208421Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=148, 2026-09-15T09:15:36.208421Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=148, 2026-09-15T09:15:36.208421Z)
- `FUELINST|fuelType=OTHER|generation` = **560** (n=148, 2026-09-15T09:15:36.208421Z)
- `FUELINST|fuelType=PS|generation` = **-1160** (n=148, 2026-09-15T09:15:36.208421Z)
- `FUELINST|fuelType=WIND|generation` = **12042** (n=148, 2026-09-15T09:15:36.208421Z)
- `IMBALNGC|TOTAL|imbalance` = **-135** (n=24, 2026-09-15T08:49:57.718820Z)
- `INDDEM|TOTAL|demand` = **-12399** (n=24, 2026-09-15T08:49:57.718820Z)
- `INDGEN|TOTAL|generation` = **20434** (n=24, 2026-09-15T08:49:57.718820Z)
- `MELNGC|TOTAL|margin` = **34498** (n=25, 2026-09-15T09:18:50.361079Z)
- `NDF|TOTAL|demand` = **20069** (n=26, 2026-09-15T09:16:58.629698Z)
- `TSDF|TOTAL|demand` = **20569** (n=26, 2026-09-15T09:16:58.629698Z)
- `WINDFOR|TOTAL|generation` = **16741** (n=4, 2026-09-15T08:30:37.267850Z)

## Latest publication events

- `2026-09-15T09:18:50.361079Z` — **MELNGC**: 666 rows; marker `2026-09-15T09:16:00Z`
- `2026-09-15T09:18:18.299236Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:17:45Z`
- `2026-09-15T09:16:58.629698Z` — **TSDF**: 666 rows; marker `2026-09-15T09:16:00Z`
- `2026-09-15T09:16:58.629698Z` — **NDF**: 37 rows; marker `2026-09-15T09:16:00Z`
- `2026-09-15T09:16:25.417192Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:15:45Z`
- `2026-09-15T09:15:36.208421Z` — **FUELINST**: 80 rows; marker `2026-09-15T09:15:00Z`
- `2026-09-15T09:14:23.087066Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:13:45Z`
- `2026-09-15T09:12:14.742046Z` — **MID**: 0 rows; marker `2026-09-15T09:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T09:12:14.742046Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:11:45Z`
- `2026-09-15T09:10:23.307837Z` — **FUELINST**: 80 rows; marker `2026-09-15T09:10:00Z`
- `2026-09-15T09:10:23.307837Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:09:45Z`
- `2026-09-15T09:08:15.816522Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:07:45Z`
- `2026-09-15T09:06:39.503711Z` — **MID**: 0 rows; marker `2026-09-15T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T09:06:17.502812Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:05:45Z`
- `2026-09-15T09:05:29.446639Z` — **FUELINST**: 80 rows; marker `2026-09-15T09:05:00Z`
