# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T08:08:23.106178Z`  
Memory snapshots: **797**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.558e+04 d1=0.0 d12=-154.0 z=-7.800620586956522
- **CHANGE_POINT** `ind_demand` value=-1.214e+04 d1=0.0 d12=-9.0 z=-6.766655233870968
- **ROBUST_OUTLIER** `margin` value=3.558e+04 d1=0.0 d12=-154.0 z=-7.800620586956522
- **CHANGE_POINT** `wind_gen` value=1.546e+04 d1=-287.0 d12=1382.0 z=5.543679929768041
- **CHANGE_POINT** `interconnector_net` value=4853 d1=472.0 d12=5253.0 z=5.221964736688852
- **ROBUST_OUTLIER** `ind_demand` value=-1.214e+04 d1=0.0 d12=-9.0 z=-6.766655233870968
- **ROBUST_OUTLIER** `residual_proxy` value=-3107 d1=0.0 d12=-2463.0 z=-5.748333059688581
- **REVERSAL** `wind_gen` value=1.546e+04 d1=-287.0 d12=1382.0 z=5.543679929768041
- **ROBUST_OUTLIER** `wind_gen` value=1.546e+04 d1=-287.0 d12=1382.0 z=5.543679929768041
- **PERSISTENT_UP** `interconnector_net` value=4853 d1=472.0 d12=5253.0 z=5.221964736688852
- **ROBUST_OUTLIER** `interconnector_net` value=4853 d1=472.0 d12=5253.0 z=5.221964736688852
- **CHANGE_POINT** `biomass_gen` value=2029 d1=-1.0 d12=-921.0 z=-2.1860261321942445
- **CHANGE_POINT** `ps_gen` value=18 d1=-207.0 d12=-205.0 z=0.8324060009920635
- **CHANGE_POINT** `imbalance` value=7157 d1=0.0 d12=-181.0 z=-0.5586682777777778
- **PERSISTENT_DOWN** `biomass_gen` value=2029 d1=-1.0 d12=-921.0 z=-2.1860261321942445

## Nearest historical live analogues

- `2026-09-17T06:52:29.952634Z` distance=0.814 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:56:43.028097Z` distance=0.814 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:00:51.548981Z` distance=0.814 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:05:06.905847Z` distance=0.814 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:09:19.225959Z` distance=0.814 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
