# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T16:42:58.171331Z`  
Current process started UTC: `2026-09-15T16:38:58.049145Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.09 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.26 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=7, delta=2, z=5.40 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.44 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-938** (n=237, 2026-09-15T16:40:37.378666Z)
- `FUELINST|fuelType=NPSHYD|generation` = **477** (n=237, 2026-09-15T16:40:37.378666Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3319** (n=237, 2026-09-15T16:40:37.378666Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=237, 2026-09-15T16:40:37.378666Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=237, 2026-09-15T16:40:37.378666Z)
- `FUELINST|fuelType=OTHER|generation` = **672** (n=237, 2026-09-15T16:40:37.378666Z)
- `FUELINST|fuelType=PS|generation` = **424** (n=237, 2026-09-15T16:40:37.378666Z)
- `FUELINST|fuelType=WIND|generation` = **10213** (n=237, 2026-09-15T16:40:37.378666Z)
- `IMBALNGC|TOTAL|imbalance` = **5827** (n=39, 2026-09-15T16:22:45.257886Z)
- `INDDEM|TOTAL|demand` = **-11916** (n=39, 2026-09-15T16:22:12.196495Z)
- `INDGEN|TOTAL|generation` = **24948** (n=39, 2026-09-15T16:22:12.196495Z)
- `MELNGC|TOTAL|margin` = **34914** (n=39, 2026-09-15T16:19:48.233939Z)
- `NDF|TOTAL|demand` = **18621** (n=40, 2026-09-15T16:17:57.040685Z)
- `TSDF|TOTAL|demand` = **19121** (n=40, 2026-09-15T16:17:57.040685Z)
- `WINDFOR|TOTAL|generation` = **17795** (n=7, 2026-09-15T16:30:51.506988Z)

## Latest publication events

- `2026-09-15T16:42:28.662093Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:41:45Z`
- `2026-09-15T16:42:12.958703Z` — **MID**: 0 rows; marker `2026-09-15T16:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T16:40:37.378666Z` — **FUELINST**: 80 rows; marker `2026-09-15T16:40:00Z`
- `2026-09-15T16:40:21.515222Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:39:45Z`
- `2026-09-15T16:38:29.669983Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:37:45Z`
- `2026-09-15T16:37:25.586537Z` — **MID**: 0 rows; marker `2026-09-15T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T16:36:22.025253Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:35:45Z`
- `2026-09-15T16:35:34.160729Z` — **FUELINST**: 80 rows; marker `2026-09-15T16:35:00Z`
- `2026-09-15T16:34:19.423444Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:33:45Z`
- `2026-09-15T16:32:27.569512Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:31:45Z`
- `2026-09-15T16:30:51.506988Z` — **WINDFOR**: 73 rows; marker `2026-09-15T16:30:00Z`
- `2026-09-15T16:30:36.142909Z` — **FUELHH**: 20 rows; marker `2026-09-15T16:30:00Z`
- `2026-09-15T16:30:36.142909Z` — **FUELINST**: 80 rows; marker `2026-09-15T16:30:00Z`
- `2026-09-15T16:30:19.817085Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:29:45Z`
- `2026-09-15T16:28:12.321115Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:27:45Z`
