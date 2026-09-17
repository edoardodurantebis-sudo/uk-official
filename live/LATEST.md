# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T08:58:54.571787Z`  
Current process started UTC: `2026-09-17T08:54:53.612000Z`  
1-second metadata polls in this process: **147**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16658, delta=-2713, z=-4.41 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16158, delta=-2463, z=-4.57 -> demand pressure easing
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=2, delta=-50, z=-0.16 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=-4, z=3.91 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.36 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=1, z=4.42 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=49, delta=49, z=4.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=3, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=1, z=4.21 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=0, z=4.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=0, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=17, z=4.30 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-1134, delta=10, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1114, delta=62, z=-3.54 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1332** (n=689, 2026-09-17T08:55:43.309151Z)
- `FUELINST|fuelType=NPSHYD|generation` = **419** (n=689, 2026-09-17T08:55:43.309151Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3316** (n=689, 2026-09-17T08:55:43.309151Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=689, 2026-09-17T08:55:43.309151Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=689, 2026-09-17T08:55:43.309151Z)
- `FUELINST|fuelType=OTHER|generation` = **307** (n=689, 2026-09-17T08:55:43.309151Z)
- `FUELINST|fuelType=PS|generation` = **-723** (n=689, 2026-09-17T08:55:43.309151Z)
- `FUELINST|fuelType=WIND|generation` = **15526** (n=689, 2026-09-17T08:55:43.309151Z)
- `IMBALNGC|TOTAL|imbalance` = **7441** (n=114, 2026-09-17T08:49:36.456573Z)
- `INDDEM|TOTAL|demand` = **-12127** (n=114, 2026-09-17T08:49:19.589745Z)
- `INDGEN|TOTAL|generation` = **26447** (n=114, 2026-09-17T08:49:36.456573Z)
- `MELNGC|TOTAL|margin` = **36058** (n=114, 2026-09-17T08:49:03.558387Z)
- `NDF|TOTAL|demand` = **18256** (n=117, 2026-09-17T08:46:53.329886Z)
- `TSDF|TOTAL|demand` = **19006** (n=117, 2026-09-17T08:46:53.329886Z)
- `WINDFOR|TOTAL|generation` = **19255** (n=20, 2026-09-17T08:30:43.563030Z)

## Latest publication events

- `2026-09-17T08:58:52.741985Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:58:51.183818Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:58:49.565309Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:58:47.993861Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:58:46.457881Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:58:44.902777Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:58:43.334127Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:58:41.355834Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:58:39.789759Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:58:38.200638Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:58:36.633069Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:58:35.062680Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:58:33.467040Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:58:31.890489Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:58:30.300517Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
