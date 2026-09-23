# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T06:08:07.177579Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2559 d1=-7.0 d12=-37.0 z=-7.600054147321429
- **CHANGE_POINT** `nuclear_gen` value=3805 d1=1.0 d12=1.0 z=6.937608857142857
- **PERSISTENT_DOWN** `biomass_gen` value=2559 d1=-7.0 d12=-37.0 z=-7.600054147321429
- **ROBUST_OUTLIER** `biomass_gen` value=2559 d1=-7.0 d12=-37.0 z=-7.600054147321429
- **ROBUST_OUTLIER** `nuclear_gen` value=3805 d1=1.0 d12=1.0 z=6.937608857142857
- **CHANGE_POINT** `imbalance` value=-7925 d1=0.0 d12=89.0 z=2.7354306527777776
- **CHANGE_POINT** `ind_generation` value=1.325e+04 d1=0.0 d12=89.0 z=2.7354306527777776
- **CHANGE_POINT** `thermal_base` value=1.346e+04 d1=-60.0 d12=1226.0 z=0.587252905362776
- **CHANGE_POINT** `ccgt_gen` value=9660 d1=-61.0 d12=1225.0 z=0.4617238776422764
- **REVERSAL** `wind_gen` value=8136 d1=69.0 d12=-776.0 z=1.4015992677304965
- **PERSISTENT_UP** `interconnector_net` value=-4017 d1=425.0 d12=857.0 z=-0.7194827561598558
- **ACCELERATION** `interconnector_net` value=-4017 d1=425.0 d12=857.0 z=-0.7194827561598558
- **REVERSAL** `thermal_base` value=1.346e+04 d1=-60.0 d12=1226.0 z=0.587252905362776
- **REVERSAL** `ccgt_gen` value=9660 d1=-61.0 d12=1225.0 z=0.4617238776422764
- **PERSISTENT_UP** `ps_gen` value=145 d1=83.0 d12=107.0 z=0.22482991666666666

## Nearest historical live analogues

- `2026-09-23T03:32:33.216215Z` distance=0.025 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T03:36:43.352003Z` distance=0.025 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T03:40:54.258660Z` distance=0.025 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T03:45:06.650607Z` distance=0.025 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T03:49:19.033601Z` distance=0.025 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
