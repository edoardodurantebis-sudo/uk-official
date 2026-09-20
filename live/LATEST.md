# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T23:29:50.926102Z`  
Current process started UTC: `2026-09-20T23:25:50.563113Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1683, 2026-09-20T23:25:50.563121Z)
- `FUELINST|fuelType=OTHER|generation` = **186** (n=1683, 2026-09-20T23:25:50.563121Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1683, 2026-09-20T23:25:50.563121Z)
- `FUELINST|fuelType=WIND|generation` = **5746** (n=1683, 2026-09-20T23:25:50.563121Z)
- `IMBALNGC|TOTAL|imbalance` = **-5221** (n=277, 2026-09-20T23:21:41.704783Z)
- `INDDEM|TOTAL|demand` = **-11829** (n=277, 2026-09-20T23:21:26.169619Z)
- `INDGEN|TOTAL|generation` = **15389** (n=277, 2026-09-20T23:21:26.169619Z)
- `MELNGC|TOTAL|margin` = **35811** (n=277, 2026-09-20T23:19:18.463918Z)
- `MID|dataProvider=APXMIDP|price` = **157.3** (n=16, 2026-09-20T23:12:15.981992Z)
- `MID|dataProvider=APXMIDP|volume` = **2248.8** (n=16, 2026-09-20T23:12:15.981992Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=32, 2026-09-20T23:12:15.981992Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=32, 2026-09-20T23:12:15.981992Z)
- `NDF|TOTAL|demand` = **20110** (n=283, 2026-09-20T23:17:42.348630Z)
- `TSDF|TOTAL|demand` = **20610** (n=283, 2026-09-20T23:17:42.348630Z)
- `WINDFOR|TOTAL|generation` = **1726** (n=47, 2026-09-20T19:30:32.161891Z)

## Latest publication events

- `2026-09-20T23:28:13.422588Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:27:45Z`
- `2026-09-20T23:26:22.119956Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:25:45Z`
- `2026-09-20T23:25:50.563121Z` — **FUELINST**: 80 rows; marker `2026-09-20T23:25:00Z`
- `2026-09-20T23:24:22.240027Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:23:45Z`
- `2026-09-20T23:22:29.800537Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:21:45Z`
- `2026-09-20T23:21:41.704783Z` — **IMBALNGC**: 1026 rows; marker `2026-09-20T23:17:00Z`
- `2026-09-20T23:21:26.169619Z` — **INDGEN**: 1026 rows; marker `2026-09-20T23:17:00Z`
- `2026-09-20T23:21:26.169619Z` — **INDDEM**: 1026 rows; marker `2026-09-20T23:17:00Z`
- `2026-09-20T23:20:37.887854Z` — **FUELINST**: 80 rows; marker `2026-09-20T23:20:00Z`
- `2026-09-20T23:20:22.012775Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:19:45Z`
- `2026-09-20T23:19:18.463918Z` — **MELNGC**: 1026 rows; marker `2026-09-20T23:17:00Z`
- `2026-09-20T23:18:13.966731Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:17:45Z`
- `2026-09-20T23:17:42.348630Z` — **TSDF**: 1026 rows; marker `2026-09-20T23:17:00Z`
- `2026-09-20T23:17:42.348630Z` — **NDF**: 57 rows; marker `2026-09-20T23:17:00Z`
- `2026-09-20T23:16:13.295650Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:15:45Z`
