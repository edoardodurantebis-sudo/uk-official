# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T15:24:41.806030Z`  
Current process started UTC: `2026-09-18T15:20:40.588194Z`  
1-second metadata polls in this process: **135**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1051** (n=1054, 2026-09-18T15:20:40.588202Z)
- `FUELINST|fuelType=NPSHYD|generation` = **346** (n=1054, 2026-09-18T15:20:40.588202Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1054, 2026-09-18T15:20:40.588202Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1054, 2026-09-18T15:20:40.588202Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1054, 2026-09-18T15:20:40.588202Z)
- `FUELINST|fuelType=OTHER|generation` = **377** (n=1054, 2026-09-18T15:20:40.588202Z)
- `FUELINST|fuelType=PS|generation` = **-49** (n=1054, 2026-09-18T15:20:40.588202Z)
- `FUELINST|fuelType=WIND|generation` = **16418** (n=1054, 2026-09-18T15:20:40.588202Z)
- `IMBALNGC|TOTAL|imbalance` = **8521** (n=174, 2026-09-18T15:23:28.385039Z)
- `INDDEM|TOTAL|demand` = **-10767** (n=174, 2026-09-18T15:23:10.555240Z)
- `INDGEN|TOTAL|generation` = **25571** (n=174, 2026-09-18T15:23:28.385039Z)
- `MELNGC|TOTAL|margin` = **38024** (n=174, 2026-09-18T15:20:56.613821Z)
- `NDF|TOTAL|demand` = **16550** (n=178, 2026-09-18T15:18:18.353381Z)
- `TSDF|TOTAL|demand` = **17050** (n=178, 2026-09-18T15:18:18.353381Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T15:24:40.239329Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:24:38.685648Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:24:37.124682Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:24:35.574375Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:24:33.679493Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:24:32.150266Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:24:30.612490Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:24:29.051902Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:24:27.490526Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:24:25.897553Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:24:24.363607Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:24:22.771387Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:24:21.198433Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:24:18.189723Z` — **MID**: 0 rows; marker `2026-09-18T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:24:18.189723Z` — **FREQ**: 5761 rows; marker `2026-09-18T15:23:45Z`
