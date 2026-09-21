# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T16:00:35.791303Z`  
Memory snapshots: **2219**  
Current physical regime: **BALANCED**

## Active patterns

- **PERSISTENT_UP** `thermal_base` value=1.569e+04 d1=387.0 d12=2610.0 z=6.194043802177858
- **ROBUST_OUTLIER** `thermal_base` value=1.569e+04 d1=387.0 d12=2610.0 z=6.194043802177858
- **PERSISTENT_UP** `ccgt_gen` value=1.219e+04 d1=391.0 d12=2601.0 z=6.044741325884956
- **ROBUST_OUTLIER** `ccgt_gen` value=1.219e+04 d1=391.0 d12=2601.0 z=6.044741325884956
- **CHANGE_POINT** `interconnector_net` value=1.08e+04 d1=-70.0 d12=-435.0 z=-1.4611196051344744
- **CHANGE_POINT** `imbalance` value=-3079 d1=0.0 d12=128.0 z=0.67448975
- **CHANGE_POINT** `ind_generation` value=1.838e+04 d1=0.0 d12=83.0 z=0.4354973188976378
- **PERSISTENT_DOWN** `interconnector_net` value=1.08e+04 d1=-70.0 d12=-435.0 z=-1.4611196051344744
- **PERSISTENT_DOWN** `margin` value=3.621e+04 d1=0.0 d12=-47.0 z=-0.854945341008772
- **REVERSAL** `ps_gen` value=-88 d1=38.0 d12=-82.0 z=-0.778988161971831
- **PERSISTENT_UP** `imbalance` value=-3079 d1=0.0 d12=128.0 z=0.67448975
- **PERSISTENT_UP** `ind_generation` value=1.838e+04 d1=0.0 d12=83.0 z=0.4354973188976378
- **PERSISTENT_DOWN** `wind_gen` value=3354 d1=-3.0 d12=-26.0 z=-0.3784265924092409
- **REVERSAL** `biomass_gen` value=2969 d1=-1.0 d12=4.0 z=-0.302357474137931
- **ACCELERATION** `biomass_gen` value=2969 d1=-1.0 d12=4.0 z=-0.302357474137931

## Nearest historical live analogues

- `2026-09-21T14:23:01.446169Z` distance=0.033 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:27:16.085310Z` distance=0.033 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:31:28.406523Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:35:41.380076Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:39:54.228512Z` distance=0.033 → {'next30m_imbalance_delta': -1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
