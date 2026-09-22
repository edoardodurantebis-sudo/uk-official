# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T00:22:06.957701Z`  
Current process started UTC: `2026-09-22T00:18:07.176443Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=3, z=4.73 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=5, z=4.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=2, z=4.66 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1979, 2026-09-22T00:20:35.062985Z)
- `FUELINST|fuelType=OTHER|generation` = **152** (n=1979, 2026-09-22T00:20:35.062985Z)
- `FUELINST|fuelType=PS|generation` = **-285** (n=1979, 2026-09-22T00:20:35.062985Z)
- `FUELINST|fuelType=WIND|generation` = **3793** (n=1979, 2026-09-22T00:20:35.062985Z)
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

- `2026-09-22T00:21:07.271210Z` — **IMBALNGC**: 990 rows; marker `2026-09-22T00:17:00Z`
- `2026-09-22T00:20:51.247111Z` — **INDGEN**: 990 rows; marker `2026-09-22T00:17:00Z`
- `2026-09-22T00:20:51.247111Z` — **INDDEM**: 990 rows; marker `2026-09-22T00:17:00Z`
- `2026-09-22T00:20:35.062985Z` — **FUELINST**: 80 rows; marker `2026-09-22T00:20:00Z`
- `2026-09-22T00:20:18.034191Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:19:45Z`
- `2026-09-22T00:19:14.685229Z` — **MELNGC**: 990 rows; marker `2026-09-22T00:17:00Z`
- `2026-09-22T00:18:11.176978Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:17:45Z`
- `2026-09-22T00:17:23.355768Z` — **TSDF**: 990 rows; marker `2026-09-22T00:17:00Z`
- `2026-09-22T00:17:23.355768Z` — **NDF**: 55 rows; marker `2026-09-22T00:17:00Z`
- `2026-09-22T00:16:19.170589Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:15:45Z`
- `2026-09-22T00:15:31.487477Z` — **FUELINST**: 80 rows; marker `2026-09-22T00:15:00Z`
- `2026-09-22T00:14:11.396270Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:13:45Z`
- `2026-09-22T00:12:10.010962Z` — **MID**: 2 rows; marker `2026-09-22T00:12:03Z`
- `2026-09-22T00:12:10.010962Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:11:45Z`
- `2026-09-22T00:10:34.518023Z` — **FUELINST**: 80 rows; marker `2026-09-22T00:10:00Z`
