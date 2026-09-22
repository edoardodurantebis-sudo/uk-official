# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T10:29:21.447875Z`  
Current process started UTC: `2026-09-22T10:25:21.131592Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2100, 2026-09-22T10:25:37.192626Z)
- `FUELINST|fuelType=OTHER|generation` = **530** (n=2100, 2026-09-22T10:25:37.192626Z)
- `FUELINST|fuelType=PS|generation` = **-167** (n=2100, 2026-09-22T10:25:37.192626Z)
- `FUELINST|fuelType=WIND|generation` = **3571** (n=2100, 2026-09-22T10:25:37.192626Z)
- `IMBALNGC|TOTAL|imbalance` = **5167** (n=345, 2026-09-22T10:19:32.170249Z)
- `INDDEM|TOTAL|demand` = **-13862** (n=345, 2026-09-22T10:19:16.023000Z)
- `INDGEN|TOTAL|generation` = **26115** (n=345, 2026-09-22T10:19:16.023000Z)
- `MELNGC|TOTAL|margin` = **40386** (n=345, 2026-09-22T10:19:00.047508Z)
- `MID|dataProvider=APXMIDP|price` = **128.53** (n=86, 2026-09-22T10:12:19.753647Z)
- `MID|dataProvider=APXMIDP|volume` = **3806.3** (n=86, 2026-09-22T10:12:19.753647Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=170, 2026-09-22T10:12:19.753647Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=170, 2026-09-22T10:12:19.753647Z)
- `NDF|TOTAL|demand` = **20200** (n=353, 2026-09-22T10:17:08.386834Z)
- `TSDF|TOTAL|demand` = **20948** (n=353, 2026-09-22T10:17:08.386834Z)
- `WINDFOR|TOTAL|generation` = **12393** (n=59, 2026-09-22T08:31:02.929426Z)

## Latest publication events

- `2026-09-22T10:28:16.671003Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:27:45Z`
- `2026-09-22T10:26:24.637701Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:25:45Z`
- `2026-09-22T10:25:37.192626Z` — **FUELINST**: 80 rows; marker `2026-09-22T10:25:00Z`
- `2026-09-22T10:24:16.411975Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:23:45Z`
- `2026-09-22T10:22:24.814133Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:21:45Z`
- `2026-09-22T10:20:36.868040Z` — **FUELINST**: 80 rows; marker `2026-09-22T10:20:00Z`
- `2026-09-22T10:20:20.550045Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:19:45Z`
- `2026-09-22T10:19:32.170249Z` — **IMBALNGC**: 630 rows; marker `2026-09-22T10:16:00Z`
- `2026-09-22T10:19:16.023000Z` — **INDGEN**: 630 rows; marker `2026-09-22T10:16:00Z`
- `2026-09-22T10:19:16.023000Z` — **INDDEM**: 630 rows; marker `2026-09-22T10:16:00Z`
- `2026-09-22T10:19:00.047508Z` — **MELNGC**: 630 rows; marker `2026-09-22T10:16:00Z`
- `2026-09-22T10:18:27.873206Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:17:45Z`
- `2026-09-22T10:17:08.386834Z` — **TSDF**: 630 rows; marker `2026-09-22T10:16:00Z`
- `2026-09-22T10:17:08.386834Z` — **NDF**: 35 rows; marker `2026-09-22T10:16:00Z`
- `2026-09-22T10:16:19.237519Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:15:45Z`
