# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T15:29:30.162883Z`  
Memory snapshots: **1243**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=0.0 z=-14.8387745
- **CHANGE_POINT** `ps_gen` value=224 d1=273.0 d12=697.0 z=5.83984237627551
- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=0.0 z=-6.528097223214285
- **CHANGE_POINT** `imbalance` value=8521 d1=0.0 d12=-29.0 z=-3.9785120036231882
- **PERSISTENT_UP** `ps_gen` value=224 d1=273.0 d12=697.0 z=5.83984237627551
- **ROBUST_OUTLIER** `ps_gen` value=224 d1=273.0 d12=697.0 z=5.83984237627551
- **PERSISTENT_DOWN** `imbalance` value=8521 d1=0.0 d12=-29.0 z=-3.9785120036231882
- **ACCELERATION** `imbalance` value=8521 d1=0.0 d12=-29.0 z=-3.9785120036231882
- **ROBUST_OUTLIER** `imbalance` value=8521 d1=0.0 d12=-29.0 z=-3.9785120036231882
- **CHANGE_POINT** `ccgt_gen` value=2652 d1=82.0 d12=170.0 z=1.829124745762712
- **CHANGE_POINT** `thermal_base` value=5985 d1=85.0 d12=167.0 z=1.7400701953781512
- **ROBUST_OUTLIER** `residual_proxy` value=9748 d1=0.0 d12=0.0 z=3.3488416087500004
- **PERSISTENT_UP** `biomass_gen` value=1489 d1=1.0 d12=3.0 z=3.15323958125
- **ROBUST_OUTLIER** `biomass_gen` value=1489 d1=1.0 d12=3.0 z=3.15323958125
- **CHANGE_POINT** `ind_generation` value=2.557e+04 d1=0.0 d12=-29.0 z=-0.9810759999999998

## Nearest historical live analogues

- `2026-09-18T14:21:00.093276Z` distance=0.072 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:25:11.108230Z` distance=0.112 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:29:22.596160Z` distance=0.112 → {'next30m_imbalance_delta': -13.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:34:10.760422Z` distance=0.112 → {'next30m_imbalance_delta': -13.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:57:04.108111Z` distance=0.141 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
