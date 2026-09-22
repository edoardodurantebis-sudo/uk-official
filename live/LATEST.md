# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T15:32:02.875502Z`  
Current process started UTC: `2026-09-22T15:28:02.625305Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3729, delta=7, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3732, delta=1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3731, delta=9, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3737, delta=0, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3722, delta=43, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3737, delta=4, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3733, delta=3, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3730, delta=10, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3136, delta=-128, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3264, delta=142, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3122, delta=169, z=3.61 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=-1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3662, delta=5, z=3.53 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3659, delta=11, z=3.61 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2161, 2026-09-22T15:30:43.314812Z)
- `FUELINST|fuelType=OTHER|generation` = **801** (n=2161, 2026-09-22T15:30:43.314812Z)
- `FUELINST|fuelType=PS|generation` = **-18** (n=2161, 2026-09-22T15:30:43.314812Z)
- `FUELINST|fuelType=WIND|generation` = **1463** (n=2161, 2026-09-22T15:30:43.314812Z)
- `IMBALNGC|TOTAL|imbalance` = **-7955** (n=355, 2026-09-22T15:22:47.715019Z)
- `INDDEM|TOTAL|demand` = **-12481** (n=355, 2026-09-22T15:22:31.530428Z)
- `INDGEN|TOTAL|generation` = **13218** (n=355, 2026-09-22T15:22:47.715019Z)
- `MELNGC|TOTAL|margin` = **37207** (n=355, 2026-09-22T15:20:24.168308Z)
- `MID|dataProvider=APXMIDP|price` = **154.24** (n=96, 2026-09-22T15:12:11.007386Z)
- `MID|dataProvider=APXMIDP|volume` = **3866.8** (n=96, 2026-09-22T15:12:11.007386Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=190, 2026-09-22T15:12:11.007386Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=190, 2026-09-22T15:12:11.007386Z)
- `NDF|TOTAL|demand` = **20673** (n=363, 2026-09-22T15:18:00.107683Z)
- `TSDF|TOTAL|demand` = **21173** (n=363, 2026-09-22T15:18:00.107683Z)
- `WINDFOR|TOTAL|generation` = **13082** (n=61, 2026-09-22T12:30:43.630179Z)

## Latest publication events

- `2026-09-22T15:30:59.346860Z` — **FUELHH**: 20 rows; marker `2026-09-22T15:30:00Z`
- `2026-09-22T15:30:43.314812Z` — **FUELINST**: 80 rows; marker `2026-09-22T15:30:00Z`
- `2026-09-22T15:30:27.113509Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:29:45Z`
- `2026-09-22T15:28:18.626830Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:27:45Z`
- `2026-09-22T15:26:16.164439Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:25:45Z`
- `2026-09-22T15:25:27.986536Z` — **FUELINST**: 80 rows; marker `2026-09-22T15:25:00Z`
- `2026-09-22T15:24:08.223748Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:23:45Z`
- `2026-09-22T15:22:47.715019Z` — **INDGEN**: 1314 rows; marker `2026-09-22T15:17:00Z`
- `2026-09-22T15:22:47.715019Z` — **IMBALNGC**: 1314 rows; marker `2026-09-22T15:17:00Z`
- `2026-09-22T15:22:31.530428Z` — **INDDEM**: 1314 rows; marker `2026-09-22T15:17:00Z`
- `2026-09-22T15:22:16.068917Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:21:45Z`
- `2026-09-22T15:20:24.168308Z` — **MELNGC**: 1314 rows; marker `2026-09-22T15:17:00Z`
- `2026-09-22T15:20:24.168308Z` — **FUELINST**: 80 rows; marker `2026-09-22T15:20:00Z`
- `2026-09-22T15:20:08.798674Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:19:45Z`
- `2026-09-22T15:18:16.145057Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:17:45Z`
