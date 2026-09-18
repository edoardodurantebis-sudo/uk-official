# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T18:25:03.886063Z`  
Memory snapshots: **1256**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=4837 d1=0.0 d12=2165.0 z=26.808109555084744
- **CHANGE_POINT** `thermal_base` value=8169 d1=0.0 d12=2161.0 z=26.497811607142857
- **ROBUST_OUTLIER** `ccgt_gen` value=4837 d1=0.0 d12=2165.0 z=26.808109555084744
- **ROBUST_OUTLIER** `thermal_base` value=8169 d1=0.0 d12=2161.0 z=26.497811607142857
- **CHANGE_POINT** `ind_generation` value=2.623e+04 d1=65.0 d12=655.0 z=18.09392068478261
- **PERSISTENT_UP** `ind_generation` value=2.623e+04 d1=65.0 d12=655.0 z=18.09392068478261
- **ROBUST_OUTLIER** `ind_generation` value=2.623e+04 d1=65.0 d12=655.0 z=18.09392068478261
- **CHANGE_POINT** `interconnector_net` value=-872 d1=0.0 d12=-5934.0 z=-10.812886395318596
- **ROBUST_OUTLIER** `interconnector_net` value=-872 d1=0.0 d12=-5934.0 z=-10.812886395318596
- **ROBUST_OUTLIER** `ps_gen` value=513 d1=0.0 d12=287.0 z=7.828898883928571
- **PERSISTENT_UP** `ind_demand` value=-1.074e+04 d1=30.0 d12=31.0 z=6.07040775
- **ACCELERATION** `ind_demand` value=-1.074e+04 d1=30.0 d12=31.0 z=6.07040775
- **ROBUST_OUTLIER** `ind_demand` value=-1.074e+04 d1=30.0 d12=31.0 z=6.07040775
- **CHANGE_POINT** `biomass_gen` value=1529 d1=0.0 d12=39.0 z=3.4904844562500004
- **CHANGE_POINT** `imbalance` value=9176 d1=65.0 d12=655.0 z=2.424253014492754

## Nearest historical live analogues

- `2026-09-18T15:24:41.804681Z` distance=0.109 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T15:29:30.162883Z` distance=0.109 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:21:00.093276Z` distance=0.174 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:31:54.164710Z` distance=0.193 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:36:05.963399Z` distance=0.193 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
