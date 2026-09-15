# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T18:24:34.306197Z`  
Memory snapshots: **297**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **PERSISTENT_UP** `biomass_gen` value=3264 d1=3.0 d12=86.0 z=44.604300423913045
- **ROBUST_OUTLIER** `biomass_gen` value=3264 d1=3.0 d12=86.0 z=44.604300423913045
- **CHANGE_POINT** `ccgt_gen` value=1.071e+04 d1=14.0 d12=304.0 z=4.175649913622231
- **CHANGE_POINT** `thermal_base` value=1.402e+04 d1=15.0 d12=295.0 z=4.162670048718944
- **PERSISTENT_UP** `ind_demand` value=-1.191e+04 d1=9.0 d12=9.0 z=5.395918
- **ACCELERATION** `ind_demand` value=-1.191e+04 d1=9.0 d12=9.0 z=5.395918
- **ROBUST_OUTLIER** `ind_demand` value=-1.191e+04 d1=9.0 d12=9.0 z=5.395918
- **CHANGE_POINT** `margin` value=3.566e+04 d1=0.0 d12=835.0 z=2.206545039285714
- **PERSISTENT_UP** `ccgt_gen` value=1.071e+04 d1=14.0 d12=304.0 z=4.175649913622231
- **ROBUST_OUTLIER** `ccgt_gen` value=1.071e+04 d1=14.0 d12=304.0 z=4.175649913622231
- **PERSISTENT_UP** `thermal_base` value=1.402e+04 d1=15.0 d12=295.0 z=4.162670048718944
- **ROBUST_OUTLIER** `thermal_base` value=1.402e+04 d1=15.0 d12=295.0 z=4.162670048718944
- **CHANGE_POINT** `ps_gen` value=805 d1=1.0 d12=303.0 z=1.082378814211695
- **CHANGE_POINT** `imbalance` value=5737 d1=-38.0 d12=-35.0 z=-0.42922075000000004
- **CHANGE_POINT** `ind_generation` value=2.486e+04 d1=-38.0 d12=-35.0 z=-0.42922075000000004

## Nearest historical live analogues

- `2026-09-15T11:22:30.581865Z` distance=0.172 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:26:42.593420Z` distance=0.172 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:30:55.285075Z` distance=0.172 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:35:06.452199Z` distance=0.172 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:39:18.571623Z` distance=0.172 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
