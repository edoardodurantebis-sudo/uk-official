# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.0.0`  
Last heartbeat UTC: `2026-09-14T17:10:56.592630Z`  
Current process started UTC: `2026-09-14T17:06:12.070840Z`  
1-second loop polls in this process: **283**  
HTTP/data errors in this process: **0**  

The loop checks for newly published information every second. Heavy interpretation
is event-driven: if the source did not change, it does not manufacture a new signal.

## Watched public Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest interpreted anomalies

- **FUELINST** `generation` z=2.86: instantaneous generation mix: generation UP, value=1.002e+04, jump=9036, anomaly=2.9σ → generation-mix shift
- **FUELINST** `generation` z=-0.48: instantaneous generation mix: generation DOWN, value=0, jump=-1.043e+04, anomaly=0.5σ → generation-mix shift
- **FUELINST** `generation` z=2.98: instantaneous generation mix: generation UP, value=1.043e+04, jump=7848, anomaly=3.0σ → generation-mix shift
- **FUELINST** `generation` z=0.38: instantaneous generation mix: generation DOWN, value=2582, jump=-7542, anomaly=0.4σ → generation-mix shift
- **FUELINST** `generation` z=2.90: instantaneous generation mix: generation UP, value=1.012e+04, jump=9144, anomaly=2.9σ → generation-mix shift
- **FUELINST** `generation` z=-0.48: instantaneous generation mix: generation DOWN, value=0, jump=-1.068e+04, anomaly=0.5σ → generation-mix shift
- **FUELINST** `generation` z=3.07: instantaneous generation mix: generation UP, value=1.068e+04, jump=8091, anomaly=3.1σ → generation-mix shift
- **FUELINST** `generation` z=0.38: instantaneous generation mix: generation DOWN, value=2586, jump=-7571, anomaly=0.4σ → generation-mix shift
- **FUELINST** `generation` z=2.92: instantaneous generation mix: generation UP, value=1.016e+04, jump=9177, anomaly=2.9σ → generation-mix shift
- **FUELINST** `generation` z=-0.48: instantaneous generation mix: generation DOWN, value=0, jump=-1.108e+04, anomaly=0.5σ → generation-mix shift
- **FUELINST** `generation` z=3.21: instantaneous generation mix: generation UP, value=1.108e+04, jump=8495, anomaly=3.2σ → generation-mix shift
- **FUELINST** `generation` z=0.38: instantaneous generation mix: generation DOWN, value=2584, jump=-7608, anomaly=0.4σ → generation-mix shift
- **FUELINST** `generation` z=2.94: instantaneous generation mix: generation UP, value=1.019e+04, jump=9212, anomaly=2.9σ → generation-mix shift
- **FUELINST** `generation` z=-0.49: instantaneous generation mix: generation DOWN, value=0, jump=-1.138e+04, anomaly=0.5σ → generation-mix shift
- **FUELINST** `generation` z=3.32: instantaneous generation mix: generation UP, value=1.138e+04, jump=8793, anomaly=3.3σ → generation-mix shift
- **FUELINST** `generation` z=2.87: instantaneous generation mix: generation UP, value=9952, jump=8972, anomaly=2.9σ → generation-mix shift
- **FUELINST** `generation` z=-0.49: instantaneous generation mix: generation DOWN, value=0, jump=-1.02e+04, anomaly=0.5σ → generation-mix shift
- **FUELINST** `generation` z=2.93: instantaneous generation mix: generation UP, value=1.02e+04, jump=7617, anomaly=2.9σ → generation-mix shift
- **FUELINST** `generation` z=2.90: instantaneous generation mix: generation UP, value=1.002e+04, jump=9036, anomaly=2.9σ → generation-mix shift
- **FUELINST** `generation` z=-0.49: instantaneous generation mix: generation DOWN, value=0, jump=-1.043e+04, anomaly=0.5σ → generation-mix shift

## Latest publication events

- `2026-09-14T17:10:27.267887Z` — **FUELINST**: 80 rows fetched; publish marker `2026-09-14T17:10:00Z`
- `2026-09-14T17:10:11.807046Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T17:09:45Z`
- `2026-09-14T17:08:20.204907Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T17:07:45Z`
- `2026-09-14T17:06:12.070851Z` — **MID**: 0 rows fetched; publish marker `2026-09-14T17:05:00Z`
- `2026-09-14T17:06:12.070851Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T17:05:45Z`
- `2026-09-14T17:05:29.654486Z` — **FUELINST**: 80 rows fetched; publish marker `2026-09-14T17:05:00Z`
- `2026-09-14T17:04:09.407851Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T17:03:45Z`
- `2026-09-14T17:02:16.427376Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T17:01:45Z`
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
