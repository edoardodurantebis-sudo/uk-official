# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T21:08:20.118569Z`  
Current process started UTC: `2026-09-17T21:04:20.091272Z`  
1-second metadata polls in this process: **231**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **503** (n=835, 2026-09-17T21:05:27.324457Z)
- `FUELINST|fuelType=NPSHYD|generation` = **533** (n=835, 2026-09-17T21:05:27.324457Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=835, 2026-09-17T21:05:27.324457Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=835, 2026-09-17T21:05:27.324457Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=835, 2026-09-17T21:05:27.324457Z)
- `FUELINST|fuelType=OTHER|generation` = **349** (n=835, 2026-09-17T21:05:27.324457Z)
- `FUELINST|fuelType=PS|generation` = **356** (n=835, 2026-09-17T21:05:27.324457Z)
- `FUELINST|fuelType=WIND|generation` = **15083** (n=835, 2026-09-17T21:05:27.324457Z)
- `IMBALNGC|TOTAL|imbalance` = **9702** (n=138, 2026-09-17T20:52:31.535620Z)
- `INDDEM|TOTAL|demand` = **-11159** (n=138, 2026-09-17T20:52:15.731180Z)
- `INDGEN|TOTAL|generation` = **26516** (n=138, 2026-09-17T20:52:15.731180Z)
- `MELNGC|TOTAL|margin` = **36461** (n=138, 2026-09-17T20:50:14.374453Z)
- `NDF|TOTAL|demand` = **16314** (n=141, 2026-09-17T20:47:47.507721Z)
- `TSDF|TOTAL|demand` = **16814** (n=141, 2026-09-17T20:47:47.507721Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T21:08:19.138242Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:08:18.138108Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:08:17.138018Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:08:16.137937Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:08:15.137853Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:08:14.137771Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:08:13.137689Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:08:12.137618Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:08:11.137522Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:08:10.137440Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:08:09.137351Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:08:08.137269Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:08:06.020105Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:08:06.020105Z` — **FREQ**: 5761 rows; marker `2026-09-17T21:07:45Z`
- `2026-09-17T21:08:04.990895Z` — **MID**: 0 rows; marker `2026-09-17T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
