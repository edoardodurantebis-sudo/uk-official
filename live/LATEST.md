# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T09:34:06.813596Z`  
Current process started UTC: `2026-09-22T09:30:06.849928Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3136, delta=-128, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3264, delta=142, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3122, delta=169, z=3.61 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=-1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3662, delta=5, z=3.53 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3659, delta=11, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3659, delta=-2, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=1, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=-3, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3663, delta=14, z=3.65 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-2, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-5, z=3.50 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2089, 2026-09-22T09:30:38.288528Z)
- `FUELINST|fuelType=OTHER|generation` = **575** (n=2089, 2026-09-22T09:30:38.288528Z)
- `FUELINST|fuelType=PS|generation` = **-171** (n=2089, 2026-09-22T09:30:38.288528Z)
- `FUELINST|fuelType=WIND|generation` = **3566** (n=2089, 2026-09-22T09:30:38.288528Z)
- `IMBALNGC|TOTAL|imbalance` = **2430** (n=343, 2026-09-22T09:19:17.697388Z)
- `INDDEM|TOTAL|demand` = **-12801** (n=343, 2026-09-22T09:19:01.822080Z)
- `INDGEN|TOTAL|generation` = **23498** (n=343, 2026-09-22T09:19:01.822080Z)
- `MELNGC|TOTAL|margin` = **40334** (n=343, 2026-09-22T09:18:29.864815Z)
- `MID|dataProvider=APXMIDP|price` = **129.53** (n=84, 2026-09-22T09:12:11.831090Z)
- `MID|dataProvider=APXMIDP|volume` = **2865.1** (n=84, 2026-09-22T09:12:11.831090Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=166, 2026-09-22T09:12:11.831090Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=166, 2026-09-22T09:12:11.831090Z)
- `NDF|TOTAL|demand` = **20320** (n=351, 2026-09-22T09:16:54.603659Z)
- `TSDF|TOTAL|demand` = **21068** (n=351, 2026-09-22T09:16:54.603659Z)
- `WINDFOR|TOTAL|generation` = **12393** (n=59, 2026-09-22T08:31:02.929426Z)

## Latest publication events

- `2026-09-22T09:32:30.300160Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:31:45Z`
- `2026-09-22T09:30:38.288528Z` — **FUELHH**: 20 rows; marker `2026-09-22T09:30:00Z`
- `2026-09-22T09:30:38.288528Z` — **FUELINST**: 80 rows; marker `2026-09-22T09:30:00Z`
- `2026-09-22T09:30:22.852003Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:29:45Z`
- `2026-09-22T09:28:18.648635Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:27:45Z`
- `2026-09-22T09:26:26.897035Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:25:45Z`
- `2026-09-22T09:25:38.577564Z` — **FUELINST**: 80 rows; marker `2026-09-22T09:25:00Z`
- `2026-09-22T09:24:18.780637Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:23:45Z`
- `2026-09-22T09:22:27.050360Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:21:45Z`
- `2026-09-22T09:20:38.000635Z` — **FUELINST**: 80 rows; marker `2026-09-22T09:20:00Z`
- `2026-09-22T09:20:21.568901Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:19:45Z`
- `2026-09-22T09:19:17.697388Z` — **IMBALNGC**: 666 rows; marker `2026-09-22T09:16:00Z`
- `2026-09-22T09:19:01.822080Z` — **INDGEN**: 666 rows; marker `2026-09-22T09:16:00Z`
- `2026-09-22T09:19:01.822080Z` — **INDDEM**: 666 rows; marker `2026-09-22T09:16:00Z`
- `2026-09-22T09:18:29.864815Z` — **MELNGC**: 666 rows; marker `2026-09-22T09:16:00Z`
