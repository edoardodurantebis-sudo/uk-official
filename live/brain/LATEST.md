# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T16:04:50.781494Z`  
Memory snapshots: **2220**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.569e+04 d1=0.0 d12=2506.0 z=6.194043802177858
- **CHANGE_POINT** `ccgt_gen` value=1.219e+04 d1=0.0 d12=2503.0 z=6.044741325884956
- **PERSISTENT_UP** `thermal_base` value=1.569e+04 d1=0.0 d12=2506.0 z=6.194043802177858
- **ROBUST_OUTLIER** `thermal_base` value=1.569e+04 d1=0.0 d12=2506.0 z=6.194043802177858
- **PERSISTENT_UP** `ccgt_gen` value=1.219e+04 d1=0.0 d12=2503.0 z=6.044741325884956
- **ROBUST_OUTLIER** `ccgt_gen` value=1.219e+04 d1=0.0 d12=2503.0 z=6.044741325884956
- **CHANGE_POINT** `interconnector_net` value=1.06e+04 d1=-198.0 d12=-632.0 z=-2.114170805623472
- **CHANGE_POINT** `margin` value=3.621e+04 d1=0.0 d12=-47.0 z=-0.854945341008772
- **CHANGE_POINT** `imbalance` value=-3079 d1=0.0 d12=128.0 z=0.67448975
- **CHANGE_POINT** `ind_generation` value=1.838e+04 d1=0.0 d12=83.0 z=0.4354973188976378
- **PERSISTENT_DOWN** `interconnector_net` value=1.06e+04 d1=-198.0 d12=-632.0 z=-2.114170805623472
- **CHANGE_POINT** `nuclear_gen` value=3502 d1=0.0 d12=3.0 z=0.044965983333333334
- **ACCELERATION** `ps_gen` value=-88 d1=0.0 d12=-67.0 z=-0.7229824771241831
- **PERSISTENT_UP** `imbalance` value=-3079 d1=0.0 d12=128.0 z=0.67448975
- **PERSISTENT_UP** `ind_generation` value=1.838e+04 d1=0.0 d12=83.0 z=0.4354973188976378

## Nearest historical live analogues

- `2026-09-21T14:23:01.446169Z` distance=0.033 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:27:16.085310Z` distance=0.033 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:31:28.406523Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:35:41.380076Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:39:54.228512Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
