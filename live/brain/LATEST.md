# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T06:31:27.066697Z`  
Memory snapshots: **128**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.989e+04 d1=0.0 d12=-66.0 z=-12.125826838888889
- **CHANGE_POINT** `imbalance` value=-590 d1=0.0 d12=-66.0 z=-11.84755908695652
- **PERSISTENT_DOWN** `ind_generation` value=1.989e+04 d1=0.0 d12=-66.0 z=-12.125826838888889
- **ROBUST_OUTLIER** `ind_generation` value=1.989e+04 d1=0.0 d12=-66.0 z=-12.125826838888889
- **PERSISTENT_DOWN** `imbalance` value=-590 d1=0.0 d12=-66.0 z=-11.84755908695652
- **ROBUST_OUTLIER** `imbalance` value=-590 d1=0.0 d12=-66.0 z=-11.84755908695652
- **CHANGE_POINT** `ccgt_gen` value=3910 d1=-7.0 d12=70.0 z=0.7479813692493947
- **CHANGE_POINT** `thermal_base` value=7233 d1=-3.0 d12=70.0 z=0.7313744277108435
- **PERSISTENT_UP** `interconnector_net` value=-606 d1=1596.0 d12=3229.0 z=0.8164502713940286
- **ACCELERATION** `interconnector_net` value=-606 d1=1596.0 d12=3229.0 z=0.8164502713940286
- **REVERSAL** `ccgt_gen` value=3910 d1=-7.0 d12=70.0 z=0.7479813692493947
- **ACCELERATION** `ccgt_gen` value=3910 d1=-7.0 d12=70.0 z=0.7479813692493947
- **REVERSAL** `thermal_base` value=7233 d1=-3.0 d12=70.0 z=0.7313744277108435
- **ACCELERATION** `thermal_base` value=7233 d1=-3.0 d12=70.0 z=0.7313744277108435
- **PERSISTENT_DOWN** `margin` value=3.39e+04 d1=0.0 d12=-90.0 z=-0.5420006919642857

## Nearest historical live analogues

- `2026-09-15T05:32:31.100785Z` distance=0.113 → {'next30m_imbalance_delta': -63.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T05:36:43.326955Z` distance=0.113 → {'next30m_imbalance_delta': -63.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T05:24:11.392435Z` distance=0.142 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -671.0}
- `2026-09-15T05:28:20.392580Z` distance=0.142 → {'next30m_imbalance_delta': -63.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': -671.0}
- `2026-09-15T05:20:00.210059Z` distance=0.143 → {'next30m_imbalance_delta': -51.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -671.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
