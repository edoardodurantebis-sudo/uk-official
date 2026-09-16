# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T17:37:11.488145Z`  
Current process started UTC: `2026-09-16T17:33:10.794541Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=685, delta=-7, z=3.92 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.87 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=689, delta=168, z=4.51 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=70, delta=102, z=5.03 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=692, delta=-1, z=4.09 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=9, z=4.99 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=693, delta=1, z=4.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=111, delta=25, z=5.03 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=692, delta=2, z=4.24 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=86, delta=25, z=4.92 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=690, delta=1, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=61, delta=26, z=4.80 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=689, delta=14, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=35, delta=25, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=675, delta=124, z=4.19 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **381** (n=536, 2026-09-16T17:35:35.225258Z)
- `FUELINST|fuelType=NPSHYD|generation` = **685** (n=536, 2026-09-16T17:35:35.225258Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3310** (n=536, 2026-09-16T17:35:35.225258Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=536, 2026-09-16T17:35:35.225258Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=536, 2026-09-16T17:35:35.225258Z)
- `FUELINST|fuelType=OTHER|generation` = **2424** (n=536, 2026-09-16T17:35:35.225258Z)
- `FUELINST|fuelType=PS|generation` = **1210** (n=536, 2026-09-16T17:35:35.225258Z)
- `FUELINST|fuelType=WIND|generation` = **7254** (n=536, 2026-09-16T17:35:35.225258Z)
- `IMBALNGC|TOTAL|imbalance` = **6467** (n=88, 2026-09-16T17:22:38.924645Z)
- `INDDEM|TOTAL|demand` = **-11776** (n=88, 2026-09-16T17:22:22.539302Z)
- `INDGEN|TOTAL|generation` = **25588** (n=88, 2026-09-16T17:22:22.539302Z)
- `MELNGC|TOTAL|margin` = **34115** (n=88, 2026-09-16T17:19:45.851595Z)
- `NDF|TOTAL|demand` = **18621** (n=90, 2026-09-16T17:17:38.753950Z)
- `TSDF|TOTAL|demand` = **19121** (n=90, 2026-09-16T17:17:54.343002Z)
- `WINDFOR|TOTAL|generation` = **19485** (n=15, 2026-09-16T16:30:25.726572Z)

## Latest publication events

- `2026-09-16T17:36:22.644001Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:35:45Z`
- `2026-09-16T17:35:35.225258Z` — **FUELINST**: 80 rows; marker `2026-09-16T17:35:00Z`
- `2026-09-16T17:34:15.001585Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:33:45Z`
- `2026-09-16T17:32:09.897598Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:31:45Z`
- `2026-09-16T17:30:33.426878Z` — **FUELHH**: 20 rows; marker `2026-09-16T17:30:00Z`
- `2026-09-16T17:30:33.426878Z` — **FUELINST**: 80 rows; marker `2026-09-16T17:30:00Z`
- `2026-09-16T17:30:17.551668Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:29:45Z`
- `2026-09-16T17:28:09.866236Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:27:45Z`
- `2026-09-16T17:26:18.394793Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:25:45Z`
- `2026-09-16T17:25:30.387429Z` — **FUELINST**: 80 rows; marker `2026-09-16T17:25:00Z`
- `2026-09-16T17:24:16.095431Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:23:45Z`
- `2026-09-16T17:22:38.924645Z` — **IMBALNGC**: 1242 rows; marker `2026-09-16T17:17:00Z`
- `2026-09-16T17:22:22.539302Z` — **INDGEN**: 1242 rows; marker `2026-09-16T17:17:00Z`
- `2026-09-16T17:22:22.539302Z` — **INDDEM**: 1242 rows; marker `2026-09-16T17:17:00Z`
- `2026-09-16T17:22:22.539302Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:21:45Z`
