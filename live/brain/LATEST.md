# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T01:12:43.029281Z`  
Memory snapshots: **52**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.235e+04 d1=0.0 d12=-76.0 z=-26.30510025
- **CHANGE_POINT** `nuclear_gen` value=3329 d1=1.0 d12=18.0 z=3.37244875
- **CHANGE_POINT** `biomass_gen` value=3169 d1=7.0 d12=284.0 z=3.1649134423076926
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=0.0 z=4.83745783721865
- **CHANGE_POINT** `ps_gen` value=-7 d1=0.0 d12=7.0 z=1.686224375
- **PERSISTENT_UP** `nuclear_gen` value=3329 d1=1.0 d12=18.0 z=3.37244875
- **ROBUST_OUTLIER** `nuclear_gen` value=3329 d1=1.0 d12=18.0 z=3.37244875
- **PERSISTENT_UP** `biomass_gen` value=3169 d1=7.0 d12=284.0 z=3.1649134423076926
- **ROBUST_OUTLIER** `biomass_gen` value=3169 d1=7.0 d12=284.0 z=3.1649134423076926
- **CHANGE_POINT** `imbalance` value=272 d1=0.0 d12=8.0 z=0.9583096943069306
- **CHANGE_POINT** `ind_generation` value=2.076e+04 d1=0.0 d12=8.0 z=0.9535889568965517
- **PERSISTENT_DOWN** `ccgt_gen` value=3602 d1=-1.0 d12=-204.0 z=-0.7880766365276664
- **PERSISTENT_DOWN** `interconnector_net` value=-570 d1=-267.0 d12=-245.0 z=0.6018523923076924
- **ACCELERATION** `interconnector_net` value=-570 d1=-267.0 d12=-245.0 z=0.6018523923076924
- **PERSISTENT_UP** `wind_gen` value=1.219e+04 d1=85.0 d12=332.0 z=-0.2688844273648649

## Nearest historical live analogues

- `2026-09-14T23:53:08.620374Z` distance=22.229 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:57:18.949614Z` distance=22.229 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T00:01:29.159410Z` distance=22.229 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T00:05:39.935821Z` distance=22.229 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T00:09:52.902274Z` distance=22.229 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
