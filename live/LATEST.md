# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T19:59:58.982423Z`  
Current process started UTC: `2026-09-16T19:55:59.102994Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=692, delta=2, z=3.51 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **158** (n=564, 2026-09-16T19:55:33.475329Z)
- `FUELINST|fuelType=NPSHYD|generation` = **513** (n=564, 2026-09-16T19:55:33.475329Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3312** (n=564, 2026-09-16T19:55:33.475329Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=564, 2026-09-16T19:55:33.475329Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=564, 2026-09-16T19:55:33.475329Z)
- `FUELINST|fuelType=OTHER|generation` = **487** (n=564, 2026-09-16T19:55:33.475329Z)
- `FUELINST|fuelType=PS|generation` = **228** (n=564, 2026-09-16T19:55:33.475329Z)
- `FUELINST|fuelType=WIND|generation` = **10012** (n=564, 2026-09-16T19:55:33.475329Z)
- `IMBALNGC|TOTAL|imbalance` = **6640** (n=93, 2026-09-16T19:52:04.923339Z)
- `INDDEM|TOTAL|demand` = **-11763** (n=93, 2026-09-16T19:51:48.845809Z)
- `INDGEN|TOTAL|generation` = **25761** (n=93, 2026-09-16T19:51:48.845809Z)
- `MELNGC|TOTAL|margin` = **34409** (n=93, 2026-09-16T19:50:18.787094Z)
- `NDF|TOTAL|demand` = **18621** (n=95, 2026-09-16T19:47:38.979377Z)
- `TSDF|TOTAL|demand` = **19121** (n=95, 2026-09-16T19:47:38.979377Z)
- `WINDFOR|TOTAL|generation` = **19445** (n=16, 2026-09-16T19:30:31.948327Z)

## Latest publication events

- `2026-09-16T19:58:06.872423Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:57:45Z`
- `2026-09-16T19:56:15.105353Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:55:45Z`
- `2026-09-16T19:55:33.475329Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:55:00Z`
- `2026-09-16T19:54:13.268805Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:53:45Z`
- `2026-09-16T19:52:04.923339Z` — **IMBALNGC**: 1152 rows; marker `2026-09-16T19:47:00Z`
- `2026-09-16T19:52:04.923339Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:51:45Z`
- `2026-09-16T19:51:48.845809Z` — **INDGEN**: 1152 rows; marker `2026-09-16T19:47:00Z`
- `2026-09-16T19:51:48.845809Z` — **INDDEM**: 1152 rows; marker `2026-09-16T19:47:00Z`
- `2026-09-16T19:50:18.787094Z` — **MELNGC**: 1152 rows; marker `2026-09-16T19:47:00Z`
- `2026-09-16T19:50:18.787094Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:50:00Z`
- `2026-09-16T19:50:18.787094Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:49:45Z`
- `2026-09-16T19:48:26.747129Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:47:45Z`
- `2026-09-16T19:47:38.979377Z` — **TSDF**: 1152 rows; marker `2026-09-16T19:47:00Z`
- `2026-09-16T19:47:38.979377Z` — **NDF**: 64 rows; marker `2026-09-16T19:47:00Z`
- `2026-09-16T19:46:25.273029Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:45:45Z`
