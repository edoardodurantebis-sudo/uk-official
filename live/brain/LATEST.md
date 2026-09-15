# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T01:04:20.750196Z`  
Memory snapshots: **50**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.235e+04 d1=0.0 d12=-77.0 z=-26.30510025
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=0.0 z=5.836138409351145
- **CHANGE_POINT** `biomass_gen` value=3150 d1=8.0 d12=342.0 z=3.1079429656862745
- **CHANGE_POINT** `imbalance` value=272 d1=0.0 d12=62.0 z=2.805486351449275
- **CHANGE_POINT** `ind_generation` value=2.076e+04 d1=0.0 d12=61.0 z=2.805486351449275
- **CHANGE_POINT** `nuclear_gen` value=3324 d1=1.0 d12=10.0 z=2.248299166666667
- **CHANGE_POINT** `ps_gen` value=-7 d1=0.0 d12=7.0 z=1.686224375
- **PERSISTENT_UP** `biomass_gen` value=3150 d1=8.0 d12=342.0 z=3.1079429656862745
- **ROBUST_OUTLIER** `biomass_gen` value=3150 d1=8.0 d12=342.0 z=3.1079429656862745
- **PERSISTENT_UP** `nuclear_gen` value=3324 d1=1.0 d12=10.0 z=2.248299166666667
- **PERSISTENT_UP** `ps_gen` value=-7 d1=0.0 d12=7.0 z=1.686224375
- **PERSISTENT_DOWN** `ccgt_gen` value=3604 d1=-2.0 d12=-301.0 z=-0.8226805636861313
- **PERSISTENT_DOWN** `thermal_base` value=6928 d1=-1.0 d12=-291.0 z=-0.817757280839416
- **REVERSAL** `interconnector_net` value=131 d1=-126.0 d12=434.0 z=0.8166122609745391
- **PERSISTENT_UP** `wind_gen` value=1.208e+04 d1=118.0 d12=60.0 z=-0.5989003814655172

## Nearest historical live analogues

- `2026-09-14T23:53:08.620374Z` distance=22.229 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:57:18.949614Z` distance=22.229 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T00:01:29.159410Z` distance=22.229 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T00:05:39.935821Z` distance=22.229 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T00:09:52.902274Z` distance=22.229 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
