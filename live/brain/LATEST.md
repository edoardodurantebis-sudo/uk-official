# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T21:37:22.236065Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.721e+04 d1=-161.0 d12=-1106.0 z=-3.066040489114659
- **CHANGE_POINT** `ccgt_gen` value=1.348e+04 d1=-165.0 d12=-1112.0 z=-3.051725958213256
- **CHANGE_POINT** `interconnector_net` value=4759 d1=11.0 d12=-1866.0 z=-2.5263550262770136
- **CHANGE_POINT** `imbalance` value=-8019 d1=0.0 d12=19.0 z=-1.8628764523809522
- **CHANGE_POINT** `ind_generation` value=1.315e+04 d1=0.0 d12=19.0 z=-1.8628764523809522
- **CHANGE_POINT** `margin` value=3.721e+04 d1=0.0 d12=78.0 z=1.42991827
- **PERSISTENT_DOWN** `thermal_base` value=1.721e+04 d1=-161.0 d12=-1106.0 z=-3.066040489114659
- **ROBUST_OUTLIER** `thermal_base` value=1.721e+04 d1=-161.0 d12=-1106.0 z=-3.066040489114659
- **PERSISTENT_DOWN** `ccgt_gen` value=1.348e+04 d1=-165.0 d12=-1112.0 z=-3.051725958213256
- **ROBUST_OUTLIER** `ccgt_gen` value=1.348e+04 d1=-165.0 d12=-1112.0 z=-3.051725958213256
- **REVERSAL** `interconnector_net` value=4759 d1=11.0 d12=-1866.0 z=-2.5263550262770136
- **ACCELERATION** `interconnector_net` value=4759 d1=11.0 d12=-1866.0 z=-2.5263550262770136
- **CHANGE_POINT** `biomass_gen` value=2914 d1=4.0 d12=-3.0 z=0.3161670703125
- **PERSISTENT_UP** `nuclear_gen` value=3736 d1=4.0 d12=6.0 z=2.0234692499999998
- **ACCELERATION** `nuclear_gen` value=3736 d1=4.0 d12=6.0 z=2.0234692499999998

## Nearest historical live analogues

- `2026-09-22T17:22:55.061007Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:27:09.876357Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:31:30.036637Z` distance=0.021 → {'next30m_imbalance_delta': -2.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:35:44.591045Z` distance=0.021 → {'next30m_imbalance_delta': -2.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:39:59.899041Z` distance=0.021 → {'next30m_imbalance_delta': -2.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
