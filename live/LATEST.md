# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T23:57:18.950948Z`  
Current process started UTC: `2026-09-14T23:53:19.049540Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2683, delta=11, z=5.04 -> generation-mix component moved
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2672, delta=95, z=11.64 -> generation-mix component moved
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2560, delta=-26, z=-2.39 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=542, delta=109, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=1193, delta=90, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=INTIFA2` `generation` — instantaneous generation mix [fuelType=INTIFA2] generation: value=-889, delta=-56, z=-4.14 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=1, delta=-96, z=-5.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTIFA2` `generation` — instantaneous generation mix [fuelType=INTIFA2] generation: value=-833, delta=-111, z=-5.27 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=97, delta=-182, z=-28.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=279, delta=-26, z=-14.31 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-134** (n=36, 2026-09-14T23:55:32.197524Z)
- `FUELINST|fuelType=NPSHYD|generation` = **366** (n=36, 2026-09-14T23:55:32.197524Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3316** (n=36, 2026-09-14T23:55:32.197524Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=36, 2026-09-14T23:55:32.197524Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=36, 2026-09-14T23:55:32.197524Z)
- `FUELINST|fuelType=OTHER|generation` = **309** (n=36, 2026-09-14T23:55:32.197524Z)
- `FUELINST|fuelType=PS|generation` = **-16** (n=36, 2026-09-14T23:55:32.197524Z)
- `FUELINST|fuelType=WIND|generation` = **12056** (n=36, 2026-09-14T23:55:32.197524Z)
- `IMBALNGC|TOTAL|imbalance` = **210** (n=7, 2026-09-14T23:51:32.096612Z)
- `INDDEM|TOTAL|demand` = **-12270** (n=7, 2026-09-14T23:51:48.749871Z)
- `INDGEN|TOTAL|generation` = **20695** (n=7, 2026-09-14T23:51:32.096612Z)
- `MELNGC|TOTAL|margin` = **32721** (n=7, 2026-09-14T23:49:56.529171Z)
- `NDF|TOTAL|demand` = **19934** (n=7, 2026-09-14T23:47:40.313990Z)
- `TSDF|TOTAL|demand` = **20485** (n=7, 2026-09-14T23:47:40.313990Z)
- `WINDFOR|TOTAL|generation` = **7851** (n=1, 2026-09-14T23:30:39.804378Z)

## Latest publication events

- `2026-09-14T23:56:20.203364Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:55:45Z`
- `2026-09-14T23:55:32.197524Z` — **FUELINST**: 80 rows; marker `2026-09-14T23:55:00Z`
- `2026-09-14T23:54:12.056109Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:53:45Z`
- `2026-09-14T23:52:20.193578Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:51:45Z`
- `2026-09-14T23:51:48.749871Z` — **INDDEM**: 1008 rows; marker `2026-09-14T23:47:00Z`
- `2026-09-14T23:51:32.096612Z` — **INDGEN**: 1008 rows; marker `2026-09-14T23:47:00Z`
- `2026-09-14T23:51:32.096612Z` — **IMBALNGC**: 1008 rows; marker `2026-09-14T23:47:00Z`
- `2026-09-14T23:50:27.814414Z` — **FUELINST**: 80 rows; marker `2026-09-14T23:50:00Z`
- `2026-09-14T23:50:11.961451Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:49:45Z`
- `2026-09-14T23:49:56.529171Z` — **MELNGC**: 1008 rows; marker `2026-09-14T23:47:00Z`
- `2026-09-14T23:48:12.094454Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:47:45Z`
- `2026-09-14T23:47:40.313990Z` — **TSDF**: 1008 rows; marker `2026-09-14T23:47:00Z`
- `2026-09-14T23:47:40.313990Z` — **NDF**: 56 rows; marker `2026-09-14T23:47:00Z`
- `2026-09-14T23:46:19.232396Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:45:45Z`
- `2026-09-14T23:45:30.645819Z` — **FUELINST**: 80 rows; marker `2026-09-14T23:45:00Z`
