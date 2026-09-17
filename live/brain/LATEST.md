# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T08:16:49.514568Z`  
Memory snapshots: **799**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.214e+04 d1=0.0 d12=0.0 z=-6.766655233870968
- **ROBUST_OUTLIER** `margin` value=3.558e+04 d1=0.0 d12=0.0 z=-7.800620586956522
- **CHANGE_POINT** `wind_gen` value=1.552e+04 d1=219.0 d12=1179.0 z=5.733162875
- **ROBUST_OUTLIER** `ind_demand` value=-1.214e+04 d1=0.0 d12=0.0 z=-6.766655233870968
- **ROBUST_OUTLIER** `residual_proxy` value=-3107 d1=0.0 d12=-2463.0 z=-5.748333059688581
- **ROBUST_OUTLIER** `wind_gen` value=1.552e+04 d1=219.0 d12=1179.0 z=5.733162875
- **REVERSAL** `interconnector_net` value=4898 d1=-68.0 d12=5278.0 z=5.204066108771061
- **ROBUST_OUTLIER** `interconnector_net` value=4898 d1=-68.0 d12=5278.0 z=5.204066108771061
- **CHANGE_POINT** `biomass_gen` value=2029 d1=-1.0 d12=-705.0 z=-1.6797292885185184
- **CHANGE_POINT** `imbalance` value=7157 d1=0.0 d12=0.0 z=-0.67448975
- **CHANGE_POINT** `ps_gen` value=-147 d1=-21.0 d12=-370.0 z=0.38637109694881894
- **PERSISTENT_DOWN** `biomass_gen` value=2029 d1=-1.0 d12=-705.0 z=-1.6797292885185184
- **PERSISTENT_UP** `nuclear_gen` value=3316 d1=1.0 d12=5.0 z=1.3489795
- **PERSISTENT_DOWN** `ccgt_gen` value=3122 d1=-67.0 d12=-237.0 z=-1.0503083852124184
- **PERSISTENT_DOWN** `thermal_base` value=6438 d1=-66.0 d12=-232.0 z=-1.0286788569692058

## Nearest historical live analogues

- `2026-09-17T07:22:04.087980Z` distance=0.809 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -2463.0}
- `2026-09-17T06:52:29.952634Z` distance=0.814 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:56:43.028097Z` distance=0.814 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:00:51.548981Z` distance=0.814 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:05:06.905847Z` distance=0.814 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
