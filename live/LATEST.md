# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T05:33:51.616397Z`  
Current process started UTC: `2026-09-21T05:29:51.307809Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3444, delta=44, z=9.38 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=813, delta=378, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3455, delta=6, z=9.04 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=824, delta=1, z=4.36 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3449, delta=1, z=8.81 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=823, delta=2, z=4.38 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3448, delta=-2, z=8.93 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=821, delta=5, z=4.38 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3450, delta=16, z=9.31 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=816, delta=5, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3434, delta=8, z=8.26 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=811, delta=28, z=4.33 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3426, delta=4, z=7.77 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=783, delta=279, z=4.05 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3400, delta=39, z=6.25 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1756, 2026-09-21T05:30:28.571701Z)
- `FUELINST|fuelType=OTHER|generation` = **867** (n=1756, 2026-09-21T05:30:28.571701Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1756, 2026-09-21T05:30:28.571701Z)
- `FUELINST|fuelType=WIND|generation` = **3861** (n=1756, 2026-09-21T05:30:28.571701Z)
- `IMBALNGC|TOTAL|imbalance` = **-4015** (n=289, 2026-09-21T05:19:58.754386Z)
- `INDDEM|TOTAL|demand` = **-11743** (n=289, 2026-09-21T05:19:58.754386Z)
- `INDGEN|TOTAL|generation` = **16595** (n=289, 2026-09-21T05:19:58.754386Z)
- `MELNGC|TOTAL|margin` = **37533** (n=289, 2026-09-21T05:18:36.808843Z)
- `MID|dataProvider=APXMIDP|price` = **167.58** (n=28, 2026-09-21T05:12:20.955026Z)
- `MID|dataProvider=APXMIDP|volume` = **2162.7** (n=28, 2026-09-21T05:12:20.955026Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=56, 2026-09-21T05:12:20.955026Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=56, 2026-09-21T05:12:20.955026Z)
- `NDF|TOTAL|demand` = **20110** (n=295, 2026-09-21T05:17:16.844589Z)
- `TSDF|TOTAL|demand` = **20610** (n=295, 2026-09-21T05:17:16.844589Z)
- `WINDFOR|TOTAL|generation` = **8794** (n=50, 2026-09-21T05:30:44.368414Z)

## Latest publication events

- `2026-09-21T05:32:04.656778Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:31:45Z`
- `2026-09-21T05:30:44.368414Z` — **WINDFOR**: 73 rows; marker `2026-09-21T05:30:00Z`
- `2026-09-21T05:30:28.571701Z` — **FUELHH**: 20 rows; marker `2026-09-21T05:30:00Z`
- `2026-09-21T05:30:28.571701Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:30:00Z`
- `2026-09-21T05:30:12.309862Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:29:45Z`
- `2026-09-21T05:28:04.713588Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:27:45Z`
- `2026-09-21T05:26:13.057299Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:25:45Z`
- `2026-09-21T05:25:40.719140Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:25:00Z`
- `2026-09-21T05:24:25.500923Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:23:45Z`
- `2026-09-21T05:22:16.087661Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:21:45Z`
- `2026-09-21T05:20:30.241601Z` — **FUELINST**: 80 rows; marker `2026-09-21T05:20:00Z`
- `2026-09-21T05:20:30.241601Z` — **FREQ**: 5761 rows; marker `2026-09-21T05:19:45Z`
- `2026-09-21T05:19:58.754386Z` — **INDGEN**: 810 rows; marker `2026-09-21T05:16:00Z`
- `2026-09-21T05:19:58.754386Z` — **INDDEM**: 810 rows; marker `2026-09-21T05:16:00Z`
- `2026-09-21T05:19:58.754386Z` — **IMBALNGC**: 810 rows; marker `2026-09-21T05:16:00Z`
