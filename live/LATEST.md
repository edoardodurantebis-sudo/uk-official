# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T03:30:29.292882Z`  
Current process started UTC: `2026-09-17T03:26:28.740365Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.92 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.98 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=-48, z=-4.03 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1128, delta=-92, z=-4.00 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1036, delta=-93, z=-3.88 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-838, delta=-46, z=-3.77 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-943, delta=-91, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-852, delta=-43, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-809, delta=0, z=-3.58 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-809, delta=0, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-809, delta=-1, z=-3.66 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-808, delta=-1, z=-3.71 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-792, delta=-154, z=-3.97 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.22 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-807, delta=0, z=-3.75 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1448** (n=623, 2026-09-17T03:25:27.875992Z)
- `FUELINST|fuelType=NPSHYD|generation` = **427** (n=623, 2026-09-17T03:25:27.875992Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3311** (n=623, 2026-09-17T03:25:27.875992Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=623, 2026-09-17T03:25:27.875992Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=623, 2026-09-17T03:25:27.875992Z)
- `FUELINST|fuelType=OTHER|generation` = **713** (n=623, 2026-09-17T03:25:27.875992Z)
- `FUELINST|fuelType=PS|generation` = **-538** (n=623, 2026-09-17T03:25:27.875992Z)
- `FUELINST|fuelType=WIND|generation` = **13342** (n=623, 2026-09-17T03:25:27.875992Z)
- `IMBALNGC|TOTAL|imbalance` = **6527** (n=104, 2026-09-17T03:20:43.155529Z)
- `INDDEM|TOTAL|demand` = **-11516** (n=104, 2026-09-17T03:20:27.781104Z)
- `INDGEN|TOTAL|generation` = **25648** (n=104, 2026-09-17T03:20:27.781104Z)
- `MELNGC|TOTAL|margin` = **35852** (n=104, 2026-09-17T03:19:22.995166Z)
- `NDF|TOTAL|demand` = **18621** (n=106, 2026-09-17T03:17:28.635447Z)
- `TSDF|TOTAL|demand` = **19121** (n=106, 2026-09-17T03:17:28.635447Z)
- `WINDFOR|TOTAL|generation` = **20102** (n=17, 2026-09-16T23:30:41.101363Z)

## Latest publication events

- `2026-09-17T03:30:15.226415Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:29:45Z`
- `2026-09-17T03:28:07.829146Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:27:45Z`
- `2026-09-17T03:26:15.703118Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:25:45Z`
- `2026-09-17T03:25:27.875992Z` — **FUELINST**: 80 rows; marker `2026-09-17T03:25:00Z`
- `2026-09-17T03:24:08.380634Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:23:45Z`
- `2026-09-17T03:22:32.827713Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:21:45Z`
- `2026-09-17T03:20:43.155529Z` — **IMBALNGC**: 882 rows; marker `2026-09-17T03:16:00Z`
- `2026-09-17T03:20:43.155529Z` — **FUELINST**: 80 rows; marker `2026-09-17T03:20:00Z`
- `2026-09-17T03:20:27.781104Z` — **INDGEN**: 882 rows; marker `2026-09-17T03:16:00Z`
- `2026-09-17T03:20:27.781104Z` — **INDDEM**: 882 rows; marker `2026-09-17T03:16:00Z`
- `2026-09-17T03:20:27.781104Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:19:45Z`
- `2026-09-17T03:19:22.995166Z` — **MELNGC**: 882 rows; marker `2026-09-17T03:16:00Z`
- `2026-09-17T03:18:17.113847Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:17:45Z`
- `2026-09-17T03:17:28.635447Z` — **TSDF**: 882 rows; marker `2026-09-17T03:16:00Z`
- `2026-09-17T03:17:28.635447Z` — **NDF**: 49 rows; marker `2026-09-17T03:16:00Z`
