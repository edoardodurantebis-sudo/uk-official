# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T01:09:28.740549Z`  
Memory snapshots: **1668**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.195e+04 d1=0.0 d12=-60.0 z=-25.293365625
- **ROBUST_OUTLIER** `ind_demand` value=-1.195e+04 d1=0.0 d12=-60.0 z=-25.293365625
- **CHANGE_POINT** `thermal_base` value=7465 d1=84.0 d12=757.0 z=-1.2584494368198307
- **CHANGE_POINT** `ccgt_gen` value=4128 d1=78.0 d12=741.0 z=-1.254250077606992
- **CHANGE_POINT** `ps_gen` value=-476 d1=-222.0 d12=-345.0 z=-1.0618204975247525
- **CHANGE_POINT** `biomass_gen` value=939 d1=39.0 d12=54.0 z=0.67448975
- **PERSISTENT_UP** `thermal_base` value=7465 d1=84.0 d12=757.0 z=-1.2584494368198307
- **PERSISTENT_UP** `ccgt_gen` value=4128 d1=78.0 d12=741.0 z=-1.254250077606992
- **PERSISTENT_DOWN** `ps_gen` value=-476 d1=-222.0 d12=-345.0 z=-1.0618204975247525
- **ACCELERATION** `ps_gen` value=-476 d1=-222.0 d12=-345.0 z=-1.0618204975247525
- **PERSISTENT_DOWN** `interconnector_net` value=-9570 d1=-126.0 d12=-696.0 z=-0.8539671562559695
- **REVERSAL** `wind_gen` value=1.558e+04 d1=15.0 d12=-147.0 z=0.7718889918772563
- **PERSISTENT_UP** `biomass_gen` value=939 d1=39.0 d12=54.0 z=0.67448975
- **ACCELERATION** `biomass_gen` value=939 d1=39.0 d12=54.0 z=0.67448975
- **PERSISTENT_UP** `nuclear_gen` value=3337 d1=6.0 d12=16.0 z=0.6744897499999999

## Nearest historical live analogues

- `2026-09-20T00:05:59.440118Z` distance=0.069 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T00:10:11.155679Z` distance=0.069 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T00:15:00.044143Z` distance=0.069 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T23:53:21.201980Z` distance=0.121 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T23:57:34.023150Z` distance=0.121 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
