# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T00:21:07.276189Z`  
Memory snapshots: **686**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=-657.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=657.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6588 d1=2.0 d12=-846.0 z=-5.128208150773196
- **CHANGE_POINT** `ccgt_gen` value=4529 d1=-4.0 d12=-1030.0 z=-3.5533906349885847
- **CHANGE_POINT** `thermal_base` value=7844 d1=1.0 d12=-1026.0 z=-3.5376142354783595
- **REVERSAL** `interconnector_net` value=-6588 d1=2.0 d12=-846.0 z=-5.128208150773196
- **ROBUST_OUTLIER** `interconnector_net` value=-6588 d1=2.0 d12=-846.0 z=-5.128208150773196
- **PERSISTENT_DOWN** `ccgt_gen` value=4529 d1=-4.0 d12=-1030.0 z=-3.5533906349885847
- **ROBUST_OUTLIER** `ccgt_gen` value=4529 d1=-4.0 d12=-1030.0 z=-3.5533906349885847
- **REVERSAL** `thermal_base` value=7844 d1=1.0 d12=-1026.0 z=-3.5376142354783595
- **ROBUST_OUTLIER** `thermal_base` value=7844 d1=1.0 d12=-1026.0 z=-3.5376142354783595
- **CHANGE_POINT** `ps_gen` value=-246 d1=-2.0 d12=4.0 z=-0.8168964150671785
- **CHANGE_POINT** `imbalance` value=6451 d1=0.0 d12=-152.0 z=-0.626622735483871
- **CHANGE_POINT** `ind_generation` value=2.557e+04 d1=0.0 d12=-152.0 z=-0.18177737943262412
- **ACCELERATION** `nuclear_gen` value=3315 d1=5.0 d12=4.0 z=1.3489795

## Nearest historical live analogues

- `2026-09-16T14:21:30.462993Z` distance=0.247 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:25:41.401432Z` distance=0.249 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:29:54.321922Z` distance=0.249 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:34:06.314775Z` distance=0.249 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:38:16.233128Z` distance=0.249 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
