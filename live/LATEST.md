# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T02:12:16.352947Z`  
Current process started UTC: `2026-09-22T02:08:16.815043Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=5, z=3.99 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=-8, z=3.94 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3655, delta=1, z=4.18 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-1, z=4.06 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-4, z=4.09 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3658, delta=3, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3655, delta=2, z=4.14 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-3, z=4.13 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=3, z=4.20 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-5, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-1, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=-1, z=4.21 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3655, delta=1, z=4.24 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3654, delta=1, z=4.25 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=-1, z=4.25 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2001, 2026-09-22T02:10:25.532309Z)
- `FUELINST|fuelType=OTHER|generation` = **167** (n=2001, 2026-09-22T02:10:25.532309Z)
- `FUELINST|fuelType=PS|generation` = **-174** (n=2001, 2026-09-22T02:10:25.532309Z)
- `FUELINST|fuelType=WIND|generation` = **3846** (n=2001, 2026-09-22T02:10:25.532309Z)
- `IMBALNGC|TOTAL|imbalance` = **-2707** (n=329, 2026-09-22T01:51:01.471021Z)
- `INDDEM|TOTAL|demand` = **-12417** (n=329, 2026-09-22T01:51:01.471021Z)
- `INDGEN|TOTAL|generation` = **18752** (n=329, 2026-09-22T01:51:01.471021Z)
- `MELNGC|TOTAL|margin` = **36168** (n=329, 2026-09-22T01:49:09.493545Z)
- `MID|dataProvider=APXMIDP|price` = **142.13** (n=69, 2026-09-22T01:42:14.315312Z)
- `MID|dataProvider=APXMIDP|volume` = **2270.5** (n=69, 2026-09-22T01:42:14.315312Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=137, 2026-09-22T02:06:27.499024Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=137, 2026-09-22T02:06:27.499024Z)
- `NDF|TOTAL|demand` = **20959** (n=336, 2026-09-22T01:47:33.864588Z)
- `TSDF|TOTAL|demand` = **21459** (n=336, 2026-09-22T01:47:33.864588Z)
- `WINDFOR|TOTAL|generation` = **9503** (n=56, 2026-09-21T23:30:37.821418Z)

## Latest publication events

- `2026-09-22T02:10:25.532309Z` — **FUELINST**: 80 rows; marker `2026-09-22T02:10:00Z`
- `2026-09-22T02:10:25.532309Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:09:45Z`
- `2026-09-22T02:08:16.815050Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:07:45Z`
- `2026-09-22T02:06:27.499024Z` — **MID**: 1 rows; marker `2026-09-22T02:05:00Z`
- `2026-09-22T02:06:11.490082Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:05:45Z`
- `2026-09-22T02:05:23.948169Z` — **FUELINST**: 80 rows; marker `2026-09-22T02:05:00Z`
- `2026-09-22T02:04:19.711699Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:03:45Z`
- `2026-09-22T02:02:27.525599Z` — **FREQ**: 5761 rows; marker `2026-09-22T02:01:45Z`
- `2026-09-22T02:00:51.402865Z` — **FUELHH**: 20 rows; marker `2026-09-22T02:00:00Z`
- `2026-09-22T02:00:35.888989Z` — **FUELINST**: 80 rows; marker `2026-09-22T02:00:00Z`
- `2026-09-22T02:00:19.875797Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:59:45Z`
- `2026-09-22T01:58:10.292033Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:57:45Z`
- `2026-09-22T01:56:18.100509Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:55:45Z`
- `2026-09-22T01:55:30.426426Z` — **FUELINST**: 80 rows; marker `2026-09-22T01:55:00Z`
- `2026-09-22T01:54:14.552537Z` — **FREQ**: 5761 rows; marker `2026-09-22T01:53:45Z`
