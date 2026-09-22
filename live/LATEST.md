# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T16:49:00.960523Z`  
Current process started UTC: `2026-09-22T16:45:01.422736Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=593, delta=0, z=13.83 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=593, delta=45, z=14.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=548, delta=67, z=13.93 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=301, delta=202, z=8.27 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=481, delta=100, z=12.60 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=381, delta=82, z=10.10 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=299, delta=62, z=7.92 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=237, delta=23, z=6.22 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=214, delta=19, z=5.60 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=195, delta=18, z=5.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=177, delta=84, z=4.58 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3729, delta=7, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3732, delta=1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3731, delta=9, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3737, delta=0, z=3.60 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2176, 2026-09-22T16:45:33.721116Z)
- `FUELINST|fuelType=OTHER|generation` = **1922** (n=2176, 2026-09-22T16:45:33.721116Z)
- `FUELINST|fuelType=PS|generation` = **1509** (n=2176, 2026-09-22T16:45:33.721116Z)
- `FUELINST|fuelType=WIND|generation` = **1334** (n=2176, 2026-09-22T16:45:33.721116Z)
- `IMBALNGC|TOTAL|imbalance` = **-7943** (n=357, 2026-09-22T16:22:23.715090Z)
- `INDDEM|TOTAL|demand` = **-12476** (n=357, 2026-09-22T16:22:08.285666Z)
- `INDGEN|TOTAL|generation` = **13230** (n=357, 2026-09-22T16:22:08.285666Z)
- `MELNGC|TOTAL|margin` = **37153** (n=357, 2026-09-22T16:19:43.389491Z)
- `MID|dataProvider=APXMIDP|price` = **224.84** (n=99, 2026-09-22T16:42:18.479088Z)
- `MID|dataProvider=APXMIDP|volume` = **4488** (n=99, 2026-09-22T16:42:18.479088Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=196, 2026-09-22T16:42:18.479088Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=196, 2026-09-22T16:42:18.479088Z)
- `NDF|TOTAL|demand` = **20673** (n=366, 2026-09-22T16:47:42.402614Z)
- `TSDF|TOTAL|demand` = **21173** (n=366, 2026-09-22T16:47:42.402614Z)
- `WINDFOR|TOTAL|generation` = **13535** (n=62, 2026-09-22T16:30:39.657630Z)

## Latest publication events

- `2026-09-22T16:48:14.752232Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:47:45Z`
- `2026-09-22T16:47:42.402614Z` — **TSDF**: 1260 rows; marker `2026-09-22T16:47:00Z`
- `2026-09-22T16:47:42.402614Z` — **NDF**: 70 rows; marker `2026-09-22T16:47:00Z`
- `2026-09-22T16:46:21.200773Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:45:45Z`
- `2026-09-22T16:45:33.721116Z` — **FUELINST**: 80 rows; marker `2026-09-22T16:45:00Z`
- `2026-09-22T16:44:10.511032Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:43:45Z`
- `2026-09-22T16:42:18.479088Z` — **MID**: 2 rows; marker `2026-09-22T16:42:03Z`
- `2026-09-22T16:42:18.479088Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:41:45Z`
- `2026-09-22T16:40:26.446242Z` — **FUELINST**: 80 rows; marker `2026-09-22T16:40:00Z`
- `2026-09-22T16:40:10.906027Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:39:45Z`
- `2026-09-22T16:38:19.384506Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:37:45Z`
- `2026-09-22T16:37:31.123228Z` — **MID**: 1 rows; marker `2026-09-22T16:35:00Z`
- `2026-09-22T16:36:27.327601Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:35:45Z`
- `2026-09-22T16:35:39.648117Z` — **FUELINST**: 80 rows; marker `2026-09-22T16:35:00Z`
- `2026-09-22T16:34:20.180630Z` — **FREQ**: 5761 rows; marker `2026-09-22T16:33:45Z`
