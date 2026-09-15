# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T03:18:27.783281Z`  
Current process started UTC: `2026-09-15T03:14:28.021324Z`  
1-second metadata polls in this process: **235**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-1354** (n=76, 2026-09-15T03:15:53.033565Z)
- `FUELINST|fuelType=NPSHYD|generation` = **338** (n=76, 2026-09-15T03:15:53.033565Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=76, 2026-09-15T03:15:53.033565Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=76, 2026-09-15T03:15:53.033565Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=76, 2026-09-15T03:15:53.033565Z)
- `FUELINST|fuelType=OTHER|generation` = **157** (n=76, 2026-09-15T03:15:53.033565Z)
- `FUELINST|fuelType=PS|generation` = **-706** (n=76, 2026-09-15T03:15:53.033565Z)
- `FUELINST|fuelType=WIND|generation` = **13641** (n=76, 2026-09-15T03:15:53.033565Z)
- `IMBALNGC|TOTAL|imbalance` = **218** (n=13, 2026-09-15T02:50:54.555327Z)
- `INDDEM|TOTAL|demand` = **-12327** (n=13, 2026-09-15T02:50:54.555327Z)
- `INDGEN|TOTAL|generation` = **20703** (n=13, 2026-09-15T02:50:54.555327Z)
- `MELNGC|TOTAL|margin` = **34104** (n=13, 2026-09-15T02:49:35.642789Z)
- `NDF|TOTAL|demand` = **19934** (n=14, 2026-09-15T03:18:02.752215Z)
- `TSDF|TOTAL|demand` = **20485** (n=14, 2026-09-15T03:17:46.512016Z)
- `WINDFOR|TOTAL|generation` = **7851** (n=1, 2026-09-14T23:30:39.804378Z)

## Latest publication events

- `2026-09-15T03:18:19.114335Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:17:45Z`
- `2026-09-15T03:18:02.752215Z` — **NDF**: 49 rows; marker `2026-09-15T03:17:00Z`
- `2026-09-15T03:17:46.512016Z` — **TSDF**: 882 rows; marker `2026-09-15T03:17:00Z`
- `2026-09-15T03:16:25.268400Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:15:45Z`
- `2026-09-15T03:15:53.033565Z` — **FUELINST**: 80 rows; marker `2026-09-15T03:15:00Z`
- `2026-09-15T03:14:16.930122Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:13:45Z`
- `2026-09-15T03:12:08.767741Z` — **MID**: 0 rows; marker `2026-09-15T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T03:12:08.767741Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:11:45Z`
- `2026-09-15T03:10:32.754589Z` — **FUELINST**: 80 rows; marker `2026-09-15T03:10:00Z`
- `2026-09-15T03:10:17.294745Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:09:45Z`
- `2026-09-15T03:08:20.877019Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:07:45Z`
- `2026-09-15T03:07:31.685983Z` — **MID**: 0 rows; marker `2026-09-15T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T03:06:26.703302Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:05:45Z`
- `2026-09-15T03:05:38.899898Z` — **FUELINST**: 80 rows; marker `2026-09-15T03:05:00Z`
- `2026-09-15T03:04:18.840166Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:03:45Z`
