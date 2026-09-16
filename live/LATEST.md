# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T14:29:54.323644Z`  
Current process started UTC: `2026-09-16T14:25:54.653111Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3288, delta=3, z=-3.98 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3285, delta=-3, z=-4.41 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3288, delta=-3, z=-4.14 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=498, 2026-09-16T14:25:26.013621Z)
- `FUELINST|fuelType=NPSHYD|generation` = **356** (n=498, 2026-09-16T14:25:26.013621Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3288** (n=498, 2026-09-16T14:25:26.013621Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=498, 2026-09-16T14:25:26.013621Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=498, 2026-09-16T14:25:26.013621Z)
- `FUELINST|fuelType=OTHER|generation` = **526** (n=498, 2026-09-16T14:25:26.013621Z)
- `FUELINST|fuelType=PS|generation` = **233** (n=498, 2026-09-16T14:25:26.013621Z)
- `FUELINST|fuelType=WIND|generation` = **5324** (n=498, 2026-09-16T14:25:26.013621Z)
- `IMBALNGC|TOTAL|imbalance` = **6670** (n=82, 2026-09-16T14:23:34.552018Z)
- `INDDEM|TOTAL|demand` = **-11776** (n=82, 2026-09-16T14:23:34.552018Z)
- `INDGEN|TOTAL|generation` = **25450** (n=82, 2026-09-16T14:23:34.552018Z)
- `MELNGC|TOTAL|margin` = **34664** (n=82, 2026-09-16T14:20:27.682808Z)
- `NDF|TOTAL|demand` = **18280** (n=84, 2026-09-16T14:18:19.617927Z)
- `TSDF|TOTAL|demand` = **18780** (n=84, 2026-09-16T14:18:19.617927Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T14:28:18.451327Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:27:45Z`
- `2026-09-16T14:26:26.766005Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:25:45Z`
- `2026-09-16T14:25:26.013621Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:25:00Z`
- `2026-09-16T14:24:22.229188Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:23:45Z`
- `2026-09-16T14:23:34.552018Z` — **INDGEN**: 1350 rows; marker `2026-09-16T14:17:00Z`
- `2026-09-16T14:23:34.552018Z` — **INDDEM**: 1350 rows; marker `2026-09-16T14:17:00Z`
- `2026-09-16T14:23:34.552018Z` — **IMBALNGC**: 1350 rows; marker `2026-09-16T14:17:00Z`
- `2026-09-16T14:22:13.750616Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:21:45Z`
- `2026-09-16T14:20:27.682808Z` — **MELNGC**: 1350 rows; marker `2026-09-16T14:17:00Z`
- `2026-09-16T14:20:27.682808Z` — **FUELINST**: 80 rows; marker `2026-09-16T14:20:00Z`
- `2026-09-16T14:20:12.262057Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:19:45Z`
- `2026-09-16T14:18:19.617927Z` — **TSDF**: 1350 rows; marker `2026-09-16T14:17:00Z`
- `2026-09-16T14:18:19.617927Z` — **NDF**: 75 rows; marker `2026-09-16T14:17:00Z`
- `2026-09-16T14:18:19.617927Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:17:45Z`
- `2026-09-16T14:16:18.035825Z` — **FREQ**: 5761 rows; marker `2026-09-16T14:15:45Z`
