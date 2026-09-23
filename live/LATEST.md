# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T10:05:31.998908Z`  
Current process started UTC: `2026-09-23T10:01:31.578289Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2383, 2026-09-23T10:00:21.687621Z)
- `FUELINST|fuelType=OTHER|generation` = **640** (n=2383, 2026-09-23T10:00:21.687621Z)
- `FUELINST|fuelType=PS|generation` = **-688** (n=2383, 2026-09-23T10:00:21.687621Z)
- `FUELINST|fuelType=WIND|generation` = **9809** (n=2383, 2026-09-23T10:00:21.687621Z)
- `IMBALNGC|TOTAL|imbalance` = **-3948** (n=391, 2026-09-23T09:54:31.341952Z)
- `INDDEM|TOTAL|demand` = **-12697** (n=391, 2026-09-23T09:54:31.341952Z)
- `INDGEN|TOTAL|generation` = **17080** (n=391, 2026-09-23T09:54:31.341952Z)
- `MELNGC|TOTAL|margin` = **40709** (n=391, 2026-09-23T09:53:44.415184Z)
- `MID|dataProvider=APXMIDP|price` = **121.85** (n=133, 2026-09-23T09:42:10.371965Z)
- `MID|dataProvider=APXMIDP|volume` = **3598.6** (n=133, 2026-09-23T09:42:10.371965Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=262, 2026-09-23T09:42:10.371965Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=262, 2026-09-23T09:42:10.371965Z)
- `NDF|TOTAL|demand` = **20282** (n=400, 2026-09-23T09:52:23.995198Z)
- `TSDF|TOTAL|demand` = **21028** (n=400, 2026-09-23T09:52:23.995198Z)
- `WINDFOR|TOTAL|generation` = **6996** (n=67, 2026-09-23T08:30:29.420655Z)

## Latest publication events

- `2026-09-23T10:04:11.554259Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:03:45Z`
- `2026-09-23T10:02:19.753036Z` — **FREQ**: 5761 rows; marker `2026-09-23T10:01:45Z`
- `2026-09-23T10:00:38.400770Z` — **FUELHH**: 20 rows; marker `2026-09-23T10:00:00Z`
- `2026-09-23T10:00:21.687621Z` — **FUELINST**: 80 rows; marker `2026-09-23T10:00:00Z`
- `2026-09-23T10:00:05.958729Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:59:45Z`
- `2026-09-23T09:58:13.087912Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:57:45Z`
- `2026-09-23T09:56:09.111643Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:55:45Z`
- `2026-09-23T09:55:19.305637Z` — **FUELINST**: 80 rows; marker `2026-09-23T09:55:00Z`
- `2026-09-23T09:54:31.341952Z` — **INDGEN**: 648 rows; marker `2026-09-23T09:51:00Z`
- `2026-09-23T09:54:31.341952Z` — **INDDEM**: 648 rows; marker `2026-09-23T09:51:00Z`
- `2026-09-23T09:54:31.341952Z` — **IMBALNGC**: 648 rows; marker `2026-09-23T09:51:00Z`
- `2026-09-23T09:54:15.936439Z` — **FREQ**: 5761 rows; marker `2026-09-23T09:53:45Z`
- `2026-09-23T09:53:44.415184Z` — **MELNGC**: 648 rows; marker `2026-09-23T09:51:00Z`
- `2026-09-23T09:52:23.995198Z` — **TSDF**: 648 rows; marker `2026-09-23T09:52:00Z`
- `2026-09-23T09:52:23.995198Z` — **NDF**: 36 rows; marker `2026-09-23T09:51:00Z`
