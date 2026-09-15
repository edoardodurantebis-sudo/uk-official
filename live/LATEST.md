# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T12:22:10.078215Z`  
Current process started UTC: `2026-09-15T12:18:09.927271Z`  
1-second metadata polls in this process: **232**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **IMBALNGC** `TOTAL` `imbalance` — indicated system imbalance [TOTAL] imbalance: value=5650, delta=-1, z=3.51 -> indicated imbalance moved; inspect sign/magnitude
- **IMBALNGC** `TOTAL` `imbalance` — indicated system imbalance [TOTAL] imbalance: value=5651, delta=-24, z=4.85 -> indicated imbalance moved; inspect sign/magnitude
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=24755, delta=-24, z=4.72 -> state changed
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11901, delta=0, z=3.83 -> demand pressure easing
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=19104, delta=0, z=-3.76 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=18604, delta=0, z=-3.74 -> demand pressure easing
- **IMBALNGC** `TOTAL` `imbalance` — indicated system imbalance [TOTAL] imbalance: value=5675, delta=6507, z=16.70 -> indicated imbalance moved; inspect sign/magnitude
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=24779, delta=5042, z=13.07 -> state changed
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11901, delta=369, z=5.90 -> demand pressure up
- **FUELHH** `fuelType=BIOMASS` `generation` — half-hour generation mix [fuelType=BIOMASS] generation: value=1292, delta=-487, z=-3.55 -> generation-mix component moved
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=19104, delta=-1465, z=-5.53 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=18604, delta=-1465, z=-5.48 -> demand pressure easing
- **FUELHH** `fuelType=INTFR` `generation` — half-hour generation mix [fuelType=INTFR] generation: value=984, delta=278, z=4.11 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=999, delta=-1, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=1000, delta=1, z=3.83 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=185, 2026-09-15T12:20:19.176282Z)
- `FUELINST|fuelType=NPSHYD|generation` = **355** (n=185, 2026-09-15T12:20:19.176282Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=185, 2026-09-15T12:20:19.176282Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=185, 2026-09-15T12:20:19.176282Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=185, 2026-09-15T12:20:19.176282Z)
- `FUELINST|fuelType=OTHER|generation` = **390** (n=185, 2026-09-15T12:20:19.176282Z)
- `FUELINST|fuelType=PS|generation` = **-1092** (n=185, 2026-09-15T12:20:19.176282Z)
- `FUELINST|fuelType=WIND|generation` = **10954** (n=185, 2026-09-15T12:20:19.176282Z)
- `IMBALNGC|TOTAL|imbalance` = **5650** (n=30, 2026-09-15T11:53:45.899936Z)
- `INDDEM|TOTAL|demand` = **-11901** (n=30, 2026-09-15T11:53:30.375632Z)
- `INDGEN|TOTAL|generation` = **24753** (n=30, 2026-09-15T11:53:30.375632Z)
- `MELNGC|TOTAL|margin` = **35178** (n=31, 2026-09-15T12:20:35.294204Z)
- `NDF|TOTAL|demand` = **18604** (n=32, 2026-09-15T12:18:26.250837Z)
- `TSDF|TOTAL|demand` = **19104** (n=32, 2026-09-15T12:18:26.250837Z)
- `WINDFOR|TOTAL|generation` = **17599** (n=5, 2026-09-15T10:30:45.227650Z)

## Latest publication events

- `2026-09-15T12:20:35.294204Z` — **MELNGC**: 1422 rows; marker `2026-09-15T12:17:00Z`
- `2026-09-15T12:20:19.176282Z` — **FUELINST**: 80 rows; marker `2026-09-15T12:20:00Z`
- `2026-09-15T12:20:19.176282Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:19:45Z`
- `2026-09-15T12:18:26.250837Z` — **TSDF**: 1422 rows; marker `2026-09-15T12:18:00Z`
- `2026-09-15T12:18:26.250837Z` — **NDF**: 79 rows; marker `2026-09-15T12:18:00Z`
- `2026-09-15T12:18:09.927279Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:17:45Z`
- `2026-09-15T12:16:19.577220Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:15:45Z`
- `2026-09-15T12:15:47.770014Z` — **FUELINST**: 80 rows; marker `2026-09-15T12:15:00Z`
- `2026-09-15T12:14:11.581438Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:13:45Z`
- `2026-09-15T12:12:09.910799Z` — **MID**: 0 rows; marker `2026-09-15T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T12:12:09.910799Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:11:45Z`
- `2026-09-15T12:10:33.553553Z` — **FUELINST**: 80 rows; marker `2026-09-15T12:10:00Z`
- `2026-09-15T12:10:01.221803Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:09:45Z`
- `2026-09-15T12:08:25.705352Z` — **FREQ**: 5761 rows; marker `2026-09-15T12:07:45Z`
- `2026-09-15T12:07:21.755779Z` — **MID**: 0 rows; marker `2026-09-15T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
