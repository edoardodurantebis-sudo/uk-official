# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T23:08:48.847748Z`  
Current process started UTC: `2026-09-16T23:04:49.373951Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.28 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.80 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.91 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=692, delta=5, z=3.75 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.97 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-373** (n=571, 2026-09-16T23:05:37.379018Z)
- `FUELINST|fuelType=NPSHYD|generation` = **437** (n=571, 2026-09-16T23:05:37.379018Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3310** (n=571, 2026-09-16T23:05:37.379018Z)
- `FUELINST|fuelType=OCGT|generation` = **24** (n=571, 2026-09-16T23:05:37.379018Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=571, 2026-09-16T23:05:37.379018Z)
- `FUELINST|fuelType=OTHER|generation` = **415** (n=571, 2026-09-16T23:05:37.379018Z)
- `FUELINST|fuelType=PS|generation` = **-248** (n=571, 2026-09-16T23:05:37.379018Z)
- `FUELINST|fuelType=WIND|generation` = **10647** (n=571, 2026-09-16T23:05:37.379018Z)
- `IMBALNGC|TOTAL|imbalance` = **6619** (n=95, 2026-09-16T23:00:38.205310Z)
- `INDDEM|TOTAL|demand` = **-11763** (n=95, 2026-09-16T23:00:38.205310Z)
- `INDGEN|TOTAL|generation` = **25740** (n=95, 2026-09-16T23:00:38.205310Z)
- `MELNGC|TOTAL|margin` = **34258** (n=95, 2026-09-16T23:00:38.205310Z)
- `NDF|TOTAL|demand` = **18621** (n=97, 2026-09-16T23:00:38.205310Z)
- `TSDF|TOTAL|demand` = **19121** (n=97, 2026-09-16T23:00:38.205310Z)
- `WINDFOR|TOTAL|generation` = **19445** (n=16, 2026-09-16T19:30:31.948327Z)

## Latest publication events

- `2026-09-16T23:08:18.198104Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:07:45Z`
- `2026-09-16T23:06:41.253299Z` — **MID**: 0 rows; marker `2026-09-16T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T23:06:25.535116Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:05:45Z`
- `2026-09-16T23:05:37.379018Z` — **FUELINST**: 80 rows; marker `2026-09-16T23:05:00Z`
- `2026-09-16T23:04:23.315999Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:03:45Z`
- `2026-09-16T23:02:15.131786Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:01:45Z`
- `2026-09-16T23:00:38.205310Z` — **MID**: 0 rows; marker `2026-09-16T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T23:00:38.205310Z` — **MELNGC**: 1044 rows; marker `2026-09-16T22:47:00Z`
- `2026-09-16T23:00:38.205310Z` — **INDGEN**: 1044 rows; marker `2026-09-16T22:47:00Z`
- `2026-09-16T23:00:38.205310Z` — **INDDEM**: 1044 rows; marker `2026-09-16T22:47:00Z`
- `2026-09-16T23:00:38.205310Z` — **IMBALNGC**: 1044 rows; marker `2026-09-16T22:47:00Z`
- `2026-09-16T23:00:38.205310Z` — **TSDF**: 1044 rows; marker `2026-09-16T22:47:00Z`
- `2026-09-16T23:00:38.205310Z` — **NDF**: 58 rows; marker `2026-09-16T22:47:00Z`
- `2026-09-16T23:00:38.205310Z` — **FUELHH**: 20 rows; marker `2026-09-16T23:00:00Z`
- `2026-09-16T23:00:38.205310Z` — **FUELINST**: 80 rows; marker `2026-09-16T23:00:00Z`
