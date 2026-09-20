# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T01:01:05.027789Z`  
Memory snapshots: **1666**  
Current physical regime: **BALANCED**

## Active patterns

- **PERSISTENT_DOWN** `ind_demand` value=-1.195e+04 d1=0.0 d12=-60.0 z=-25.293365625
- **ROBUST_OUTLIER** `ind_demand` value=-1.195e+04 d1=0.0 d12=-60.0 z=-25.293365625
- **PERSISTENT_DOWN** `ps_gen` value=-254 d1=-2.0 d12=-110.0 z=-3.379963956128134
- **ROBUST_OUTLIER** `ps_gen` value=-254 d1=-2.0 d12=-110.0 z=-3.379963956128134
- **CHANGE_POINT** `imbalance` value=-3763 d1=0.0 d12=-55.0 z=0.519539402027027
- **CHANGE_POINT** `ind_generation` value=1.619e+04 d1=0.0 d12=-55.0 z=0.519539402027027
- **PERSISTENT_UP** `thermal_base` value=7381 d1=108.0 d12=802.0 z=-1.362436671553809
- **PERSISTENT_UP** `ccgt_gen` value=4050 d1=111.0 d12=801.0 z=-1.3530378017448859
- **PERSISTENT_DOWN** `wind_gen` value=1.557e+04 d1=-21.0 d12=-454.0 z=1.1390760508298754
- **PERSISTENT_DOWN** `interconnector_net` value=-9444 d1=-121.0 d12=-682.0 z=-0.8213866396258828
- **PERSISTENT_DOWN** `imbalance` value=-3763 d1=0.0 d12=-55.0 z=0.519539402027027
- **PERSISTENT_DOWN** `ind_generation` value=1.619e+04 d1=0.0 d12=-55.0 z=0.519539402027027
- **REVERSAL** `nuclear_gen` value=3331 d1=-3.0 d12=1.0 z=-0.5058673124999999
- **PERSISTENT_UP** `margin` value=3.603e+04 d1=0.0 d12=33.0 z=-0.3412124617647059
- **PERSISTENT_UP** `biomass_gen` value=900 d1=15.0 d12=16.0 z=-0.18395175

## Nearest historical live analogues

- `2026-09-20T00:05:59.440118Z` distance=0.069 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T23:53:21.201980Z` distance=0.121 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T23:57:34.023150Z` distance=0.121 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T23:32:17.355228Z` distance=0.122 → {'next30m_imbalance_delta': 232.0, 'next30m_margin_delta': -76.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T23:36:30.492110Z` distance=0.122 → {'next30m_imbalance_delta': 232.0, 'next30m_margin_delta': -76.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
