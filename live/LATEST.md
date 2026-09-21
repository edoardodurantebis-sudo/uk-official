# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T17:21:51.080386Z`  
Current process started UTC: `2026-09-21T17:17:50.754248Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2997, delta=305, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=110, delta=50, z=3.54 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3508, delta=4, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=CCGT` `generation` — instantaneous generation mix [fuelType=CCGT] generation: value=13659, delta=226, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=-5, z=3.50 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=0, z=3.62 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=5, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=CCGT` `generation` — instantaneous generation mix [fuelType=CCGT] generation: value=13468, delta=4, z=3.51 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3506, delta=0, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=3, z=3.54 -> generation-mix component moved
- **FUELINST** `fuelType=CCGT` `generation` — instantaneous generation mix [fuelType=CCGT] generation: value=13464, delta=103, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3507, delta=-3, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3510, delta=1, z=3.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=5, z=3.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3504, delta=-1, z=3.61 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1895, 2026-09-21T17:20:29.849386Z)
- `FUELINST|fuelType=OTHER|generation` = **2997** (n=1895, 2026-09-21T17:20:29.849386Z)
- `FUELINST|fuelType=PS|generation` = **855** (n=1895, 2026-09-21T17:20:29.849386Z)
- `FUELINST|fuelType=WIND|generation` = **3330** (n=1895, 2026-09-21T17:20:29.849386Z)
- `IMBALNGC|TOTAL|imbalance` = **-3026** (n=311, 2026-09-21T16:52:56.638577Z)
- `INDDEM|TOTAL|demand` = **-12277** (n=311, 2026-09-21T16:52:40.661443Z)
- `INDGEN|TOTAL|generation` = **18433** (n=311, 2026-09-21T16:52:40.661443Z)
- `MELNGC|TOTAL|margin` = **36168** (n=312, 2026-09-21T17:20:29.849386Z)
- `MID|dataProvider=APXMIDP|price` = **207.07** (n=52, 2026-09-21T17:12:20.269195Z)
- `MID|dataProvider=APXMIDP|volume` = **3426** (n=52, 2026-09-21T17:12:20.269195Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=102, 2026-09-21T17:12:20.269195Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=102, 2026-09-21T17:12:20.269195Z)
- `NDF|TOTAL|demand` = **20959** (n=319, 2026-09-21T17:18:22.758203Z)
- `TSDF|TOTAL|demand` = **21459** (n=319, 2026-09-21T17:18:22.758203Z)
- `WINDFOR|TOTAL|generation` = **8620** (n=54, 2026-09-21T16:30:47.714491Z)

## Latest publication events

- `2026-09-21T17:20:29.849386Z` — **MELNGC**: 1242 rows; marker `2026-09-21T17:17:00Z`
- `2026-09-21T17:20:29.849386Z` — **FUELINST**: 80 rows; marker `2026-09-21T17:20:00Z`
- `2026-09-21T17:20:14.314253Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:19:45Z`
- `2026-09-21T17:18:22.758203Z` — **TSDF**: 1242 rows; marker `2026-09-21T17:17:00Z`
- `2026-09-21T17:18:22.758203Z` — **NDF**: 69 rows; marker `2026-09-21T17:17:00Z`
- `2026-09-21T17:18:22.758203Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:17:45Z`
- `2026-09-21T17:16:18.550573Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:15:45Z`
- `2026-09-21T17:15:30.768488Z` — **FUELINST**: 80 rows; marker `2026-09-21T17:15:00Z`
- `2026-09-21T17:14:09.531180Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:13:45Z`
- `2026-09-21T17:12:20.269195Z` — **MID**: 2 rows; marker `2026-09-21T17:12:04Z`
- `2026-09-21T17:12:20.269195Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:11:45Z`
- `2026-09-21T17:10:28.630637Z` — **FUELINST**: 80 rows; marker `2026-09-21T17:10:00Z`
- `2026-09-21T17:10:12.285210Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:09:45Z`
- `2026-09-21T17:08:20.780673Z` — **FREQ**: 5761 rows; marker `2026-09-21T17:07:45Z`
- `2026-09-21T17:07:32.504896Z` — **MID**: 1 rows; marker `2026-09-21T17:05:00Z`
