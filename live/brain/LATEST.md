# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T09:30:05.383319Z`  
Memory snapshots: **1158**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1731 d1=0.0 d12=-433.0 z=-18.21122325
- **ROBUST_OUTLIER** `biomass_gen` value=1731 d1=0.0 d12=-433.0 z=-18.21122325
- **PERSISTENT_DOWN** `ind_demand` value=-1.318e+04 d1=0.0 d12=-1449.0 z=-16.121137728395063
- **ROBUST_OUTLIER** `ind_demand` value=-1.318e+04 d1=0.0 d12=-1449.0 z=-16.121137728395063
- **PERSISTENT_DOWN** `imbalance` value=8100 d1=0.0 d12=-1525.0 z=-8.313086168749999
- **ROBUST_OUTLIER** `imbalance` value=8100 d1=0.0 d12=-1525.0 z=-8.313086168749999
- **PERSISTENT_DOWN** `margin` value=3.621e+04 d1=0.0 d12=-1444.0 z=-7.524121683229814
- **ROBUST_OUTLIER** `margin` value=3.621e+04 d1=0.0 d12=-1444.0 z=-7.524121683229814
- **CHANGE_POINT** `ps_gen` value=-427 d1=0.0 d12=-647.0 z=-3.757267353448276
- **CHANGE_POINT** `wind_gen` value=1.161e+04 d1=0.0 d12=-656.0 z=-3.078153111572536
- **PERSISTENT_DOWN** `ps_gen` value=-427 d1=0.0 d12=-647.0 z=-3.757267353448276
- **ROBUST_OUTLIER** `ps_gen` value=-427 d1=0.0 d12=-647.0 z=-3.757267353448276
- **CHANGE_POINT** `interconnector_net` value=3896 d1=0.0 d12=967.0 z=1.5165677535153328
- **PERSISTENT_DOWN** `wind_gen` value=1.161e+04 d1=0.0 d12=-656.0 z=-3.078153111572536
- **ROBUST_OUTLIER** `wind_gen` value=1.161e+04 d1=0.0 d12=-656.0 z=-3.078153111572536

## Nearest historical live analogues

- `2026-09-18T08:34:36.525091Z` distance=1.864 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:22:03.400207Z` distance=1.865 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 74.0}
- `2026-09-18T08:26:15.822729Z` distance=1.865 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 74.0}
- `2026-09-18T08:30:26.157851Z` distance=1.865 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 74.0}
- `2026-09-18T08:17:51.592822Z` distance=1.878 → {'next30m_imbalance_delta': -593.0, 'next30m_margin_delta': -112.0, 'next30m_residual_proxy_delta': 74.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
