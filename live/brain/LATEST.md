# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T15:22:11.004183Z`  
Memory snapshots: **2210**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.342e+04 d1=142.0 d12=1751.0 z=3.4238617617967333
- **CHANGE_POINT** `ccgt_gen` value=9930 d1=142.0 d12=1752.0 z=3.3515574745575223
- **PERSISTENT_UP** `thermal_base` value=1.342e+04 d1=142.0 d12=1751.0 z=3.4238617617967333
- **ROBUST_OUTLIER** `thermal_base` value=1.342e+04 d1=142.0 d12=1751.0 z=3.4238617617967333
- **PERSISTENT_UP** `ccgt_gen` value=9930 d1=142.0 d12=1752.0 z=3.3515574745575223
- **ROBUST_OUTLIER** `ccgt_gen` value=9930 d1=142.0 d12=1752.0 z=3.3515574745575223
- **CHANGE_POINT** `ps_gen` value=-21 d1=0.0 d12=2.0 z=-0.735807
- **CHANGE_POINT** `wind_gen` value=3336 d1=-10.0 d12=-933.0 z=-0.5976177564338235
- **CHANGE_POINT** `interconnector_net` value=1.121e+04 d1=-24.0 d12=-258.0 z=-0.0982700298013245
- **PERSISTENT_DOWN** `biomass_gen` value=2953 d1=-9.0 d12=-8.0 z=-1.7151310785714284
- **ACCELERATION** `biomass_gen` value=2953 d1=-9.0 d12=-8.0 z=-1.7151310785714284
- **PERSISTENT_UP** `margin` value=3.626e+04 d1=4.0 d12=12.0 z=-0.6911027980295567
- **PERSISTENT_DOWN** `wind_gen` value=3336 d1=-10.0 d12=-933.0 z=-0.5976177564338235
- **PERSISTENT_DOWN** `residual_proxy` value=1.234e+04 d1=-45.0 d12=-45.0 z=0.5249723177339901
- **ACCELERATION** `residual_proxy` value=1.234e+04 d1=-45.0 d12=-45.0 z=0.5249723177339901

## Nearest historical live analogues

- `2026-09-21T13:57:37.194603Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:01:53.716346Z` distance=0.005 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:06:06.412176Z` distance=0.005 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:10:22.067665Z` distance=0.005 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:14:36.526736Z` distance=0.005 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
