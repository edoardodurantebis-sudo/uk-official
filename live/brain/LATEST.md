# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T05:33:49.242345Z`  
Memory snapshots: **1102**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `imbalance` value=1.07e+04 d1=0.0 d12=-35.0 z=10.77199806617647
- **CHANGE_POINT** `ind_generation` value=2.752e+04 d1=0.0 d12=-35.0 z=10.77199806617647
- **ROBUST_OUTLIER** `imbalance` value=1.07e+04 d1=0.0 d12=-35.0 z=10.77199806617647
- **ROBUST_OUTLIER** `ind_generation` value=2.752e+04 d1=0.0 d12=-35.0 z=10.77199806617647
- **CHANGE_POINT** `margin` value=3.802e+04 d1=0.0 d12=-143.0 z=4.409350902985074
- **CHANGE_POINT** `thermal_base` value=8274 d1=250.0 d12=1738.0 z=4.236000020833333
- **CHANGE_POINT** `ccgt_gen` value=4940 d1=249.0 d12=1744.0 z=4.073132276699029
- **ROBUST_OUTLIER** `margin` value=3.802e+04 d1=0.0 d12=-143.0 z=4.409350902985074
- **PERSISTENT_UP** `thermal_base` value=8274 d1=250.0 d12=1738.0 z=4.236000020833333
- **ROBUST_OUTLIER** `thermal_base` value=8274 d1=250.0 d12=1738.0 z=4.236000020833333
- **PERSISTENT_UP** `ccgt_gen` value=4940 d1=249.0 d12=1744.0 z=4.073132276699029
- **ROBUST_OUTLIER** `ccgt_gen` value=4940 d1=249.0 d12=1744.0 z=4.073132276699029
- **CHANGE_POINT** `biomass_gen` value=2178 d1=2.0 d12=65.0 z=1.688129713276836
- **CHANGE_POINT** `interconnector_net` value=-4788 d1=1079.0 d12=2233.0 z=1.3965905411764705
- **CHANGE_POINT** `wind_gen` value=1.371e+04 d1=103.0 d12=-94.0 z=-0.8948454394693202

## Nearest historical live analogues

- `2026-09-18T04:22:33.656419Z` distance=0.085 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T04:26:45.757776Z` distance=0.085 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -106.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T04:30:58.266480Z` distance=0.085 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -106.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T04:35:10.163579Z` distance=0.085 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -106.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T04:39:23.438454Z` distance=0.085 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -106.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
