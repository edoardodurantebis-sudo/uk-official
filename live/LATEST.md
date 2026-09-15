# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T16:26:08.231906Z`  
Current process started UTC: `2026-09-15T16:22:08.196091Z`  
1-second metadata polls in this process: **232**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.65 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.90 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=5.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=5.54 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=5.96 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=5, delta=5, z=4.84 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=2, z=6.51 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=5, delta=0, z=4.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=5, delta=0, z=5.10 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=5, delta=0, z=5.44 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=5, delta=3, z=5.86 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.81 -> generation-mix component moved
- **IMBALNGC** `TOTAL` `imbalance` — indicated system imbalance [TOTAL] imbalance: value=5650, delta=-1, z=3.51 -> indicated imbalance moved; inspect sign/magnitude
- **IMBALNGC** `TOTAL` `imbalance` — indicated system imbalance [TOTAL] imbalance: value=5651, delta=-24, z=4.85 -> indicated imbalance moved; inspect sign/magnitude
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=24755, delta=-24, z=4.72 -> state changed

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-938** (n=234, 2026-09-15T16:25:27.329511Z)
- `FUELINST|fuelType=NPSHYD|generation` = **477** (n=234, 2026-09-15T16:25:27.329511Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=234, 2026-09-15T16:25:27.329511Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=234, 2026-09-15T16:25:27.329511Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=234, 2026-09-15T16:25:27.329511Z)
- `FUELINST|fuelType=OTHER|generation` = **1046** (n=234, 2026-09-15T16:25:27.329511Z)
- `FUELINST|fuelType=PS|generation` = **124** (n=234, 2026-09-15T16:25:27.329511Z)
- `FUELINST|fuelType=WIND|generation` = **10202** (n=234, 2026-09-15T16:25:27.329511Z)
- `IMBALNGC|TOTAL|imbalance` = **5827** (n=39, 2026-09-15T16:22:45.257886Z)
- `INDDEM|TOTAL|demand` = **-11916** (n=39, 2026-09-15T16:22:12.196495Z)
- `INDGEN|TOTAL|generation` = **24948** (n=39, 2026-09-15T16:22:12.196495Z)
- `MELNGC|TOTAL|margin` = **34914** (n=39, 2026-09-15T16:19:48.233939Z)
- `NDF|TOTAL|demand` = **18621** (n=40, 2026-09-15T16:17:57.040685Z)
- `TSDF|TOTAL|demand` = **19121** (n=40, 2026-09-15T16:17:57.040685Z)
- `WINDFOR|TOTAL|generation` = **17848** (n=6, 2026-09-15T12:30:22.163636Z)

## Latest publication events

- `2026-09-15T16:25:27.329511Z` — **FUELINST**: 80 rows; marker `2026-09-15T16:25:00Z`
- `2026-09-15T16:24:22.552271Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:23:45Z`
- `2026-09-15T16:22:45.257886Z` — **IMBALNGC**: 1278 rows; marker `2026-09-15T16:17:00Z`
- `2026-09-15T16:22:12.196495Z` — **INDGEN**: 1278 rows; marker `2026-09-15T16:17:00Z`
- `2026-09-15T16:22:12.196495Z` — **INDDEM**: 1278 rows; marker `2026-09-15T16:17:00Z`
- `2026-09-15T16:22:12.196495Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:21:45Z`
- `2026-09-15T16:20:36.217482Z` — **FUELINST**: 80 rows; marker `2026-09-15T16:20:00Z`
- `2026-09-15T16:20:20.475922Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:19:45Z`
- `2026-09-15T16:19:48.233939Z` — **MELNGC**: 1278 rows; marker `2026-09-15T16:17:00Z`
- `2026-09-15T16:18:12.761913Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:17:45Z`
- `2026-09-15T16:17:57.040685Z` — **TSDF**: 1278 rows; marker `2026-09-15T16:17:00Z`
- `2026-09-15T16:17:57.040685Z` — **NDF**: 71 rows; marker `2026-09-15T16:17:00Z`
- `2026-09-15T16:16:25.446386Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:15:45Z`
- `2026-09-15T16:15:37.086168Z` — **FUELINST**: 80 rows; marker `2026-09-15T16:15:00Z`
- `2026-09-15T16:14:17.078513Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:13:45Z`
