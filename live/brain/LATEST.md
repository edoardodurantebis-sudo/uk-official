# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T05:20:00.210059Z`  
Memory snapshots: **111**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `ind_generation` value=2.001e+04 d1=0.0 d12=-4.0 z=-12.265063611842105
- **ROBUST_OUTLIER** `imbalance` value=-473 d1=0.0 d12=-4.0 z=-12.105777071428571
- **PERSISTENT_DOWN** `ps_gen` value=-815 d1=0.0 d12=-497.0 z=-5.625946296242774
- **ROBUST_OUTLIER** `ps_gen` value=-815 d1=0.0 d12=-497.0 z=-5.625946296242774
- **CHANGE_POINT** `ind_demand` value=-1.244e+04 d1=0.0 d12=0.0 z=-1.6931069234693876
- **PERSISTENT_DOWN** `margin` value=3.399e+04 d1=-73.0 d12=-78.0 z=3.2509889099616855
- **ACCELERATION** `margin` value=3.399e+04 d1=-73.0 d12=-78.0 z=3.2509889099616855
- **ROBUST_OUTLIER** `margin` value=3.399e+04 d1=-73.0 d12=-78.0 z=3.2509889099616855
- **CHANGE_POINT** `interconnector_net` value=-5252 d1=0.0 d12=2131.0 z=-0.5796779030655843
- **PERSISTENT_UP** `nuclear_gen` value=3333 d1=0.0 d12=9.0 z=1.21408155
- **ACCELERATION** `nuclear_gen` value=3333 d1=0.0 d12=9.0 z=1.21408155
- **PERSISTENT_UP** `interconnector_net` value=-5252 d1=0.0 d12=2131.0 z=-0.5796779030655843
- **PERSISTENT_UP** `thermal_base` value=7167 d1=0.0 d12=290.0 z=0.45635689468085106
- **PERSISTENT_UP** `ccgt_gen` value=3834 d1=0.0 d12=281.0 z=0.4410125288461539
- **PERSISTENT_DOWN** `ts_demand_forecast` value=2.048e+04 d1=-1.0 d12=-1.0 z=None

## Nearest historical live analogues

- `2026-09-15T04:21:21.535515Z` distance=0.185 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:25:31.752703Z` distance=0.185 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:51:58.464857Z` distance=0.502 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:56:09.070441Z` distance=0.502 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:00:20.228720Z` distance=0.502 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
