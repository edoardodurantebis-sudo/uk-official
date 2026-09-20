# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T08:17:09.650773Z`  
Memory snapshots: **1769**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **PERSISTENT_DOWN** `biomass_gen` value=883 d1=-8.0 d12=-4.0 z=-7.8731349
- **ACCELERATION** `biomass_gen` value=883 d1=-8.0 d12=-4.0 z=-7.8731349
- **ROBUST_OUTLIER** `biomass_gen` value=883 d1=-8.0 d12=-4.0 z=-7.8731349
- **CHANGE_POINT** `interconnector_net` value=-4913 d1=-68.0 d12=3050.0 z=3.960448905263158
- **ROBUST_OUTLIER** `residual_proxy` value=1.796e+04 d1=0.0 d12=1162.0 z=5.542546206521739
- **ROBUST_OUTLIER** `margin` value=3.803e+04 d1=0.0 d12=0.0 z=5.0033045634328355
- **CHANGE_POINT** `wind_gen` value=1.48e+04 d1=29.0 d12=-875.0 z=-2.492851005847953
- **CHANGE_POINT** `ccgt_gen` value=3201 d1=73.0 d12=-586.0 z=-2.2837652943661975
- **CHANGE_POINT** `thermal_base` value=6530 d1=67.0 d12=-597.0 z=-2.2721637946927373
- **REVERSAL** `interconnector_net` value=-4913 d1=-68.0 d12=3050.0 z=3.960448905263158
- **ROBUST_OUTLIER** `interconnector_net` value=-4913 d1=-68.0 d12=3050.0 z=3.960448905263158
- **CHANGE_POINT** `ps_gen` value=-933 d1=-10.0 d12=-128.0 z=-1.6395841263297872
- **REVERSAL** `wind_gen` value=1.48e+04 d1=29.0 d12=-875.0 z=-2.492851005847953
- **CHANGE_POINT** `imbalance` value=-6364 d1=0.0 d12=0.0 z=0.39978847
- **CHANGE_POINT** `ind_generation` value=1.359e+04 d1=0.0 d12=0.0 z=0.39978847

## Nearest historical live analogues

- `2026-09-20T07:22:31.595881Z` distance=0.122 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T06:53:07.699769Z` distance=0.174 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:57:19.576758Z` distance=0.174 → {'next30m_imbalance_delta': 438.0, 'next30m_margin_delta': 348.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T07:01:30.503093Z` distance=0.174 → {'next30m_imbalance_delta': 438.0, 'next30m_margin_delta': 348.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T07:05:43.852829Z` distance=0.174 → {'next30m_imbalance_delta': 438.0, 'next30m_margin_delta': 348.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
