# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T05:53:47.931661Z`  
Current process started UTC: `2026-09-22T05:49:47.950771Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3646, delta=-9, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3655, delta=-1, z=3.65 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2045, 2026-09-22T05:50:40.720229Z)
- `FUELINST|fuelType=OTHER|generation` = **1857** (n=2045, 2026-09-22T05:50:40.720229Z)
- `FUELINST|fuelType=PS|generation` = **-173** (n=2045, 2026-09-22T05:50:40.720229Z)
- `FUELINST|fuelType=WIND|generation` = **3691** (n=2045, 2026-09-22T05:50:40.720229Z)
- `IMBALNGC|TOTAL|imbalance` = **-3209** (n=337, 2026-09-22T05:50:25.164362Z)
- `INDDEM|TOTAL|demand` = **-12477** (n=337, 2026-09-22T05:50:25.164362Z)
- `INDGEN|TOTAL|generation` = **18250** (n=337, 2026-09-22T05:50:25.164362Z)
- `MELNGC|TOTAL|margin` = **37749** (n=337, 2026-09-22T05:49:21.035666Z)
- `MID|dataProvider=APXMIDP|price` = **168.7** (n=77, 2026-09-22T05:42:19.076776Z)
- `MID|dataProvider=APXMIDP|volume` = **2947.7** (n=77, 2026-09-22T05:42:19.076776Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=152, 2026-09-22T05:42:19.076776Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=152, 2026-09-22T05:42:19.076776Z)
- `NDF|TOTAL|demand` = **20959** (n=344, 2026-09-22T05:47:13.556598Z)
- `TSDF|TOTAL|demand` = **21459** (n=344, 2026-09-22T05:47:13.556598Z)
- `WINDFOR|TOTAL|generation` = **12340** (n=58, 2026-09-22T05:30:40.954997Z)

## Latest publication events

- `2026-09-22T05:52:16.947333Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:51:45Z`
- `2026-09-22T05:50:40.720229Z` — **FUELINST**: 80 rows; marker `2026-09-22T05:50:00Z`
- `2026-09-22T05:50:25.164362Z` — **INDGEN**: 792 rows; marker `2026-09-22T05:46:00Z`
- `2026-09-22T05:50:25.164362Z` — **INDDEM**: 792 rows; marker `2026-09-22T05:46:00Z`
- `2026-09-22T05:50:25.164362Z` — **IMBALNGC**: 792 rows; marker `2026-09-22T05:46:00Z`
- `2026-09-22T05:50:25.164362Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:49:45Z`
- `2026-09-22T05:49:21.035666Z` — **MELNGC**: 792 rows; marker `2026-09-22T05:46:00Z`
- `2026-09-22T05:48:17.642748Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:47:45Z`
- `2026-09-22T05:47:13.556598Z` — **TSDF**: 792 rows; marker `2026-09-22T05:46:00Z`
- `2026-09-22T05:47:13.556598Z` — **NDF**: 44 rows; marker `2026-09-22T05:46:00Z`
- `2026-09-22T05:46:25.235378Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:45:45Z`
- `2026-09-22T05:45:37.013323Z` — **FUELINST**: 80 rows; marker `2026-09-22T05:45:00Z`
- `2026-09-22T05:44:26.993923Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:43:45Z`
- `2026-09-22T05:42:19.076776Z` — **MID**: 2 rows; marker `2026-09-22T05:42:03Z`
- `2026-09-22T05:42:19.076776Z` — **FREQ**: 5761 rows; marker `2026-09-22T05:41:45Z`
