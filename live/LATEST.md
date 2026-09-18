# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T22:52:51.342124Z`  
Current process started UTC: `2026-09-18T22:48:50.527990Z`  
1-second metadata polls in this process: **188**  
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

- `FUELINST|fuelType=INTVKL|generation` = **443** (n=1100, 2026-09-18T22:50:26.115559Z)
- `FUELINST|fuelType=NPSHYD|generation` = **443** (n=1100, 2026-09-18T22:50:26.115559Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1100, 2026-09-18T22:50:26.115559Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1100, 2026-09-18T22:50:26.115559Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1100, 2026-09-18T22:50:26.115559Z)
- `FUELINST|fuelType=OTHER|generation` = **1153** (n=1100, 2026-09-18T22:50:26.115559Z)
- `FUELINST|fuelType=PS|generation` = **-478** (n=1100, 2026-09-18T22:50:26.115559Z)
- `FUELINST|fuelType=WIND|generation` = **15802** (n=1100, 2026-09-18T22:50:26.115559Z)
- `IMBALNGC|TOTAL|imbalance` = **8984** (n=181, 2026-09-18T22:23:06.697614Z)
- `INDDEM|TOTAL|demand` = **-10889** (n=181, 2026-09-18T22:22:50.501799Z)
- `INDGEN|TOTAL|generation` = **26179** (n=181, 2026-09-18T22:23:06.697614Z)
- `MELNGC|TOTAL|margin` = **37610** (n=182, 2026-09-18T22:50:10.642009Z)
- `NDF|TOTAL|demand` = **16550** (n=186, 2026-09-18T22:48:26.880797Z)
- `TSDF|TOTAL|demand` = **17194** (n=186, 2026-09-18T22:48:26.880797Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T22:52:50.148480Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:52:48.954003Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:52:47.792048Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:52:46.614385Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:52:45.429549Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:52:44.220581Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:52:43.030213Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:52:41.843152Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:52:40.682981Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:52:39.506372Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:52:38.308172Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:52:37.093287Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:52:35.430472Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:52:34.231675Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:52:33.051054Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
