# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T12:46:10.768945Z`  
Current process started UTC: `2026-09-22T12:42:10.300985Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3659, delta=-2, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=1, z=3.60 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2128, 2026-09-22T12:45:37.461629Z)
- `FUELINST|fuelType=OTHER|generation` = **636** (n=2128, 2026-09-22T12:45:37.461629Z)
- `FUELINST|fuelType=PS|generation` = **-126** (n=2128, 2026-09-22T12:45:37.461629Z)
- `FUELINST|fuelType=WIND|generation` = **2549** (n=2128, 2026-09-22T12:45:37.461629Z)
- `IMBALNGC|TOTAL|imbalance` = **-7075** (n=349, 2026-09-22T12:23:54.131907Z)
- `INDDEM|TOTAL|demand` = **-12511** (n=349, 2026-09-22T12:23:38.146172Z)
- `INDGEN|TOTAL|generation` = **14083** (n=349, 2026-09-22T12:23:38.146172Z)
- `MELNGC|TOTAL|margin` = **37065** (n=349, 2026-09-22T12:20:42.277962Z)
- `MID|dataProvider=APXMIDP|price` = **122.03** (n=91, 2026-09-22T12:42:10.300993Z)
- `MID|dataProvider=APXMIDP|volume` = **4211.6** (n=91, 2026-09-22T12:42:10.300993Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=180, 2026-09-22T12:42:10.300993Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=180, 2026-09-22T12:42:10.300993Z)
- `NDF|TOTAL|demand` = **20658** (n=357, 2026-09-22T12:18:18.895814Z)
- `TSDF|TOTAL|demand` = **21158** (n=357, 2026-09-22T12:18:18.895814Z)
- `WINDFOR|TOTAL|generation` = **13082** (n=61, 2026-09-22T12:30:43.630179Z)

## Latest publication events

- `2026-09-22T12:45:37.461629Z` — **FUELINST**: 80 rows; marker `2026-09-22T12:45:00Z`
- `2026-09-22T12:44:18.637575Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:43:45Z`
- `2026-09-22T12:42:10.300993Z` — **MID**: 2 rows; marker `2026-09-22T12:42:03Z`
- `2026-09-22T12:42:10.300993Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:41:45Z`
- `2026-09-22T12:40:52.455244Z` — **FUELINST**: 80 rows; marker `2026-09-22T12:40:00Z`
- `2026-09-22T12:40:20.017812Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:39:45Z`
- `2026-09-22T12:38:43.671840Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:37:45Z`
- `2026-09-22T12:36:34.292120Z` — **MID**: 1 rows; marker `2026-09-22T12:35:00Z`
- `2026-09-22T12:36:18.282137Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:35:45Z`
- `2026-09-22T12:35:30.967784Z` — **FUELINST**: 80 rows; marker `2026-09-22T12:35:00Z`
- `2026-09-22T12:34:10.966777Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:33:45Z`
- `2026-09-22T12:32:20.151013Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:31:45Z`
- `2026-09-22T12:30:43.630179Z` — **WINDFOR**: 73 rows; marker `2026-09-22T12:30:00Z`
- `2026-09-22T12:30:43.630179Z` — **FUELHH**: 20 rows; marker `2026-09-22T12:30:00Z`
- `2026-09-22T12:30:27.795528Z` — **FUELINST**: 80 rows; marker `2026-09-22T12:30:00Z`
