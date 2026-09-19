# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T13:18:17.293407Z`  
Memory snapshots: **1499**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `ind_generation` value=1.679e+04 d1=0.0 d12=30.0 z=-32.61569215487805
- **CHANGE_POINT** `imbalance` value=-3220 d1=0.0 d12=30.0 z=-6.041823017318664
- **ROBUST_OUTLIER** `imbalance` value=-3220 d1=0.0 d12=30.0 z=-6.041823017318664
- **CHANGE_POINT** `wind_gen` value=1.502e+04 d1=-6.0 d12=-275.0 z=-3.018285235785953
- **CHANGE_POINT** `residual_proxy` value=1.285e+04 d1=0.0 d12=1.0 z=2.954730270344828
- **ROBUST_OUTLIER** `demand_forecast` value=1.951e+04 d1=0.0 d12=0.0 z=3.2718281479508198
- **CHANGE_POINT** `interconnector_net` value=-2595 d1=22.0 d12=-1015.0 z=-1.1608724541702866
- **PERSISTENT_DOWN** `wind_gen` value=1.502e+04 d1=-6.0 d12=-275.0 z=-3.018285235785953
- **ROBUST_OUTLIER** `wind_gen` value=1.502e+04 d1=-6.0 d12=-275.0 z=-3.018285235785953
- **CHANGE_POINT** `thermal_base` value=6498 d1=25.0 d12=229.0 z=0.1951353993710692
- **CHANGE_POINT** `ccgt_gen` value=3166 d1=17.0 d12=225.0 z=0.1633857158385093
- **CHANGE_POINT** `margin` value=3.676e+04 d1=0.0 d12=0.0 z=0.0
- **REVERSAL** `interconnector_net` value=-2595 d1=22.0 d12=-1015.0 z=-1.1608724541702866
- **ACCELERATION** `biomass_gen` value=476 d1=0.0 d12=-1.0 z=-0.40469384999999997
- **PERSISTENT_UP** `thermal_base` value=6498 d1=25.0 d12=229.0 z=0.1951353993710692

## Nearest historical live analogues

- `2026-09-19T12:23:39.094440Z` distance=0.085 → {'next30m_imbalance_delta': 10.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1.0}
- `2026-09-19T11:54:18.195696Z` distance=0.085 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:58:27.853052Z` distance=0.085 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T12:02:38.156173Z` distance=0.085 → {'next30m_imbalance_delta': 10.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T12:06:51.129462Z` distance=0.085 → {'next30m_imbalance_delta': 10.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 1.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
