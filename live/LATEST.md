# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T10:12:22.788931Z`  
Current process started UTC: `2026-09-22T10:08:20.726445Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3136, delta=-128, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3264, delta=142, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3122, delta=169, z=3.61 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=-1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3662, delta=5, z=3.53 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3659, delta=11, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3659, delta=-2, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=1, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=-3, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3663, delta=14, z=3.65 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-2, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-5, z=3.50 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2097, 2026-09-22T10:10:27.935864Z)
- `FUELINST|fuelType=OTHER|generation` = **490** (n=2097, 2026-09-22T10:10:27.935864Z)
- `FUELINST|fuelType=PS|generation` = **-168** (n=2097, 2026-09-22T10:10:27.935864Z)
- `FUELINST|fuelType=WIND|generation` = **3776** (n=2097, 2026-09-22T10:10:27.935864Z)
- `IMBALNGC|TOTAL|imbalance` = **3833** (n=344, 2026-09-22T09:49:20.892309Z)
- `INDDEM|TOTAL|demand` = **-13095** (n=344, 2026-09-22T09:49:20.892309Z)
- `INDGEN|TOTAL|generation` = **24901** (n=344, 2026-09-22T09:49:20.892309Z)
- `MELNGC|TOTAL|margin` = **40269** (n=344, 2026-09-22T09:48:48.787526Z)
- `MID|dataProvider=APXMIDP|price` = **128.53** (n=86, 2026-09-22T10:12:19.753647Z)
- `MID|dataProvider=APXMIDP|volume` = **3806.3** (n=86, 2026-09-22T10:12:19.753647Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=170, 2026-09-22T10:12:19.753647Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=170, 2026-09-22T10:12:19.753647Z)
- `NDF|TOTAL|demand` = **20320** (n=352, 2026-09-22T09:46:55.536738Z)
- `TSDF|TOTAL|demand` = **21068** (n=352, 2026-09-22T09:46:55.536738Z)
- `WINDFOR|TOTAL|generation` = **12393** (n=59, 2026-09-22T08:31:02.929426Z)

## Latest publication events

- `2026-09-22T10:12:19.753647Z` — **MID**: 2 rows; marker `2026-09-22T10:12:03Z`
- `2026-09-22T10:12:19.753647Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:11:45Z`
- `2026-09-22T10:10:27.935864Z` — **FUELINST**: 80 rows; marker `2026-09-22T10:10:00Z`
- `2026-09-22T10:10:12.496399Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:09:45Z`
- `2026-09-22T10:08:20.726457Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:07:45Z`
- `2026-09-22T10:06:31.097235Z` — **MID**: 1 rows; marker `2026-09-22T10:05:00Z`
- `2026-09-22T10:06:15.001715Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:05:45Z`
- `2026-09-22T10:05:27.341724Z` — **FUELINST**: 80 rows; marker `2026-09-22T10:05:00Z`
- `2026-09-22T10:04:23.202362Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:03:45Z`
- `2026-09-22T10:02:20.279496Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:01:45Z`
- `2026-09-22T10:00:28.840045Z` — **FUELHH**: 20 rows; marker `2026-09-22T10:00:00Z`
- `2026-09-22T10:00:28.840045Z` — **FUELINST**: 80 rows; marker `2026-09-22T10:00:00Z`
- `2026-09-22T10:00:13.258591Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:59:45Z`
- `2026-09-22T09:58:20.920484Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:57:45Z`
- `2026-09-22T09:56:13.457200Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:55:45Z`
