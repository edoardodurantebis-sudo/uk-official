# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T03:34:39.683738Z`  
Current process started UTC: `2026-09-21T03:30:39.847112Z`  
1-second metadata polls in this process: **232**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=994, delta=146, z=3.51 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=2793, delta=365, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2736, delta=-158, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2894, delta=-83, z=3.94 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2977, delta=12, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2965, delta=268, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2697, delta=209, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2791, delta=35, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2756, delta=187, z=3.80 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=938, delta=-6, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=-1, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=947, delta=3, z=3.59 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1732, 2026-09-21T03:30:39.847119Z)
- `FUELINST|fuelType=OTHER|generation` = **166** (n=1732, 2026-09-21T03:30:39.847119Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1732, 2026-09-21T03:30:39.847119Z)
- `FUELINST|fuelType=WIND|generation` = **3827** (n=1732, 2026-09-21T03:30:39.847119Z)
- `IMBALNGC|TOTAL|imbalance` = **-4820** (n=285, 2026-09-21T03:20:59.430477Z)
- `INDDEM|TOTAL|demand` = **-11798** (n=285, 2026-09-21T03:20:59.430477Z)
- `INDGEN|TOTAL|generation` = **15790** (n=285, 2026-09-21T03:20:59.430477Z)
- `MELNGC|TOTAL|margin` = **37568** (n=285, 2026-09-21T03:19:55.823626Z)
- `MID|dataProvider=APXMIDP|price` = **138.05** (n=24, 2026-09-21T03:12:10.827573Z)
- `MID|dataProvider=APXMIDP|volume` = **2255.8** (n=24, 2026-09-21T03:12:10.827573Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=48, 2026-09-21T03:12:10.827573Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=48, 2026-09-21T03:12:10.827573Z)
- `NDF|TOTAL|demand` = **20110** (n=291, 2026-09-21T03:17:46.317131Z)
- `TSDF|TOTAL|demand` = **20610** (n=291, 2026-09-21T03:17:46.317131Z)
- `WINDFOR|TOTAL|generation` = **8021** (n=49, 2026-09-21T03:30:39.847119Z)

## Latest publication events

- `2026-09-21T03:34:07.555208Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:33:45Z`
- `2026-09-21T03:32:15.799122Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:31:45Z`
- `2026-09-21T03:30:39.847119Z` — **WINDFOR**: 73 rows; marker `2026-09-21T03:30:00Z`
- `2026-09-21T03:30:39.847119Z` — **FUELHH**: 20 rows; marker `2026-09-21T03:30:00Z`
- `2026-09-21T03:30:39.847119Z` — **FUELINST**: 80 rows; marker `2026-09-21T03:30:00Z`
- `2026-09-21T03:30:12.718007Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:29:45Z`
- `2026-09-21T03:28:03.430609Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:27:45Z`
- `2026-09-21T03:26:00.997667Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:25:45Z`
- `2026-09-21T03:25:45.458493Z` — **FUELINST**: 80 rows; marker `2026-09-21T03:25:00Z`
- `2026-09-21T03:24:24.441299Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:23:45Z`
- `2026-09-21T03:22:16.043335Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:21:45Z`
- `2026-09-21T03:20:59.430477Z` — **INDGEN**: 882 rows; marker `2026-09-21T03:16:00Z`
- `2026-09-21T03:20:59.430477Z` — **INDDEM**: 882 rows; marker `2026-09-21T03:16:00Z`
- `2026-09-21T03:20:59.430477Z` — **IMBALNGC**: 882 rows; marker `2026-09-21T03:17:00Z`
- `2026-09-21T03:20:43.247078Z` — **FUELINST**: 80 rows; marker `2026-09-21T03:20:00Z`
