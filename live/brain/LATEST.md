# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T09:25:46.604177Z`  
Memory snapshots: **1157**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1731 d1=-1.0 d12=-421.0 z=-18.21122325
- **PERSISTENT_DOWN** `biomass_gen` value=1731 d1=-1.0 d12=-421.0 z=-18.21122325
- **ROBUST_OUTLIER** `biomass_gen` value=1731 d1=-1.0 d12=-421.0 z=-18.21122325
- **PERSISTENT_DOWN** `ind_demand` value=-1.318e+04 d1=0.0 d12=-1449.0 z=-16.121137728395063
- **ACCELERATION** `ind_demand` value=-1.318e+04 d1=0.0 d12=-1449.0 z=-16.121137728395063
- **ROBUST_OUTLIER** `ind_demand` value=-1.318e+04 d1=0.0 d12=-1449.0 z=-16.121137728395063
- **PERSISTENT_DOWN** `imbalance` value=8100 d1=0.0 d12=-1525.0 z=-8.313086168749999
- **ACCELERATION** `imbalance` value=8100 d1=0.0 d12=-1525.0 z=-8.313086168749999
- **ROBUST_OUTLIER** `imbalance` value=8100 d1=0.0 d12=-1525.0 z=-8.313086168749999
- **PERSISTENT_DOWN** `margin` value=3.621e+04 d1=0.0 d12=-1444.0 z=-7.524121683229814
- **ACCELERATION** `margin` value=3.621e+04 d1=0.0 d12=-1444.0 z=-7.524121683229814
- **ROBUST_OUTLIER** `margin` value=3.621e+04 d1=0.0 d12=-1444.0 z=-7.524121683229814
- **CHANGE_POINT** `ps_gen` value=-427 d1=1.0 d12=-801.0 z=-3.757267353448276
- **CHANGE_POINT** `wind_gen` value=1.161e+04 d1=-29.0 d12=-632.0 z=-3.4789912851368157
- **ROBUST_OUTLIER** `residual_proxy` value=8755 d1=0.0 d12=0.0 z=4.683956597222222

## Nearest historical live analogues

- `2026-09-18T08:22:03.400207Z` distance=1.865 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 74.0}
- `2026-09-18T08:26:15.822729Z` distance=1.865 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 74.0}
- `2026-09-18T08:30:26.157851Z` distance=1.865 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 74.0}
- `2026-09-18T08:17:51.592822Z` distance=1.878 → {'next30m_imbalance_delta': -593.0, 'next30m_margin_delta': -112.0, 'next30m_residual_proxy_delta': 74.0}
- `2026-09-18T07:23:09.699179Z` distance=1.879 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
