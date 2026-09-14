# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T22:12:32.875934Z`  
Current process started UTC: `2026-09-14T22:08:32.452947Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=1193, delta=90, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=INTIFA2` `generation` — instantaneous generation mix [fuelType=INTIFA2] generation: value=-889, delta=-56, z=-4.14 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=1, delta=-96, z=-5.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTIFA2` `generation` — instantaneous generation mix [fuelType=INTIFA2] generation: value=-833, delta=-111, z=-5.27 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=97, delta=-182, z=-28.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=279, delta=-26, z=-14.31 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTNSL|generation` = **1193** (n=15, 2026-09-14T22:10:29.506785Z)
- `FUELINST|fuelType=INTVKL|generation` = **-669** (n=15, 2026-09-14T22:10:29.506785Z)
- `FUELINST|fuelType=NPSHYD|generation` = **416** (n=15, 2026-09-14T22:10:29.506785Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3317** (n=15, 2026-09-14T22:10:29.506785Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=15, 2026-09-14T22:10:29.506785Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=15, 2026-09-14T22:10:29.506785Z)
- `FUELINST|fuelType=OTHER|generation` = **113** (n=15, 2026-09-14T22:10:29.506785Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=15, 2026-09-14T22:10:29.506785Z)
- `FUELINST|fuelType=WIND|generation` = **12770** (n=15, 2026-09-14T22:10:29.506785Z)
- `IMBALNGC|TOTAL|imbalance` = **-15** (n=3, 2026-09-14T21:51:44.824674Z)
- `INDDEM|TOTAL|demand` = **-12253** (n=3, 2026-09-14T21:51:44.824674Z)
- `INDGEN|TOTAL|generation` = **20469** (n=3, 2026-09-14T21:51:44.824674Z)
- `MELNGC|TOTAL|margin` = **32283** (n=3, 2026-09-14T21:50:04.672506Z)
- `NDF|TOTAL|demand` = **19934** (n=3, 2026-09-14T21:47:57.557399Z)
- `TSDF|TOTAL|demand` = **20485** (n=3, 2026-09-14T21:47:57.557399Z)

## Latest publication events

- `2026-09-14T22:12:21.198449Z` — **MID**: 0 rows; marker `2026-09-14T22:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T22:12:21.198449Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:11:45Z`
- `2026-09-14T22:10:29.506785Z` — **FUELINST**: 80 rows; marker `2026-09-14T22:10:00Z`
- `2026-09-14T22:10:13.228517Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:09:45Z`
- `2026-09-14T22:08:20.447032Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:07:45Z`
- `2026-09-14T22:07:16.198271Z` — **MID**: 0 rows; marker `2026-09-14T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T22:06:12.483569Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:05:45Z`
- `2026-09-14T22:05:40.444284Z` — **FUELINST**: 80 rows; marker `2026-09-14T22:05:00Z`
- `2026-09-14T22:04:20.955377Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:03:45Z`
- `2026-09-14T22:02:19.801410Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:01:45Z`
- `2026-09-14T22:00:58.473805Z` — **FUELHH**: 20 rows; marker `2026-09-14T22:00:00Z`
- `2026-09-14T22:00:26.225522Z` — **FUELINST**: 80 rows; marker `2026-09-14T22:00:00Z`
- `2026-09-14T22:00:26.225522Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:59:45Z`
- `2026-09-14T21:58:22.313211Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:57:45Z`
- `2026-09-14T21:56:13.927850Z` — **FREQ**: 5761 rows; marker `2026-09-14T21:55:45Z`
