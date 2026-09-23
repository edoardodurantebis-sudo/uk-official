# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T08:40:52.174403Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.265e+04 d1=0.0 d12=-4.0 z=-39.6262728125
- **PERSISTENT_UP** `ps_gen` value=-17 d1=0.0 d12=1.0 z=-21.516223025
- **ROBUST_OUTLIER** `ps_gen` value=-17 d1=0.0 d12=1.0 z=-21.516223025
- **ROBUST_OUTLIER** `imbalance` value=-7271 d1=0.0 d12=183.0 z=9.157495451923078
- **CHANGE_POINT** `ccgt_gen` value=4893 d1=-219.0 d12=-2797.0 z=-6.158853634061834
- **ROBUST_OUTLIER** `ind_generation` value=1.376e+04 d1=0.0 d12=-208.0 z=7.276706725961538
- **CHANGE_POINT** `thermal_base` value=8697 d1=-216.0 d12=-2803.0 z=-5.228848255294659
- **ROBUST_OUTLIER** `margin` value=3.93e+04 d1=0.0 d12=523.0 z=6.174175403846154
- **PERSISTENT_DOWN** `ccgt_gen` value=4893 d1=-219.0 d12=-2797.0 z=-6.158853634061834
- **ROBUST_OUTLIER** `ccgt_gen` value=4893 d1=-219.0 d12=-2797.0 z=-6.158853634061834
- **PERSISTENT_DOWN** `thermal_base` value=8697 d1=-216.0 d12=-2803.0 z=-5.228848255294659
- **ROBUST_OUTLIER** `thermal_base` value=8697 d1=-216.0 d12=-2803.0 z=-5.228848255294659
- **PERSISTENT_UP** `interconnector_net` value=9866 d1=50.0 d12=6067.0 z=4.901487369370591
- **ROBUST_OUTLIER** `interconnector_net` value=9866 d1=50.0 d12=6067.0 z=4.901487369370591
- **CHANGE_POINT** `biomass_gen` value=2333 d1=16.0 d12=-222.0 z=-0.8162614808917198

## Nearest historical live analogues

- `2026-09-23T07:24:02.339254Z` distance=0.270 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1169.0}
- `2026-09-23T07:28:16.303767Z` distance=0.270 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1169.0}
- `2026-09-23T07:32:30.264126Z` distance=0.270 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1169.0}
- `2026-09-23T07:36:43.962318Z` distance=0.270 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1169.0}
- `2026-09-23T07:40:56.431050Z` distance=0.270 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1169.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
