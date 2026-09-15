# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T00:34:59.294733Z`  
Memory snapshots: **43**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2945 d1=0.0 d12=255.0 z=8.943234462962963
- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=0.0 z=8.373992961748634
- **PERSISTENT_UP** `biomass_gen` value=2945 d1=0.0 d12=255.0 z=8.943234462962963
- **ROBUST_OUTLIER** `biomass_gen` value=2945 d1=0.0 d12=255.0 z=8.943234462962963
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=0.0 z=8.373992961748634
- **CHANGE_POINT** `imbalance` value=264 d1=0.0 d12=77.0 z=2.727284641304348
- **CHANGE_POINT** `ind_generation` value=2.075e+04 d1=0.0 d12=76.0 z=2.727284641304348
- **CHANGE_POINT** `margin` value=3.27e+04 d1=0.0 d12=216.0 z=1.26466828125
- **CHANGE_POINT** `wind_gen` value=1.184e+04 d1=0.0 d12=-398.0 z=-1.1492069633587785
- **CHANGE_POINT** `ind_demand` value=-1.227e+04 d1=0.0 d12=-1.0 z=-0.67448975
- **CHANGE_POINT** `ps_gen` value=-12 d1=0.0 d12=4.0 z=0.0
- **PERSISTENT_UP** `interconnector_net` value=228 d1=0.0 d12=1210.0 z=1.4151419822888283
- **ACCELERATION** `interconnector_net` value=228 d1=0.0 d12=1210.0 z=1.4151419822888283
- **PERSISTENT_DOWN** `wind_gen` value=1.184e+04 d1=0.0 d12=-398.0 z=-1.1492069633587785
- **ACCELERATION** `nuclear_gen` value=3311 d1=0.0 d12=1.0 z=-0.6744897499999999

## Nearest historical live analogues

- `2026-09-14T23:32:10.678260Z` distance=1.079 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:36:23.316269Z` distance=1.079 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:28:00.797408Z` distance=7.007 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 4389.0}
- `2026-09-14T23:23:50.457848Z` distance=7.113 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 4457.0}
- `2026-09-14T22:54:28.088906Z` distance=7.263 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': -8.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
