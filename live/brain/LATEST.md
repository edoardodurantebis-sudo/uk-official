# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T21:13:44.577743Z`  
Memory snapshots: **337**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `wind_gen` value=1.254e+04 d1=98.0 d12=1051.0 z=7.037507023897058
- **CHANGE_POINT** `thermal_base` value=1e+04 d1=-364.0 d12=-3742.0 z=-5.469000410835214
- **CHANGE_POINT** `ccgt_gen` value=6677 d1=-363.0 d12=-3744.0 z=-5.431457258127803
- **PERSISTENT_UP** `wind_gen` value=1.254e+04 d1=98.0 d12=1051.0 z=7.037507023897058
- **ROBUST_OUTLIER** `wind_gen` value=1.254e+04 d1=98.0 d12=1051.0 z=7.037507023897058
- **PERSISTENT_DOWN** `thermal_base` value=1e+04 d1=-364.0 d12=-3742.0 z=-5.469000410835214
- **ROBUST_OUTLIER** `thermal_base` value=1e+04 d1=-364.0 d12=-3742.0 z=-5.469000410835214
- **PERSISTENT_DOWN** `ccgt_gen` value=6677 d1=-363.0 d12=-3744.0 z=-5.431457258127803
- **ROBUST_OUTLIER** `ccgt_gen` value=6677 d1=-363.0 d12=-3744.0 z=-5.431457258127803
- **CHANGE_POINT** `imbalance` value=5722 d1=0.0 d12=-66.0 z=-0.9661609932432432
- **CHANGE_POINT** `ind_generation` value=2.484e+04 d1=0.0 d12=-66.0 z=-0.9661609932432432
- **PERSISTENT_DOWN** `ps_gen` value=-262 d1=-2.0 d12=-5.0 z=-0.6869145611842105
- **ACCELERATION** `ps_gen` value=-262 d1=-2.0 d12=-5.0 z=-0.6869145611842105
- **ACCELERATION** `biomass_gen` value=3265 d1=-1.0 d12=-10.0 z=0.4351546774193549
- **REVERSAL** `nuclear_gen` value=3323 d1=-1.0 d12=2.0 z=0.22482991666666666

## Nearest historical live analogues

- `2026-09-15T19:31:50.302711Z` distance=0.057 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:36:02.892054Z` distance=0.057 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:40:15.609389Z` distance=0.057 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:44:28.590533Z` distance=0.057 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:48:40.904493Z` distance=0.057 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
