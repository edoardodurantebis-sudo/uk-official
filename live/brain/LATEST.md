# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T07:38:59.971580Z`  
Memory snapshots: **790**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.558e+04 d1=0.0 d12=-196.0 z=-7.800620586956522
- **ROBUST_OUTLIER** `margin` value=3.558e+04 d1=0.0 d12=-196.0 z=-7.800620586956522
- **CHANGE_POINT** `interconnector_net` value=3961 d1=25.0 d12=9363.0 z=5.125120028210117
- **ROBUST_OUTLIER** `ind_demand` value=-1.214e+04 d1=0.0 d12=-320.0 z=-6.766655233870968
- **PERSISTENT_UP** `interconnector_net` value=3961 d1=25.0 d12=9363.0 z=5.125120028210117
- **ACCELERATION** `interconnector_net` value=3961 d1=25.0 d12=9363.0 z=5.125120028210117
- **ROBUST_OUTLIER** `interconnector_net` value=3961 d1=25.0 d12=9363.0 z=5.125120028210117
- **CHANGE_POINT** `wind_gen` value=1.472e+04 d1=142.0 d12=713.0 z=2.7071775387243737
- **CHANGE_POINT** `biomass_gen` value=2470 d1=-99.0 d12=-703.0 z=-2.089044642361111
- **CHANGE_POINT** `ps_gen` value=223 d1=0.0 d12=-3.0 z=1.4609280062240664
- **CHANGE_POINT** `ind_generation` value=2.653e+04 d1=0.0 d12=48.0 z=0.94428565
- **PERSISTENT_UP** `wind_gen` value=1.472e+04 d1=142.0 d12=713.0 z=2.7071775387243737
- **CHANGE_POINT** `imbalance` value=7157 d1=0.0 d12=-202.0 z=-0.4609013291666667
- **PERSISTENT_DOWN** `biomass_gen` value=2470 d1=-99.0 d12=-703.0 z=-2.089044642361111
- **PERSISTENT_UP** `nuclear_gen` value=3316 d1=8.0 d12=9.0 z=1.3489795

## Nearest historical live analogues

- `2026-09-17T06:23:11.376027Z` distance=0.604 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:27:23.488219Z` distance=0.604 → {'next30m_imbalance_delta': -21.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:31:35.953435Z` distance=0.604 → {'next30m_imbalance_delta': -21.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:35:47.177085Z` distance=0.604 → {'next30m_imbalance_delta': -21.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:39:57.616616Z` distance=0.604 → {'next30m_imbalance_delta': -21.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
