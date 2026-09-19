# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T05:38:30.030676Z`  
Current process started UTC: `2026-09-19T05:34:29.248621Z`  
1-second metadata polls in this process: **144**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-454** (n=1181, 2026-09-19T05:35:34.757777Z)
- `FUELINST|fuelType=NPSHYD|generation` = **359** (n=1181, 2026-09-19T05:35:34.757777Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1181, 2026-09-19T05:35:34.757777Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1181, 2026-09-19T05:35:34.757777Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1181, 2026-09-19T05:35:34.757777Z)
- `FUELINST|fuelType=OTHER|generation` = **692** (n=1181, 2026-09-19T05:35:34.757777Z)
- `FUELINST|fuelType=PS|generation` = **-539** (n=1181, 2026-09-19T05:35:34.757777Z)
- `FUELINST|fuelType=WIND|generation` = **15830** (n=1181, 2026-09-19T05:35:34.757777Z)
- `IMBALNGC|TOTAL|imbalance` = **9712** (n=195, 2026-09-19T05:21:11.032937Z)
- `INDDEM|TOTAL|demand` = **-10865** (n=195, 2026-09-19T05:21:11.032937Z)
- `INDGEN|TOTAL|generation` = **26901** (n=195, 2026-09-19T05:21:11.032937Z)
- `MELNGC|TOTAL|margin` = **38254** (n=195, 2026-09-19T05:19:51.225658Z)
- `NDF|TOTAL|demand` = **16550** (n=199, 2026-09-19T05:17:24.210800Z)
- `TSDF|TOTAL|demand` = **17190** (n=199, 2026-09-19T05:17:24.210800Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T05:38:28.470582Z` — **MID**: 0 rows; marker `2026-09-19T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:38:26.869107Z` — **MID**: 0 rows; marker `2026-09-19T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:38:25.200867Z` — **MID**: 0 rows; marker `2026-09-19T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:38:23.647488Z` — **MID**: 0 rows; marker `2026-09-19T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:38:22.105680Z` — **MID**: 0 rows; marker `2026-09-19T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:38:18.597131Z` — **MID**: 0 rows; marker `2026-09-19T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:38:18.597131Z` — **FREQ**: 5761 rows; marker `2026-09-19T05:37:45Z`
- `2026-09-19T05:38:17.039641Z` — **MID**: 0 rows; marker `2026-09-19T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:38:15.452010Z` — **MID**: 0 rows; marker `2026-09-19T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:38:13.872038Z` — **MID**: 0 rows; marker `2026-09-19T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:38:12.287798Z` — **MID**: 0 rows; marker `2026-09-19T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:38:10.735513Z` — **MID**: 0 rows; marker `2026-09-19T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:38:09.165058Z` — **MID**: 0 rows; marker `2026-09-19T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:38:07.580625Z` — **MID**: 0 rows; marker `2026-09-19T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:38:06.010551Z` — **MID**: 0 rows; marker `2026-09-19T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
