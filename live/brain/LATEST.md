# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T18:37:00.976118Z`  
Memory snapshots: **946**  
Current physical regime: **BALANCED**

## Active patterns

- **ROBUST_OUTLIER** `ind_generation` value=2.65e+04 d1=0.0 d12=18.0 z=-111.4594311875
- **CHANGE_POINT** `ind_demand` value=-1.125e+04 d1=0.0 d12=29.0 z=5.8455778333333335
- **ROBUST_OUTLIER** `ind_demand` value=-1.125e+04 d1=0.0 d12=29.0 z=5.8455778333333335
- **PERSISTENT_UP** `imbalance` value=9682 d1=0.0 d12=18.0 z=-5.175411735576923
- **ROBUST_OUTLIER** `imbalance` value=9682 d1=0.0 d12=18.0 z=-5.175411735576923
- **CHANGE_POINT** `interconnector_net` value=-409 d1=-64.0 d12=-1194.0 z=-1.61893373092723
- **CHANGE_POINT** `wind_gen` value=1.501e+04 d1=2.0 d12=376.0 z=1.0767520538793103
- **PERSISTENT_UP** `nuclear_gen` value=3326 d1=3.0 d12=8.0 z=2.8665814375
- **PERSISTENT_UP** `thermal_base` value=1.044e+04 d1=46.0 d12=676.0 z=2.4703187093750003
- **PERSISTENT_UP** `ccgt_gen` value=7112 d1=43.0 d12=668.0 z=2.4556724097501115
- **REVERSAL** `ps_gen` value=281 d1=2.0 d12=-74.0 z=1.6935878002183404
- **PERSISTENT_DOWN** `interconnector_net` value=-409 d1=-64.0 d12=-1194.0 z=-1.61893373092723
- **PERSISTENT_UP** `wind_gen` value=1.501e+04 d1=2.0 d12=376.0 z=1.0767520538793103
- **PERSISTENT_UP** `biomass_gen` value=2923 d1=50.0 d12=104.0 z=0.4452942038834951
- **ACCELERATION** `biomass_gen` value=2923 d1=50.0 d12=104.0 z=0.4452942038834951

## Nearest historical live analogues

- `2026-09-17T16:51:11.529831Z` distance=0.040 → {'next30m_imbalance_delta': -25.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T17:21:14.586656Z` distance=0.043 → {'next30m_imbalance_delta': -1933.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T16:55:22.028914Z` distance=0.043 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T16:59:33.030689Z` distance=0.043 → {'next30m_imbalance_delta': -1933.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T17:04:23.689660Z` distance=0.043 → {'next30m_imbalance_delta': -1933.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
