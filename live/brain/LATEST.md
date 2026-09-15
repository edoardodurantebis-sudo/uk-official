# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T03:47:47.828928Z`  
Memory snapshots: **89**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **PERSISTENT_UP** `ps_gen` value=-318 d1=1.0 d12=326.0 z=-41.278772700000005
- **ROBUST_OUTLIER** `ps_gen` value=-318 d1=1.0 d12=326.0 z=-41.278772700000005
- **CHANGE_POINT** `ind_demand` value=-1.241e+04 d1=0.0 d12=-86.0 z=-5.320974694444445
- **CHANGE_POINT** `wind_gen` value=1.382e+04 d1=-9.0 d12=974.0 z=3.4984383448113205
- **ROBUST_OUTLIER** `ind_demand` value=-1.241e+04 d1=0.0 d12=-86.0 z=-5.320974694444445
- **ROBUST_OUTLIER** `margin` value=3.411e+04 d1=0.0 d12=6.0 z=4.321617583710407
- **CHANGE_POINT** `interconnector_net` value=-7638 d1=-7.0 d12=-4202.0 z=-1.659107099763505
- **REVERSAL** `wind_gen` value=1.382e+04 d1=-9.0 d12=974.0 z=3.4984383448113205
- **ROBUST_OUTLIER** `wind_gen` value=1.382e+04 d1=-9.0 d12=974.0 z=3.4984383448113205
- **PERSISTENT_DOWN** `interconnector_net` value=-7638 d1=-7.0 d12=-4202.0 z=-1.659107099763505
- **PERSISTENT_UP** `nuclear_gen` value=3328 d1=3.0 d12=0.0 z=1.16502775
- **ACCELERATION** `nuclear_gen` value=3328 d1=3.0 d12=0.0 z=1.16502775
- **PERSISTENT_DOWN** `thermal_base` value=6589 d1=-31.0 d12=-145.0 z=-0.9066766665575916
- **PERSISTENT_DOWN** `ccgt_gen` value=3261 d1=-34.0 d12=-145.0 z=-0.9044488662864385
- **ACCELERATION** `biomass_gen` value=3211 d1=-10.0 d12=-12.0 z=0.6546030743243244

## Nearest historical live analogues

- `2026-09-15T02:53:16.366736Z` distance=3.378 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:23:56.984916Z` distance=3.693 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:28:08.328313Z` distance=3.693 → {'next30m_imbalance_delta': -29.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:32:19.562106Z` distance=3.693 → {'next30m_imbalance_delta': -29.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:36:29.545958Z` distance=3.693 → {'next30m_imbalance_delta': -29.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
