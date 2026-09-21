# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T02:52:34.820210Z`  
Memory snapshots: **2033**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.756e+04 d1=14.0 d12=1730.0 z=30.71522553846154
- **PERSISTENT_UP** `margin` value=3.756e+04 d1=14.0 d12=1730.0 z=30.71522553846154
- **ROBUST_OUTLIER** `margin` value=3.756e+04 d1=14.0 d12=1730.0 z=30.71522553846154
- **CHANGE_POINT** `thermal_base` value=8122 d1=-39.0 d12=-684.0 z=-1.7145152233688417
- **CHANGE_POINT** `ccgt_gen` value=4786 d1=-42.0 d12=-678.0 z=-1.6987813650265957
- **CHANGE_POINT** `ind_demand` value=-1.18e+04 d1=0.0 d12=26.0 z=1.4613944583333334
- **CHANGE_POINT** `interconnector_net` value=1.252e+04 d1=2.0 d12=290.0 z=1.1800546911237297
- **CHANGE_POINT** `imbalance` value=-4865 d1=39.0 d12=34.0 z=1.0516925485781992
- **CHANGE_POINT** `ind_generation` value=1.574e+04 d1=39.0 d12=34.0 z=1.0516925485781992
- **PERSISTENT_DOWN** `wind_gen` value=3735 d1=-32.0 d12=-103.0 z=-2.109551988521401
- **PERSISTENT_DOWN** `thermal_base` value=8122 d1=-39.0 d12=-684.0 z=-1.7145152233688417
- **PERSISTENT_DOWN** `ccgt_gen` value=4786 d1=-42.0 d12=-678.0 z=-1.6987813650265957
- **PERSISTENT_UP** `interconnector_net` value=1.252e+04 d1=2.0 d12=290.0 z=1.1800546911237297
- **PERSISTENT_UP** `imbalance` value=-4865 d1=39.0 d12=34.0 z=1.0516925485781992
- **ACCELERATION** `imbalance` value=-4865 d1=39.0 d12=34.0 z=1.0516925485781992

## Nearest historical live analogues

- `2026-09-21T01:53:20.720277Z` distance=0.848 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:57:30.190951Z` distance=0.848 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:23:21.503053Z` distance=0.851 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:28:09.159328Z` distance=0.851 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:32:22.156789Z` distance=0.851 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
