# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T00:46:15.772022Z`  
Memory snapshots: **692**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6592 d1=-25.0 d12=-141.0 z=-5.0210424051697995
- **CHANGE_POINT** `ccgt_gen` value=4444 d1=-129.0 d12=-807.0 z=-3.6188376997716896
- **CHANGE_POINT** `thermal_base` value=7762 d1=-134.0 d12=-801.0 z=-3.6006075834282463
- **PERSISTENT_DOWN** `interconnector_net` value=-6592 d1=-25.0 d12=-141.0 z=-5.0210424051697995
- **ROBUST_OUTLIER** `interconnector_net` value=-6592 d1=-25.0 d12=-141.0 z=-5.0210424051697995
- **CHANGE_POINT** `margin` value=3.451e+04 d1=0.0 d12=0.0 z=1.6287678407407407
- **PERSISTENT_DOWN** `ccgt_gen` value=4444 d1=-129.0 d12=-807.0 z=-3.6188376997716896
- **ROBUST_OUTLIER** `ccgt_gen` value=4444 d1=-129.0 d12=-807.0 z=-3.6188376997716896
- **PERSISTENT_DOWN** `thermal_base` value=7762 d1=-134.0 d12=-801.0 z=-3.6006075834282463
- **ROBUST_OUTLIER** `thermal_base` value=7762 d1=-134.0 d12=-801.0 z=-3.6006075834282463
- **CHANGE_POINT** `ps_gen` value=-244 d1=3.0 d12=6.0 z=-0.7106433044388609
- **REVERSAL** `nuclear_gen` value=3318 d1=-5.0 d12=6.0 z=2.02346925
- **ACCELERATION** `nuclear_gen` value=3318 d1=-5.0 d12=6.0 z=2.02346925

## Nearest historical live analogues

- `2026-09-16T23:51:11.579176Z` distance=0.041 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:33:53.959539Z` distance=0.043 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:38:04.318669Z` distance=0.043 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:42:15.181563Z` distance=0.043 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:47:00.820172Z` distance=0.043 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
