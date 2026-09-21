# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T06:28:37.702450Z`  
Current process started UTC: `2026-09-21T06:24:37.940182Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3495, delta=4, z=9.11 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=837, delta=-1, z=4.24 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3491, delta=-1, z=9.10 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=838, delta=1, z=4.27 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3492, delta=-4, z=9.38 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=837, delta=10, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=9, z=9.87 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=827, delta=7, z=4.21 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3487, delta=11, z=9.59 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=820, delta=-5, z=4.16 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3468, delta=24, z=9.91 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=826, delta=13, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3476, delta=3, z=9.14 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=825, delta=-4, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3473, delta=7, z=9.17 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1767, 2026-09-21T06:25:27.946343Z)
- `FUELINST|fuelType=OTHER|generation` = **2583** (n=1767, 2026-09-21T06:25:27.946343Z)
- `FUELINST|fuelType=PS|generation` = **226** (n=1767, 2026-09-21T06:25:27.946343Z)
- `FUELINST|fuelType=WIND|generation` = **3713** (n=1767, 2026-09-21T06:25:27.946343Z)
- `IMBALNGC|TOTAL|imbalance` = **-3867** (n=291, 2026-09-21T06:19:53.385768Z)
- `INDDEM|TOTAL|demand` = **-12146** (n=291, 2026-09-21T06:19:53.385768Z)
- `INDGEN|TOTAL|generation` = **16734** (n=291, 2026-09-21T06:19:53.385768Z)
- `MELNGC|TOTAL|margin` = **38135** (n=291, 2026-09-21T06:19:04.392006Z)
- `MID|dataProvider=APXMIDP|price` = **194.74** (n=30, 2026-09-21T06:12:12.514844Z)
- `MID|dataProvider=APXMIDP|volume` = **2536.8** (n=30, 2026-09-21T06:12:12.514844Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=60, 2026-09-21T06:12:12.514844Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=60, 2026-09-21T06:12:12.514844Z)
- `NDF|TOTAL|demand` = **20110** (n=297, 2026-09-21T06:16:56.393050Z)
- `TSDF|TOTAL|demand` = **20610** (n=297, 2026-09-21T06:16:56.393050Z)
- `WINDFOR|TOTAL|generation` = **8794** (n=50, 2026-09-21T05:30:44.368414Z)

## Latest publication events

- `2026-09-21T06:28:08.223602Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:27:45Z`
- `2026-09-21T06:26:16.349699Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:25:45Z`
- `2026-09-21T06:25:27.946343Z` — **FUELINST**: 80 rows; marker `2026-09-21T06:25:00Z`
- `2026-09-21T06:24:07.245659Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:23:45Z`
- `2026-09-21T06:22:15.094718Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:21:45Z`
- `2026-09-21T06:20:23.212498Z` — **FUELINST**: 80 rows; marker `2026-09-21T06:20:00Z`
- `2026-09-21T06:20:23.212498Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:19:45Z`
- `2026-09-21T06:19:53.385768Z` — **INDGEN**: 774 rows; marker `2026-09-21T06:16:00Z`
- `2026-09-21T06:19:53.385768Z` — **INDDEM**: 774 rows; marker `2026-09-21T06:16:00Z`
- `2026-09-21T06:19:53.385768Z` — **IMBALNGC**: 774 rows; marker `2026-09-21T06:16:00Z`
- `2026-09-21T06:19:04.392006Z` — **MELNGC**: 774 rows; marker `2026-09-21T06:16:00Z`
- `2026-09-21T06:18:16.832654Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:17:45Z`
- `2026-09-21T06:16:56.393050Z` — **TSDF**: 774 rows; marker `2026-09-21T06:16:00Z`
- `2026-09-21T06:16:56.393050Z` — **NDF**: 43 rows; marker `2026-09-21T06:16:00Z`
- `2026-09-21T06:16:08.921130Z` — **FREQ**: 5761 rows; marker `2026-09-21T06:15:45Z`
