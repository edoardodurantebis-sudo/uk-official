# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T08:09:34.484235Z`  
Memory snapshots: **493**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.632e+04 d1=0.0 d12=0.0 z=-50.628886859375
- **ROBUST_OUTLIER** `margin` value=3.632e+04 d1=0.0 d12=0.0 z=-50.628886859375
- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=-195.0 z=-22.065450392857144
- **ROBUST_OUTLIER** `residual_proxy` value=864 d1=0.0 d12=1249.0 z=4.691355458598727
- **CHANGE_POINT** `wind_gen` value=7117 d1=-113.0 d12=-1004.0 z=-1.834283100609756
- **CHANGE_POINT** `ps_gen` value=230 d1=0.0 d12=8.0 z=1.3489795
- **CHANGE_POINT** `ind_generation` value=2.644e+04 d1=0.0 d12=2.0 z=0.6825674715568862
- **PERSISTENT_UP** `interconnector_net` value=1.007e+04 d1=93.0 d12=3122.0 z=2.474663758532423
- **PERSISTENT_UP** `biomass_gen` value=3239 d1=14.0 d12=9.0 z=2.360714125
- **ACCELERATION** `biomass_gen` value=3239 d1=14.0 d12=9.0 z=2.360714125
- **PERSISTENT_UP** `thermal_base` value=1.183e+04 d1=73.0 d12=152.0 z=2.0180823102329453
- **ACCELERATION** `thermal_base` value=1.183e+04 d1=73.0 d12=152.0 z=2.0180823102329453
- **PERSISTENT_UP** `ccgt_gen` value=8499 d1=77.0 d12=156.0 z=2.0153861504660453
- **ACCELERATION** `ccgt_gen` value=8499 d1=77.0 d12=156.0 z=2.0153861504660453
- **PERSISTENT_DOWN** `wind_gen` value=7117 d1=-113.0 d12=-1004.0 z=-1.834283100609756

## Nearest historical live analogues

- `2026-09-16T06:54:08.413156Z` distance=1.129 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:58:18.248300Z` distance=1.129 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T07:02:28.186045Z` distance=1.129 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T07:06:38.418412Z` distance=1.129 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T07:10:48.323528Z` distance=1.129 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
