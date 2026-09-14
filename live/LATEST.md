# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.0.0`  
Last heartbeat UTC: `2026-09-14T15:19:11.326873Z`  
Current process started UTC: `2026-09-14T15:14:26.232359Z`  
1-second loop polls in this process: **282**  
HTTP/data errors in this process: **0**  

The loop checks for newly published information every second. Heavy interpretation
is event-driven: if the source did not change, it does not manufacture a new signal.

## Watched public Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest interpreted anomalies

- **TSDF** `settlementPeriod` z=-1.59: transmission-demand forecast: settlementPeriod DOWN, value=1, jump=-47, anomaly=1.6σ → demand pressure easing
- **TSDF** `demand` z=3.50: transmission-demand forecast: demand DOWN, value=2.623e+04, jump=-993, anomaly=3.5σ → demand pressure easing
- **TSDF** `demand` z=3.69: transmission-demand forecast: demand DOWN, value=2.722e+04, jump=-1352, anomaly=3.7σ → demand pressure easing
- **TSDF** `demand` z=3.93: transmission-demand forecast: demand DOWN, value=2.858e+04, jump=-843, anomaly=3.9σ → demand pressure easing
- **TSDF** `demand` z=4.10: transmission-demand forecast: demand DOWN, value=2.942e+04, jump=-455, anomaly=4.1σ → demand pressure easing
- **TSDF** `demand` z=4.21: transmission-demand forecast: demand DOWN, value=2.987e+04, jump=-2624, anomaly=4.2σ → demand pressure easing
- **TSDF** `demand` z=4.69: transmission-demand forecast: demand UP, value=3.25e+04, jump=367, anomaly=4.7σ → demand pressure increasing
- **TSDF** `demand` z=4.67: transmission-demand forecast: demand DOWN, value=3.213e+04, jump=-394, anomaly=4.7σ → demand pressure easing
- **TSDF** `demand` z=4.78: transmission-demand forecast: demand DOWN, value=3.252e+04, jump=-106, anomaly=4.8σ → demand pressure easing
- **TSDF** `demand` z=4.84: transmission-demand forecast: demand UP, value=3.263e+04, jump=1502, anomaly=4.8σ → demand pressure increasing
- **TSDF** `demand` z=4.62: transmission-demand forecast: demand UP, value=3.113e+04, jump=970, anomaly=4.6σ → demand pressure increasing
- **TSDF** `demand` z=4.49: transmission-demand forecast: demand UP, value=3.016e+04, jump=2276, anomaly=4.5σ → demand pressure increasing
- **TSDF** `demand` z=4.12: transmission-demand forecast: demand UP, value=2.788e+04, jump=1308, anomaly=4.1σ → demand pressure increasing
- **TSDF** `demand` z=3.91: transmission-demand forecast: demand UP, value=2.657e+04, jump=1605, anomaly=3.9σ → demand pressure increasing
- **TSDF** `demand` z=3.64: transmission-demand forecast: demand UP, value=2.497e+04, jump=991, anomaly=3.6σ → demand pressure increasing
- **TSDF** `demand` z=3.59: transmission-demand forecast: demand DOWN, value=2.435e+04, jump=-51, anomaly=3.6σ → demand pressure easing
- **TSDF** `demand` z=3.62: transmission-demand forecast: demand DOWN, value=2.44e+04, jump=-262, anomaly=3.6σ → demand pressure easing
- **TSDF** `demand` z=3.69: transmission-demand forecast: demand DOWN, value=2.466e+04, jump=-388, anomaly=3.7σ → demand pressure easing
- **TSDF** `demand` z=3.78: transmission-demand forecast: demand DOWN, value=2.505e+04, jump=-629, anomaly=3.8σ → demand pressure easing
- **TSDF** `demand` z=3.92: transmission-demand forecast: demand DOWN, value=2.568e+04, jump=-283, anomaly=3.9σ → demand pressure easing

## Latest publication events

- `2026-09-14T15:18:08.432832Z` — **TSDF**: 1314 rows fetched; publish marker `2026-09-14T15:17:00Z`
- `2026-09-14T15:18:08.432832Z` — **NDF**: 73 rows fetched; publish marker `2026-09-14T15:17:00Z`
- `2026-09-14T15:18:08.432832Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T15:17:45Z`
- `2026-09-14T15:16:16.248148Z` — **FREQ**: 5761 rows fetched; publish marker `2026-09-14T15:15:45Z`
- `2026-09-14T15:16:01.246059Z` — **FUELINST**: 80 rows fetched; publish marker `2026-09-14T15:15:00Z`
