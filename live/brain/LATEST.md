# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T14:01:53.716346Z`  
Memory snapshots: **2191**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.23e+04 d1=0.0 d12=-57.0 z=13.334143519230768
- **PERSISTENT_DOWN** `ind_demand` value=-1.23e+04 d1=0.0 d12=-57.0 z=13.334143519230768
- **ACCELERATION** `ind_demand` value=-1.23e+04 d1=0.0 d12=-57.0 z=13.334143519230768
- **ROBUST_OUTLIER** `ind_demand` value=-1.23e+04 d1=0.0 d12=-57.0 z=13.334143519230768
- **ROBUST_OUTLIER** `ps_gen` value=219 d1=0.0 d12=-9.0 z=6.71277894047619
- **CHANGE_POINT** `wind_gen` value=4262 d1=-6.0 d12=242.0 z=0.9175107092288244
- **CHANGE_POINT** `margin` value=3.627e+04 d1=0.0 d12=-4.0 z=-0.8533647807244501
- **CHANGE_POINT** `ccgt_gen` value=7176 d1=-98.0 d12=1053.0 z=0.051697996597421206
- **CHANGE_POINT** `thermal_base` value=1.068e+04 d1=-102.0 d12=1044.0 z=0.04597682124728064
- **REVERSAL** `wind_gen` value=4262 d1=-6.0 d12=242.0 z=0.9175107092288244
- **PERSISTENT_DOWN** `interconnector_net` value=1.144e+04 d1=-34.0 d12=-6.0 z=0.9171415503048781
- **ACCELERATION** `interconnector_net` value=1.144e+04 d1=-34.0 d12=-6.0 z=0.9171415503048781
- **PERSISTENT_DOWN** `margin` value=3.627e+04 d1=0.0 d12=-4.0 z=-0.8533647807244501
- **ACCELERATION** `imbalance` value=-3238 d1=0.0 d12=10.0 z=-0.47299123977987423
- **ACCELERATION** `ind_generation` value=1.827e+04 d1=0.0 d12=10.0 z=-0.29093078191489363

## Nearest historical live analogues

- `2026-09-21T12:57:13.016306Z` distance=0.067 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T13:01:25.788515Z` distance=0.067 → {'next30m_imbalance_delta': 17.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T13:05:39.062581Z` distance=0.067 → {'next30m_imbalance_delta': 17.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T12:53:00.200547Z` distance=0.071 → {'next30m_imbalance_delta': 85.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:54:44.355248Z` distance=0.121 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
