# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T02:31:01.989979Z`  
Current process started UTC: `2026-09-21T02:27:02.114483Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1720, 2026-09-21T02:30:30.617471Z)
- `FUELINST|fuelType=OTHER|generation` = **122** (n=1720, 2026-09-21T02:30:30.617471Z)
- `FUELINST|fuelType=PS|generation` = **-130** (n=1720, 2026-09-21T02:30:30.617471Z)
- `FUELINST|fuelType=WIND|generation` = **3888** (n=1720, 2026-09-21T02:30:30.617471Z)
- `IMBALNGC|TOTAL|imbalance` = **-4904** (n=283, 2026-09-21T02:20:35.453156Z)
- `INDDEM|TOTAL|demand` = **-11802** (n=283, 2026-09-21T02:20:19.738942Z)
- `INDGEN|TOTAL|generation` = **15706** (n=283, 2026-09-21T02:20:19.738942Z)
- `MELNGC|TOTAL|margin` = **37546** (n=283, 2026-09-21T02:19:15.834490Z)
- `MID|dataProvider=APXMIDP|price` = **148.62** (n=22, 2026-09-21T02:12:10.973392Z)
- `MID|dataProvider=APXMIDP|volume` = **2271.3** (n=22, 2026-09-21T02:12:10.973392Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=44, 2026-09-21T02:12:10.973392Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=44, 2026-09-21T02:12:10.973392Z)
- `NDF|TOTAL|demand` = **20110** (n=289, 2026-09-21T02:17:23.986288Z)
- `TSDF|TOTAL|demand` = **20610** (n=289, 2026-09-21T02:17:23.986288Z)
- `WINDFOR|TOTAL|generation` = **1603** (n=48, 2026-09-20T23:30:37.519891Z)

## Latest publication events

- `2026-09-21T02:30:46.647403Z` — **FUELHH**: 20 rows; marker `2026-09-21T02:30:00Z`
- `2026-09-21T02:30:30.617471Z` — **FUELINST**: 80 rows; marker `2026-09-21T02:30:00Z`
- `2026-09-21T02:30:13.643616Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:29:45Z`
- `2026-09-21T02:28:06.121678Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:27:45Z`
- `2026-09-21T02:26:04.401470Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:25:45Z`
- `2026-09-21T02:25:48.135999Z` — **FUELINST**: 80 rows; marker `2026-09-21T02:25:00Z`
- `2026-09-21T02:24:11.853034Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:23:45Z`
- `2026-09-21T02:22:27.561237Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:21:45Z`
- `2026-09-21T02:20:35.453156Z` — **IMBALNGC**: 918 rows; marker `2026-09-21T02:16:00Z`
- `2026-09-21T02:20:35.453156Z` — **FUELINST**: 80 rows; marker `2026-09-21T02:20:00Z`
- `2026-09-21T02:20:19.738942Z` — **INDGEN**: 918 rows; marker `2026-09-21T02:16:00Z`
- `2026-09-21T02:20:19.738942Z` — **INDDEM**: 918 rows; marker `2026-09-21T02:16:00Z`
- `2026-09-21T02:20:19.738942Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:19:45Z`
- `2026-09-21T02:19:15.834490Z` — **MELNGC**: 918 rows; marker `2026-09-21T02:16:00Z`
- `2026-09-21T02:18:28.202490Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:17:45Z`
