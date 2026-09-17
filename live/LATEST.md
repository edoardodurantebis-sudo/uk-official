# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T14:19:40.658590Z`  
Current process started UTC: `2026-09-17T14:15:40.275924Z`  
1-second metadata polls in this process: **224**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16543, delta=0, z=-3.52 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16043, delta=0, z=-3.54 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16043, delta=0, z=-3.76 -> demand pressure easing
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16543, delta=0, z=-3.73 -> demand pressure easing
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16543, delta=-54, z=-3.99 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16043, delta=-54, z=-4.02 -> demand pressure easing
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11265, delta=1771, z=1.70 -> demand pressure up
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16597, delta=-3265, z=-4.21 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16097, delta=-2159, z=-4.24 -> demand pressure easing
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16658, delta=-2713, z=-4.41 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16158, delta=-2463, z=-4.57 -> demand pressure easing
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=2, delta=-50, z=-0.16 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=-4, z=3.91 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.36 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-433** (n=753, 2026-09-17T14:15:40.275932Z)
- `FUELINST|fuelType=NPSHYD|generation` = **273** (n=753, 2026-09-17T14:15:40.275932Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3309** (n=753, 2026-09-17T14:15:40.275932Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=753, 2026-09-17T14:15:40.275932Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=753, 2026-09-17T14:15:40.275932Z)
- `FUELINST|fuelType=OTHER|generation` = **737** (n=753, 2026-09-17T14:15:40.275932Z)
- `FUELINST|fuelType=PS|generation` = **-934** (n=753, 2026-09-17T14:15:40.275932Z)
- `FUELINST|fuelType=WIND|generation` = **12740** (n=753, 2026-09-17T14:15:40.275932Z)
- `IMBALNGC|TOTAL|imbalance` = **11937** (n=124, 2026-09-17T13:56:05.761870Z)
- `INDDEM|TOTAL|demand` = **-11256** (n=124, 2026-09-17T13:55:49.436735Z)
- `INDGEN|TOTAL|generation` = **28480** (n=124, 2026-09-17T13:55:49.436735Z)
- `MELNGC|TOTAL|margin` = **35870** (n=124, 2026-09-17T13:52:37.774938Z)
- `NDF|TOTAL|demand` = **16043** (n=128, 2026-09-17T14:19:23.791920Z)
- `TSDF|TOTAL|demand` = **16543** (n=128, 2026-09-17T14:19:23.791920Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T14:19:39.435236Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:19:38.435123Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:19:37.435037Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:19:36.434928Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:19:35.434804Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:19:34.434696Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:19:33.434570Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:19:32.434463Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:19:31.434385Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:19:30.434267Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:19:29.434189Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:19:28.434071Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:19:27.433969Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:19:26.433852Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:19:23.791920Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
