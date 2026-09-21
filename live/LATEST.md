# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T08:09:45.784386Z`  
Current process started UTC: `2026-09-21T08:05:45.728746Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=0, z=6.62 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3500, delta=1, z=7.30 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=791, delta=-14, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=-2, z=6.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=0, z=6.88 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=-3, z=6.98 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=3, z=7.20 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=5, z=7.18 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=793, delta=-7, z=3.54 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-2, z=7.07 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=800, delta=-4, z=3.62 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3499, delta=5, z=8.02 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=805, delta=-32, z=3.79 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3498, delta=4, z=7.26 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=804, delta=-2, z=3.67 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1787, 2026-09-21T08:05:45.728752Z)
- `FUELINST|fuelType=OTHER|generation` = **1671** (n=1787, 2026-09-21T08:05:45.728752Z)
- `FUELINST|fuelType=PS|generation` = **-10** (n=1787, 2026-09-21T08:05:45.728752Z)
- `FUELINST|fuelType=WIND|generation` = **4451** (n=1787, 2026-09-21T08:05:45.728752Z)
- `IMBALNGC|TOTAL|imbalance` = **-3297** (n=293, 2026-09-21T07:20:01.335621Z)
- `INDDEM|TOTAL|demand` = **-12833** (n=293, 2026-09-21T07:19:45.573026Z)
- `INDGEN|TOTAL|generation` = **17972** (n=293, 2026-09-21T07:19:45.573026Z)
- `MELNGC|TOTAL|margin` = **38254** (n=293, 2026-09-21T07:18:45.711844Z)
- `MID|dataProvider=APXMIDP|price` = **201.36** (n=33, 2026-09-21T07:42:06.733970Z)
- `MID|dataProvider=APXMIDP|volume` = **2565.6** (n=33, 2026-09-21T07:42:06.733970Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=67, 2026-09-21T08:06:17.463257Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=67, 2026-09-21T08:06:17.463257Z)
- `NDF|TOTAL|demand` = **21092** (n=300, 2026-09-21T07:45:48.625669Z)
- `TSDF|TOTAL|demand` = **21592** (n=300, 2026-09-21T07:45:48.625669Z)
- `WINDFOR|TOTAL|generation` = **8794** (n=50, 2026-09-21T05:30:44.368414Z)

## Latest publication events

- `2026-09-21T08:08:09.020763Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:07:45Z`
- `2026-09-21T08:06:17.463257Z` — **MID**: 1 rows; marker `2026-09-21T08:05:00Z`
- `2026-09-21T08:06:17.463257Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:05:45Z`
- `2026-09-21T08:05:45.728752Z` — **FUELINST**: 80 rows; marker `2026-09-21T08:05:00Z`
- `2026-09-21T08:04:15.169360Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:03:45Z`
- `2026-09-21T08:02:07.727452Z` — **FREQ**: 5761 rows; marker `2026-09-21T08:01:45Z`
- `2026-09-21T08:00:48.627830Z` — **FUELHH**: 20 rows; marker `2026-09-21T08:00:00Z`
- `2026-09-21T08:00:48.627830Z` — **FUELINST**: 80 rows; marker `2026-09-21T08:00:00Z`
- `2026-09-21T08:00:17.129049Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:59:45Z`
- `2026-09-21T07:58:08.783815Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:57:45Z`
- `2026-09-21T07:56:07.550153Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:55:45Z`
- `2026-09-21T07:55:20.037570Z` — **FUELINST**: 80 rows; marker `2026-09-21T07:55:00Z`
- `2026-09-21T07:54:15.900540Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:53:45Z`
- `2026-09-21T07:52:24.437629Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:51:45Z`
- `2026-09-21T07:50:32.384545Z` — **FUELINST**: 80 rows; marker `2026-09-21T07:50:00Z`
