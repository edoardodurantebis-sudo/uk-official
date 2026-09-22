# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T06:15:28.439651Z`  
Memory snapshots: **2420**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.783e+04 d1=0.0 d12=632.0 z=4.511036951834862
- **CHANGE_POINT** `ccgt_gen` value=1.418e+04 d1=0.0 d12=639.0 z=4.47434554294653
- **PERSISTENT_UP** `thermal_base` value=1.783e+04 d1=0.0 d12=632.0 z=4.511036951834862
- **ROBUST_OUTLIER** `thermal_base` value=1.783e+04 d1=0.0 d12=632.0 z=4.511036951834862
- **PERSISTENT_UP** `ccgt_gen` value=1.418e+04 d1=0.0 d12=639.0 z=4.47434554294653
- **ROBUST_OUTLIER** `ccgt_gen` value=1.418e+04 d1=0.0 d12=639.0 z=4.47434554294653
- **CHANGE_POINT** `wind_gen` value=3477 d1=0.0 d12=55.0 z=-0.948420453065134
- **CHANGE_POINT** `ps_gen` value=-174 d1=0.0 d12=-2.0 z=0.6682444745370371
- **CHANGE_POINT** `imbalance` value=-3209 d1=0.0 d12=53.0 z=-0.6571291939942803
- **CHANGE_POINT** `ind_generation` value=1.825e+04 d1=0.0 d12=53.0 z=-0.6571291939942803
- **CHANGE_POINT** `ind_demand` value=-1.248e+04 d1=0.0 d12=-2.0 z=-0.01482395054945055
- **PERSISTENT_UP** `interconnector_net` value=-441 d1=0.0 d12=2594.0 z=-0.9299782916666668
- **PERSISTENT_DOWN** `ps_gen` value=-174 d1=0.0 d12=-2.0 z=0.6682444745370371

## Nearest historical live analogues

- `2026-09-22T03:33:35.816390Z` distance=0.074 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:37:48.990972Z` distance=0.074 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:42:37.215255Z` distance=0.074 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:46:49.421565Z` distance=0.074 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:51:00.662974Z` distance=0.075 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
