# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T08:01:03.976513Z`  
Memory snapshots: **491**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.632e+04 d1=0.0 d12=-1077.0 z=-50.628886859375
- **ROBUST_OUTLIER** `margin` value=3.632e+04 d1=0.0 d12=-1077.0 z=-50.628886859375
- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=-195.0 z=-22.065450392857144
- **ROBUST_OUTLIER** `residual_proxy` value=864 d1=0.0 d12=1249.0 z=4.691355458598727
- **CHANGE_POINT** `biomass_gen` value=3225 d1=-1.0 d12=-5.0 z=-2.360714125
- **PERSISTENT_UP** `nuclear_gen` value=3337 d1=7.0 d12=8.0 z=2.697959
- **ACCELERATION** `nuclear_gen` value=3337 d1=7.0 d12=8.0 z=2.697959
- **CHANGE_POINT** `imbalance` value=6872 d1=0.0 d12=-442.0 z=-0.5207200660621761
- **PERSISTENT_UP** `interconnector_net` value=9977 d1=190.0 d12=3070.0 z=2.453650426823299
- **PERSISTENT_UP** `thermal_base` value=1.176e+04 d1=35.0 d12=109.0 z=2.384544024001536
- **PERSISTENT_UP** `ccgt_gen` value=8422 d1=28.0 d12=101.0 z=2.3748036962437715
- **PERSISTENT_DOWN** `biomass_gen` value=3225 d1=-1.0 d12=-5.0 z=-2.360714125
- **ACCELERATION** `biomass_gen` value=3225 d1=-1.0 d12=-5.0 z=-2.360714125
- **PERSISTENT_DOWN** `wind_gen` value=7230 d1=-139.0 d12=-873.0 z=-1.8824791345161291
- **PERSISTENT_UP** `ps_gen` value=230 d1=0.0 d12=8.0 z=1.5416908571428571

## Nearest historical live analogues

- `2026-09-16T06:54:08.413156Z` distance=1.127 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:58:18.248300Z` distance=1.127 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T07:02:28.186045Z` distance=1.127 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T07:06:38.418412Z` distance=1.127 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T05:22:04.416358Z` distance=1.499 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -157.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
