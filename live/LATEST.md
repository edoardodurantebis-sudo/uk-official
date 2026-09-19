# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T02:58:27.255300Z`  
Current process started UTC: `2026-09-19T02:54:26.864587Z`  
1-second metadata polls in this process: **177**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-10744, delta=3052, z=1.92 -> demand pressure up
- **WINDFOR** `TOTAL` `generation` — wind forecast [TOTAL] generation: value=7845, delta=-11023, z=-4.38 -> renewable cushion down / residual-load pressure up
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=80, delta=-38, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=97, delta=-21, z=4.20 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.28 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=118, delta=27, z=6.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.70 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=-1, z=5.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=0, z=6.01 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=91, delta=9, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=11, z=6.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=108, delta=29, z=5.66 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-509** (n=1149, 2026-09-19T02:55:34.637269Z)
- `FUELINST|fuelType=NPSHYD|generation` = **345** (n=1149, 2026-09-19T02:55:34.637269Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1149, 2026-09-19T02:55:34.637269Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1149, 2026-09-19T02:55:34.637269Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1149, 2026-09-19T02:55:34.637269Z)
- `FUELINST|fuelType=OTHER|generation` = **370** (n=1149, 2026-09-19T02:55:34.637269Z)
- `FUELINST|fuelType=PS|generation` = **-542** (n=1149, 2026-09-19T02:55:34.637269Z)
- `FUELINST|fuelType=WIND|generation` = **16190** (n=1149, 2026-09-19T02:55:34.637269Z)
- `IMBALNGC|TOTAL|imbalance` = **9396** (n=190, 2026-09-19T02:52:05.369639Z)
- `INDDEM|TOTAL|demand` = **-10882** (n=190, 2026-09-19T02:51:49.347775Z)
- `INDGEN|TOTAL|generation` = **26591** (n=190, 2026-09-19T02:51:49.347775Z)
- `MELNGC|TOTAL|margin` = **38308** (n=190, 2026-09-19T02:50:14.190789Z)
- `NDF|TOTAL|demand` = **16550** (n=194, 2026-09-19T02:47:39.775856Z)
- `TSDF|TOTAL|demand` = **17194** (n=194, 2026-09-19T02:47:56.052582Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T02:58:25.972715Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:58:24.718638Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:58:23.423160Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:58:22.145923Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:58:20.856935Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:58:19.488774Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:58:18.167568Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:58:15.362139Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:58:15.362139Z` — **FREQ**: 5761 rows; marker `2026-09-19T02:57:45Z`
- `2026-09-19T02:58:14.097699Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:58:12.779912Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:58:11.494497Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:58:10.167356Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:58:08.897383Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:58:07.604850Z` — **MID**: 0 rows; marker `2026-09-19T02:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
