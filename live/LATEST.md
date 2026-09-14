# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.0.0`  
Last heartbeat UTC: `2026-09-14T17:00:54.907523Z`  
Current process started UTC: `2026-09-14T16:56:08.879229Z`  
1-second loop polls in this process: **280**  
HTTP/data errors in this process: **0**  

The loop checks for newly published information every second. Heavy interpretation
is event-driven: if the source did not change, it does not manufacture a new signal.

## Watched public Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest interpreted anomalies

- **FUELHH** `generation` z=3.17: half-hour generation mix: generation UP, value=1.002e+04, jump=9061, anomaly=3.2σ → generation-mix shift
- **FUELHH** `generation` z=-0.54: half-hour generation mix: generation DOWN, value=0, jump=-1.026e+04, anomaly=0.5σ → generation-mix shift
- **FUELHH** `settlementPeriod` z=4.36: half-hour generation mix: settlementPeriod FLAT, value=36, jump=0, anomaly=4.4σ → generation-mix shift
- **FUELHH** `settlementPeriod` z=NA: half-hour generation mix: settlementPeriod UP, value=36, jump=1, anomaly=new baseline → generation-mix shift
- **FUELINST** `generation` z=2.91: instantaneous generation mix: generation UP, value=9968, jump=8987, anomaly=2.9σ → generation-mix shift
- **FUELINST** `generation` z=-0.49: instantaneous generation mix: generation DOWN, value=0, jump=-1.008e+04, anomaly=0.5σ → generation-mix shift
- **FUELINST** `generation` z=2.92: instantaneous generation mix: generation UP, value=1.008e+04, jump=7495, anomaly=2.9σ → generation-mix shift
- **FUELINST** `generation` z=2.91: instantaneous generation mix: generation UP, value=9952, jump=8972, anomaly=2.9σ → generation-mix shift
- **FUELINST** `generation` z=-0.49: instantaneous generation mix: generation DOWN, value=0, jump=-1.02e+04, anomaly=0.5σ → generation-mix shift
- **FUELINST** `generation` z=2.97: instantaneous generation mix: generation UP, value=1.02e+04, jump=7617, anomaly=3.0σ → generation-mix shift
- **FUELINST** `generation` z=0.39: instantaneous generation mix: generation DOWN, value=2583, jump=-7432, anomaly=0.4σ → generation-mix shift
- **FUELINST** `generation` z=2.94: instantaneous generation mix: generation UP, value=1.002e+04, jump=9036, anomaly=2.9σ → generation-mix shift
- **FUELINST** `generation` z=-0.49: instantaneous generation mix: generation DOWN, value=0, jump=-1.043e+04, anomaly=0.5σ → generation-mix shift
- **FUELINST** `generation` z=3.06: instantaneous generation mix: generation UP, value=1.043e+04, jump=7848, anomaly=3.1σ → generation-mix shift
- **FUELINST** `generation` z=0.39: instantaneous generation mix: generation DOWN, value=2582, jump=-7542, anomaly=0.4σ → generation-mix shift
- **FUELINST** `generation` z=2.99: instantaneous generation mix: generation UP, value=1.012e+04, jump=9144, anomaly=3.0σ → generation-mix shift
- **FUELINST** `generation` z=-0.49: instantaneous generation mix: generation DOWN, value=0, jump=-1.068e+04, anomaly=0.5σ → generation-mix shift
- **FUELINST** `generation` z=3.16: instantaneous generation mix: generation UP, value=1.068e+04, jump=8091, anomaly=3.2σ → generation-mix shift
- **FUELINST** `generation` z=0.40: instantaneous generation mix: generation DOWN, value=2586, jump=-7401, anomaly=0.4σ → generation-mix shift
- **FUELINST** `generation` z=2.96: instantaneous generation mix: generation UP, value=9987, jump=9007, anomaly=3.0σ → generation-mix shift

## Latest publication events

- `2026-09-14T17:00:38.243007Z` — **FUELHH**: 20 rows fetched; publish marker `2026-09-14T17:00:00Z`
- `2026-09-14T17:00:22.473103Z` — **FUELINST**: 80 rows fetched; publish marker `2026-09-14T17:00:00Z`
- `2026-09-14T17:00:06.483011Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T16:59:45Z`
- `2026-09-14T16:58:15.043846Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T16:57:45Z`
- `2026-09-14T16:56:24.945856Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T16:55:45Z`
- `2026-09-14T16:55:34.415100Z` — **FUELINST**: 80 rows fetched; publish marker `2026-09-14T16:55:00Z`
- `2026-09-14T16:54:30.451677Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T16:53:45Z`
- `2026-09-14T16:53:26.720646Z` — **INDGEN**: 1260 rows fetched; publish marker `2026-09-14T16:47:00Z`
- `2026-09-14T16:53:26.720646Z` — **INDDEM**: 1260 rows fetched; publish marker `2026-09-14T16:47:00Z`
- `2026-09-14T16:53:26.720646Z` — **IMBALNGC**: 1260 rows fetched; publish marker `2026-09-14T16:48:00Z`
- `2026-09-14T16:52:22.704577Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T16:51:45Z`
- `2026-09-14T16:50:32.279961Z` — **MELNGC**: 1260 rows fetched; publish marker `2026-09-14T16:48:00Z`
- `2026-09-14T16:50:32.279961Z` — **FUELINST**: 80 rows fetched; publish marker `2026-09-14T16:50:00Z`
- `2026-09-14T16:50:16.554128Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T16:49:45Z`
- `2026-09-14T16:48:24.791306Z` — **TSDF**: 1260 rows fetched; publish marker `2026-09-14T16:48:00Z`
- `2026-09-14T16:48:24.791306Z` — **NDF**: 70 rows fetched; publish marker `2026-09-14T16:48:00Z`
- `2026-09-14T16:48:09.330478Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T16:47:45Z`
- `2026-09-14T16:46:17.430095Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T16:45:45Z`
- `2026-09-14T16:46:01.725236Z` — **MID**: 0 rows fetched; publish marker `2026-09-14T16:42:04Z`
- `2026-09-14T16:46:01.725236Z` — **MELNGC**: 0 rows fetched; publish marker `2026-09-14T16:17:00Z`
