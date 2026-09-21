# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T16:34:47.781584Z`  
Current process started UTC: `2026-09-21T16:30:47.714481Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3506, delta=4, z=3.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3505, delta=1, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=1, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3503, delta=-6, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=3, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3506, delta=-1, z=3.72 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3507, delta=5, z=3.76 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3502, delta=7, z=3.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3502, delta=-4, z=3.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3506, delta=0, z=3.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3506, delta=2, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=5, z=3.75 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=5, z=3.65 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3494, delta=1, z=3.55 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3495, delta=2, z=3.63 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1885, 2026-09-21T16:30:47.714491Z)
- `FUELINST|fuelType=OTHER|generation` = **1320** (n=1885, 2026-09-21T16:30:47.714491Z)
- `FUELINST|fuelType=PS|generation` = **74** (n=1885, 2026-09-21T16:30:47.714491Z)
- `FUELINST|fuelType=WIND|generation` = **3263** (n=1885, 2026-09-21T16:30:47.714491Z)
- `IMBALNGC|TOTAL|imbalance` = **-3071** (n=310, 2026-09-21T16:23:11.472727Z)
- `INDDEM|TOTAL|demand` = **-12280** (n=310, 2026-09-21T16:22:55.453530Z)
- `INDGEN|TOTAL|generation` = **18388** (n=310, 2026-09-21T16:22:55.453530Z)
- `MELNGC|TOTAL|margin` = **36276** (n=310, 2026-09-21T16:20:15.056024Z)
- `MID|dataProvider=APXMIDP|price` = **200.43** (n=50, 2026-09-21T16:12:15.278008Z)
- `MID|dataProvider=APXMIDP|volume` = **2657.2** (n=50, 2026-09-21T16:12:15.278008Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=98, 2026-09-21T16:12:15.278008Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=98, 2026-09-21T16:12:15.278008Z)
- `NDF|TOTAL|demand` = **20959** (n=317, 2026-09-21T16:18:22.784357Z)
- `TSDF|TOTAL|demand` = **21459** (n=317, 2026-09-21T16:18:22.784357Z)
- `WINDFOR|TOTAL|generation` = **8620** (n=54, 2026-09-21T16:30:47.714491Z)

## Latest publication events

- `2026-09-21T16:34:16.306533Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:33:45Z`
- `2026-09-21T16:32:24.389880Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:31:45Z`
- `2026-09-21T16:30:47.714491Z` — **WINDFOR**: 73 rows; marker `2026-09-21T16:30:00Z`
- `2026-09-21T16:30:47.714491Z` — **FUELHH**: 20 rows; marker `2026-09-21T16:30:00Z`
- `2026-09-21T16:30:47.714491Z` — **FUELINST**: 80 rows; marker `2026-09-21T16:30:00Z`
- `2026-09-21T16:30:17.674185Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:29:45Z`
- `2026-09-21T16:28:25.584992Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:27:45Z`
- `2026-09-21T16:26:34.081513Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:25:45Z`
- `2026-09-21T16:25:34.770198Z` — **FUELINST**: 80 rows; marker `2026-09-21T16:25:00Z`
- `2026-09-21T16:24:15.100232Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:23:45Z`
- `2026-09-21T16:23:11.472727Z` — **IMBALNGC**: 1278 rows; marker `2026-09-21T16:17:00Z`
- `2026-09-21T16:22:55.453530Z` — **INDGEN**: 1278 rows; marker `2026-09-21T16:17:00Z`
- `2026-09-21T16:22:55.453530Z` — **INDDEM**: 1278 rows; marker `2026-09-21T16:17:00Z`
- `2026-09-21T16:22:22.921573Z` — **FREQ**: 5761 rows; marker `2026-09-21T16:21:45Z`
- `2026-09-21T16:20:31.347509Z` — **FUELINST**: 80 rows; marker `2026-09-21T16:20:00Z`
