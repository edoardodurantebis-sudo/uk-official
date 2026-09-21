# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T07:40:19.774148Z`  
Memory snapshots: **2101**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.825e+04 d1=0.0 d12=101.0 z=14.695700916666667
- **ROBUST_OUTLIER** `ind_demand` value=-1.283e+04 d1=0.0 d12=-687.0 z=-16.55711743452381
- **ROBUST_OUTLIER** `margin` value=3.825e+04 d1=0.0 d12=101.0 z=14.695700916666667
- **CHANGE_POINT** `ind_generation` value=1.797e+04 d1=0.0 d12=1238.0 z=5.674599393712575
- **ROBUST_OUTLIER** `ind_generation` value=1.797e+04 d1=0.0 d12=1238.0 z=5.674599393712575
- **PERSISTENT_UP** `nuclear_gen` value=3496 d1=0.0 d12=6.0 z=4.923775175
- **ROBUST_OUTLIER** `nuclear_gen` value=3496 d1=0.0 d12=6.0 z=4.923775175
- **CHANGE_POINT** `imbalance` value=-3297 d1=0.0 d12=570.0 z=1.5489905297619047
- **CHANGE_POINT** `ps_gen` value=20 d1=0.0 d12=-210.0 z=0.1829124745762712
- **PERSISTENT_UP** `wind_gen` value=4296 d1=0.0 d12=402.0 z=1.4243414832402235
- **PERSISTENT_DOWN** `thermal_base` value=1.223e+04 d1=0.0 d12=-196.0 z=0.6931661318863571
- **PERSISTENT_DOWN** `ccgt_gen` value=8731 d1=0.0 d12=-202.0 z=0.6503295191681469
- **PERSISTENT_UP** `interconnector_net` value=1.067e+04 d1=0.0 d12=2189.0 z=0.3239182042755344
- **PERSISTENT_DOWN** `biomass_gen` value=3016 d1=0.0 d12=-2.0 z=-0.30658625
- **ACCELERATION** `biomass_gen` value=3016 d1=0.0 d12=-2.0 z=-0.30658625

## Nearest historical live analogues

- `2026-09-21T06:20:09.477286Z` distance=0.846 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:24:24.498463Z` distance=0.846 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:28:37.700638Z` distance=0.846 → {'next30m_imbalance_delta': -491.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:32:53.849371Z` distance=0.846 → {'next30m_imbalance_delta': -491.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:37:05.518712Z` distance=0.846 → {'next30m_imbalance_delta': -491.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
