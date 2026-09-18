# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T15:24:41.804681Z`  
Memory snapshots: **1242**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=0.0 z=-14.8387745
- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=0.0 z=-6.528097223214285
- **CHANGE_POINT** `imbalance` value=8521 d1=-16.0 d12=-29.0 z=-3.9785120036231882
- **CHANGE_POINT** `ps_gen` value=-49 d1=124.0 d12=419.0 z=3.960906644132653
- **PERSISTENT_DOWN** `imbalance` value=8521 d1=-16.0 d12=-29.0 z=-3.9785120036231882
- **ACCELERATION** `imbalance` value=8521 d1=-16.0 d12=-29.0 z=-3.9785120036231882
- **ROBUST_OUTLIER** `imbalance` value=8521 d1=-16.0 d12=-29.0 z=-3.9785120036231882
- **PERSISTENT_UP** `ps_gen` value=-49 d1=124.0 d12=419.0 z=3.960906644132653
- **ROBUST_OUTLIER** `ps_gen` value=-49 d1=124.0 d12=419.0 z=3.960906644132653
- **ROBUST_OUTLIER** `residual_proxy` value=9748 d1=0.0 d12=0.0 z=3.3488416087500004
- **PERSISTENT_UP** `biomass_gen` value=1488 d1=0.0 d12=31.0 z=3.144808459375
- **ROBUST_OUTLIER** `biomass_gen` value=1488 d1=0.0 d12=31.0 z=3.144808459375
- **CHANGE_POINT** `nuclear_gen` value=3330 d1=0.0 d12=-10.0 z=-1.1241495833333335
- **CHANGE_POINT** `ind_generation` value=2.557e+04 d1=-16.0 d12=-29.0 z=-0.9810759999999998
- **CHANGE_POINT** `ccgt_gen` value=2570 d1=17.0 d12=81.0 z=0.8916983135593219

## Nearest historical live analogues

- `2026-09-18T14:21:00.093276Z` distance=0.072 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:25:11.108230Z` distance=0.112 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:29:22.596160Z` distance=0.112 → {'next30m_imbalance_delta': -13.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:57:04.108111Z` distance=0.141 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:01:14.855580Z` distance=0.141 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
