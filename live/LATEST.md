# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T03:17:48.256712Z`  
Current process started UTC: `2026-09-21T03:13:47.372527Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1729, 2026-09-21T03:15:39.293002Z)
- `FUELINST|fuelType=OTHER|generation` = **150** (n=1729, 2026-09-21T03:15:39.293002Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1729, 2026-09-21T03:15:39.293002Z)
- `FUELINST|fuelType=WIND|generation` = **3766** (n=1729, 2026-09-21T03:15:39.293002Z)
- `IMBALNGC|TOTAL|imbalance` = **-4865** (n=284, 2026-09-21T02:50:47.426347Z)
- `INDDEM|TOTAL|demand` = **-11802** (n=284, 2026-09-21T02:50:47.426347Z)
- `INDGEN|TOTAL|generation` = **15745** (n=284, 2026-09-21T02:50:47.426347Z)
- `MELNGC|TOTAL|margin` = **37560** (n=284, 2026-09-21T02:49:27.461116Z)
- `MID|dataProvider=APXMIDP|price` = **138.05** (n=24, 2026-09-21T03:12:10.827573Z)
- `MID|dataProvider=APXMIDP|volume` = **2255.8** (n=24, 2026-09-21T03:12:10.827573Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=48, 2026-09-21T03:12:10.827573Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=48, 2026-09-21T03:12:10.827573Z)
- `NDF|TOTAL|demand` = **20110** (n=291, 2026-09-21T03:17:46.317131Z)
- `TSDF|TOTAL|demand` = **20610** (n=291, 2026-09-21T03:17:46.317131Z)
- `WINDFOR|TOTAL|generation` = **1603** (n=48, 2026-09-20T23:30:37.519891Z)

## Latest publication events

- `2026-09-21T03:17:46.317131Z` — **TSDF**: 882 rows; marker `2026-09-21T03:17:00Z`
- `2026-09-21T03:17:46.317131Z` — **NDF**: 49 rows; marker `2026-09-21T03:17:00Z`
- `2026-09-21T03:16:10.501635Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:15:45Z`
- `2026-09-21T03:15:39.293002Z` — **FUELINST**: 80 rows; marker `2026-09-21T03:15:00Z`
- `2026-09-21T03:14:19.377010Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:13:45Z`
- `2026-09-21T03:12:10.827573Z` — **MID**: 2 rows; marker `2026-09-21T03:12:03Z`
- `2026-09-21T03:12:10.827573Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:11:45Z`
- `2026-09-21T03:10:35.076354Z` — **FUELINST**: 80 rows; marker `2026-09-21T03:10:00Z`
- `2026-09-21T03:10:18.907611Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:09:45Z`
- `2026-09-21T03:08:14.740272Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:07:45Z`
- `2026-09-21T03:06:23.329982Z` — **MID**: 1 rows; marker `2026-09-21T03:05:00Z`
- `2026-09-21T03:06:07.476978Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:05:45Z`
- `2026-09-21T03:05:34.221176Z` — **FUELINST**: 80 rows; marker `2026-09-21T03:05:00Z`
- `2026-09-21T03:04:20.752074Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:03:45Z`
- `2026-09-21T03:02:13.040565Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:01:45Z`
