# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T03:11:49.653031Z`  
Current process started UTC: `2026-09-22T03:07:49.480962Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=6, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3655, delta=1, z=3.87 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3654, delta=1, z=3.96 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-2, z=3.87 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=2, z=3.92 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=1, z=3.91 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=0, z=3.91 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=0, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-7, z=3.94 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-2, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=1, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3659, delta=5, z=4.06 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=2, z=4.01 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3652, delta=2, z=4.00 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=5, z=3.99 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2013, 2026-09-22T03:10:45.262112Z)
- `FUELINST|fuelType=OTHER|generation` = **209** (n=2013, 2026-09-22T03:10:45.262112Z)
- `FUELINST|fuelType=PS|generation` = **-170** (n=2013, 2026-09-22T03:10:45.262112Z)
- `FUELINST|fuelType=WIND|generation` = **4030** (n=2013, 2026-09-22T03:10:45.262112Z)
- `IMBALNGC|TOTAL|imbalance` = **-2659** (n=331, 2026-09-22T02:50:47.389141Z)
- `INDDEM|TOTAL|demand` = **-12500** (n=331, 2026-09-22T02:50:47.389141Z)
- `INDGEN|TOTAL|generation` = **18800** (n=331, 2026-09-22T02:50:47.389141Z)
- `MELNGC|TOTAL|margin` = **37837** (n=331, 2026-09-22T02:49:27.371772Z)
- `MID|dataProvider=APXMIDP|price` = **139.03** (n=71, 2026-09-22T02:42:15.162936Z)
- `MID|dataProvider=APXMIDP|volume` = **2028.3** (n=71, 2026-09-22T02:42:15.162936Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=141, 2026-09-22T03:07:27.944651Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=141, 2026-09-22T03:07:27.944651Z)
- `NDF|TOTAL|demand` = **20959** (n=338, 2026-09-22T02:47:20.220307Z)
- `TSDF|TOTAL|demand` = **21459** (n=338, 2026-09-22T02:47:20.220307Z)
- `WINDFOR|TOTAL|generation` = **9503** (n=56, 2026-09-21T23:30:37.821418Z)

## Latest publication events

- `2026-09-22T03:10:45.262112Z` — **FUELINST**: 80 rows; marker `2026-09-22T03:10:00Z`
- `2026-09-22T03:10:13.913535Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:09:45Z`
- `2026-09-22T03:08:21.532610Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:07:45Z`
- `2026-09-22T03:07:27.944651Z` — **MID**: 1 rows; marker `2026-09-22T03:05:00Z`
- `2026-09-22T03:06:24.549069Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:05:45Z`
- `2026-09-22T03:05:36.758655Z` — **FUELINST**: 80 rows; marker `2026-09-22T03:05:00Z`
- `2026-09-22T03:04:16.436340Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:03:45Z`
- `2026-09-22T03:02:15.875850Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:01:45Z`
- `2026-09-22T03:00:40.146373Z` — **FUELHH**: 20 rows; marker `2026-09-22T03:00:00Z`
- `2026-09-22T03:00:40.146373Z` — **FUELINST**: 80 rows; marker `2026-09-22T03:00:00Z`
- `2026-09-22T03:00:24.783841Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:59:45Z`
- `2026-09-22T02:58:16.944023Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:57:45Z`
- `2026-09-22T02:56:24.768180Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:55:45Z`
- `2026-09-22T02:55:36.754047Z` — **FUELINST**: 80 rows; marker `2026-09-22T02:55:00Z`
- `2026-09-22T02:54:14.854492Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:53:45Z`
