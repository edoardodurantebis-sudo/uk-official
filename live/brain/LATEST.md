# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T00:42:04.078560Z`  
Memory snapshots: **691**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6567 d1=-13.0 d12=-116.0 z=-5.0167475947543965
- **CHANGE_POINT** `ccgt_gen` value=4573 d1=-54.0 d12=-678.0 z=-3.519512154394977
- **CHANGE_POINT** `thermal_base` value=7896 d1=-47.0 d12=-667.0 z=-3.4976672343394077
- **ROBUST_OUTLIER** `interconnector_net` value=-6567 d1=-13.0 d12=-116.0 z=-5.0167475947543965
- **CHANGE_POINT** `margin` value=3.451e+04 d1=0.0 d12=0.0 z=1.6287678407407407
- **PERSISTENT_DOWN** `ccgt_gen` value=4573 d1=-54.0 d12=-678.0 z=-3.519512154394977
- **ROBUST_OUTLIER** `ccgt_gen` value=4573 d1=-54.0 d12=-678.0 z=-3.519512154394977
- **PERSISTENT_DOWN** `thermal_base` value=7896 d1=-47.0 d12=-667.0 z=-3.4976672343394077
- **ROBUST_OUTLIER** `thermal_base` value=7896 d1=-47.0 d12=-667.0 z=-3.4976672343394077
- **PERSISTENT_UP** `nuclear_gen` value=3323 d1=7.0 d12=11.0 z=2.7943146785714283
- **CHANGE_POINT** `ps_gen` value=-247 d1=4.0 d12=3.0 z=-0.7200633817567568
- **CHANGE_POINT** `ind_generation` value=2.562e+04 d1=0.0 d12=-107.0 z=0.27836084920634924
- **REVERSAL** `wind_gen` value=1.23e+04 d1=-67.0 d12=687.0 z=1.4687182209103842

## Nearest historical live analogues

- `2026-09-16T23:33:53.959539Z` distance=0.043 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:38:04.318669Z` distance=0.043 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:42:15.181563Z` distance=0.043 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:47:00.820172Z` distance=0.043 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:21:30.462993Z` distance=0.248 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
