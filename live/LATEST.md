# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T12:27:33.511044Z`  
Current process started UTC: `2026-09-21T12:23:34.101186Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3513, delta=-3, z=4.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3516, delta=0, z=4.88 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3516, delta=3, z=4.91 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3513, delta=4, z=4.86 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=0, z=4.79 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3512, delta=-3, z=5.00 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3509, delta=3, z=4.82 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3506, delta=-6, z=4.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3512, delta=-1, z=4.97 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3513, delta=-4, z=5.03 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3517, delta=2, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3515, delta=0, z=5.16 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3515, delta=13, z=5.33 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3515, delta=-3, z=5.20 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3518, delta=2, z=5.33 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1836, 2026-09-21T12:25:26.190128Z)
- `FUELINST|fuelType=OTHER|generation` = **664** (n=1836, 2026-09-21T12:25:26.190128Z)
- `FUELINST|fuelType=PS|generation` = **228** (n=1836, 2026-09-21T12:25:26.190128Z)
- `FUELINST|fuelType=WIND|generation` = **3883** (n=1836, 2026-09-21T12:25:26.190128Z)
- `IMBALNGC|TOTAL|imbalance` = **-3333** (n=302, 2026-09-21T12:23:51.221953Z)
- `INDDEM|TOTAL|demand` = **-12237** (n=302, 2026-09-21T12:23:35.101349Z)
- `INDGEN|TOTAL|generation` = **18171** (n=302, 2026-09-21T12:23:35.101349Z)
- `MELNGC|TOTAL|margin` = **36677** (n=302, 2026-09-21T12:20:39.601841Z)
- `MID|dataProvider=APXMIDP|price` = **161.96** (n=42, 2026-09-21T12:12:17.180493Z)
- `MID|dataProvider=APXMIDP|volume` = **3282.3** (n=42, 2026-09-21T12:12:17.180493Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=82, 2026-09-21T12:12:17.180493Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=82, 2026-09-21T12:12:17.180493Z)
- `NDF|TOTAL|demand` = **21004** (n=309, 2026-09-21T12:18:19.589290Z)
- `TSDF|TOTAL|demand` = **21504** (n=309, 2026-09-21T12:18:51.982318Z)
- `WINDFOR|TOTAL|generation` = **8923** (n=52, 2026-09-21T10:30:49.343841Z)

## Latest publication events

- `2026-09-21T12:26:14.600225Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:25:45Z`
- `2026-09-21T12:25:26.190128Z` — **FUELINST**: 80 rows; marker `2026-09-21T12:25:00Z`
- `2026-09-21T12:24:06.600542Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:23:45Z`
- `2026-09-21T12:23:51.221953Z` — **IMBALNGC**: 1422 rows; marker `2026-09-21T12:18:00Z`
- `2026-09-21T12:23:35.101349Z` — **INDGEN**: 1422 rows; marker `2026-09-21T12:18:00Z`
- `2026-09-21T12:23:35.101349Z` — **INDDEM**: 1422 rows; marker `2026-09-21T12:18:00Z`
- `2026-09-21T12:22:15.411047Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:21:45Z`
- `2026-09-21T12:20:39.601841Z` — **MELNGC**: 1422 rows; marker `2026-09-21T12:18:00Z`
- `2026-09-21T12:20:39.601841Z` — **FUELINST**: 80 rows; marker `2026-09-21T12:20:00Z`
- `2026-09-21T12:20:07.617109Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:19:45Z`
- `2026-09-21T12:18:51.982318Z` — **TSDF**: 1422 rows; marker `2026-09-21T12:18:00Z`
- `2026-09-21T12:18:19.589290Z` — **NDF**: 79 rows; marker `2026-09-21T12:18:00Z`
- `2026-09-21T12:18:19.589290Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:17:45Z`
- `2026-09-21T12:16:10.530061Z` — **FREQ**: 5761 rows; marker `2026-09-21T12:15:45Z`
- `2026-09-21T12:15:22.461218Z` — **FUELINST**: 80 rows; marker `2026-09-21T12:15:00Z`
