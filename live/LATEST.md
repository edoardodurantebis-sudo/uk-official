# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T00:16:55.133556Z`  
Current process started UTC: `2026-09-17T00:12:54.447842Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=-40, z=-3.98 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-272, delta=-77, z=-3.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-195, delta=-78, z=-3.76 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-28, delta=-68, z=-3.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-117, delta=-77, z=-3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=3, delta=-50, z=-0.06 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=-3, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.63 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.72 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.82 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=50, delta=50, z=5.13 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=40, delta=-418, z=-3.53 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.92 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.03 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-4, delta=0, z=-3.54 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1221** (n=585, 2026-09-17T00:15:34.629703Z)
- `FUELINST|fuelType=NPSHYD|generation` = **422** (n=585, 2026-09-17T00:15:34.629703Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3310** (n=585, 2026-09-17T00:15:34.629703Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=585, 2026-09-17T00:15:34.629703Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=585, 2026-09-17T00:15:34.629703Z)
- `FUELINST|fuelType=OTHER|generation` = **564** (n=585, 2026-09-17T00:15:34.629703Z)
- `FUELINST|fuelType=PS|generation` = **-244** (n=585, 2026-09-17T00:15:34.629703Z)
- `FUELINST|fuelType=WIND|generation` = **11780** (n=585, 2026-09-17T00:15:34.629703Z)
- `IMBALNGC|TOTAL|imbalance` = **6451** (n=97, 2026-09-16T23:51:22.800815Z)
- `INDDEM|TOTAL|demand` = **-11763** (n=97, 2026-09-16T23:51:22.800815Z)
- `INDGEN|TOTAL|generation` = **25572** (n=97, 2026-09-16T23:51:22.800815Z)
- `MELNGC|TOTAL|margin` = **34508** (n=97, 2026-09-16T23:49:04.834499Z)
- `NDF|TOTAL|demand` = **18621** (n=99, 2026-09-16T23:47:28.553408Z)
- `TSDF|TOTAL|demand` = **19121** (n=99, 2026-09-16T23:47:28.553408Z)
- `WINDFOR|TOTAL|generation` = **20102** (n=17, 2026-09-16T23:30:41.101363Z)

## Latest publication events

- `2026-09-17T00:16:06.804222Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:15:45Z`
- `2026-09-17T00:15:34.629703Z` — **FUELINST**: 80 rows; marker `2026-09-17T00:15:00Z`
- `2026-09-17T00:14:15.075618Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:13:45Z`
- `2026-09-17T00:12:54.447850Z` — **MID**: 0 rows; marker `2026-09-17T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T00:12:54.447850Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:11:45Z`
- `2026-09-17T00:10:31.538588Z` — **FUELINST**: 80 rows; marker `2026-09-17T00:10:00Z`
- `2026-09-17T00:10:15.315004Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:09:45Z`
- `2026-09-17T00:08:23.075722Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:07:45Z`
- `2026-09-17T00:06:37.670534Z` — **MID**: 0 rows; marker `2026-09-17T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T00:06:21.853883Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:05:45Z`
- `2026-09-17T00:05:33.692190Z` — **FUELINST**: 80 rows; marker `2026-09-17T00:05:00Z`
- `2026-09-17T00:04:27.870157Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:03:45Z`
- `2026-09-17T00:02:24.408990Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:01:45Z`
- `2026-09-17T00:00:32.870555Z` — **FUELHH**: 20 rows; marker `2026-09-17T00:00:00Z`
- `2026-09-17T00:00:32.870555Z` — **FUELINST**: 80 rows; marker `2026-09-17T00:00:00Z`
