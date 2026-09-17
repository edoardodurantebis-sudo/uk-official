# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T07:55:48.803008Z`  
Memory snapshots: **794**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.558e+04 d1=0.0 d12=-154.0 z=-7.800620586956522
- **ROBUST_OUTLIER** `margin` value=3.558e+04 d1=0.0 d12=-154.0 z=-7.800620586956522
- **CHANGE_POINT** `wind_gen` value=1.551e+04 d1=0.0 d12=1504.0 z=5.410651999393203
- **CHANGE_POINT** `interconnector_net` value=4023 d1=0.0 d12=7968.0 z=4.904864035257489
- **ROBUST_OUTLIER** `ind_demand` value=-1.214e+04 d1=0.0 d12=-9.0 z=-6.766655233870968
- **PERSISTENT_DOWN** `residual_proxy` value=-3107 d1=0.0 d12=-2463.0 z=-5.748333059688581
- **ROBUST_OUTLIER** `residual_proxy` value=-3107 d1=0.0 d12=-2463.0 z=-5.748333059688581
- **PERSISTENT_UP** `wind_gen` value=1.551e+04 d1=0.0 d12=1504.0 z=5.410651999393203
- **ROBUST_OUTLIER** `wind_gen` value=1.551e+04 d1=0.0 d12=1504.0 z=5.410651999393203
- **PERSISTENT_UP** `interconnector_net` value=4023 d1=0.0 d12=7968.0 z=4.904864035257489
- **ROBUST_OUTLIER** `interconnector_net` value=4023 d1=0.0 d12=7968.0 z=4.904864035257489
- **CHANGE_POINT** `biomass_gen` value=2073 d1=0.0 d12=-1102.0 z=-2.835326477688787
- **CHANGE_POINT** `ps_gen` value=226 d1=0.0 d12=0.0 z=1.4086928782696175
- **CHANGE_POINT** `ind_generation` value=2.653e+04 d1=0.0 d12=69.0 z=1.011734625
- **PERSISTENT_DOWN** `biomass_gen` value=2073 d1=0.0 d12=-1102.0 z=-2.835326477688787

## Nearest historical live analogues

- `2026-09-17T06:52:29.952634Z` distance=0.814 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:56:43.028097Z` distance=0.814 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:00:51.548981Z` distance=0.814 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T12:23:49.836209Z` distance=1.003 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T12:28:01.597273Z` distance=1.003 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 199.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
