# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.0.0`  
Last heartbeat UTC: `2026-09-14T16:55:47.259099Z`  
Current process started UTC: `2026-09-14T16:51:02.387329Z`  
1-second loop polls in this process: **280**  
HTTP/data errors in this process: **0**  

The loop checks for newly published information every second. Heavy interpretation
is event-driven: if the source did not change, it does not manufacture a new signal.

## Watched public Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest interpreted anomalies

- **FUELINST** `generation` z=2.96: instantaneous generation mix: generation UP, value=9987, jump=9007, anomaly=3.0σ → generation-mix shift
- **FUELINST** `generation` z=-0.49: instantaneous generation mix: generation DOWN, value=0, jump=-1.004e+04, anomaly=0.5σ → generation-mix shift
- **FUELINST** `generation` z=2.95: instantaneous generation mix: generation UP, value=1.004e+04, jump=7457, anomaly=2.9σ → generation-mix shift
- **FUELINST** `generation` z=0.40: instantaneous generation mix: generation DOWN, value=2586, jump=-7382, anomaly=0.4σ → generation-mix shift
- **FUELINST** `generation` z=2.97: instantaneous generation mix: generation UP, value=9968, jump=8987, anomaly=3.0σ → generation-mix shift
- **FUELINST** `generation` z=-0.49: instantaneous generation mix: generation DOWN, value=0, jump=-1.008e+04, anomaly=0.5σ → generation-mix shift
- **FUELINST** `generation` z=2.97: instantaneous generation mix: generation UP, value=1.008e+04, jump=7495, anomaly=3.0σ → generation-mix shift
- **FUELINST** `generation` z=0.40: instantaneous generation mix: generation DOWN, value=2585, jump=-7367, anomaly=0.4σ → generation-mix shift
- **FUELINST** `generation` z=2.97: instantaneous generation mix: generation UP, value=9952, jump=8972, anomaly=3.0σ → generation-mix shift
- **FUELINST** `generation` z=-0.49: instantaneous generation mix: generation DOWN, value=0, jump=-1.02e+04, anomaly=0.5σ → generation-mix shift
- **FUELINST** `generation` z=3.02: instantaneous generation mix: generation UP, value=1.02e+04, jump=7617, anomaly=3.0σ → generation-mix shift
- **FUELINST** `generation` z=0.40: instantaneous generation mix: generation DOWN, value=2583, jump=-7432, anomaly=0.4σ → generation-mix shift
- **FUELINST** `generation` z=3.01: instantaneous generation mix: generation UP, value=1.002e+04, jump=9036, anomaly=3.0σ → generation-mix shift
- **FUELINST** `generation` z=-0.49: instantaneous generation mix: generation DOWN, value=0, jump=-1.043e+04, anomaly=0.5σ → generation-mix shift
- **FUELINST** `generation` z=3.12: instantaneous generation mix: generation UP, value=1.043e+04, jump=7848, anomaly=3.1σ → generation-mix shift
- **FUELINST** `generation` z=0.41: instantaneous generation mix: generation DOWN, value=2582, jump=-7474, anomaly=0.4σ → generation-mix shift
- **INDGEN** `settlementPeriod` z=-1.55: indicated generation: settlementPeriod DOWN, value=1, jump=-47, anomaly=1.5σ → state change
- **INDGEN** `settlementPeriod` z=-1.54: indicated generation: settlementPeriod DOWN, value=1, jump=-47, anomaly=1.5σ → state change
- **INDGEN** `generation` z=3.61: indicated generation: generation DOWN, value=3.117e+04, jump=-880, anomaly=3.6σ → state change
- **INDGEN** `generation` z=3.76: indicated generation: generation DOWN, value=3.205e+04, jump=-575, anomaly=3.8σ → state change

## Latest publication events

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
- `2026-09-14T16:46:01.725236Z` — **INDGEN**: 0 rows fetched; publish marker `2026-09-14T16:17:00Z`
- `2026-09-14T16:46:01.725236Z` — **INDDEM**: 0 rows fetched; publish marker `2026-09-14T16:17:00Z`
- `2026-09-14T16:46:01.725236Z` — **IMBALNGC**: 0 rows fetched; publish marker `2026-09-14T16:17:00Z`
- `2026-09-14T16:46:01.725236Z` — **TSDF**: 0 rows fetched; publish marker `2026-09-14T16:17:00Z`
- `2026-09-14T16:46:01.725236Z` — **NDF**: 0 rows fetched; publish marker `2026-09-14T16:17:00Z`
