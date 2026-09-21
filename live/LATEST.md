# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T07:44:30.563454Z`  
Current process started UTC: `2026-09-21T07:40:30.693798Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=5, z=7.18 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=793, delta=-7, z=3.54 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-2, z=7.07 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=800, delta=-4, z=3.62 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3499, delta=5, z=8.02 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=805, delta=-32, z=3.79 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3498, delta=4, z=7.26 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=804, delta=-2, z=3.67 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3494, delta=-6, z=7.20 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=806, delta=2, z=3.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3500, delta=-1, z=7.58 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=804, delta=0, z=3.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=1, z=7.75 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=804, delta=0, z=3.72 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3500, delta=1, z=7.84 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1782, 2026-09-21T07:40:30.693807Z)
- `FUELINST|fuelType=OTHER|generation` = **2161** (n=1782, 2026-09-21T07:40:30.693807Z)
- `FUELINST|fuelType=PS|generation` = **-10** (n=1782, 2026-09-21T07:40:30.693807Z)
- `FUELINST|fuelType=WIND|generation` = **4280** (n=1782, 2026-09-21T07:40:30.693807Z)
- `IMBALNGC|TOTAL|imbalance` = **-3297** (n=293, 2026-09-21T07:20:01.335621Z)
- `INDDEM|TOTAL|demand` = **-12833** (n=293, 2026-09-21T07:19:45.573026Z)
- `INDGEN|TOTAL|generation` = **17972** (n=293, 2026-09-21T07:19:45.573026Z)
- `MELNGC|TOTAL|margin` = **38254** (n=293, 2026-09-21T07:18:45.711844Z)
- `MID|dataProvider=APXMIDP|price` = **201.36** (n=33, 2026-09-21T07:42:06.733970Z)
- `MID|dataProvider=APXMIDP|volume` = **2565.6** (n=33, 2026-09-21T07:42:06.733970Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=66, 2026-09-21T07:42:06.733970Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=66, 2026-09-21T07:42:06.733970Z)
- `NDF|TOTAL|demand` = **20110** (n=299, 2026-09-21T07:17:09.233740Z)
- `TSDF|TOTAL|demand` = **21269** (n=299, 2026-09-21T07:17:09.233740Z)
- `WINDFOR|TOTAL|generation` = **8794** (n=50, 2026-09-21T05:30:44.368414Z)

## Latest publication events

- `2026-09-21T07:44:14.513023Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:43:45Z`
- `2026-09-21T07:42:22.926040Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:41:45Z`
- `2026-09-21T07:42:06.733970Z` — **MID**: 2 rows; marker `2026-09-21T07:42:03Z`
- `2026-09-21T07:40:30.693807Z` — **FUELINST**: 80 rows; marker `2026-09-21T07:40:00Z`
- `2026-09-21T07:40:30.693807Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:39:45Z`
- `2026-09-21T07:38:14.818569Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:37:45Z`
- `2026-09-21T07:36:38.807113Z` — **MID**: 1 rows; marker `2026-09-21T07:35:00Z`
- `2026-09-21T07:36:23.272594Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:35:45Z`
- `2026-09-21T07:35:36.180614Z` — **FUELINST**: 80 rows; marker `2026-09-21T07:35:00Z`
- `2026-09-21T07:34:15.656482Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:33:45Z`
- `2026-09-21T07:32:24.379754Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:31:45Z`
- `2026-09-21T07:30:36.300397Z` — **FUELHH**: 20 rows; marker `2026-09-21T07:30:00Z`
- `2026-09-21T07:30:36.300397Z` — **FUELINST**: 80 rows; marker `2026-09-21T07:30:00Z`
- `2026-09-21T07:30:20.159348Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:29:45Z`
- `2026-09-21T07:28:12.200568Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:27:45Z`
