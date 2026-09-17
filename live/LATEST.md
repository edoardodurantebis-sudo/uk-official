# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T20:30:29.041440Z`  
Current process started UTC: `2026-09-17T20:26:28.097481Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **728** (n=827, 2026-09-17T20:25:40.383893Z)
- `FUELINST|fuelType=NPSHYD|generation` = **561** (n=827, 2026-09-17T20:25:40.383893Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3317** (n=827, 2026-09-17T20:25:40.383893Z)
- `FUELINST|fuelType=OCGT|generation` = **38** (n=827, 2026-09-17T20:25:40.383893Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=827, 2026-09-17T20:25:40.383893Z)
- `FUELINST|fuelType=OTHER|generation` = **789** (n=827, 2026-09-17T20:25:40.383893Z)
- `FUELINST|fuelType=PS|generation` = **498** (n=827, 2026-09-17T20:25:40.383893Z)
- `FUELINST|fuelType=WIND|generation` = **15458** (n=827, 2026-09-17T20:25:40.383893Z)
- `IMBALNGC|TOTAL|imbalance` = **9686** (n=137, 2026-09-17T20:23:01.759732Z)
- `INDDEM|TOTAL|demand` = **-11161** (n=137, 2026-09-17T20:22:29.150648Z)
- `INDGEN|TOTAL|generation` = **26500** (n=137, 2026-09-17T20:22:29.150648Z)
- `MELNGC|TOTAL|margin` = **36451** (n=137, 2026-09-17T20:20:13.977200Z)
- `NDF|TOTAL|demand` = **16314** (n=140, 2026-09-17T20:18:03.614644Z)
- `TSDF|TOTAL|demand` = **16814** (n=140, 2026-09-17T20:18:03.614644Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T20:30:28.076758Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:30:27.076659Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:30:26.076519Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:30:25.076377Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:30:24.076309Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:30:23.076186Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:30:22.076102Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:30:21.075979Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:30:20.075891Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:30:19.075771Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:30:18.075644Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:30:15.643948Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:30:15.643948Z` — **FREQ**: 5761 rows; marker `2026-09-17T20:29:45Z`
- `2026-09-17T20:30:14.643811Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:30:13.643667Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
