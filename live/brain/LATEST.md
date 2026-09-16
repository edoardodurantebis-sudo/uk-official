# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T01:30:51.171877Z`  
Memory snapshots: **398**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.216e+04 d1=0.0 d12=-64.0 z=-55.08332958333333
- **ROBUST_OUTLIER** `ind_demand` value=-1.216e+04 d1=0.0 d12=-64.0 z=-55.08332958333333
- **PERSISTENT_UP** `margin` value=3.604e+04 d1=0.0 d12=373.0 z=6.017158559210526
- **ROBUST_OUTLIER** `margin` value=3.604e+04 d1=0.0 d12=373.0 z=6.017158559210526
- **PERSISTENT_DOWN** `imbalance` value=5960 d1=0.0 d12=-75.0 z=3.135465864864865
- **ROBUST_OUTLIER** `imbalance` value=5960 d1=0.0 d12=-75.0 z=3.135465864864865
- **PERSISTENT_DOWN** `ind_generation` value=2.508e+04 d1=0.0 d12=-75.0 z=3.135465864864865
- **ROBUST_OUTLIER** `ind_generation` value=2.508e+04 d1=0.0 d12=-75.0 z=3.135465864864865
- **CHANGE_POINT** `interconnector_net` value=4598 d1=239.0 d12=422.0 z=0.8668934253592336
- **CHANGE_POINT** `ccgt_gen` value=3247 d1=3.0 d12=3.0 z=-0.6092293848082596
- **REVERSAL** `biomass_gen` value=3231 d1=-1.0 d12=31.0 z=-1.1562681428571426
- **REVERSAL** `nuclear_gen` value=3330 d1=2.0 d12=-1.0 z=1.0599124642857143
- **ACCELERATION** `nuclear_gen` value=3330 d1=2.0 d12=-1.0 z=1.0599124642857143
- **PERSISTENT_UP** `interconnector_net` value=4598 d1=239.0 d12=422.0 z=0.8668934253592336
- **ACCELERATION** `interconnector_net` value=4598 d1=239.0 d12=422.0 z=0.8668934253592336

## Nearest historical live analogues

- `2026-09-15T23:32:16.606471Z` distance=0.278 → {'next30m_imbalance_delta': 39.0, 'next30m_margin_delta': -78.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T23:36:27.405223Z` distance=0.278 → {'next30m_imbalance_delta': 39.0, 'next30m_margin_delta': -78.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T23:41:14.503194Z` distance=0.278 → {'next30m_imbalance_delta': 39.0, 'next30m_margin_delta': -78.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T23:45:24.499489Z` distance=0.278 → {'next30m_imbalance_delta': 39.0, 'next30m_margin_delta': -78.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T00:23:43.289309Z` distance=0.315 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
