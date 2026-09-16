# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T00:10:30.730818Z`  
Current process started UTC: `2026-09-16T00:06:30.752615Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-10.18 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-10.91 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-11.82 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-13.01 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=-0.006, z=-14.65 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.978, delta=-0.11, z=-15.92 -> frequency excursion; balancing stress check
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.36 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=-1, z=3.74 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.30 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=54, delta=-1, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.76 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **114** (n=326, 2026-09-16T00:05:32.230787Z)
- `FUELINST|fuelType=NPSHYD|generation` = **403** (n=326, 2026-09-16T00:05:32.230787Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=326, 2026-09-16T00:05:32.230787Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=326, 2026-09-16T00:05:32.230787Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=326, 2026-09-16T00:05:32.230787Z)
- `FUELINST|fuelType=OTHER|generation` = **207** (n=326, 2026-09-16T00:05:32.230787Z)
- `FUELINST|fuelType=PS|generation` = **202** (n=326, 2026-09-16T00:05:32.230787Z)
- `FUELINST|fuelType=WIND|generation` = **10343** (n=326, 2026-09-16T00:05:32.230787Z)
- `IMBALNGC|TOTAL|imbalance` = **5865** (n=54, 2026-09-15T23:50:54.652718Z)
- `INDDEM|TOTAL|demand` = **-12080** (n=54, 2026-09-15T23:50:54.652718Z)
- `INDGEN|TOTAL|generation` = **24986** (n=54, 2026-09-15T23:50:54.652718Z)
- `MELNGC|TOTAL|margin` = **35662** (n=54, 2026-09-15T23:49:18.398374Z)
- `NDF|TOTAL|demand` = **18621** (n=55, 2026-09-15T23:47:27.510265Z)
- `TSDF|TOTAL|demand` = **19121** (n=55, 2026-09-15T23:47:27.510265Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-16T00:10:19.327177Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:09:45Z`
- `2026-09-16T00:08:11.474521Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:07:45Z`
- `2026-09-16T00:06:35.753095Z` — **MID**: 0 rows; marker `2026-09-16T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T00:06:20.237665Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:05:45Z`
- `2026-09-16T00:05:32.230787Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:05:00Z`
- `2026-09-16T00:04:12.470606Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:03:45Z`
- `2026-09-16T00:02:20.278249Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:01:45Z`
- `2026-09-16T00:00:22.660225Z` — **FUELHH**: 20 rows; marker `2026-09-16T00:00:00Z`
- `2026-09-16T00:00:22.660225Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:00:00Z`
- `2026-09-16T00:00:22.660225Z` — **FREQ**: 5760 rows; marker `2026-09-15T23:59:45Z`
- `2026-09-15T23:58:14.786596Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:57:45Z`
- `2026-09-15T23:56:23.146761Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:55:45Z`
- `2026-09-15T23:55:34.887041Z` — **FUELINST**: 80 rows; marker `2026-09-15T23:55:00Z`
- `2026-09-15T23:54:31.167862Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:53:45Z`
- `2026-09-15T23:52:13.370303Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:51:45Z`
