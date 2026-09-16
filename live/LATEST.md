# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T13:01:39.158869Z`  
Current process started UTC: `2026-09-16T12:57:39.071516Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3293, delta=-7, z=-3.99 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3292, delta=-3, z=-3.79 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3290, delta=0, z=-4.16 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3290, delta=-7, z=-4.24 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3295, delta=-5, z=-3.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3297, delta=3, z=-3.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3294, delta=-4, z=-4.20 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3298, delta=-3, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3290, delta=-7, z=-5.03 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3297, delta=-24, z=-4.07 -> generation-mix component moved
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11768, delta=3343, z=1.00 -> demand pressure up
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-15111, delta=-1226, z=-8.15 -> demand pressure easing
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-13885, delta=0, z=-5.69 -> demand pressure easing
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-13885, delta=-1204, z=-7.82 -> demand pressure easing
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.27 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=481, 2026-09-16T13:00:34.778646Z)
- `FUELINST|fuelType=NPSHYD|generation` = **352** (n=481, 2026-09-16T13:00:34.778646Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3292** (n=481, 2026-09-16T13:00:34.778646Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=481, 2026-09-16T13:00:34.778646Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=481, 2026-09-16T13:00:34.778646Z)
- `FUELINST|fuelType=OTHER|generation` = **506** (n=481, 2026-09-16T13:00:34.778646Z)
- `FUELINST|fuelType=PS|generation` = **-3** (n=481, 2026-09-16T13:00:34.778646Z)
- `FUELINST|fuelType=WIND|generation` = **3857** (n=481, 2026-09-16T13:00:34.778646Z)
- `IMBALNGC|TOTAL|imbalance` = **6176** (n=79, 2026-09-16T12:53:54.729559Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=79, 2026-09-16T12:53:54.729559Z)
- `INDGEN|TOTAL|generation` = **24956** (n=79, 2026-09-16T12:53:54.729559Z)
- `MELNGC|TOTAL|margin` = **35502** (n=79, 2026-09-16T12:50:48.860242Z)
- `NDF|TOTAL|demand` = **18280** (n=81, 2026-09-16T12:48:32.910664Z)
- `TSDF|TOTAL|demand` = **18780** (n=81, 2026-09-16T12:48:32.910664Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T13:00:34.778646Z` — **FUELHH**: 20 rows; marker `2026-09-16T13:00:00Z`
- `2026-09-16T13:00:34.778646Z` — **FUELINST**: 80 rows; marker `2026-09-16T13:00:00Z`
- `2026-09-16T13:00:18.406738Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:59:45Z`
- `2026-09-16T12:58:11.075523Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:57:45Z`
- `2026-09-16T12:56:18.286766Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:55:45Z`
- `2026-09-16T12:55:46.095565Z` — **FUELINST**: 80 rows; marker `2026-09-16T12:55:00Z`
- `2026-09-16T12:54:26.156999Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:53:45Z`
- `2026-09-16T12:53:54.729559Z` — **INDGEN**: 1404 rows; marker `2026-09-16T12:48:00Z`
- `2026-09-16T12:53:54.729559Z` — **INDDEM**: 1404 rows; marker `2026-09-16T12:48:00Z`
- `2026-09-16T12:53:54.729559Z` — **IMBALNGC**: 1404 rows; marker `2026-09-16T12:48:00Z`
- `2026-09-16T12:52:25.313481Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:51:45Z`
- `2026-09-16T12:50:48.860242Z` — **MELNGC**: 1404 rows; marker `2026-09-16T12:48:00Z`
- `2026-09-16T12:50:32.688065Z` — **FUELINST**: 80 rows; marker `2026-09-16T12:50:00Z`
- `2026-09-16T12:50:16.837760Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:49:45Z`
- `2026-09-16T12:48:32.910664Z` — **TSDF**: 1404 rows; marker `2026-09-16T12:48:00Z`
