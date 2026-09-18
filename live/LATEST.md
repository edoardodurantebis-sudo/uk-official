# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T13:38:52.309027Z`  
Current process started UTC: `2026-09-18T13:34:52.119451Z`  
1-second metadata polls in this process: **218**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1389** (n=1033, 2026-09-18T13:35:43.129106Z)
- `FUELINST|fuelType=NPSHYD|generation` = **317** (n=1033, 2026-09-18T13:35:43.129106Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1033, 2026-09-18T13:35:43.129106Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1033, 2026-09-18T13:35:43.129106Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1033, 2026-09-18T13:35:43.129106Z)
- `FUELINST|fuelType=OTHER|generation` = **399** (n=1033, 2026-09-18T13:35:43.129106Z)
- `FUELINST|fuelType=PS|generation` = **-482** (n=1033, 2026-09-18T13:35:43.129106Z)
- `FUELINST|fuelType=WIND|generation` = **15283** (n=1033, 2026-09-18T13:35:43.129106Z)
- `IMBALNGC|TOTAL|imbalance` = **8935** (n=170, 2026-09-18T13:25:04.803083Z)
- `INDDEM|TOTAL|demand` = **-10745** (n=170, 2026-09-18T13:25:04.803083Z)
- `INDGEN|TOTAL|generation` = **25605** (n=170, 2026-09-18T13:25:04.803083Z)
- `MELNGC|TOTAL|margin` = **38174** (n=170, 2026-09-18T13:21:37.459648Z)
- `NDF|TOTAL|demand` = **16170** (n=174, 2026-09-18T13:18:55.653418Z)
- `TSDF|TOTAL|demand` = **16670** (n=174, 2026-09-18T13:18:55.653418Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T13:38:51.298188Z` — **MID**: 0 rows; marker `2026-09-18T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:38:50.244766Z` — **MID**: 0 rows; marker `2026-09-18T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:38:49.201110Z` — **MID**: 0 rows; marker `2026-09-18T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:38:48.168480Z` — **MID**: 0 rows; marker `2026-09-18T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:38:47.145272Z` — **MID**: 0 rows; marker `2026-09-18T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:38:46.113455Z` — **MID**: 0 rows; marker `2026-09-18T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:38:45.073072Z` — **MID**: 0 rows; marker `2026-09-18T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:38:43.977266Z` — **MID**: 0 rows; marker `2026-09-18T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:38:42.741275Z` — **MID**: 0 rows; marker `2026-09-18T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:38:41.693256Z` — **MID**: 0 rows; marker `2026-09-18T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:38:40.675369Z` — **MID**: 0 rows; marker `2026-09-18T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:38:39.630647Z` — **MID**: 0 rows; marker `2026-09-18T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:38:38.235901Z` — **MID**: 0 rows; marker `2026-09-18T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:38:37.228392Z` — **MID**: 0 rows; marker `2026-09-18T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:38:36.195980Z` — **MID**: 0 rows; marker `2026-09-18T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
