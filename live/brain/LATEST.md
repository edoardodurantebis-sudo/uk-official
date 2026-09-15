# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T07:38:22.525585Z`  
Memory snapshots: **144**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=6420 d1=39.0 d12=7072.0 z=2.6384216938684832
- **CHANGE_POINT** `biomass_gen` value=3235 d1=-2.0 d12=19.0 z=2.5293365625
- **CHANGE_POINT** `wind_gen` value=1.25e+04 d1=36.0 d12=-1236.0 z=-1.9542908141025641
- **CHANGE_POINT** `thermal_base` value=6508 d1=-104.0 d12=-744.0 z=-1.4559318388746805
- **CHANGE_POINT** `ccgt_gen` value=3195 d1=-100.0 d12=-734.0 z=-1.3986246846446702
- **ROBUST_OUTLIER** `ind_demand` value=-1.228e+04 d1=0.0 d12=155.0 z=3.1074706339285716
- **CHANGE_POINT** `margin` value=3.413e+04 d1=0.0 d12=231.0 z=0.9323828897058823
- **PERSISTENT_DOWN** `nuclear_gen` value=3313 d1=-4.0 d12=-10.0 z=-2.6979589999999996
- **PERSISTENT_UP** `interconnector_net` value=6420 d1=39.0 d12=7072.0 z=2.6384216938684832
- **ACCELERATION** `interconnector_net` value=6420 d1=39.0 d12=7072.0 z=2.6384216938684832
- **REVERSAL** `biomass_gen` value=3235 d1=-2.0 d12=19.0 z=2.5293365625
- **CHANGE_POINT** `ind_generation` value=2.003e+04 d1=0.0 d12=136.0 z=-0.24274695372750643
- **CHANGE_POINT** `imbalance` value=-454 d1=0.0 d12=136.0 z=-0.24163421456185566
- **REVERSAL** `wind_gen` value=1.25e+04 d1=36.0 d12=-1236.0 z=-1.9542908141025641
- **PERSISTENT_DOWN** `thermal_base` value=6508 d1=-104.0 d12=-744.0 z=-1.4559318388746805

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=1.003 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=1.003 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=1.003 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=1.003 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=1.003 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
