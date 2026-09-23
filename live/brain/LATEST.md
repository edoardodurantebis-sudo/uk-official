# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T03:19:54.383554Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ps_gen` value=-11 d1=0.0 d12=-153.0 z=-106.5693805
- **PERSISTENT_DOWN** `ps_gen` value=-11 d1=0.0 d12=-153.0 z=-106.5693805
- **ROBUST_OUTLIER** `ps_gen` value=-11 d1=0.0 d12=-153.0 z=-106.5693805
- **CHANGE_POINT** `margin` value=3.857e+04 d1=-111.0 d12=-91.0 z=90.51652444999999
- **PERSISTENT_DOWN** `margin` value=3.857e+04 d1=-111.0 d12=-91.0 z=90.51652444999999
- **ACCELERATION** `margin` value=3.857e+04 d1=-111.0 d12=-91.0 z=90.51652444999999
- **ROBUST_OUTLIER** `margin` value=3.857e+04 d1=-111.0 d12=-91.0 z=90.51652444999999
- **CHANGE_POINT** `interconnector_net` value=-2244 d1=0.0 d12=-2805.0 z=-2.5844972216881947
- **ROBUST_OUTLIER** `ind_demand` value=-1.242e+04 d1=0.0 d12=1.0 z=4.346711722222222
- **PERSISTENT_UP** `biomass_gen` value=2881 d1=0.0 d12=13.0 z=-3.2600337916666664
- **ROBUST_OUTLIER** `biomass_gen` value=2881 d1=0.0 d12=13.0 z=-3.2600337916666664
- **PERSISTENT_DOWN** `interconnector_net` value=-2244 d1=0.0 d12=-2805.0 z=-2.5844972216881947
- **PERSISTENT_DOWN** `nuclear_gen` value=3718 d1=0.0 d12=-15.0 z=-2.5293365625
- **ACCELERATION** `nuclear_gen` value=3718 d1=0.0 d12=-15.0 z=-2.5293365625
- **PERSISTENT_UP** `wind_gen` value=5840 d1=0.0 d12=541.0 z=1.2365166035181236

## Nearest historical live analogues

- `2026-09-23T02:25:13.002873Z` distance=0.051 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T02:21:01.680995Z` distance=0.053 → {'next30m_imbalance_delta': 3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T06:53:31.262818Z` distance=0.677 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T06:57:43.435702Z` distance=0.677 → {'next30m_imbalance_delta': -691.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T07:01:58.015466Z` distance=0.677 → {'next30m_imbalance_delta': -691.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
