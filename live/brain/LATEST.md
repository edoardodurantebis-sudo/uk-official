# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T15:26:27.469405Z`  
Memory snapshots: **2211**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.365e+04 d1=228.0 d12=1707.0 z=3.7029609686932847
- **CHANGE_POINT** `ccgt_gen` value=1.016e+04 d1=229.0 d12=1702.0 z=3.624934736061947
- **PERSISTENT_UP** `thermal_base` value=1.365e+04 d1=228.0 d12=1707.0 z=3.7029609686932847
- **ROBUST_OUTLIER** `thermal_base` value=1.365e+04 d1=228.0 d12=1707.0 z=3.7029609686932847
- **PERSISTENT_UP** `ccgt_gen` value=1.016e+04 d1=229.0 d12=1702.0 z=3.624934736061947
- **ROBUST_OUTLIER** `ccgt_gen` value=1.016e+04 d1=229.0 d12=1702.0 z=3.624934736061947
- **CHANGE_POINT** `ps_gen` value=-21 d1=0.0 d12=-86.0 z=-0.7326354181034482
- **CHANGE_POINT** `wind_gen` value=3338 d1=2.0 d12=-866.0 z=-0.5751354507261411
- **CHANGE_POINT** `imbalance` value=-3107 d1=100.0 d12=99.0 z=0.3496046348167539
- **CHANGE_POINT** `interconnector_net` value=1.116e+04 d1=-48.0 d12=-284.0 z=-0.24665313656884877
- **CHANGE_POINT** `ind_generation` value=1.835e+04 d1=55.0 d12=54.0 z=0.19069343717277487
- **PERSISTENT_DOWN** `biomass_gen` value=2953 d1=0.0 d12=-15.0 z=-1.7151310785714284
- **ACCELERATION** `biomass_gen` value=2953 d1=0.0 d12=-15.0 z=-1.7151310785714284
- **PERSISTENT_UP** `margin` value=3.626e+04 d1=0.0 d12=12.0 z=-0.6911027980295567
- **REVERSAL** `nuclear_gen` value=3494 d1=-1.0 d12=5.0 z=-0.5781340714285713

## Nearest historical live analogues

- `2026-09-21T13:57:37.194603Z` distance=0.023 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:01:53.716346Z` distance=0.023 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:06:06.412176Z` distance=0.023 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:10:22.067665Z` distance=0.023 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:14:36.526736Z` distance=0.023 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
