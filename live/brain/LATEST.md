# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T09:10:29.403352Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=-10.0 z=-40.6380074375
- **PERSISTENT_DOWN** `ccgt_gen` value=2972 d1=0.0 d12=-3032.0 z=-6.936238106903766
- **ROBUST_OUTLIER** `ccgt_gen` value=2972 d1=0.0 d12=-3032.0 z=-6.936238106903766
- **REVERSAL** `thermal_base` value=6776 d1=5.0 d12=-3036.0 z=-6.480433534782609
- **ROBUST_OUTLIER** `thermal_base` value=6776 d1=5.0 d12=-3036.0 z=-6.480433534782609
- **ROBUST_OUTLIER** `margin` value=3.966e+04 d1=0.0 d12=360.0 z=5.945060097345133
- **PERSISTENT_UP** `interconnector_net` value=1.076e+04 d1=94.0 d12=3762.0 z=5.226838095225177
- **ROBUST_OUTLIER** `interconnector_net` value=1.076e+04 d1=94.0 d12=3762.0 z=5.226838095225177
- **ROBUST_OUTLIER** `imbalance` value=-7365 d1=0.0 d12=89.0 z=5.010495285714286
- **ROBUST_OUTLIER** `ind_generation` value=1.366e+04 d1=0.0 d12=-302.0 z=3.74035225
- **CHANGE_POINT** `ps_gen` value=-19 d1=1.0 d12=272.0 z=-1.011734625
- **CHANGE_POINT** `biomass_gen` value=2693 d1=22.0 d12=379.0 z=0.4343572735602094
- **CHANGE_POINT** `residual_proxy` value=1.329e+04 d1=0.0 d12=309.0 z=0.35293068313953485
- **PERSISTENT_DOWN** `wind_gen` value=1.039e+04 d1=-55.0 d12=-92.0 z=0.7455462066450567
- **ACCELERATION** `wind_gen` value=1.039e+04 d1=-55.0 d12=-92.0 z=0.7455462066450567

## Nearest historical live analogues

- `2026-09-21T09:22:16.225384Z` distance=0.443 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:26:26.475864Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:30:39.158321Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:34:50.037660Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:39:02.425016Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
