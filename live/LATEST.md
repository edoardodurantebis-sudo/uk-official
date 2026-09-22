# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T03:20:28.291429Z`  
Current process started UTC: `2026-09-22T03:16:27.907744Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=-1, z=3.91 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2014, 2026-09-22T03:15:45.959247Z)
- `FUELINST|fuelType=OTHER|generation` = **240** (n=2014, 2026-09-22T03:15:45.959247Z)
- `FUELINST|fuelType=PS|generation` = **-171** (n=2014, 2026-09-22T03:15:45.959247Z)
- `FUELINST|fuelType=WIND|generation` = **3942** (n=2014, 2026-09-22T03:15:45.959247Z)
- `IMBALNGC|TOTAL|imbalance` = **-2659** (n=331, 2026-09-22T02:50:47.389141Z)
- `INDDEM|TOTAL|demand` = **-12500** (n=331, 2026-09-22T02:50:47.389141Z)
- `INDGEN|TOTAL|generation` = **18800** (n=331, 2026-09-22T02:50:47.389141Z)
- `MELNGC|TOTAL|margin` = **37794** (n=332, 2026-09-22T03:19:41.062165Z)
- `MID|dataProvider=APXMIDP|price` = **136.31** (n=72, 2026-09-22T03:12:15.087057Z)
- `MID|dataProvider=APXMIDP|volume` = **1871.5** (n=72, 2026-09-22T03:12:15.087057Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=142, 2026-09-22T03:12:15.087057Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=142, 2026-09-22T03:12:15.087057Z)
- `NDF|TOTAL|demand` = **20959** (n=339, 2026-09-22T03:17:16.111810Z)
- `TSDF|TOTAL|demand` = **21459** (n=339, 2026-09-22T03:17:32.668673Z)
- `WINDFOR|TOTAL|generation` = **9503** (n=56, 2026-09-21T23:30:37.821418Z)

## Latest publication events

- `2026-09-22T03:20:13.123364Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:19:45Z`
- `2026-09-22T03:19:41.062165Z` — **MELNGC**: 882 rows; marker `2026-09-22T03:17:00Z`
- `2026-09-22T03:18:04.226152Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:17:45Z`
- `2026-09-22T03:17:32.668673Z` — **TSDF**: 882 rows; marker `2026-09-22T03:17:00Z`
- `2026-09-22T03:17:16.111810Z` — **NDF**: 49 rows; marker `2026-09-22T03:17:00Z`
- `2026-09-22T03:16:27.907753Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:15:45Z`
- `2026-09-22T03:15:45.959247Z` — **FUELINST**: 80 rows; marker `2026-09-22T03:15:00Z`
- `2026-09-22T03:14:25.817814Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:13:45Z`
- `2026-09-22T03:12:15.087057Z` — **MID**: 2 rows; marker `2026-09-22T03:12:03Z`
- `2026-09-22T03:12:15.087057Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:11:45Z`
- `2026-09-22T03:10:45.262112Z` — **FUELINST**: 80 rows; marker `2026-09-22T03:10:00Z`
- `2026-09-22T03:10:13.913535Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:09:45Z`
- `2026-09-22T03:08:21.532610Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:07:45Z`
- `2026-09-22T03:07:27.944651Z` — **MID**: 1 rows; marker `2026-09-22T03:05:00Z`
- `2026-09-22T03:06:24.549069Z` — **FREQ**: 5761 rows; marker `2026-09-22T03:05:45Z`
