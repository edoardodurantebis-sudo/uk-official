# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T03:15:19.784891Z`  
Current process started UTC: `2026-09-19T03:11:17.469679Z`  
1-second metadata polls in this process: **134**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-487** (n=1152, 2026-09-19T03:10:42.614604Z)
- `FUELINST|fuelType=NPSHYD|generation` = **334** (n=1152, 2026-09-19T03:10:42.614604Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1152, 2026-09-19T03:10:42.614604Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1152, 2026-09-19T03:10:42.614604Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1152, 2026-09-19T03:10:42.614604Z)
- `FUELINST|fuelType=OTHER|generation` = **505** (n=1152, 2026-09-19T03:10:42.614604Z)
- `FUELINST|fuelType=PS|generation` = **-543** (n=1152, 2026-09-19T03:10:42.614604Z)
- `FUELINST|fuelType=WIND|generation` = **16149** (n=1152, 2026-09-19T03:10:42.614604Z)
- `IMBALNGC|TOTAL|imbalance` = **9396** (n=190, 2026-09-19T02:52:05.369639Z)
- `INDDEM|TOTAL|demand` = **-10882** (n=190, 2026-09-19T02:51:49.347775Z)
- `INDGEN|TOTAL|generation` = **26591** (n=190, 2026-09-19T02:51:49.347775Z)
- `MELNGC|TOTAL|margin` = **38308** (n=190, 2026-09-19T02:50:14.190789Z)
- `NDF|TOTAL|demand` = **16550** (n=194, 2026-09-19T02:47:39.775856Z)
- `TSDF|TOTAL|demand` = **17194** (n=194, 2026-09-19T02:47:56.052582Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T03:15:16.866373Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:15:15.134000Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:15:13.441735Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:15:11.752761Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:15:10.059741Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:15:08.346202Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:15:06.624051Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:15:04.913095Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:15:03.205445Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:15:00.672657Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:14:58.959407Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:14:57.241686Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:14:55.546844Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:14:53.865200Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:14:52.166750Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
