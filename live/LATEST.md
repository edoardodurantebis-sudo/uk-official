# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T10:30:53.106369Z`  
Current process started UTC: `2026-09-23T10:26:53.332004Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=COAL` `generation` — half-hour generation mix [fuelType=COAL] generation: value=0, delta=-133, z=-0.05 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3187, delta=-614, z=-1.49 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=772, delta=-9447, z=-0.02 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=0, delta=-871, z=-0.35 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3202, delta=1895, z=-1.32 -> generation-mix component moved
- **FUELINST** `fuelType=COAL` `generation` — instantaneous generation mix [fuelType=COAL] generation: value=0, delta=-795, z=-0.02 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=10219, delta=9339, z=13.89 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=871, delta=871, z=11.02 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=1307, delta=-2493, z=-13.96 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=165, delta=-434, z=1.76 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=437, delta=-153, z=5.21 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3204, delta=-351, z=3.66 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=599, delta=-36, z=7.95 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=0, z=7.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=0, z=7.34 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2389, 2026-09-23T10:30:38.458402Z)
- `FUELINST|fuelType=OTHER|generation` = **706** (n=2389, 2026-09-23T10:30:38.458402Z)
- `FUELINST|fuelType=PS|generation` = **-870** (n=2389, 2026-09-23T10:30:38.458402Z)
- `FUELINST|fuelType=WIND|generation` = **9565** (n=2389, 2026-09-23T10:30:38.458402Z)
- `IMBALNGC|TOTAL|imbalance` = **-2300** (n=392, 2026-09-23T10:19:00.590799Z)
- `INDDEM|TOTAL|demand` = **-13737** (n=392, 2026-09-23T10:19:00.590799Z)
- `INDGEN|TOTAL|generation` = **18728** (n=392, 2026-09-23T10:19:00.590799Z)
- `MELNGC|TOTAL|margin` = **40780** (n=392, 2026-09-23T10:18:44.331652Z)
- `MID|dataProvider=APXMIDP|price` = **113.24** (n=134, 2026-09-23T10:12:07.743818Z)
- `MID|dataProvider=APXMIDP|volume` = **3860.9** (n=134, 2026-09-23T10:12:07.743818Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=264, 2026-09-23T10:12:07.743818Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=264, 2026-09-23T10:12:07.743818Z)
- `NDF|TOTAL|demand` = **20282** (n=401, 2026-09-23T10:16:52.679866Z)
- `TSDF|TOTAL|demand` = **21028** (n=401, 2026-09-23T10:16:52.679866Z)
- `WINDFOR|TOTAL|generation` = **7178** (n=68, 2026-09-23T10:30:38.458402Z)

## Latest publication events

- `2026-09-23T10:30:38.458402Z` — **WINDFOR**: 73 rows; marker `2026-09-23T10:30:00Z`
- `2026-09-23T10:30:38.458402Z` — **FUELHH**: 20 rows; marker `2026-09-23T10:30:00Z`
- `2026-09-23T10:30:38.458402Z` — **FUELINST**: 80 rows; marker `2026-09-23T10:30:00Z`
- `2026-09-23T10:30:22.517342Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:29:45Z`
- `2026-09-23T10:28:14.342387Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:27:45Z`
- `2026-09-23T10:26:22.289310Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:25:45Z`
- `2026-09-23T10:25:34.789487Z` — **FUELINST**: 80 rows; marker `2026-09-23T10:25:00Z`
- `2026-09-23T10:24:14.580821Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:23:45Z`
- `2026-09-23T10:22:38.496760Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:21:45Z`
- `2026-09-23T10:20:35.915130Z` — **FUELINST**: 80 rows; marker `2026-09-23T10:20:00Z`
- `2026-09-23T10:20:20.441230Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:19:45Z`
- `2026-09-23T10:19:00.590799Z` — **INDGEN**: 630 rows; marker `2026-09-23T10:16:00Z`
- `2026-09-23T10:19:00.590799Z` — **INDDEM**: 630 rows; marker `2026-09-23T10:16:00Z`
- `2026-09-23T10:19:00.590799Z` — **IMBALNGC**: 630 rows; marker `2026-09-23T10:16:00Z`
- `2026-09-23T10:18:44.331652Z` — **MELNGC**: 630 rows; marker `2026-09-23T10:16:00Z`
