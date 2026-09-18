# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T04:01:30.504638Z`  
Memory snapshots: **1080**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.817e+04 d1=0.0 d12=-6.0 z=8.44166077734375
- **CHANGE_POINT** `imbalance` value=1.069e+04 d1=0.0 d12=518.0 z=8.438616205555554
- **CHANGE_POINT** `ind_generation` value=2.75e+04 d1=0.0 d12=518.0 z=8.438616205555554
- **ROBUST_OUTLIER** `margin` value=3.817e+04 d1=0.0 d12=-6.0 z=8.44166077734375
- **PERSISTENT_UP** `imbalance` value=1.069e+04 d1=0.0 d12=518.0 z=8.438616205555554
- **ROBUST_OUTLIER** `imbalance` value=1.069e+04 d1=0.0 d12=518.0 z=8.438616205555554
- **PERSISTENT_UP** `ind_generation` value=2.75e+04 d1=0.0 d12=518.0 z=8.438616205555554
- **ROBUST_OUTLIER** `ind_generation` value=2.75e+04 d1=0.0 d12=518.0 z=8.438616205555554
- **CHANGE_POINT** `biomass_gen` value=2091 d1=122.0 d12=339.0 z=1.8116460227272728
- **CHANGE_POINT** `interconnector_net` value=-6768 d1=93.0 d12=-592.0 z=-1.2561465021505378
- **PERSISTENT_UP** `biomass_gen` value=2091 d1=122.0 d12=339.0 z=1.8116460227272728
- **REVERSAL** `interconnector_net` value=-6768 d1=93.0 d12=-592.0 z=-1.2561465021505378
- **PERSISTENT_UP** `nuclear_gen` value=3336 d1=3.0 d12=5.0 z=1.2365645416666666
- **ACCELERATION** `nuclear_gen` value=3336 d1=3.0 d12=5.0 z=1.2365645416666666
- **PERSISTENT_UP** `wind_gen` value=1.379e+04 d1=54.0 d12=92.0 z=-1.099207514453125

## Nearest historical live analogues

- `2026-09-14T23:53:08.620374Z` distance=5.385 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:57:18.949614Z` distance=5.385 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:32:10.678260Z` distance=5.436 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:36:23.316269Z` distance=5.436 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:40:34.642541Z` distance=5.436 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
