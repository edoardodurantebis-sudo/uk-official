# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T10:18:13.876880Z`  
Current process started UTC: `2026-09-23T10:14:13.194136Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2386, 2026-09-23T10:15:32.887217Z)
- `FUELINST|fuelType=OTHER|generation` = **657** (n=2386, 2026-09-23T10:15:32.887217Z)
- `FUELINST|fuelType=PS|generation` = **-870** (n=2386, 2026-09-23T10:15:32.887217Z)
- `FUELINST|fuelType=WIND|generation` = **9780** (n=2386, 2026-09-23T10:15:32.887217Z)
- `IMBALNGC|TOTAL|imbalance` = **-3948** (n=391, 2026-09-23T09:54:31.341952Z)
- `INDDEM|TOTAL|demand` = **-12697** (n=391, 2026-09-23T09:54:31.341952Z)
- `INDGEN|TOTAL|generation` = **17080** (n=391, 2026-09-23T09:54:31.341952Z)
- `MELNGC|TOTAL|margin` = **40709** (n=391, 2026-09-23T09:53:44.415184Z)
- `MID|dataProvider=APXMIDP|price` = **113.24** (n=134, 2026-09-23T10:12:07.743818Z)
- `MID|dataProvider=APXMIDP|volume` = **3860.9** (n=134, 2026-09-23T10:12:07.743818Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=264, 2026-09-23T10:12:07.743818Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=264, 2026-09-23T10:12:07.743818Z)
- `NDF|TOTAL|demand` = **20282** (n=401, 2026-09-23T10:16:52.679866Z)
- `TSDF|TOTAL|demand` = **21028** (n=401, 2026-09-23T10:16:52.679866Z)
- `WINDFOR|TOTAL|generation` = **6996** (n=67, 2026-09-23T08:30:29.420655Z)

## Latest publication events

- `2026-09-23T10:18:12.317936Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:17:45Z`
- `2026-09-23T10:16:52.679866Z` — **TSDF**: 630 rows; marker `2026-09-23T10:16:00Z`
- `2026-09-23T10:16:52.679866Z` — **NDF**: 35 rows; marker `2026-09-23T10:16:00Z`
- `2026-09-23T10:16:21.111492Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:15:45Z`
- `2026-09-23T10:15:32.887217Z` — **FUELINST**: 80 rows; marker `2026-09-23T10:15:00Z`
- `2026-09-23T10:14:13.194143Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:13:45Z`
- `2026-09-23T10:12:07.743818Z` — **MID**: 2 rows; marker `2026-09-23T10:12:03Z`
- `2026-09-23T10:12:07.743818Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:11:45Z`
- `2026-09-23T10:10:31.938577Z` — **FUELINST**: 80 rows; marker `2026-09-23T10:10:00Z`
- `2026-09-23T10:10:15.967694Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:09:45Z`
- `2026-09-23T10:08:11.685561Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:07:45Z`
- `2026-09-23T10:06:35.244132Z` — **MID**: 1 rows; marker `2026-09-23T10:05:00Z`
- `2026-09-23T10:06:18.957528Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:05:45Z`
- `2026-09-23T10:05:47.228130Z` — **FUELINST**: 80 rows; marker `2026-09-23T10:05:00Z`
- `2026-09-23T10:04:11.554259Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:03:45Z`
