# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T20:48:37.344077Z`  
Memory snapshots: **331**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `wind_gen` value=1.217e+04 d1=136.0 d12=1381.0 z=6.840716378133704
- **PERSISTENT_UP** `wind_gen` value=1.217e+04 d1=136.0 d12=1381.0 z=6.840716378133704
- **ROBUST_OUTLIER** `wind_gen` value=1.217e+04 d1=136.0 d12=1381.0 z=6.840716378133704
- **CHANGE_POINT** `thermal_base` value=1.195e+04 d1=-477.0 d12=-2005.0 z=-2.503072571106095
- **CHANGE_POINT** `ccgt_gen` value=8627 d1=-474.0 d12=-2006.0 z=-2.4824549879484303
- **CHANGE_POINT** `margin` value=3.57e+04 d1=0.0 d12=96.0 z=1.4274085406976744
- **PERSISTENT_DOWN** `thermal_base` value=1.195e+04 d1=-477.0 d12=-2005.0 z=-2.503072571106095
- **PERSISTENT_DOWN** `ccgt_gen` value=8627 d1=-474.0 d12=-2006.0 z=-2.4824549879484303
- **CHANGE_POINT** `imbalance` value=5788 d1=0.0 d12=37.0 z=0.23698288513513513
- **CHANGE_POINT** `ind_generation` value=2.491e+04 d1=0.0 d12=37.0 z=0.23698288513513513
- **REVERSAL** `ps_gen` value=-262 d1=2.0 d12=-387.0 z=-0.6869145611842105
- **PERSISTENT_UP** `biomass_gen` value=3285 d1=5.0 d12=22.0 z=0.6556886419860627
- **REVERSAL** `nuclear_gen` value=3321 d1=-3.0 d12=1.0 z=-0.22482991666666666
- **ACCELERATION** `nuclear_gen` value=3321 d1=-3.0 d12=1.0 z=-0.22482991666666666
- **REVERSAL** `interconnector_net` value=127 d1=24.0 d12=-465.0 z=-0.12136469960883571

## Nearest historical live analogues

- `2026-09-15T19:31:50.302711Z` distance=0.033 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:36:02.892054Z` distance=0.033 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:40:15.609389Z` distance=0.033 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:44:28.590533Z` distance=0.033 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:48:40.904493Z` distance=0.033 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
