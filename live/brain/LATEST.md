# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T07:34:46.180062Z`  
Memory snapshots: **789**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.558e+04 d1=0.0 d12=-196.0 z=-7.800620586956522
- **ROBUST_OUTLIER** `margin` value=3.558e+04 d1=0.0 d12=-196.0 z=-7.800620586956522
- **CHANGE_POINT** `interconnector_net` value=3936 d1=4316.0 d12=9338.0 z=5.201507676232458
- **ROBUST_OUTLIER** `ind_demand` value=-1.214e+04 d1=0.0 d12=-320.0 z=-6.766655233870968
- **PERSISTENT_UP** `interconnector_net` value=3936 d1=4316.0 d12=9338.0 z=5.201507676232458
- **ACCELERATION** `interconnector_net` value=3936 d1=4316.0 d12=9338.0 z=5.201507676232458
- **ROBUST_OUTLIER** `interconnector_net` value=3936 d1=4316.0 d12=9338.0 z=5.201507676232458
- **CHANGE_POINT** `biomass_gen` value=2569 d1=-165.0 d12=-587.0 z=-2.5906538125000003
- **CHANGE_POINT** `wind_gen` value=1.458e+04 d1=240.0 d12=633.0 z=2.2063817245762714
- **CHANGE_POINT** `ps_gen` value=223 d1=0.0 d12=-3.0 z=1.4609280062240664
- **PERSISTENT_DOWN** `biomass_gen` value=2569 d1=-165.0 d12=-587.0 z=-2.5906538125000003
- **PERSISTENT_UP** `wind_gen` value=1.458e+04 d1=240.0 d12=633.0 z=2.2063817245762714
- **ACCELERATION** `wind_gen` value=1.458e+04 d1=240.0 d12=633.0 z=2.2063817245762714
- **REVERSAL** `nuclear_gen` value=3308 d1=-3.0 d12=1.0 z=-1.3489795
- **ACCELERATION** `nuclear_gen` value=3308 d1=-3.0 d12=1.0 z=-1.3489795

## Nearest historical live analogues

- `2026-09-17T06:23:11.376027Z` distance=0.604 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:27:23.488219Z` distance=0.604 → {'next30m_imbalance_delta': -21.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:31:35.953435Z` distance=0.604 → {'next30m_imbalance_delta': -21.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:35:47.177085Z` distance=0.604 → {'next30m_imbalance_delta': -21.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:39:57.616616Z` distance=0.604 → {'next30m_imbalance_delta': -21.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
