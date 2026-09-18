# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T04:14:07.474221Z`  
Memory snapshots: **1083**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.817e+04 d1=0.0 d12=8.0 z=9.143083277777778
- **CHANGE_POINT** `imbalance` value=1.069e+04 d1=0.0 d12=521.0 z=8.438616205555554
- **CHANGE_POINT** `ind_generation` value=2.75e+04 d1=0.0 d12=521.0 z=8.438616205555554
- **ROBUST_OUTLIER** `margin` value=3.817e+04 d1=0.0 d12=8.0 z=9.143083277777778
- **ROBUST_OUTLIER** `imbalance` value=1.069e+04 d1=0.0 d12=521.0 z=8.438616205555554
- **ROBUST_OUTLIER** `ind_generation` value=2.75e+04 d1=0.0 d12=521.0 z=8.438616205555554
- **CHANGE_POINT** `biomass_gen` value=2143 d1=13.0 d12=353.0 z=2.39137275
- **CHANGE_POINT** `ind_demand` value=-1.125e+04 d1=0.0 d12=0.0 z=-1.6083986346153847
- **CHANGE_POINT** `interconnector_net` value=-6945 d1=-38.0 d12=-736.0 z=-1.3198838637254902
- **PERSISTENT_UP** `biomass_gen` value=2143 d1=13.0 d12=353.0 z=2.39137275
- **PERSISTENT_DOWN** `thermal_base` value=6601 d1=-43.0 d12=-204.0 z=-1.427546437912088
- **PERSISTENT_DOWN** `ccgt_gen` value=3266 d1=-41.0 d12=-211.0 z=-1.394707618644068
- **PERSISTENT_DOWN** `interconnector_net` value=-6945 d1=-38.0 d12=-736.0 z=-1.3198838637254902
- **REVERSAL** `nuclear_gen` value=3335 d1=-2.0 d12=7.0 z=1.011734625
- **PERSISTENT_UP** `wind_gen` value=1.383e+04 d1=6.0 d12=198.0 z=-0.9191979214939026

## Nearest historical live analogues

- `2026-09-14T23:53:08.620374Z` distance=5.410 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:57:18.949614Z` distance=5.410 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:32:10.678260Z` distance=5.460 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:36:23.316269Z` distance=5.460 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:40:34.642541Z` distance=5.460 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
