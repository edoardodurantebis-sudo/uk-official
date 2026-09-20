# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T20:50:15.206633Z`  
Current process started UTC: `2026-09-20T20:46:15.407085Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1651, 2026-09-20T20:45:47.289846Z)
- `FUELINST|fuelType=OTHER|generation` = **290** (n=1651, 2026-09-20T20:45:47.289846Z)
- `FUELINST|fuelType=PS|generation` = **230** (n=1651, 2026-09-20T20:45:47.289846Z)
- `FUELINST|fuelType=WIND|generation` = **6314** (n=1651, 2026-09-20T20:45:47.289846Z)
- `IMBALNGC|TOTAL|imbalance` = **-5360** (n=271, 2026-09-20T20:22:08.658879Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=271, 2026-09-20T20:22:08.658879Z)
- `INDGEN|TOTAL|generation` = **15250** (n=271, 2026-09-20T20:22:08.658879Z)
- `MELNGC|TOTAL|margin` = **35539** (n=272, 2026-09-20T20:49:45.480150Z)
- `MID|dataProvider=APXMIDP|price` = **192.91** (n=11, 2026-09-20T20:42:19.161036Z)
- `MID|dataProvider=APXMIDP|volume` = **2427.2** (n=11, 2026-09-20T20:42:19.161036Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=22, 2026-09-20T20:42:19.161036Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=22, 2026-09-20T20:42:19.161036Z)
- `NDF|TOTAL|demand` = **20110** (n=278, 2026-09-20T20:47:37.817444Z)
- `TSDF|TOTAL|demand` = **20610** (n=278, 2026-09-20T20:47:37.817444Z)
- `WINDFOR|TOTAL|generation` = **1726** (n=47, 2026-09-20T19:30:32.161891Z)

## Latest publication events

- `2026-09-20T20:49:45.480150Z` — **MELNGC**: 1116 rows; marker `2026-09-20T20:47:00Z`
- `2026-09-20T20:48:25.992340Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:47:45Z`
- `2026-09-20T20:47:37.817444Z` — **TSDF**: 1116 rows; marker `2026-09-20T20:47:00Z`
- `2026-09-20T20:47:37.817444Z` — **NDF**: 62 rows; marker `2026-09-20T20:47:00Z`
- `2026-09-20T20:46:18.407408Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:45:45Z`
- `2026-09-20T20:45:47.289846Z` — **FUELINST**: 80 rows; marker `2026-09-20T20:45:00Z`
- `2026-09-20T20:44:27.053081Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:43:45Z`
- `2026-09-20T20:42:19.161036Z` — **MID**: 2 rows; marker `2026-09-20T20:42:03Z`
- `2026-09-20T20:42:19.161036Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:41:45Z`
- `2026-09-20T20:40:30.838746Z` — **FUELINST**: 80 rows; marker `2026-09-20T20:40:00Z`
- `2026-09-20T20:40:14.500115Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:39:45Z`
- `2026-09-20T20:38:21.870169Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:37:45Z`
- `2026-09-20T20:37:18.118771Z` — **MID**: 1 rows; marker `2026-09-20T20:35:00Z`
- `2026-09-20T20:36:13.801704Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:35:45Z`
- `2026-09-20T20:35:41.781921Z` — **FUELINST**: 80 rows; marker `2026-09-20T20:35:00Z`
