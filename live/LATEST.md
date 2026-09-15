# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T20:22:50.213757Z`  
Current process started UTC: `2026-09-15T20:18:49.905867Z`  
1-second metadata polls in this process: **232**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=-1, z=3.74 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.30 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=54, delta=-1, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.76 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=17, z=8.89 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.93 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.39 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.98 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=281, 2026-09-15T20:20:24.876902Z)
- `FUELINST|fuelType=NPSHYD|generation` = **484** (n=281, 2026-09-15T20:20:24.876902Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3321** (n=281, 2026-09-15T20:20:24.876902Z)
- `FUELINST|fuelType=OCGT|generation` = **2** (n=281, 2026-09-15T20:20:24.876902Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=281, 2026-09-15T20:20:24.876902Z)
- `FUELINST|fuelType=OTHER|generation` = **227** (n=281, 2026-09-15T20:20:24.876902Z)
- `FUELINST|fuelType=PS|generation` = **-257** (n=281, 2026-09-15T20:20:24.876902Z)
- `FUELINST|fuelType=WIND|generation` = **11487** (n=281, 2026-09-15T20:20:24.876902Z)
- `IMBALNGC|TOTAL|imbalance` = **5788** (n=47, 2026-09-15T20:21:44.851897Z)
- `INDDEM|TOTAL|demand` = **-11914** (n=47, 2026-09-15T20:21:44.851897Z)
- `INDGEN|TOTAL|generation` = **24909** (n=47, 2026-09-15T20:21:44.851897Z)
- `MELNGC|TOTAL|margin` = **35696** (n=47, 2026-09-15T20:19:53.455183Z)
- `NDF|TOTAL|demand` = **18621** (n=48, 2026-09-15T20:17:38.969739Z)
- `TSDF|TOTAL|demand` = **19121** (n=48, 2026-09-15T20:17:38.969739Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T20:22:16.390991Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:21:45Z`
- `2026-09-15T20:21:44.851897Z` — **INDGEN**: 1134 rows; marker `2026-09-15T20:17:00Z`
- `2026-09-15T20:21:44.851897Z` — **INDDEM**: 1134 rows; marker `2026-09-15T20:17:00Z`
- `2026-09-15T20:21:44.851897Z` — **IMBALNGC**: 1134 rows; marker `2026-09-15T20:17:00Z`
- `2026-09-15T20:20:24.876902Z` — **FUELINST**: 80 rows; marker `2026-09-15T20:20:00Z`
- `2026-09-15T20:20:09.458654Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:19:45Z`
- `2026-09-15T20:19:53.455183Z` — **MELNGC**: 1134 rows; marker `2026-09-15T20:17:00Z`
- `2026-09-15T20:18:11.178491Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:17:45Z`
- `2026-09-15T20:17:38.969739Z` — **TSDF**: 1134 rows; marker `2026-09-15T20:17:00Z`
- `2026-09-15T20:17:38.969739Z` — **NDF**: 63 rows; marker `2026-09-15T20:17:00Z`
- `2026-09-15T20:16:19.107656Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:15:45Z`
- `2026-09-15T20:15:47.836682Z` — **FUELINST**: 80 rows; marker `2026-09-15T20:15:00Z`
- `2026-09-15T20:14:12.801226Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:13:45Z`
- `2026-09-15T20:12:20.699947Z` — **MID**: 0 rows; marker `2026-09-15T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T20:12:20.699947Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:11:45Z`
