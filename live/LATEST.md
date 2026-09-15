# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T19:19:15.607489Z`  
Current process started UTC: `2026-09-15T19:15:15.497767Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.76 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=17, z=8.89 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.93 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.39 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.98 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=7.77 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=2942, delta=440, z=3.58 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=39, delta=32, z=16.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=8.90 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=10.72 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=7, z=14.50 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-291** (n=268, 2026-09-15T19:15:47.502269Z)
- `FUELINST|fuelType=NPSHYD|generation` = **498** (n=268, 2026-09-15T19:15:47.502269Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3320** (n=268, 2026-09-15T19:15:47.502269Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=268, 2026-09-15T19:15:47.502269Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=268, 2026-09-15T19:15:47.502269Z)
- `FUELINST|fuelType=OTHER|generation` = **1480** (n=268, 2026-09-15T19:15:47.502269Z)
- `FUELINST|fuelType=PS|generation` = **552** (n=268, 2026-09-15T19:15:47.502269Z)
- `FUELINST|fuelType=WIND|generation` = **10413** (n=268, 2026-09-15T19:15:47.502269Z)
- `IMBALNGC|TOTAL|imbalance` = **5739** (n=44, 2026-09-15T18:51:56.171679Z)
- `INDDEM|TOTAL|demand` = **-11910** (n=44, 2026-09-15T18:51:56.171679Z)
- `INDGEN|TOTAL|generation` = **24860** (n=44, 2026-09-15T18:51:40.439586Z)
- `MELNGC|TOTAL|margin` = **35590** (n=44, 2026-09-15T18:49:36.986440Z)
- `NDF|TOTAL|demand` = **18621** (n=46, 2026-09-15T19:17:40.131677Z)
- `TSDF|TOTAL|demand` = **19121** (n=46, 2026-09-15T19:17:40.131677Z)
- `WINDFOR|TOTAL|generation` = **17795** (n=7, 2026-09-15T16:30:51.506988Z)

## Latest publication events

- `2026-09-15T19:18:11.847686Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:17:45Z`
- `2026-09-15T19:17:40.131677Z` — **TSDF**: 1170 rows; marker `2026-09-15T19:17:00Z`
- `2026-09-15T19:17:40.131677Z` — **NDF**: 65 rows; marker `2026-09-15T19:17:00Z`
- `2026-09-15T19:16:19.808722Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:15:45Z`
- `2026-09-15T19:15:47.502269Z` — **FUELINST**: 80 rows; marker `2026-09-15T19:15:00Z`
- `2026-09-15T19:14:16.785361Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:13:45Z`
- `2026-09-15T19:12:08.830895Z` — **MID**: 0 rows; marker `2026-09-15T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T19:12:08.830895Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:11:45Z`
- `2026-09-15T19:10:33.455685Z` — **FUELINST**: 80 rows; marker `2026-09-15T19:10:00Z`
- `2026-09-15T19:10:18.097985Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:09:45Z`
- `2026-09-15T19:08:09.869176Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:07:45Z`
- `2026-09-15T19:07:38.045972Z` — **MID**: 0 rows; marker `2026-09-15T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T19:06:26.729222Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:05:45Z`
- `2026-09-15T19:05:39.336629Z` — **FUELINST**: 80 rows; marker `2026-09-15T19:05:00Z`
- `2026-09-15T19:04:19.307951Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:03:45Z`
