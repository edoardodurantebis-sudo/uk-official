# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T18:04:37.827459Z`  
Memory snapshots: **1567**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=7021 d1=36.0 d12=817.0 z=6.078653345965771
- **CHANGE_POINT** `thermal_base` value=1.034e+04 d1=36.0 d12=811.0 z=6.0124310281477
- **PERSISTENT_UP** `ccgt_gen` value=7021 d1=36.0 d12=817.0 z=6.078653345965771
- **ROBUST_OUTLIER** `ccgt_gen` value=7021 d1=36.0 d12=817.0 z=6.078653345965771
- **PERSISTENT_UP** `thermal_base` value=1.034e+04 d1=36.0 d12=811.0 z=6.0124310281477
- **ROBUST_OUTLIER** `thermal_base` value=1.034e+04 d1=36.0 d12=811.0 z=6.0124310281477
- **CHANGE_POINT** `ind_generation` value=1.681e+04 d1=0.0 d12=11.0 z=2.5480723888888885
- **CHANGE_POINT** `biomass_gen` value=759 d1=29.0 d12=154.0 z=1.5632291852941176
- **REVERSAL** `ps_gen` value=824 d1=18.0 d12=-7.0 z=3.524843923640167
- **ACCELERATION** `ps_gen` value=824 d1=18.0 d12=-7.0 z=3.524843923640167
- **ROBUST_OUTLIER** `ps_gen` value=824 d1=18.0 d12=-7.0 z=3.524843923640167
- **CHANGE_POINT** `imbalance` value=-3139 d1=0.0 d12=11.0 z=1.187688472826087
- **ROBUST_OUTLIER** `residual_proxy` value=1.259e+04 d1=0.0 d12=0.0 z=-3.1556484732142858
- **CHANGE_POINT** `wind_gen` value=1.428e+04 d1=1.0 d12=-414.0 z=-0.6315514104774537
- **PERSISTENT_DOWN** `nuclear_gen` value=3324 d1=0.0 d12=-6.0 z=-2.360714125

## Nearest historical live analogues

- `2026-09-19T16:52:42.433757Z` distance=0.014 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T16:56:53.146650Z` distance=0.014 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:01:39.109374Z` distance=0.014 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:05:49.699644Z` distance=0.014 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:10:02.143135Z` distance=0.014 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
