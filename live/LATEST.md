# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T21:57:35.086899Z`  
Current process started UTC: `2026-09-21T21:53:35.318734Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3641, delta=-1, z=5.12 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3642, delta=-1, z=5.17 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3643, delta=-6, z=5.23 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=1, z=5.37 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=7, z=5.40 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3621, delta=45, z=5.10 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3641, delta=11, z=5.31 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3630, delta=10, z=5.15 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3620, delta=4, z=5.00 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3616, delta=2, z=4.96 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3614, delta=9, z=4.96 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3605, delta=9, z=4.82 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3576, delta=42, z=4.41 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3596, delta=9, z=4.68 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3587, delta=7, z=4.54 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1950, 2026-09-21T21:55:42.787442Z)
- `FUELINST|fuelType=OTHER|generation` = **208** (n=1950, 2026-09-21T21:55:42.787442Z)
- `FUELINST|fuelType=PS|generation` = **-9** (n=1950, 2026-09-21T21:55:42.787442Z)
- `FUELINST|fuelType=WIND|generation` = **3869** (n=1950, 2026-09-21T21:55:42.787442Z)
- `IMBALNGC|TOTAL|imbalance` = **-2513** (n=321, 2026-09-21T21:51:47.142688Z)
- `INDDEM|TOTAL|demand` = **-12258** (n=321, 2026-09-21T21:51:31.174771Z)
- `INDGEN|TOTAL|generation` = **18946** (n=321, 2026-09-21T21:51:31.174771Z)
- `MELNGC|TOTAL|margin` = **36139** (n=321, 2026-09-21T21:49:39.238592Z)
- `MID|dataProvider=APXMIDP|price` = **156.16** (n=61, 2026-09-21T21:42:14.237076Z)
- `MID|dataProvider=APXMIDP|volume` = **2626.3** (n=61, 2026-09-21T21:42:14.237076Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=120, 2026-09-21T21:42:14.237076Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=120, 2026-09-21T21:42:14.237076Z)
- `NDF|TOTAL|demand` = **20959** (n=328, 2026-09-21T21:47:36.336063Z)
- `TSDF|TOTAL|demand` = **21459** (n=328, 2026-09-21T21:47:51.844627Z)
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T21:56:31.029936Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:55:45Z`
- `2026-09-21T21:55:42.787442Z` — **FUELINST**: 80 rows; marker `2026-09-21T21:55:00Z`
- `2026-09-21T21:54:23.323895Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:53:45Z`
- `2026-09-21T21:52:19.432410Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:51:45Z`
- `2026-09-21T21:51:47.142688Z` — **IMBALNGC**: 1080 rows; marker `2026-09-21T21:47:00Z`
- `2026-09-21T21:51:31.174771Z` — **INDGEN**: 1080 rows; marker `2026-09-21T21:47:00Z`
- `2026-09-21T21:51:31.174771Z` — **INDDEM**: 1080 rows; marker `2026-09-21T21:47:00Z`
- `2026-09-21T21:50:42.182257Z` — **FUELINST**: 80 rows; marker `2026-09-21T21:50:00Z`
- `2026-09-21T21:50:26.725265Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:49:45Z`
- `2026-09-21T21:49:39.238592Z` — **MELNGC**: 1080 rows; marker `2026-09-21T21:47:00Z`
- `2026-09-21T21:48:23.747206Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:47:45Z`
- `2026-09-21T21:47:51.844627Z` — **TSDF**: 1080 rows; marker `2026-09-21T21:47:00Z`
- `2026-09-21T21:47:36.336063Z` — **NDF**: 60 rows; marker `2026-09-21T21:47:00Z`
- `2026-09-21T21:46:15.859307Z` — **FREQ**: 5761 rows; marker `2026-09-21T21:45:45Z`
- `2026-09-21T21:45:43.096420Z` — **FUELINST**: 80 rows; marker `2026-09-21T21:45:00Z`
