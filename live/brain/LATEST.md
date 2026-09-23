# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T08:32:20.526470Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.265e+04 d1=0.0 d12=-4.0 z=-39.6262728125
- **PERSISTENT_DOWN** `ind_demand` value=-1.265e+04 d1=0.0 d12=-4.0 z=-39.6262728125
- **ROBUST_OUTLIER** `ind_demand` value=-1.265e+04 d1=0.0 d12=-4.0 z=-39.6262728125
- **PERSISTENT_UP** `ps_gen` value=-17 d1=50.0 d12=1.0 z=-27.1482124375
- **ACCELERATION** `ps_gen` value=-17 d1=50.0 d12=1.0 z=-27.1482124375
- **ROBUST_OUTLIER** `ps_gen` value=-17 d1=50.0 d12=1.0 z=-27.1482124375
- **CHANGE_POINT** `imbalance` value=-7271 d1=0.0 d12=183.0 z=9.157495451923078
- **PERSISTENT_UP** `imbalance` value=-7271 d1=0.0 d12=183.0 z=9.157495451923078
- **ROBUST_OUTLIER** `imbalance` value=-7271 d1=0.0 d12=183.0 z=9.157495451923078
- **CHANGE_POINT** `margin` value=3.93e+04 d1=0.0 d12=523.0 z=6.174175403846154
- **CHANGE_POINT** `ccgt_gen` value=5121 d1=-40.0 d12=-2946.0 z=-5.995874418763676
- **CHANGE_POINT** `thermal_base` value=8919 d1=-43.0 d12=-2957.0 z=-5.42988022306143
- **PERSISTENT_DOWN** `ind_generation` value=1.376e+04 d1=0.0 d12=-208.0 z=7.276706725961538
- **ROBUST_OUTLIER** `ind_generation` value=1.376e+04 d1=0.0 d12=-208.0 z=7.276706725961538
- **ROBUST_OUTLIER** `margin` value=3.93e+04 d1=0.0 d12=523.0 z=6.174175403846154

## Nearest historical live analogues

- `2026-09-23T07:24:02.339254Z` distance=0.270 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1169.0}
- `2026-09-23T07:28:16.303767Z` distance=0.270 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1169.0}
- `2026-09-23T07:32:30.264126Z` distance=0.270 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1169.0}
- `2026-09-23T07:36:43.962318Z` distance=0.270 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1169.0}
- `2026-09-23T06:20:46.707492Z` distance=0.340 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
