# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T00:34:40.894762Z`  
Current process started UTC: `2026-09-22T00:30:40.576583Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3652, delta=3, z=4.54 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3652, delta=-1, z=4.42 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=1, z=4.46 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3652, delta=0, z=4.46 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3652, delta=2, z=4.49 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=-2, z=4.48 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3652, delta=2, z=4.54 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3649, delta=2, z=4.64 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=4, z=4.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3646, delta=-1, z=4.49 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3647, delta=-3, z=4.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=-2, z=4.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3652, delta=3, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=-4, z=4.64 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3647, delta=5, z=4.77 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1981, 2026-09-22T00:30:40.576592Z)
- `FUELINST|fuelType=OTHER|generation` = **137** (n=1981, 2026-09-22T00:30:40.576592Z)
- `FUELINST|fuelType=PS|generation` = **-285** (n=1981, 2026-09-22T00:30:40.576592Z)
- `FUELINST|fuelType=WIND|generation` = **3688** (n=1981, 2026-09-22T00:30:40.576592Z)
- `IMBALNGC|TOTAL|imbalance` = **-1960** (n=326, 2026-09-22T00:21:07.271210Z)
- `INDDEM|TOTAL|demand` = **-12382** (n=326, 2026-09-22T00:20:51.247111Z)
- `INDGEN|TOTAL|generation` = **19499** (n=326, 2026-09-22T00:20:51.247111Z)
- `MELNGC|TOTAL|margin` = **36214** (n=326, 2026-09-22T00:19:14.685229Z)
- `MID|dataProvider=APXMIDP|price` = **143.47** (n=66, 2026-09-22T00:12:10.010962Z)
- `MID|dataProvider=APXMIDP|volume` = **2140.6** (n=66, 2026-09-22T00:12:10.010962Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=130, 2026-09-22T00:12:10.010962Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=130, 2026-09-22T00:12:10.010962Z)
- `NDF|TOTAL|demand` = **20959** (n=333, 2026-09-22T00:17:23.355768Z)
- `TSDF|TOTAL|demand` = **21459** (n=333, 2026-09-22T00:17:23.355768Z)
- `WINDFOR|TOTAL|generation` = **9503** (n=56, 2026-09-21T23:30:37.821418Z)

## Latest publication events

- `2026-09-22T00:34:25.632117Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:33:45Z`
- `2026-09-22T00:32:17.554088Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:31:45Z`
- `2026-09-22T00:30:40.576592Z` — **FUELHH**: 20 rows; marker `2026-09-22T00:30:00Z`
- `2026-09-22T00:30:40.576592Z` — **FUELINST**: 80 rows; marker `2026-09-22T00:30:00Z`
- `2026-09-22T00:30:16.603232Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:29:45Z`
- `2026-09-22T00:28:08.767673Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:27:45Z`
- `2026-09-22T00:26:17.172870Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:25:45Z`
- `2026-09-22T00:25:28.947445Z` — **FUELINST**: 80 rows; marker `2026-09-22T00:25:00Z`
- `2026-09-22T00:24:09.131819Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:23:45Z`
- `2026-09-22T00:22:17.299130Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:21:45Z`
- `2026-09-22T00:21:07.271210Z` — **IMBALNGC**: 990 rows; marker `2026-09-22T00:17:00Z`
- `2026-09-22T00:20:51.247111Z` — **INDGEN**: 990 rows; marker `2026-09-22T00:17:00Z`
- `2026-09-22T00:20:51.247111Z` — **INDDEM**: 990 rows; marker `2026-09-22T00:17:00Z`
- `2026-09-22T00:20:35.062985Z` — **FUELINST**: 80 rows; marker `2026-09-22T00:20:00Z`
- `2026-09-22T00:20:18.034191Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:19:45Z`
