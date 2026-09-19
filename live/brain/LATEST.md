# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T01:09:07.681606Z`  
Memory snapshots: **1326**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.713e+04 d1=0.0 d12=-382.0 z=-3.7533370794117644
- **CHANGE_POINT** `ind_generation` value=2.643e+04 d1=0.0 d12=49.0 z=3.3724487499999998
- **ROBUST_OUTLIER** `margin` value=3.713e+04 d1=0.0 d12=-382.0 z=-3.7533370794117644
- **ROBUST_OUTLIER** `ind_generation` value=2.643e+04 d1=0.0 d12=49.0 z=3.3724487499999998
- **CHANGE_POINT** `imbalance` value=9233 d1=0.0 d12=48.0 z=1.0028929990636704
- **CHANGE_POINT** `interconnector_net` value=-9963 d1=-408.0 d12=-855.0 z=-0.8652239466976596
- **CHANGE_POINT** `biomass_gen` value=1137 d1=-2.0 d12=-66.0 z=-0.6883610044987147
- **CHANGE_POINT** `ps_gen` value=-832 d1=2.0 d12=-3.0 z=-0.6819381030674846
- **CHANGE_POINT** `wind_gen` value=1.646e+04 d1=71.0 d12=521.0 z=-0.05828923765432099
- **PERSISTENT_DOWN** `interconnector_net` value=-9963 d1=-408.0 d12=-855.0 z=-0.8652239466976596
- **ACCELERATION** `interconnector_net` value=-9963 d1=-408.0 d12=-855.0 z=-0.8652239466976596
- **PERSISTENT_DOWN** `biomass_gen` value=1137 d1=-2.0 d12=-66.0 z=-0.6883610044987147
- **REVERSAL** `ps_gen` value=-832 d1=2.0 d12=-3.0 z=-0.6819381030674846
- **ACCELERATION** `ps_gen` value=-832 d1=2.0 d12=-3.0 z=-0.6819381030674846
- **REVERSAL** `nuclear_gen` value=3336 d1=-3.0 d12=1.0 z=-0.40469384999999997

## Nearest historical live analogues

- `2026-09-19T00:05:15.769782Z` distance=0.137 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:09:28.868640Z` distance=0.137 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:13:40.553498Z` distance=0.137 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:01:02.143708Z` distance=0.468 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T23:52:35.320958Z` distance=0.905 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
