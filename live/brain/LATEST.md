# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T03:46:44.690279Z`  
Memory snapshots: **1705**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=-62.0 z=28.579094264285715
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=-62.0 z=28.579094264285715
- **ROBUST_OUTLIER** `ind_demand` value=-1.229e+04 d1=0.0 d12=-9.0 z=-9.2742340625
- **CHANGE_POINT** `ps_gen` value=-695 d1=0.0 d12=0.0 z=-0.8726950712719298
- **PERSISTENT_UP** `biomass_gen` value=1226 d1=7.0 d12=58.0 z=2.6802092697368423
- **CHANGE_POINT** `imbalance` value=-3815 d1=0.0 d12=-66.0 z=-0.6555788224299065
- **CHANGE_POINT** `ind_generation` value=1.614e+04 d1=0.0 d12=-66.0 z=-0.6555788224299065
- **CHANGE_POINT** `thermal_base` value=7021 d1=-16.0 d12=-163.0 z=-0.5352499125971143
- **CHANGE_POINT** `ccgt_gen` value=3691 d1=-12.0 d12=-164.0 z=-0.528313203520352
- **REVERSAL** `interconnector_net` value=-1.188e+04 d1=1.0 d12=-833.0 z=-1.6430788768218623
- **REVERSAL** `nuclear_gen` value=3330 d1=-4.0 d12=1.0 z=-0.8993196666666666
- **ACCELERATION** `nuclear_gen` value=3330 d1=-4.0 d12=1.0 z=-0.8993196666666666
- **REVERSAL** `wind_gen` value=1.508e+04 d1=12.0 d12=-356.0 z=-0.8064866688172043

## Nearest historical live analogues

- `2026-09-20T02:20:49.967105Z` distance=1.035 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:25:01.524399Z` distance=1.035 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:29:13.820300Z` distance=1.035 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:33:25.726465Z` distance=1.035 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:37:39.122581Z` distance=1.035 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
