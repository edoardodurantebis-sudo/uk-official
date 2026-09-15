# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T03:05:55.845066Z`  
Current process started UTC: `2026-09-15T03:01:54.884310Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **MELNGC** `TOTAL` `margin` — indicated margin [TOTAL] margin: value=34104, delta=1370, z=NA -> margin/tightness state changed
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=1, delta=0, z=3.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=1, delta=1, z=4.75 -> generation-mix component moved
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=3.56 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=3.86 -> frequency excursion; balancing stress check
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=-299, delta=8, z=3.95 -> generation-mix component moved
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=4.25 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=4.80 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=5.62 -> frequency excursion; balancing stress check
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=-307, delta=170, z=4.89 -> generation-mix component moved
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=7.11 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0.004, z=11.23 -> frequency excursion; balancing stress check
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2683, delta=11, z=5.04 -> generation-mix component moved
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2672, delta=95, z=11.64 -> generation-mix component moved
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2560, delta=-26, z=-2.39 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1104** (n=74, 2026-09-15T03:05:38.899898Z)
- `FUELINST|fuelType=NPSHYD|generation` = **336** (n=74, 2026-09-15T03:05:38.899898Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=74, 2026-09-15T03:05:38.899898Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=74, 2026-09-15T03:05:38.899898Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=74, 2026-09-15T03:05:38.899898Z)
- `FUELINST|fuelType=OTHER|generation` = **185** (n=74, 2026-09-15T03:05:38.899898Z)
- `FUELINST|fuelType=PS|generation` = **-704** (n=74, 2026-09-15T03:05:38.899898Z)
- `FUELINST|fuelType=WIND|generation` = **13332** (n=74, 2026-09-15T03:05:38.899898Z)
- `IMBALNGC|TOTAL|imbalance` = **218** (n=13, 2026-09-15T02:50:54.555327Z)
- `INDDEM|TOTAL|demand` = **-12327** (n=13, 2026-09-15T02:50:54.555327Z)
- `INDGEN|TOTAL|generation` = **20703** (n=13, 2026-09-15T02:50:54.555327Z)
- `MELNGC|TOTAL|margin` = **34104** (n=13, 2026-09-15T02:49:35.642789Z)
- `NDF|TOTAL|demand` = **19934** (n=13, 2026-09-15T02:47:43.890383Z)
- `TSDF|TOTAL|demand` = **20485** (n=13, 2026-09-15T02:47:43.890383Z)
- `WINDFOR|TOTAL|generation` = **7851** (n=1, 2026-09-14T23:30:39.804378Z)

## Latest publication events

- `2026-09-15T03:05:38.899898Z` — **FUELINST**: 80 rows; marker `2026-09-15T03:05:00Z`
- `2026-09-15T03:04:18.840166Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:03:45Z`
- `2026-09-15T03:02:26.888101Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:01:45Z`
- `2026-09-15T03:00:38.504850Z` — **FUELHH**: 20 rows; marker `2026-09-15T03:00:00Z`
- `2026-09-15T03:00:38.504850Z` — **FUELINST**: 80 rows; marker `2026-09-15T03:00:00Z`
- `2026-09-15T03:00:22.156435Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:59:45Z`
- `2026-09-15T02:58:13.819188Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:57:45Z`
- `2026-09-15T02:56:26.011697Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:55:45Z`
- `2026-09-15T02:55:38.399147Z` — **FUELINST**: 80 rows; marker `2026-09-15T02:55:00Z`
- `2026-09-15T02:54:17.664220Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:53:45Z`
- `2026-09-15T02:52:15.094680Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:51:45Z`
- `2026-09-15T02:50:54.555327Z` — **INDGEN**: 900 rows; marker `2026-09-15T02:47:00Z`
- `2026-09-15T02:50:54.555327Z` — **INDDEM**: 900 rows; marker `2026-09-15T02:47:00Z`
- `2026-09-15T02:50:54.555327Z` — **IMBALNGC**: 900 rows; marker `2026-09-15T02:47:00Z`
- `2026-09-15T02:50:23.126537Z` — **FUELINST**: 80 rows; marker `2026-09-15T02:50:00Z`
