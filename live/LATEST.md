# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T11:45:16.811021Z`  
Current process started UTC: `2026-09-21T11:41:17.184382Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3517, delta=2, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3515, delta=0, z=5.16 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3515, delta=13, z=5.33 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3515, delta=-3, z=5.20 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3518, delta=2, z=5.33 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3516, delta=-3, z=5.32 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3519, delta=10, z=5.45 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3502, delta=8, z=5.16 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=6, z=5.19 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3503, delta=-2, z=5.05 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3505, delta=5, z=5.15 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3500, delta=1, z=5.04 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=4, z=5.05 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3494, delta=3, z=5.14 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3495, delta=2, z=4.96 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1827, 2026-09-21T11:40:33.734043Z)
- `FUELINST|fuelType=OTHER|generation` = **577** (n=1827, 2026-09-21T11:40:33.734043Z)
- `FUELINST|fuelType=PS|generation` = **-8** (n=1827, 2026-09-21T11:40:33.734043Z)
- `FUELINST|fuelType=WIND|generation` = **3407** (n=1827, 2026-09-21T11:40:33.734043Z)
- `IMBALNGC|TOTAL|imbalance` = **-3015** (n=300, 2026-09-21T11:23:47.986467Z)
- `INDDEM|TOTAL|demand` = **-12241** (n=300, 2026-09-21T11:23:32.299552Z)
- `INDGEN|TOTAL|generation` = **18489** (n=300, 2026-09-21T11:23:32.299552Z)
- `MELNGC|TOTAL|margin` = **36677** (n=300, 2026-09-21T11:28:54.815846Z)
- `MID|dataProvider=APXMIDP|price` = **151.37** (n=41, 2026-09-21T11:42:21.248182Z)
- `MID|dataProvider=APXMIDP|volume` = **3253.6** (n=41, 2026-09-21T11:42:21.248182Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=80, 2026-09-21T11:42:21.248182Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=80, 2026-09-21T11:42:21.248182Z)
- `NDF|TOTAL|demand` = **21004** (n=307, 2026-09-21T11:28:38.668544Z)
- `TSDF|TOTAL|demand` = **21504** (n=307, 2026-09-21T11:18:27.676306Z)
- `WINDFOR|TOTAL|generation` = **8923** (n=52, 2026-09-21T10:30:49.343841Z)

## Latest publication events

- `2026-09-21T11:44:12.986599Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:43:45Z`
- `2026-09-21T11:42:21.248182Z` — **MID**: 2 rows; marker `2026-09-21T11:42:03Z`
- `2026-09-21T11:42:21.248182Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:41:45Z`
- `2026-09-21T11:40:33.734043Z` — **FUELINST**: 80 rows; marker `2026-09-21T11:40:00Z`
- `2026-09-21T11:40:17.697145Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:39:45Z`
- `2026-09-21T11:38:25.589423Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:37:45Z`
- `2026-09-21T11:37:21.547847Z` — **MID**: 1 rows; marker `2026-09-21T11:35:00Z`
- `2026-09-21T11:36:18.473713Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:35:45Z`
- `2026-09-21T11:35:30.390578Z` — **FUELINST**: 80 rows; marker `2026-09-21T11:35:00Z`
- `2026-09-21T11:34:10.260389Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:33:45Z`
- `2026-09-21T11:32:08.468086Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:31:45Z`
- `2026-09-21T11:30:31.370615Z` — **FUELHH**: 20 rows; marker `2026-09-21T11:30:00Z`
- `2026-09-21T11:30:31.370615Z` — **FUELINST**: 80 rows; marker `2026-09-21T11:30:00Z`
- `2026-09-21T11:30:15.093803Z` — **FREQ**: 5761 rows; marker `2026-09-21T11:29:45Z`
- `2026-09-21T11:28:54.815846Z` — **MELNGC**: 1458 rows; marker `2026-09-21T11:17:00Z`
