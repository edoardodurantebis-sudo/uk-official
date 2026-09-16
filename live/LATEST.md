# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T15:20:13.884442Z`  
Current process started UTC: `2026-09-16T15:16:13.847542Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3282, delta=0, z=-3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3282, delta=-3, z=-3.63 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3286, delta=2, z=-3.65 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3285, delta=6, z=-3.64 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3279, delta=-1, z=-4.31 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3284, delta=-5, z=-4.28 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3280, delta=-3, z=-4.29 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3283, delta=-4, z=-4.06 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3287, delta=3, z=-3.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3284, delta=0, z=-4.09 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3284, delta=-3, z=-4.16 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3287, delta=-2, z=-3.91 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3289, delta=-4, z=-4.11 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3289, delta=-1, z=-3.74 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3290, delta=2, z=-3.69 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **777** (n=508, 2026-09-16T15:15:34.481797Z)
- `FUELINST|fuelType=NPSHYD|generation` = **393** (n=508, 2026-09-16T15:15:34.481797Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3295** (n=508, 2026-09-16T15:15:34.481797Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=508, 2026-09-16T15:15:34.481797Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=508, 2026-09-16T15:15:34.481797Z)
- `FUELINST|fuelType=OTHER|generation` = **176** (n=508, 2026-09-16T15:15:34.481797Z)
- `FUELINST|fuelType=PS|generation` = **233** (n=508, 2026-09-16T15:15:34.481797Z)
- `FUELINST|fuelType=WIND|generation` = **5425** (n=508, 2026-09-16T15:15:34.481797Z)
- `IMBALNGC|TOTAL|imbalance` = **6731** (n=83, 2026-09-16T14:53:31.076071Z)
- `INDDEM|TOTAL|demand` = **-11776** (n=83, 2026-09-16T14:53:14.892448Z)
- `INDGEN|TOTAL|generation` = **25511** (n=83, 2026-09-16T14:53:14.892448Z)
- `MELNGC|TOTAL|margin` = **34664** (n=83, 2026-09-16T14:50:36.190848Z)
- `NDF|TOTAL|demand` = **18280** (n=85, 2026-09-16T14:48:13.119768Z)
- `TSDF|TOTAL|demand` = **18780** (n=85, 2026-09-16T14:48:13.119768Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T15:18:22.547719Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:17:45Z`
- `2026-09-16T15:16:13.847548Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:15:45Z`
- `2026-09-16T15:15:34.481797Z` — **FUELINST**: 80 rows; marker `2026-09-16T15:15:00Z`
- `2026-09-16T15:14:15.019407Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:13:45Z`
- `2026-09-16T15:12:22.858245Z` — **MID**: 0 rows; marker `2026-09-16T15:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T15:12:22.858245Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:11:45Z`
- `2026-09-16T15:10:30.913434Z` — **FUELINST**: 80 rows; marker `2026-09-16T15:10:00Z`
- `2026-09-16T15:10:14.838639Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:09:45Z`
- `2026-09-16T15:08:22.635094Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:07:45Z`
- `2026-09-16T15:06:35.814810Z` — **MID**: 0 rows; marker `2026-09-16T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T15:06:19.809255Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:05:45Z`
- `2026-09-16T15:05:31.471832Z` — **FUELINST**: 80 rows; marker `2026-09-16T15:05:00Z`
- `2026-09-16T15:04:11.723306Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:03:45Z`
- `2026-09-16T15:02:24.413211Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:01:45Z`
- `2026-09-16T15:00:32.042962Z` — **FUELHH**: 20 rows; marker `2026-09-16T15:00:00Z`
