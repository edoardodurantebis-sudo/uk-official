# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T05:42:58.696391Z`  
Memory snapshots: **458**  
Current physical regime: **BALANCED**

Regime read: wind rising.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=7847 d1=222.0 d12=3498.0 z=22.40858752158273
- **CHANGE_POINT** `thermal_base` value=1.118e+04 d1=222.0 d12=3505.0 z=21.698828786585366
- **PERSISTENT_UP** `ccgt_gen` value=7847 d1=222.0 d12=3498.0 z=22.40858752158273
- **ROBUST_OUTLIER** `ccgt_gen` value=7847 d1=222.0 d12=3498.0 z=22.40858752158273
- **PERSISTENT_UP** `thermal_base` value=1.118e+04 d1=222.0 d12=3505.0 z=21.698828786585366
- **ROBUST_OUTLIER** `thermal_base` value=1.118e+04 d1=222.0 d12=3505.0 z=21.698828786585366
- **CHANGE_POINT** `imbalance` value=7173 d1=0.0 d12=-30.0 z=13.935440013392858
- **CHANGE_POINT** `ind_generation` value=2.629e+04 d1=0.0 d12=-30.0 z=13.935440013392858
- **ROBUST_OUTLIER** `imbalance` value=7173 d1=0.0 d12=-30.0 z=13.935440013392858
- **ROBUST_OUTLIER** `ind_generation` value=2.629e+04 d1=0.0 d12=-30.0 z=13.935440013392858
- **PERSISTENT_DOWN** `interconnector_net` value=-1808 d1=-51.0 d12=-796.0 z=-7.226223518779342
- **ROBUST_OUTLIER** `interconnector_net` value=-1808 d1=-51.0 d12=-796.0 z=-7.226223518779342
- **CHANGE_POINT** `wind_gen` value=8503 d1=-91.0 d12=-644.0 z=-2.477595902869757
- **CHANGE_POINT** `ind_demand` value=-1.222e+04 d1=0.0 d12=-41.0 z=-1.1616212361111111
- **CHANGE_POINT** `margin` value=3.755e+04 d1=0.0 d12=26.0 z=0.6790317685185184

## Nearest historical live analogues

- `2026-09-16T03:32:58.473492Z` distance=0.284 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:37:08.879637Z` distance=0.284 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:41:19.622154Z` distance=0.284 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:45:29.518871Z` distance=0.284 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:49:41.884820Z` distance=0.284 → {'next30m_imbalance_delta': 996.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
