# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T16:13:30.611420Z`  
Current process started UTC: `2026-09-15T16:09:29.865055Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11901, delta=0, z=3.83 -> demand pressure easing
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=19104, delta=0, z=-3.76 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=18604, delta=0, z=-3.74 -> demand pressure easing

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-892** (n=231, 2026-09-15T16:10:34.375937Z)
- `FUELINST|fuelType=NPSHYD|generation` = **490** (n=231, 2026-09-15T16:10:34.375937Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3322** (n=231, 2026-09-15T16:10:34.375937Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=231, 2026-09-15T16:10:34.375937Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=231, 2026-09-15T16:10:34.375937Z)
- `FUELINST|fuelType=OTHER|generation` = **1172** (n=231, 2026-09-15T16:10:34.375937Z)
- `FUELINST|fuelType=PS|generation` = **129** (n=231, 2026-09-15T16:10:34.375937Z)
- `FUELINST|fuelType=WIND|generation` = **10348** (n=231, 2026-09-15T16:10:34.375937Z)
- `IMBALNGC|TOTAL|imbalance` = **5825** (n=38, 2026-09-15T15:52:53.128338Z)
- `INDDEM|TOTAL|demand` = **-11916** (n=38, 2026-09-15T15:52:53.128338Z)
- `INDGEN|TOTAL|generation` = **24946** (n=38, 2026-09-15T15:52:53.128338Z)
- `MELNGC|TOTAL|margin` = **34968** (n=38, 2026-09-15T15:50:08.173773Z)
- `NDF|TOTAL|demand` = **18621** (n=39, 2026-09-15T15:48:00.289174Z)
- `TSDF|TOTAL|demand` = **19121** (n=39, 2026-09-15T15:48:00.289174Z)
- `WINDFOR|TOTAL|generation` = **17848** (n=6, 2026-09-15T12:30:22.163636Z)

## Latest publication events

- `2026-09-15T16:12:10.255600Z` — **MID**: 0 rows; marker `2026-09-15T16:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T16:12:10.255600Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:11:45Z`
- `2026-09-15T16:10:34.375937Z` — **FUELINST**: 80 rows; marker `2026-09-15T16:10:00Z`
- `2026-09-15T16:10:18.980157Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:09:45Z`
- `2026-09-15T16:09:47.005406Z` — **MID**: 0 rows; marker `2026-09-15T16:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T16:08:11.391149Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:07:45Z`
- `2026-09-15T16:06:03.323103Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:05:45Z`
- `2026-09-15T16:05:31.822989Z` — **FUELINST**: 80 rows; marker `2026-09-15T16:05:00Z`
- `2026-09-15T16:04:13.535663Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:03:45Z`
- `2026-09-15T16:02:05.436353Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:01:45Z`
- `2026-09-15T16:00:35.966007Z` — **FUELHH**: 20 rows; marker `2026-09-15T16:00:00Z`
- `2026-09-15T16:00:35.966007Z` — **FUELINST**: 80 rows; marker `2026-09-15T16:00:00Z`
- `2026-09-15T16:00:04.010825Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:59:45Z`
- `2026-09-15T15:58:28.061955Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:57:45Z`
- `2026-09-15T15:56:20.611582Z` — **FREQ**: 5761 rows; marker `2026-09-15T15:55:45Z`
