# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T10:47:46.205660Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.374e+04 d1=0.0 d12=-1040.0 z=-6.787229492677825
- **CHANGE_POINT** `margin` value=4.078e+04 d1=0.0 d12=71.0 z=5.537477577160494
- **ROBUST_OUTLIER** `imbalance` value=-2300 d1=0.0 d12=1648.0 z=7.502244827047414
- **ROBUST_OUTLIER** `ind_generation` value=1.873e+04 d1=0.0 d12=1648.0 z=7.413483619803063
- **ROBUST_OUTLIER** `ind_demand` value=-1.374e+04 d1=0.0 d12=-1040.0 z=-6.787229492677825
- **CHANGE_POINT** `ps_gen` value=-862 d1=-4.0 d12=-289.0 z=-3.540023843167702
- **ROBUST_OUTLIER** `margin` value=4.078e+04 d1=0.0 d12=71.0 z=5.537477577160494
- **ROBUST_OUTLIER** `ps_gen` value=-862 d1=-4.0 d12=-289.0 z=-3.540023843167702
- **CHANGE_POINT** `biomass_gen` value=2680 d1=-2.0 d12=-2.0 z=0.8468593527777778
- **CHANGE_POINT** `nuclear_gen` value=3803 d1=2.0 d12=-1.0 z=0.0
- **REVERSAL** `interconnector_net` value=1.145e+04 d1=-15.0 d12=30.0 z=1.4234685176643305
- **ACCELERATION** `interconnector_net` value=1.145e+04 d1=-15.0 d12=30.0 z=1.4234685176643305
- **REVERSAL** `wind_gen` value=9561 d1=31.0 d12=-225.0 z=-0.018445026422764226
- **REVERSAL** `nuclear_gen` value=3803 d1=2.0 d12=-1.0 z=0.0
- **ACCELERATION** `nuclear_gen` value=3803 d1=2.0 d12=-1.0 z=0.0

## Nearest historical live analogues

- `2026-09-22T10:20:52.187902Z` distance=0.962 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -614.0}
- `2026-09-22T10:25:04.719488Z` distance=0.962 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -127.0}
- `2026-09-22T10:29:21.446166Z` distance=0.962 → {'next30m_imbalance_delta': -11397.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3381.0, 'next30m_residual_proxy_delta': -127.0}
- `2026-09-22T10:50:36.865474Z` distance=1.006 → {'next30m_imbalance_delta': -11397.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3381.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:33:45.224867Z` distance=1.009 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
