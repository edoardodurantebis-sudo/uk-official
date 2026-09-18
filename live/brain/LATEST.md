# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T04:05:42.091579Z`  
Memory snapshots: **1081**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.817e+04 d1=0.0 d12=-6.0 z=8.44166077734375
- **CHANGE_POINT** `imbalance` value=1.069e+04 d1=0.0 d12=518.0 z=8.438616205555554
- **CHANGE_POINT** `ind_generation` value=2.75e+04 d1=0.0 d12=518.0 z=8.438616205555554
- **ROBUST_OUTLIER** `margin` value=3.817e+04 d1=0.0 d12=-6.0 z=8.44166077734375
- **ROBUST_OUTLIER** `imbalance` value=1.069e+04 d1=0.0 d12=518.0 z=8.438616205555554
- **ROBUST_OUTLIER** `ind_generation` value=2.75e+04 d1=0.0 d12=518.0 z=8.438616205555554
- **CHANGE_POINT** `biomass_gen` value=2130 d1=39.0 d12=378.0 z=2.2464410681818183
- **CHANGE_POINT** `interconnector_net` value=-6907 d1=-139.0 d12=-731.0 z=-1.3761822923991727
- **PERSISTENT_UP** `biomass_gen` value=2130 d1=39.0 d12=378.0 z=2.2464410681818183
- **PERSISTENT_DOWN** `ccgt_gen` value=3307 d1=-162.0 d12=-115.0 z=-1.3775213825167036
- **PERSISTENT_DOWN** `thermal_base` value=6644 d1=-161.0 d12=-109.0 z=-1.3489795
- **ACCELERATION** `thermal_base` value=6644 d1=-161.0 d12=-109.0 z=-1.3489795
- **PERSISTENT_UP** `nuclear_gen` value=3337 d1=1.0 d12=6.0 z=1.3489794999999998
- **PERSISTENT_UP** `wind_gen` value=1.382e+04 d1=30.0 d12=122.0 z=-0.9512560607902735

## Nearest historical live analogues

- `2026-09-14T23:53:08.620374Z` distance=5.396 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:57:18.949614Z` distance=5.396 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:32:10.678260Z` distance=5.447 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:36:23.316269Z` distance=5.447 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:40:34.642541Z` distance=5.447 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
