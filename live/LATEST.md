# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T17:24:29.926287Z`  
Current process started UTC: `2026-09-16T17:20:29.940535Z`  
1-second metadata polls in this process: **231**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=692, delta=2, z=4.24 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=86, delta=25, z=4.92 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=690, delta=1, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=61, delta=26, z=4.80 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=689, delta=14, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=35, delta=25, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=675, delta=124, z=4.19 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=10, delta=20, z=4.51 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=-32, delta=138, z=4.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-10, delta=-9, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-1, delta=7, z=4.58 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-8, delta=24, z=4.61 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-32, delta=24, z=4.45 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-56, delta=26, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-82, delta=26, z=4.07 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **381** (n=533, 2026-09-16T17:20:29.940545Z)
- `FUELINST|fuelType=NPSHYD|generation` = **692** (n=533, 2026-09-16T17:20:29.940545Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3304** (n=533, 2026-09-16T17:20:29.940545Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=533, 2026-09-16T17:20:29.940545Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=533, 2026-09-16T17:20:29.940545Z)
- `FUELINST|fuelType=OTHER|generation` = **2677** (n=533, 2026-09-16T17:20:29.940545Z)
- `FUELINST|fuelType=PS|generation` = **1209** (n=533, 2026-09-16T17:20:29.940545Z)
- `FUELINST|fuelType=WIND|generation` = **7041** (n=533, 2026-09-16T17:20:29.940545Z)
- `IMBALNGC|TOTAL|imbalance` = **6467** (n=88, 2026-09-16T17:22:38.924645Z)
- `INDDEM|TOTAL|demand` = **-11776** (n=88, 2026-09-16T17:22:22.539302Z)
- `INDGEN|TOTAL|generation` = **25588** (n=88, 2026-09-16T17:22:22.539302Z)
- `MELNGC|TOTAL|margin` = **34115** (n=88, 2026-09-16T17:19:45.851595Z)
- `NDF|TOTAL|demand` = **18621** (n=90, 2026-09-16T17:17:38.753950Z)
- `TSDF|TOTAL|demand` = **19121** (n=90, 2026-09-16T17:17:54.343002Z)
- `WINDFOR|TOTAL|generation` = **19485** (n=15, 2026-09-16T16:30:25.726572Z)

## Latest publication events

- `2026-09-16T17:24:16.095431Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:23:45Z`
- `2026-09-16T17:22:38.924645Z` — **IMBALNGC**: 1242 rows; marker `2026-09-16T17:17:00Z`
- `2026-09-16T17:22:22.539302Z` — **INDGEN**: 1242 rows; marker `2026-09-16T17:17:00Z`
- `2026-09-16T17:22:22.539302Z` — **INDDEM**: 1242 rows; marker `2026-09-16T17:17:00Z`
- `2026-09-16T17:22:22.539302Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:21:45Z`
- `2026-09-16T17:20:29.940545Z` — **FUELINST**: 80 rows; marker `2026-09-16T17:20:00Z`
- `2026-09-16T17:20:29.940545Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:19:45Z`
- `2026-09-16T17:19:45.851595Z` — **MELNGC**: 1242 rows; marker `2026-09-16T17:17:00Z`
- `2026-09-16T17:18:10.433903Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:17:45Z`
- `2026-09-16T17:17:54.343002Z` — **TSDF**: 1242 rows; marker `2026-09-16T17:17:00Z`
- `2026-09-16T17:17:38.753950Z` — **NDF**: 69 rows; marker `2026-09-16T17:17:00Z`
- `2026-09-16T17:16:35.285670Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:15:45Z`
- `2026-09-16T17:15:31.382432Z` — **FUELINST**: 80 rows; marker `2026-09-16T17:15:00Z`
- `2026-09-16T17:14:28.099087Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:13:45Z`
- `2026-09-16T17:12:20.371842Z` — **MID**: 0 rows; marker `2026-09-16T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
