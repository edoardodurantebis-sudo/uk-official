# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T15:19:19.452964Z`  
Current process started UTC: `2026-09-22T15:15:19.855853Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3729, delta=7, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3732, delta=1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3731, delta=9, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3737, delta=0, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3722, delta=43, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3737, delta=4, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3733, delta=3, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3730, delta=10, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3136, delta=-128, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3264, delta=142, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3122, delta=169, z=3.61 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=-1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3662, delta=5, z=3.53 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3659, delta=11, z=3.61 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2158, 2026-09-22T15:15:35.857761Z)
- `FUELINST|fuelType=OTHER|generation` = **789** (n=2158, 2026-09-22T15:15:35.857761Z)
- `FUELINST|fuelType=PS|generation` = **-16** (n=2158, 2026-09-22T15:15:35.857761Z)
- `FUELINST|fuelType=WIND|generation` = **1486** (n=2158, 2026-09-22T15:15:35.857761Z)
- `IMBALNGC|TOTAL|imbalance` = **-7961** (n=354, 2026-09-22T14:53:01.821911Z)
- `INDDEM|TOTAL|demand` = **-12481** (n=354, 2026-09-22T14:52:45.550953Z)
- `INDGEN|TOTAL|generation` = **13212** (n=354, 2026-09-22T14:52:45.550953Z)
- `MELNGC|TOTAL|margin` = **37097** (n=354, 2026-09-22T14:50:21.926312Z)
- `MID|dataProvider=APXMIDP|price` = **154.24** (n=96, 2026-09-22T15:12:11.007386Z)
- `MID|dataProvider=APXMIDP|volume` = **3866.8** (n=96, 2026-09-22T15:12:11.007386Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=190, 2026-09-22T15:12:11.007386Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=190, 2026-09-22T15:12:11.007386Z)
- `NDF|TOTAL|demand` = **20673** (n=363, 2026-09-22T15:18:00.107683Z)
- `TSDF|TOTAL|demand` = **21173** (n=363, 2026-09-22T15:18:00.107683Z)
- `WINDFOR|TOTAL|generation` = **13082** (n=61, 2026-09-22T12:30:43.630179Z)

## Latest publication events

- `2026-09-22T15:18:16.145057Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:17:45Z`
- `2026-09-22T15:18:00.107683Z` — **TSDF**: 1314 rows; marker `2026-09-22T15:17:00Z`
- `2026-09-22T15:18:00.107683Z` — **NDF**: 73 rows; marker `2026-09-22T15:17:00Z`
- `2026-09-22T15:16:24.212343Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:15:45Z`
- `2026-09-22T15:15:35.857761Z` — **FUELINST**: 80 rows; marker `2026-09-22T15:15:00Z`
- `2026-09-22T15:14:18.762231Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:13:45Z`
- `2026-09-22T15:12:27.017166Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:11:45Z`
- `2026-09-22T15:12:11.007386Z` — **MID**: 2 rows; marker `2026-09-22T15:12:02Z`
- `2026-09-22T15:11:06.780583Z` — **FUELINST**: 80 rows; marker `2026-09-22T15:10:00Z`
- `2026-09-22T15:10:24.703050Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:09:45Z`
- `2026-09-22T15:08:16.626767Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:07:45Z`
- `2026-09-22T15:07:28.274273Z` — **MID**: 1 rows; marker `2026-09-22T15:05:00Z`
- `2026-09-22T15:06:40.331987Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:05:45Z`
- `2026-09-22T15:05:35.247320Z` — **FUELINST**: 80 rows; marker `2026-09-22T15:05:00Z`
- `2026-09-22T15:04:14.492147Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:03:45Z`
