# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T09:39:05.140398Z`  
Memory snapshots: **1160**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1710 d1=-22.0 d12=-434.0 z=-19.096491046875
- **PERSISTENT_DOWN** `biomass_gen` value=1710 d1=-22.0 d12=-434.0 z=-19.096491046875
- **ROBUST_OUTLIER** `biomass_gen` value=1710 d1=-22.0 d12=-434.0 z=-19.096491046875
- **CHANGE_POINT** `ind_demand` value=-1.318e+04 d1=0.0 d12=-1449.0 z=-16.121137728395063
- **ROBUST_OUTLIER** `ind_demand` value=-1.318e+04 d1=0.0 d12=-1449.0 z=-16.121137728395063
- **CHANGE_POINT** `imbalance` value=8100 d1=0.0 d12=-1525.0 z=-8.313086168749999
- **CHANGE_POINT** `margin` value=3.621e+04 d1=0.0 d12=-1444.0 z=-7.524121683229814
- **ROBUST_OUTLIER** `imbalance` value=8100 d1=0.0 d12=-1525.0 z=-8.313086168749999
- **ROBUST_OUTLIER** `margin` value=3.621e+04 d1=0.0 d12=-1444.0 z=-7.524121683229814
- **CHANGE_POINT** `ps_gen` value=-423 d1=5.0 d12=-647.0 z=-3.6940320982972135
- **CHANGE_POINT** `wind_gen` value=1.175e+04 d1=99.0 d12=-500.0 z=-2.385405825764597
- **CHANGE_POINT** `residual_proxy` value=8755 d1=0.0 d12=0.0 z=2.0047334236111114
- **REVERSAL** `ps_gen` value=-423 d1=5.0 d12=-647.0 z=-3.6940320982972135
- **ROBUST_OUTLIER** `ps_gen` value=-423 d1=5.0 d12=-647.0 z=-3.6940320982972135
- **CHANGE_POINT** `ind_generation` value=2.719e+04 d1=0.0 d12=-76.0 z=-1.678130498

## Nearest historical live analogues

- `2026-09-18T08:34:36.525091Z` distance=1.865 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:38:47.543853Z` distance=1.865 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:43:00.251145Z` distance=1.865 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:22:03.400207Z` distance=1.865 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 74.0}
- `2026-09-18T08:26:15.822729Z` distance=1.865 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 74.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
