# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T21:22:07.815206Z`  
Current process started UTC: `2026-09-15T21:18:07.444899Z`  
1-second metadata polls in this process: **235**  
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

- `FUELINST|fuelType=INTVKL|generation` = **344** (n=293, 2026-09-15T21:20:31.362984Z)
- `FUELINST|fuelType=NPSHYD|generation` = **430** (n=293, 2026-09-15T21:20:31.362984Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3323** (n=293, 2026-09-15T21:20:31.362984Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=293, 2026-09-15T21:20:31.362984Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=293, 2026-09-15T21:20:31.362984Z)
- `FUELINST|fuelType=OTHER|generation` = **120** (n=293, 2026-09-15T21:20:31.362984Z)
- `FUELINST|fuelType=PS|generation` = **-260** (n=293, 2026-09-15T21:20:31.362984Z)
- `FUELINST|fuelType=WIND|generation` = **12509** (n=293, 2026-09-15T21:20:31.362984Z)
- `IMBALNGC|TOTAL|imbalance` = **5769** (n=49, 2026-09-15T21:21:18.653976Z)
- `INDDEM|TOTAL|demand` = **-11914** (n=49, 2026-09-15T21:21:18.653976Z)
- `INDGEN|TOTAL|generation` = **24890** (n=49, 2026-09-15T21:21:18.653976Z)
- `MELNGC|TOTAL|margin` = **35719** (n=49, 2026-09-15T21:19:11.341888Z)
- `NDF|TOTAL|demand` = **18621** (n=50, 2026-09-15T21:17:24.696002Z)
- `TSDF|TOTAL|demand` = **19121** (n=50, 2026-09-15T21:17:24.696002Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T21:21:18.653976Z` — **INDGEN**: 1098 rows; marker `2026-09-15T21:17:00Z`
- `2026-09-15T21:21:18.653976Z` — **INDDEM**: 1098 rows; marker `2026-09-15T21:17:00Z`
- `2026-09-15T21:21:18.653976Z` — **IMBALNGC**: 1098 rows; marker `2026-09-15T21:17:00Z`
- `2026-09-15T21:20:31.362984Z` — **FUELINST**: 80 rows; marker `2026-09-15T21:20:00Z`
- `2026-09-15T21:20:15.401323Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:19:45Z`
- `2026-09-15T21:19:11.341888Z` — **MELNGC**: 1098 rows; marker `2026-09-15T21:17:00Z`
- `2026-09-15T21:18:23.446634Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:17:45Z`
- `2026-09-15T21:17:24.696002Z` — **TSDF**: 1098 rows; marker `2026-09-15T21:17:00Z`
- `2026-09-15T21:17:24.696002Z` — **NDF**: 61 rows; marker `2026-09-15T21:17:00Z`
- `2026-09-15T21:16:20.407458Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:15:45Z`
- `2026-09-15T21:15:48.660157Z` — **FUELINST**: 80 rows; marker `2026-09-15T21:15:00Z`
- `2026-09-15T21:14:12.399090Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:13:45Z`
- `2026-09-15T21:12:11.724470Z` — **MID**: 0 rows; marker `2026-09-15T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T21:12:11.724470Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:11:45Z`
- `2026-09-15T21:10:36.284340Z` — **FUELINST**: 80 rows; marker `2026-09-15T21:10:00Z`
