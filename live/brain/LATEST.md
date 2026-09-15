# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T00:09:52.902274Z`  
Memory snapshots: **37**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=4544.0 z=9.441820417434716
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=4544.0 z=9.441820417434716
- **CHANGE_POINT** `biomass_gen` value=2774 d1=32.0 d12=91.0 z=6.673898578947369
- **CHANGE_POINT** `margin` value=3.272e+04 d1=0.0 d12=248.0 z=5.4157559338235295
- **PERSISTENT_UP** `biomass_gen` value=2774 d1=32.0 d12=91.0 z=6.673898578947369
- **ACCELERATION** `biomass_gen` value=2774 d1=32.0 d12=91.0 z=6.673898578947369
- **ROBUST_OUTLIER** `biomass_gen` value=2774 d1=32.0 d12=91.0 z=6.673898578947369
- **CHANGE_POINT** `imbalance` value=210 d1=0.0 d12=273.0 z=3.6225404550561797
- **CHANGE_POINT** `ind_generation` value=2.07e+04 d1=0.0 d12=274.0 z=3.542924181318681
- **ROBUST_OUTLIER** `margin` value=3.272e+04 d1=0.0 d12=248.0 z=5.4157559338235295
- **CHANGE_POINT** `interconnector_net` value=-376 d1=429.0 d12=2251.0 z=2.6625420196328995
- **ROBUST_OUTLIER** `ind_demand` value=-1.227e+04 d1=0.0 d12=-1.0 z=-3.9120405499999995
- **ROBUST_OUTLIER** `imbalance` value=210 d1=0.0 d12=273.0 z=3.6225404550561797
- **ROBUST_OUTLIER** `ind_generation` value=2.07e+04 d1=0.0 d12=274.0 z=3.542924181318681
- **CHANGE_POINT** `wind_gen` value=1.203e+04 d1=5.0 d12=-368.0 z=-0.9281857138336348

## Nearest historical live analogues

- `2026-09-14T22:54:28.088906Z` distance=9.087 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': -8.0}
- `2026-09-14T23:11:14.299399Z` distance=9.097 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 4544.0}
- `2026-09-14T23:02:51.731221Z` distance=9.101 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 158.0}
- `2026-09-14T23:07:03.439519Z` distance=9.131 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 4566.0}
- `2026-09-14T22:58:38.297578Z` distance=9.142 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 116.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
