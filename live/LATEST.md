# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T03:09:17.895636Z`  
Current process started UTC: `2026-09-21T03:05:18.202650Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1727, 2026-09-21T03:05:34.221176Z)
- `FUELINST|fuelType=OTHER|generation` = **368** (n=1727, 2026-09-21T03:05:34.221176Z)
- `FUELINST|fuelType=PS|generation` = **-79** (n=1727, 2026-09-21T03:05:34.221176Z)
- `FUELINST|fuelType=WIND|generation` = **3783** (n=1727, 2026-09-21T03:05:34.221176Z)
- `IMBALNGC|TOTAL|imbalance` = **-4865** (n=284, 2026-09-21T02:50:47.426347Z)
- `INDDEM|TOTAL|demand` = **-11802** (n=284, 2026-09-21T02:50:47.426347Z)
- `INDGEN|TOTAL|generation` = **15745** (n=284, 2026-09-21T02:50:47.426347Z)
- `MELNGC|TOTAL|margin` = **37560** (n=284, 2026-09-21T02:49:27.461116Z)
- `MID|dataProvider=APXMIDP|price` = **141.32** (n=23, 2026-09-21T02:42:07.304445Z)
- `MID|dataProvider=APXMIDP|volume` = **2210.4** (n=23, 2026-09-21T02:42:07.304445Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=47, 2026-09-21T03:06:23.329982Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=47, 2026-09-21T03:06:23.329982Z)
- `NDF|TOTAL|demand` = **20110** (n=290, 2026-09-21T02:47:35.834113Z)
- `TSDF|TOTAL|demand` = **20610** (n=290, 2026-09-21T02:47:35.834113Z)
- `WINDFOR|TOTAL|generation` = **1603** (n=48, 2026-09-20T23:30:37.519891Z)

## Latest publication events

- `2026-09-21T03:08:14.740272Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:07:45Z`
- `2026-09-21T03:06:23.329982Z` — **MID**: 1 rows; marker `2026-09-21T03:05:00Z`
- `2026-09-21T03:06:07.476978Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:05:45Z`
- `2026-09-21T03:05:34.221176Z` — **FUELINST**: 80 rows; marker `2026-09-21T03:05:00Z`
- `2026-09-21T03:04:20.752074Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:03:45Z`
- `2026-09-21T03:02:13.040565Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:01:45Z`
- `2026-09-21T03:00:45.305779Z` — **FUELHH**: 20 rows; marker `2026-09-21T03:00:00Z`
- `2026-09-21T03:00:29.042412Z` — **FUELINST**: 80 rows; marker `2026-09-21T03:00:00Z`
- `2026-09-21T03:00:13.291918Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:59:45Z`
- `2026-09-21T02:58:05.496801Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:57:45Z`
- `2026-09-21T02:56:13.597969Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:55:45Z`
- `2026-09-21T02:55:41.403016Z` — **FUELINST**: 80 rows; marker `2026-09-21T02:55:00Z`
- `2026-09-21T02:54:21.820213Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:53:45Z`
- `2026-09-21T02:52:23.059060Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:51:45Z`
- `2026-09-21T02:50:47.426347Z` — **INDGEN**: 900 rows; marker `2026-09-21T02:47:00Z`
