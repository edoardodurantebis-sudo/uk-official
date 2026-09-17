# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T08:04:11.303736Z`  
Memory snapshots: **796**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.558e+04 d1=0.0 d12=-154.0 z=-7.800620586956522
- **CHANGE_POINT** `wind_gen` value=1.575e+04 d1=98.0 d12=1638.0 z=6.452162100888325
- **ROBUST_OUTLIER** `margin` value=3.558e+04 d1=0.0 d12=-154.0 z=-7.800620586956522
- **CHANGE_POINT** `interconnector_net` value=4381 d1=419.0 d12=4833.0 z=5.015085179796802
- **ROBUST_OUTLIER** `ind_demand` value=-1.214e+04 d1=0.0 d12=-9.0 z=-6.766655233870968
- **PERSISTENT_UP** `wind_gen` value=1.575e+04 d1=98.0 d12=1638.0 z=6.452162100888325
- **ROBUST_OUTLIER** `wind_gen` value=1.575e+04 d1=98.0 d12=1638.0 z=6.452162100888325
- **ROBUST_OUTLIER** `residual_proxy` value=-3107 d1=0.0 d12=-2463.0 z=-5.748333059688581
- **PERSISTENT_UP** `interconnector_net` value=4381 d1=419.0 d12=4833.0 z=5.015085179796802
- **ROBUST_OUTLIER** `interconnector_net` value=4381 d1=419.0 d12=4833.0 z=5.015085179796802
- **CHANGE_POINT** `biomass_gen` value=2030 d1=1.0 d12=-984.0 z=-2.503705952
- **CHANGE_POINT** `ps_gen` value=225 d1=-1.0 d12=2.0 z=1.3919748625498007
- **CHANGE_POINT** `ind_generation` value=2.653e+04 d1=0.0 d12=69.0 z=1.011734625
- **CHANGE_POINT** `imbalance` value=7157 d1=0.0 d12=-181.0 z=-0.5586682777777778
- **REVERSAL** `biomass_gen` value=2030 d1=1.0 d12=-984.0 z=-2.503705952

## Nearest historical live analogues

- `2026-09-17T06:52:29.952634Z` distance=0.814 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:56:43.028097Z` distance=0.814 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:00:51.548981Z` distance=0.814 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:05:06.905847Z` distance=0.814 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:09:19.225959Z` distance=0.814 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
