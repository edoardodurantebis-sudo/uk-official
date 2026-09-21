# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T23:52:19.540319Z`  
Current process started UTC: `2026-09-21T23:48:19.750951Z`  
1-second metadata polls in this process: **232**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3647, delta=-3, z=4.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=-2, z=4.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3652, delta=3, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=-4, z=4.64 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3647, delta=5, z=4.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=3, z=4.73 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=5, z=4.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=2, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3643, delta=-2, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=0, z=4.72 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=-2, z=4.75 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3642, delta=4, z=4.87 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3647, delta=5, z=4.81 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3642, delta=-2, z=4.75 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3644, delta=-2, z=4.82 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1973, 2026-09-21T23:50:44.243079Z)
- `FUELINST|fuelType=OTHER|generation` = **181** (n=1973, 2026-09-21T23:50:44.243079Z)
- `FUELINST|fuelType=PS|generation` = **-284** (n=1973, 2026-09-21T23:50:44.243079Z)
- `FUELINST|fuelType=WIND|generation` = **3745** (n=1973, 2026-09-21T23:50:44.243079Z)
- `IMBALNGC|TOTAL|imbalance` = **-2010** (n=325, 2026-09-21T23:51:16.103087Z)
- `INDDEM|TOTAL|demand` = **-12382** (n=325, 2026-09-21T23:51:16.103087Z)
- `INDGEN|TOTAL|generation` = **19449** (n=325, 2026-09-21T23:51:16.103087Z)
- `MELNGC|TOTAL|margin` = **36218** (n=325, 2026-09-21T23:49:39.843008Z)
- `MID|dataProvider=APXMIDP|price` = **139.68** (n=65, 2026-09-21T23:42:13.807294Z)
- `MID|dataProvider=APXMIDP|volume` = **1760.8** (n=65, 2026-09-21T23:42:13.807294Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=128, 2026-09-21T23:42:13.807294Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=128, 2026-09-21T23:42:13.807294Z)
- `NDF|TOTAL|demand` = **20959** (n=332, 2026-09-21T23:47:50.474224Z)
- `TSDF|TOTAL|demand` = **21459** (n=332, 2026-09-21T23:47:50.474224Z)
- `WINDFOR|TOTAL|generation` = **9503** (n=56, 2026-09-21T23:30:37.821418Z)

## Latest publication events

- `2026-09-21T23:52:03.776608Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:51:45Z`
- `2026-09-21T23:51:16.103087Z` — **INDGEN**: 1008 rows; marker `2026-09-21T23:47:00Z`
- `2026-09-21T23:51:16.103087Z` — **INDDEM**: 1008 rows; marker `2026-09-21T23:47:00Z`
- `2026-09-21T23:51:16.103087Z` — **IMBALNGC**: 1008 rows; marker `2026-09-21T23:47:00Z`
- `2026-09-21T23:50:44.243079Z` — **FUELINST**: 80 rows; marker `2026-09-21T23:50:00Z`
- `2026-09-21T23:50:28.032193Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:49:45Z`
- `2026-09-21T23:49:39.843008Z` — **MELNGC**: 1008 rows; marker `2026-09-21T23:47:00Z`
- `2026-09-21T23:48:19.750988Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:47:45Z`
- `2026-09-21T23:47:50.474224Z` — **TSDF**: 1008 rows; marker `2026-09-21T23:47:00Z`
- `2026-09-21T23:47:50.474224Z` — **NDF**: 56 rows; marker `2026-09-21T23:47:00Z`
- `2026-09-21T23:46:14.475785Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:45:45Z`
- `2026-09-21T23:45:42.766939Z` — **FUELINST**: 80 rows; marker `2026-09-21T23:45:00Z`
- `2026-09-21T23:44:22.297982Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:43:45Z`
- `2026-09-21T23:42:13.807294Z` — **MID**: 2 rows; marker `2026-09-21T23:42:03Z`
- `2026-09-21T23:42:13.807294Z` — **FREQ**: 5761 rows; marker `2026-09-21T23:41:45Z`
