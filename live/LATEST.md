# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T06:19:45.632578Z`  
Current process started UTC: `2026-09-22T06:15:45.203725Z`  
1-second metadata polls in this process: **231**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=6, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3647, delta=3, z=3.52 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3650, delta=-4, z=3.64 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2050, 2026-09-22T06:15:45.203733Z)
- `FUELINST|fuelType=OTHER|generation` = **2025** (n=2050, 2026-09-22T06:15:45.203733Z)
- `FUELINST|fuelType=PS|generation` = **-172** (n=2050, 2026-09-22T06:15:45.203733Z)
- `FUELINST|fuelType=WIND|generation` = **3470** (n=2050, 2026-09-22T06:15:45.203733Z)
- `IMBALNGC|TOTAL|imbalance` = **-3209** (n=337, 2026-09-22T05:50:25.164362Z)
- `INDDEM|TOTAL|demand` = **-12477** (n=337, 2026-09-22T05:50:25.164362Z)
- `INDGEN|TOTAL|generation` = **18250** (n=337, 2026-09-22T05:50:25.164362Z)
- `MELNGC|TOTAL|margin` = **37790** (n=338, 2026-09-22T06:19:14.153555Z)
- `MID|dataProvider=APXMIDP|price` = **180.97** (n=78, 2026-09-22T06:12:19.847218Z)
- `MID|dataProvider=APXMIDP|volume` = **3045.3** (n=78, 2026-09-22T06:12:19.847218Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=154, 2026-09-22T06:12:19.847218Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=154, 2026-09-22T06:12:19.847218Z)
- `NDF|TOTAL|demand` = **20959** (n=345, 2026-09-22T06:17:20.431637Z)
- `TSDF|TOTAL|demand` = **21459** (n=345, 2026-09-22T06:17:20.431637Z)
- `WINDFOR|TOTAL|generation` = **12340** (n=58, 2026-09-22T05:30:40.954997Z)

## Latest publication events

- `2026-09-22T06:19:14.153555Z` — **MELNGC**: 774 rows; marker `2026-09-22T06:16:00Z`
- `2026-09-22T06:18:08.149785Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:17:45Z`
- `2026-09-22T06:17:20.431637Z` — **TSDF**: 774 rows; marker `2026-09-22T06:16:00Z`
- `2026-09-22T06:17:20.431637Z` — **NDF**: 43 rows; marker `2026-09-22T06:16:00Z`
- `2026-09-22T06:16:16.467290Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:15:45Z`
- `2026-09-22T06:15:45.203733Z` — **FUELINST**: 80 rows; marker `2026-09-22T06:15:00Z`
- `2026-09-22T06:14:12.136418Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:13:45Z`
- `2026-09-22T06:12:19.847218Z` — **MID**: 2 rows; marker `2026-09-22T06:12:03Z`
- `2026-09-22T06:12:19.847218Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:11:45Z`
- `2026-09-22T06:10:26.601371Z` — **FUELINST**: 80 rows; marker `2026-09-22T06:10:00Z`
- `2026-09-22T06:10:11.021537Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:09:45Z`
- `2026-09-22T06:08:19.351231Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:07:45Z`
- `2026-09-22T06:07:15.206258Z` — **MID**: 1 rows; marker `2026-09-22T06:05:00Z`
- `2026-09-22T06:06:09.645941Z` — **FREQ**: 5761 rows; marker `2026-09-22T06:05:45Z`
- `2026-09-22T06:05:22.027946Z` — **FUELINST**: 80 rows; marker `2026-09-22T06:05:00Z`
