# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.0.0`  
Last heartbeat UTC: `2026-09-14T16:50:46.570760Z`  
Current process started UTC: `2026-09-14T16:46:01.725225Z`  
1-second loop polls in this process: **277**  
HTTP/data errors in this process: **0**  

The loop checks for newly published information every second. Heavy interpretation
is event-driven: if the source did not change, it does not manufacture a new signal.

## Watched public Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest interpreted anomalies

- **MELNGC** `settlementPeriod` z=-1.55: indicated margin: settlementPeriod DOWN, value=1, jump=-47, anomaly=1.5σ → system tightness increasing
- **MELNGC** `margin` z=3.57: indicated margin: margin UP, value=3.299e+04, jump=259, anomaly=3.6σ → margin improving
- **MELNGC** `margin` z=3.56: indicated margin: margin DOWN, value=3.273e+04, jump=-412, anomaly=3.6σ → system tightness increasing
- **MELNGC** `margin` z=3.63: indicated margin: margin UP, value=3.314e+04, jump=1267, anomaly=3.6σ → margin improving
- **MELNGC** `margin` z=3.51: indicated margin: margin UP, value=3.188e+04, jump=1442, anomaly=3.5σ → margin improving
- **MELNGC** `margin` z=3.65: indicated margin: margin DOWN, value=3.157e+04, jump=-1268, anomaly=3.6σ → system tightness increasing
- **MELNGC** `margin` z=3.81: indicated margin: margin DOWN, value=3.284e+04, jump=-2461, anomaly=3.8σ → system tightness increasing
- **MELNGC** `margin` z=4.11: indicated margin: margin DOWN, value=3.53e+04, jump=-964, anomaly=4.1σ → system tightness increasing
- **MELNGC** `margin` z=4.25: indicated margin: margin DOWN, value=3.626e+04, jump=-1816, anomaly=4.3σ → system tightness increasing
- **MELNGC** `margin` z=4.49: indicated margin: margin UP, value=3.808e+04, jump=552, anomaly=4.5σ → margin improving
- **MELNGC** `margin` z=4.47: indicated margin: margin DOWN, value=3.753e+04, jump=-430, anomaly=4.5σ → system tightness increasing
- **MELNGC** `margin` z=4.56: indicated margin: margin UP, value=3.796e+04, jump=338, anomaly=4.6σ → margin improving
- **MELNGC** `margin` z=4.56: indicated margin: margin UP, value=3.762e+04, jump=371, anomaly=4.6σ → margin improving
- **MELNGC** `margin` z=4.56: indicated margin: margin UP, value=3.725e+04, jump=641, anomaly=4.6σ → margin improving
- **MELNGC** `margin` z=4.52: indicated margin: margin UP, value=3.661e+04, jump=425, anomaly=4.5σ → margin improving
- **MELNGC** `margin` z=4.51: indicated margin: margin UP, value=3.618e+04, jump=622, anomaly=4.5σ → margin improving
- **MELNGC** `margin` z=4.47: indicated margin: margin UP, value=3.556e+04, jump=731, anomaly=4.5σ → margin improving
- **MELNGC** `margin` z=4.42: indicated margin: margin UP, value=3.483e+04, jump=118, anomaly=4.4σ → margin improving
- **MELNGC** `margin` z=4.45: indicated margin: margin UP, value=3.471e+04, jump=710, anomaly=4.4σ → margin improving
- **MELNGC** `margin` z=4.40: indicated margin: margin UP, value=3.4e+04, jump=642, anomaly=4.4σ → margin improving

## Latest publication events

- `2026-09-14T16:50:32.279961Z` — **MELNGC**: 1260 rows fetched; publish marker `2026-09-14T16:48:00Z`
- `2026-09-14T16:50:32.279961Z` — **FUELINST**: 80 rows fetched; publish marker `2026-09-14T16:50:00Z`
- `2026-09-14T16:50:16.554128Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T16:49:45Z`
- `2026-09-14T16:48:24.791306Z` — **TSDF**: 1260 rows fetched; publish marker `2026-09-14T16:48:00Z`
- `2026-09-14T16:48:24.791306Z` — **NDF**: 70 rows fetched; publish marker `2026-09-14T16:48:00Z`
- `2026-09-14T16:48:09.330478Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T16:47:45Z`
- `2026-09-14T16:46:17.430095Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T16:45:45Z`
- `2026-09-14T16:46:01.725236Z` — **MID**: 0 rows fetched; publish marker `2026-09-14T16:42:04Z`
- `2026-09-14T16:46:01.725236Z` — **MELNGC**: 0 rows fetched; publish marker `2026-09-14T16:17:00Z`
- `2026-09-14T16:46:01.725236Z` — **INDGEN**: 0 rows fetched; publish marker `2026-09-14T16:17:00Z`
- `2026-09-14T16:46:01.725236Z` — **INDDEM**: 0 rows fetched; publish marker `2026-09-14T16:17:00Z`
- `2026-09-14T16:46:01.725236Z` — **IMBALNGC**: 0 rows fetched; publish marker `2026-09-14T16:17:00Z`
- `2026-09-14T16:46:01.725236Z` — **TSDF**: 0 rows fetched; publish marker `2026-09-14T16:17:00Z`
- `2026-09-14T16:46:01.725236Z` — **NDF**: 0 rows fetched; publish marker `2026-09-14T16:17:00Z`
- `2026-09-14T16:46:01.725236Z` — **WINDFOR**: 73 rows fetched; publish marker `2026-09-14T16:30:00Z`
- `2026-09-14T16:46:01.725236Z` — **FUELHH**: 20 rows fetched; publish marker `2026-09-14T16:30:00Z`
- `2026-09-14T16:46:01.725236Z` — **FUELINST**: 80 rows fetched; publish marker `2026-09-14T16:45:00Z`
- `2026-09-14T16:46:01.725236Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T16:43:45Z`
- `2026-09-14T15:18:08.432832Z` — **TSDF**: 1314 rows fetched; publish marker `2026-09-14T15:17:00Z`
- `2026-09-14T15:18:08.432832Z` — **NDF**: 73 rows fetched; publish marker `2026-09-14T15:17:00Z`
