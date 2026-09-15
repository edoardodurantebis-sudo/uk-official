# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T01:54:40.060641Z`  
Memory snapshots: **62**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.232e+04 d1=0.0 d12=32.0 z=-1.785414044117647
- **CHANGE_POINT** `ccgt_gen` value=3407 d1=-45.0 d12=-197.0 z=-0.8105652766731329
- **CHANGE_POINT** `thermal_base` value=6735 d1=-46.0 d12=-193.0 z=-0.8095200826790971
- **CHANGE_POINT** `wind_gen` value=1.254e+04 d1=-48.0 d12=466.0 z=0.5376006863468634
- **REVERSAL** `nuclear_gen` value=3328 d1=-1.0 d12=4.0 z=2.0234692499999998
- **PERSISTENT_UP** `margin` value=3.273e+04 d1=0.0 d12=65.0 z=0.8541277236180904
- **ACCELERATION** `margin` value=3.273e+04 d1=0.0 d12=65.0 z=0.8541277236180904
- **PERSISTENT_DOWN** `ccgt_gen` value=3407 d1=-45.0 d12=-197.0 z=-0.8105652766731329
- **PERSISTENT_DOWN** `thermal_base` value=6735 d1=-46.0 d12=-193.0 z=-0.8095200826790971
- **REVERSAL** `wind_gen` value=1.254e+04 d1=-48.0 d12=466.0 z=0.5376006863468634
- **PERSISTENT_DOWN** `ind_generation` value=2.073e+04 d1=-2.0 d12=-27.0 z=0.45768947321428566
- **PERSISTENT_DOWN** `imbalance` value=244 d1=-2.0 d12=-28.0 z=0.45230489117647055
- **PERSISTENT_DOWN** `interconnector_net` value=-1599 d1=-12.0 d12=-1730.0 z=-0.004711220605355063

## Nearest historical live analogues

- `2026-09-15T00:51:49.246305Z` distance=1.351 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T00:55:59.461560Z` distance=1.351 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 25.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T01:00:10.370005Z` distance=1.351 → {'next30m_imbalance_delta': -26.0, 'next30m_margin_delta': 25.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T00:22:28.991704Z` distance=1.835 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T00:26:37.805564Z` distance=1.835 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': -29.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
