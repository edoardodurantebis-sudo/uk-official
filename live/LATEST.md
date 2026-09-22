# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T01:42:29.754466Z`  
Current process started UTC: `2026-09-22T01:38:29.740536Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-3, z=4.13 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=3, z=4.20 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-5, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-1, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-1, z=4.21 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3655, delta=1, z=4.24 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=1, z=4.25 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-1, z=4.25 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-6, z=4.29 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3659, delta=7, z=4.50 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=-1, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=2, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3659, delta=1, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3658, delta=-1, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3659, delta=2, z=4.47 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1995, 2026-09-22T01:40:22.704931Z)
- `FUELINST|fuelType=OTHER|generation` = **219** (n=1995, 2026-09-22T01:40:22.704931Z)
- `FUELINST|fuelType=PS|generation` = **-285** (n=1995, 2026-09-22T01:40:22.704931Z)
- `FUELINST|fuelType=WIND|generation` = **3601** (n=1995, 2026-09-22T01:40:22.704931Z)
- `IMBALNGC|TOTAL|imbalance` = **-2699** (n=328, 2026-09-22T01:21:30.196066Z)
- `INDDEM|TOTAL|demand` = **-12404** (n=328, 2026-09-22T01:21:30.196066Z)
- `INDGEN|TOTAL|generation` = **18760** (n=328, 2026-09-22T01:21:30.196066Z)
- `MELNGC|TOTAL|margin` = **36168** (n=328, 2026-09-22T01:19:23.823814Z)
- `MID|dataProvider=APXMIDP|price` = **142.13** (n=69, 2026-09-22T01:42:14.315312Z)
- `MID|dataProvider=APXMIDP|volume` = **2270.5** (n=69, 2026-09-22T01:42:14.315312Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=136, 2026-09-22T01:42:14.315312Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=136, 2026-09-22T01:42:14.315312Z)
- `NDF|TOTAL|demand` = **20959** (n=335, 2026-09-22T01:17:31.321953Z)
- `TSDF|TOTAL|demand` = **21459** (n=335, 2026-09-22T01:17:31.321953Z)
- `WINDFOR|TOTAL|generation` = **9503** (n=56, 2026-09-21T23:30:37.821418Z)

## Latest publication events

- `2026-09-22T01:42:14.315312Z` — **MID**: 2 rows; marker `2026-09-22T01:42:03Z`
- `2026-09-22T01:42:14.315312Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:41:45Z`
- `2026-09-22T01:40:22.704931Z` — **FUELINST**: 80 rows; marker `2026-09-22T01:40:00Z`
- `2026-09-22T01:40:06.449251Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:39:45Z`
- `2026-09-22T01:38:11.924957Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:37:45Z`
- `2026-09-22T01:36:19.890093Z` — **MID**: 1 rows; marker `2026-09-22T01:35:00Z`
- `2026-09-22T01:36:19.890093Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:35:45Z`
- `2026-09-22T01:35:48.360566Z` — **FUELINST**: 80 rows; marker `2026-09-22T01:35:00Z`
- `2026-09-22T01:34:12.690528Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:33:45Z`
- `2026-09-22T01:32:22.155910Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:31:45Z`
- `2026-09-22T01:30:45.390757Z` — **FUELHH**: 20 rows; marker `2026-09-22T01:30:00Z`
- `2026-09-22T01:30:45.390757Z` — **FUELINST**: 80 rows; marker `2026-09-22T01:30:00Z`
- `2026-09-22T01:30:13.998068Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:29:45Z`
- `2026-09-22T01:28:23.899244Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:27:45Z`
- `2026-09-22T01:26:15.739659Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:25:45Z`
