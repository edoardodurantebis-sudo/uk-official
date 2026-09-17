# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T11:56:11.140344Z`  
Current process started UTC: `2026-09-17T11:52:10.378691Z`  
1-second metadata polls in this process: **144**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=1, z=4.42 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=49, delta=49, z=4.48 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-622** (n=725, 2026-09-17T11:55:24.234300Z)
- `FUELINST|fuelType=NPSHYD|generation` = **270** (n=725, 2026-09-17T11:55:24.234300Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3313** (n=725, 2026-09-17T11:55:24.234300Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=725, 2026-09-17T11:55:24.234300Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=725, 2026-09-17T11:55:24.234300Z)
- `FUELINST|fuelType=OTHER|generation` = **786** (n=725, 2026-09-17T11:55:24.234300Z)
- `FUELINST|fuelType=PS|generation` = **-939** (n=725, 2026-09-17T11:55:24.234300Z)
- `FUELINST|fuelType=WIND|generation` = **14904** (n=725, 2026-09-17T11:55:24.234300Z)
- `IMBALNGC|TOTAL|imbalance` = **11963** (n=120, 2026-09-17T11:53:31.798888Z)
- `INDDEM|TOTAL|demand` = **-11265** (n=120, 2026-09-17T11:53:31.798888Z)
- `INDGEN|TOTAL|generation` = **28506** (n=120, 2026-09-17T11:53:31.798888Z)
- `MELNGC|TOTAL|margin` = **36723** (n=120, 2026-09-17T11:50:23.103050Z)
- `NDF|TOTAL|demand` = **16043** (n=123, 2026-09-17T11:48:45.810334Z)
- `TSDF|TOTAL|demand` = **16543** (n=123, 2026-09-17T11:48:29.902929Z)
- `WINDFOR|TOTAL|generation` = **19032** (n=21, 2026-09-17T10:30:44.687451Z)

## Latest publication events

- `2026-09-17T11:56:09.583848Z` — **MID**: 0 rows; marker `2026-09-17T11:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:56:08.022383Z` — **MID**: 0 rows; marker `2026-09-17T11:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:56:06.431815Z` — **MID**: 0 rows; marker `2026-09-17T11:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:56:04.793294Z` — **MID**: 0 rows; marker `2026-09-17T11:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:56:03.163744Z` — **MID**: 0 rows; marker `2026-09-17T11:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:56:01.587164Z` — **MID**: 0 rows; marker `2026-09-17T11:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:55:59.941985Z` — **MID**: 0 rows; marker `2026-09-17T11:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:55:58.065926Z` — **MID**: 0 rows; marker `2026-09-17T11:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:55:56.480939Z` — **MID**: 0 rows; marker `2026-09-17T11:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:55:54.811561Z` — **MID**: 0 rows; marker `2026-09-17T11:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:55:53.271566Z` — **MID**: 0 rows; marker `2026-09-17T11:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:55:51.703268Z` — **MID**: 0 rows; marker `2026-09-17T11:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:55:50.152694Z` — **MID**: 0 rows; marker `2026-09-17T11:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:55:48.544855Z` — **MID**: 0 rows; marker `2026-09-17T11:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:55:46.931683Z` — **MID**: 0 rows; marker `2026-09-17T11:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
