# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T20:58:37.720674Z`  
Current process started UTC: `2026-09-20T20:54:38.137603Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1653, 2026-09-20T20:55:26.144180Z)
- `FUELINST|fuelType=OTHER|generation` = **330** (n=1653, 2026-09-20T20:55:26.144180Z)
- `FUELINST|fuelType=PS|generation` = **230** (n=1653, 2026-09-20T20:55:26.144180Z)
- `FUELINST|fuelType=WIND|generation` = **6179** (n=1653, 2026-09-20T20:55:26.144180Z)
- `IMBALNGC|TOTAL|imbalance` = **-5405** (n=272, 2026-09-20T20:52:02.810373Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=272, 2026-09-20T20:52:02.810373Z)
- `INDGEN|TOTAL|generation` = **15205** (n=272, 2026-09-20T20:52:02.810373Z)
- `MELNGC|TOTAL|margin` = **35539** (n=272, 2026-09-20T20:49:45.480150Z)
- `MID|dataProvider=APXMIDP|price` = **192.91** (n=11, 2026-09-20T20:42:19.161036Z)
- `MID|dataProvider=APXMIDP|volume` = **2427.2** (n=11, 2026-09-20T20:42:19.161036Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=22, 2026-09-20T20:42:19.161036Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=22, 2026-09-20T20:42:19.161036Z)
- `NDF|TOTAL|demand` = **20110** (n=278, 2026-09-20T20:47:37.817444Z)
- `TSDF|TOTAL|demand` = **20610** (n=278, 2026-09-20T20:47:37.817444Z)
- `WINDFOR|TOTAL|generation` = **1726** (n=47, 2026-09-20T19:30:32.161891Z)

## Latest publication events

- `2026-09-20T20:58:06.425574Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:57:45Z`
- `2026-09-20T20:56:14.582306Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:55:45Z`
- `2026-09-20T20:55:26.144180Z` — **FUELINST**: 80 rows; marker `2026-09-20T20:55:00Z`
- `2026-09-20T20:54:10.632343Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:53:45Z`
- `2026-09-20T20:52:02.810373Z` — **INDGEN**: 1116 rows; marker `2026-09-20T20:47:00Z`
- `2026-09-20T20:52:02.810373Z` — **INDDEM**: 1116 rows; marker `2026-09-20T20:47:00Z`
- `2026-09-20T20:52:02.810373Z` — **IMBALNGC**: 1116 rows; marker `2026-09-20T20:47:00Z`
- `2026-09-20T20:52:02.810373Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:51:45Z`
- `2026-09-20T20:50:26.386250Z` — **FUELINST**: 80 rows; marker `2026-09-20T20:50:00Z`
- `2026-09-20T20:50:26.386250Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:49:45Z`
- `2026-09-20T20:49:45.480150Z` — **MELNGC**: 1116 rows; marker `2026-09-20T20:47:00Z`
- `2026-09-20T20:48:25.992340Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:47:45Z`
- `2026-09-20T20:47:37.817444Z` — **TSDF**: 1116 rows; marker `2026-09-20T20:47:00Z`
- `2026-09-20T20:47:37.817444Z` — **NDF**: 62 rows; marker `2026-09-20T20:47:00Z`
- `2026-09-20T20:46:18.407408Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:45:45Z`
