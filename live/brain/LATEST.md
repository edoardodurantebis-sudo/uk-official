# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T09:39:02.425016Z`  
Memory snapshots: **2129**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.168e+04 d1=0.0 d12=2686.0 z=36.192832968085106
- **ROBUST_OUTLIER** `ind_generation` value=2.168e+04 d1=0.0 d12=2686.0 z=36.192832968085106
- **CHANGE_POINT** `biomass_gen` value=2921 d1=-12.0 d12=-101.0 z=-11.8955465
- **CHANGE_POINT** `ind_demand` value=-1.282e+04 d1=0.0 d12=11.0 z=-11.68353431355932
- **PERSISTENT_DOWN** `biomass_gen` value=2921 d1=-12.0 d12=-101.0 z=-11.8955465
- **ROBUST_OUTLIER** `biomass_gen` value=2921 d1=-12.0 d12=-101.0 z=-11.8955465
- **ROBUST_OUTLIER** `ind_demand` value=-1.282e+04 d1=0.0 d12=11.0 z=-11.68353431355932
- **CHANGE_POINT** `imbalance` value=415 d1=0.0 d12=2686.0 z=7.887583592420213
- **ROBUST_OUTLIER** `imbalance` value=415 d1=0.0 d12=2686.0 z=7.887583592420213
- **CHANGE_POINT** `margin` value=3.968e+04 d1=0.0 d12=1427.0 z=2.6564325788246266
- **CHANGE_POINT** `ccgt_gen` value=7676 d1=-24.0 d12=-1202.0 z=-1.7670674726950353
- **CHANGE_POINT** `thermal_base` value=1.116e+04 d1=-28.0 d12=-1211.0 z=-1.635841897039031
- **CHANGE_POINT** `wind_gen` value=3327 d1=-3.0 d12=-434.0 z=-1.3501969905234659
- **CHANGE_POINT** `ps_gen` value=-11 d1=0.0 d12=-119.0 z=0.0
- **PERSISTENT_DOWN** `ccgt_gen` value=7676 d1=-24.0 d12=-1202.0 z=-1.7670674726950353

## Nearest historical live analogues

- `2026-09-21T08:31:05.309327Z` distance=0.631 → {'next30m_imbalance_delta': 271.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -29.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T08:35:54.594917Z` distance=0.631 → {'next30m_imbalance_delta': 271.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -29.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T08:40:08.617756Z` distance=0.631 → {'next30m_imbalance_delta': 271.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -29.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T08:44:20.619753Z` distance=0.631 → {'next30m_imbalance_delta': 271.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -29.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:23:29.263598Z` distance=0.632 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 982.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
