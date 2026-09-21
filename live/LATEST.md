# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T14:14:36.527918Z`  
Current process started UTC: `2026-09-21T14:10:36.215762Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-2, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3498, delta=-1, z=3.91 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3508, delta=1, z=4.24 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=-4, z=3.95 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3503, delta=-10, z=4.07 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3513, delta=-2, z=4.34 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3515, delta=8, z=4.41 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3507, delta=-3, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3510, delta=2, z=4.33 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3507, delta=0, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3508, delta=4, z=4.30 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=0, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=-3, z=4.25 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3507, delta=-2, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=1, z=4.42 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1857, 2026-09-21T14:10:18.957366Z)
- `FUELINST|fuelType=OTHER|generation` = **486** (n=1857, 2026-09-21T14:10:18.957366Z)
- `FUELINST|fuelType=PS|generation` = **219** (n=1857, 2026-09-21T14:10:18.957366Z)
- `FUELINST|fuelType=WIND|generation` = **4338** (n=1857, 2026-09-21T14:10:18.957366Z)
- `IMBALNGC|TOTAL|imbalance` = **-3238** (n=305, 2026-09-21T13:53:53.274334Z)
- `INDDEM|TOTAL|demand` = **-12297** (n=305, 2026-09-21T13:53:36.984750Z)
- `INDGEN|TOTAL|generation` = **18266** (n=305, 2026-09-21T13:53:36.984750Z)
- `MELNGC|TOTAL|margin` = **36267** (n=305, 2026-09-21T13:50:26.201478Z)
- `MID|dataProvider=APXMIDP|price` = **145.73** (n=46, 2026-09-21T14:12:12.402077Z)
- `MID|dataProvider=APXMIDP|volume` = **3192.1** (n=46, 2026-09-21T14:12:12.402077Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=90, 2026-09-21T14:12:12.402077Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=90, 2026-09-21T14:12:12.402077Z)
- `NDF|TOTAL|demand` = **21004** (n=312, 2026-09-21T13:48:21.083702Z)
- `TSDF|TOTAL|demand` = **21504** (n=312, 2026-09-21T13:48:21.083702Z)
- `WINDFOR|TOTAL|generation` = **8616** (n=53, 2026-09-21T12:30:32.614458Z)

## Latest publication events

- `2026-09-21T14:14:19.982311Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:13:45Z`
- `2026-09-21T14:12:12.402077Z` — **MID**: 2 rows; marker `2026-09-21T14:12:04Z`
- `2026-09-21T14:12:12.402077Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:11:45Z`
- `2026-09-21T14:10:18.957366Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:10:00Z`
- `2026-09-21T14:10:18.957366Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:09:45Z`
- `2026-09-21T14:08:27.457575Z` — **MID**: 1 rows; marker `2026-09-21T14:05:00Z`
- `2026-09-21T14:08:11.890232Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:07:45Z`
- `2026-09-21T14:06:20.321999Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:05:45Z`
- `2026-09-21T14:05:18.923595Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:05:00Z`
- `2026-09-21T14:04:15.399426Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:03:45Z`
- `2026-09-21T14:02:06.340815Z` — **FREQ**: 5761 rows; marker `2026-09-21T14:01:45Z`
- `2026-09-21T14:00:42.678462Z` — **FUELHH**: 20 rows; marker `2026-09-21T14:00:00Z`
- `2026-09-21T14:00:42.678462Z` — **FUELINST**: 80 rows; marker `2026-09-21T14:00:00Z`
- `2026-09-21T14:00:08.335397Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:59:45Z`
- `2026-09-21T13:58:44.398715Z` — **FREQ**: 5761 rows; marker `2026-09-21T13:57:45Z`
