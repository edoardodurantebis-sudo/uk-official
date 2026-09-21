# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T09:55:50.937524Z`  
Current process started UTC: `2026-09-21T09:51:50.637133Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3494, delta=0, z=5.19 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3494, delta=5, z=5.23 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3489, delta=5, z=5.11 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3484, delta=-4, z=4.98 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3488, delta=-4, z=5.15 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3500, delta=4, z=5.90 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3492, delta=-7, z=5.32 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=0, z=5.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=-2, z=5.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=-2, z=5.78 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3503, delta=5, z=5.90 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3498, delta=7, z=5.79 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-3, z=6.11 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3491, delta=-2, z=5.59 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3493, delta=0, z=5.72 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1809, 2026-09-21T09:55:19.223809Z)
- `FUELINST|fuelType=OTHER|generation` = **765** (n=1809, 2026-09-21T09:55:19.223809Z)
- `FUELINST|fuelType=PS|generation` = **-11** (n=1809, 2026-09-21T09:55:19.223809Z)
- `FUELINST|fuelType=WIND|generation` = **3270** (n=1809, 2026-09-21T09:55:19.223809Z)
- `IMBALNGC|TOTAL|imbalance` = **569** (n=297, 2026-09-21T09:49:16.952337Z)
- `INDDEM|TOTAL|demand` = **-12811** (n=297, 2026-09-21T09:49:16.952337Z)
- `INDGEN|TOTAL|generation` = **21728** (n=297, 2026-09-21T09:49:16.952337Z)
- `MELNGC|TOTAL|margin` = **39819** (n=297, 2026-09-21T09:48:45.225710Z)
- `MID|dataProvider=APXMIDP|price` = **185.3** (n=37, 2026-09-21T09:42:14.042386Z)
- `MID|dataProvider=APXMIDP|volume` = **3412.1** (n=37, 2026-09-21T09:42:14.042386Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=74, 2026-09-21T09:42:14.042386Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=74, 2026-09-21T09:42:14.042386Z)
- `NDF|TOTAL|demand` = **20000** (n=304, 2026-09-21T09:46:53.428239Z)
- `TSDF|TOTAL|demand` = **21159** (n=304, 2026-09-21T09:46:53.428239Z)
- `WINDFOR|TOTAL|generation` = **9277** (n=51, 2026-09-21T08:30:33.936824Z)

## Latest publication events

- `2026-09-21T09:55:19.223809Z` — **FUELINST**: 80 rows; marker `2026-09-21T09:55:00Z`
- `2026-09-21T09:54:14.787329Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:53:45Z`
- `2026-09-21T09:52:06.730014Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:51:45Z`
- `2026-09-21T09:50:21.030260Z` — **FUELINST**: 80 rows; marker `2026-09-21T09:50:00Z`
- `2026-09-21T09:50:04.937276Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:49:45Z`
- `2026-09-21T09:49:16.952337Z` — **INDGEN**: 648 rows; marker `2026-09-21T09:46:00Z`
- `2026-09-21T09:49:16.952337Z` — **INDDEM**: 648 rows; marker `2026-09-21T09:46:00Z`
- `2026-09-21T09:49:16.952337Z` — **IMBALNGC**: 648 rows; marker `2026-09-21T09:46:00Z`
- `2026-09-21T09:48:45.225710Z` — **MELNGC**: 648 rows; marker `2026-09-21T09:46:00Z`
- `2026-09-21T09:48:12.937841Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:47:45Z`
- `2026-09-21T09:46:53.428239Z` — **TSDF**: 648 rows; marker `2026-09-21T09:46:00Z`
- `2026-09-21T09:46:53.428239Z` — **NDF**: 36 rows; marker `2026-09-21T09:46:00Z`
- `2026-09-21T09:46:05.615902Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:45:45Z`
- `2026-09-21T09:45:33.428372Z` — **FUELINST**: 80 rows; marker `2026-09-21T09:45:00Z`
- `2026-09-21T09:44:29.936609Z` — **FREQ**: 5761 rows; marker `2026-09-21T09:43:45Z`
