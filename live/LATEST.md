# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T08:18:19.088701Z`  
Current process started UTC: `2026-09-19T08:14:18.096019Z`  
1-second metadata polls in this process: **133**  
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

- `FUELINST|fuelType=INTVKL|generation` = **910** (n=1213, 2026-09-19T08:15:37.356031Z)
- `FUELINST|fuelType=NPSHYD|generation` = **369** (n=1213, 2026-09-19T08:15:37.356031Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1213, 2026-09-19T08:15:37.356031Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1213, 2026-09-19T08:15:37.356031Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1213, 2026-09-19T08:15:37.356031Z)
- `FUELINST|fuelType=OTHER|generation` = **308** (n=1213, 2026-09-19T08:15:37.356031Z)
- `FUELINST|fuelType=PS|generation` = **-424** (n=1213, 2026-09-19T08:15:37.356031Z)
- `FUELINST|fuelType=WIND|generation` = **15297** (n=1213, 2026-09-19T08:15:37.356031Z)
- `IMBALNGC|TOTAL|imbalance` = **8458** (n=199, 2026-09-19T07:20:02.514143Z)
- `INDDEM|TOTAL|demand` = **-12078** (n=199, 2026-09-19T07:19:46.165443Z)
- `INDGEN|TOTAL|generation` = **26869** (n=199, 2026-09-19T07:19:46.165443Z)
- `MELNGC|TOTAL|margin` = **37026** (n=199, 2026-09-19T07:19:09.074847Z)
- `NDF|TOTAL|demand` = **15940** (n=205, 2026-09-19T08:17:14.399276Z)
- `TSDF|TOTAL|demand` = **17802** (n=205, 2026-09-19T08:17:14.399276Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T08:18:17.225183Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:18:15.550314Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:18:13.607854Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:18:11.921413Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:18:10.234315Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:18:08.452749Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:18:06.696587Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:18:04.924514Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:18:02.414209Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:18:00.749590Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:17:59.064152Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:17:57.386062Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:17:55.557967Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:17:53.864359Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:17:52.123618Z` — **MID**: 0 rows; marker `2026-09-19T08:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
