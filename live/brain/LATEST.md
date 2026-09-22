# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T21:12:03.980282Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-8041 d1=0.0 d12=-5.0 z=-3.8670745666666666
- **CHANGE_POINT** `ind_generation` value=1.313e+04 d1=0.0 d12=-5.0 z=-2.697959
- **ROBUST_OUTLIER** `imbalance` value=-8041 d1=0.0 d12=-5.0 z=-3.8670745666666666
- **CHANGE_POINT** `margin` value=3.721e+04 d1=0.0 d12=78.0 z=1.8307578928571426
- **CHANGE_POINT** `thermal_base` value=1.81e+04 d1=-207.0 d12=-706.0 z=-1.337232218432511
- **CHANGE_POINT** `ccgt_gen` value=1.436e+04 d1=-197.0 d12=-706.0 z=-1.3275979805475504
- **CHANGE_POINT** `biomass_gen` value=2920 d1=4.0 d12=75.0 z=0.5058673124999999
- **PERSISTENT_DOWN** `thermal_base` value=1.81e+04 d1=-207.0 d12=-706.0 z=-1.337232218432511
- **PERSISTENT_DOWN** `ccgt_gen` value=1.436e+04 d1=-197.0 d12=-706.0 z=-1.3275979805475504
- **PERSISTENT_DOWN** `interconnector_net` value=5684 d1=-224.0 d12=-1020.0 z=-1.1948104142857143
- **ACCELERATION** `interconnector_net` value=5684 d1=-224.0 d12=-1020.0 z=-1.1948104142857143
- **PERSISTENT_DOWN** `nuclear_gen` value=3732 d1=-10.0 d12=0.0 z=0.67448975
- **ACCELERATION** `nuclear_gen` value=3732 d1=-10.0 d12=0.0 z=0.67448975
- **PERSISTENT_UP** `biomass_gen` value=2920 d1=4.0 d12=75.0 z=0.5058673124999999

## Nearest historical live analogues

- `2026-09-22T17:22:55.061007Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:27:09.876357Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:31:30.036637Z` distance=0.021 → {'next30m_imbalance_delta': -2.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:35:44.591045Z` distance=0.021 → {'next30m_imbalance_delta': -2.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:39:59.899041Z` distance=0.021 → {'next30m_imbalance_delta': -2.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
