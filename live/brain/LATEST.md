# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T04:35:10.163579Z`  
Memory snapshots: **1088**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=1.074e+04 d1=0.0 d12=570.0 z=9.568342965116278
- **CHANGE_POINT** `ind_generation` value=2.755e+04 d1=0.0 d12=570.0 z=9.568342965116278
- **ROBUST_OUTLIER** `margin` value=3.816e+04 d1=0.0 d12=-4.0 z=10.404505252475248
- **ROBUST_OUTLIER** `imbalance` value=1.074e+04 d1=0.0 d12=570.0 z=9.568342965116278
- **ROBUST_OUTLIER** `ind_generation` value=2.755e+04 d1=0.0 d12=570.0 z=9.568342965116278
- **CHANGE_POINT** `biomass_gen` value=2130 d1=0.0 d12=202.0 z=2.2464410681818183
- **CHANGE_POINT** `ind_demand` value=-1.116e+04 d1=0.0 d12=85.0 z=0.6295237666666667
- **PERSISTENT_UP** `biomass_gen` value=2130 d1=0.0 d12=202.0 z=2.2464410681818183
- **PERSISTENT_DOWN** `ccgt_gen` value=3307 d1=0.0 d12=-389.0 z=-1.2030694724489794
- **PERSISTENT_DOWN** `thermal_base` value=6640 d1=0.0 d12=-395.0 z=-1.1665355512295084
- **PERSISTENT_DOWN** `interconnector_net` value=-7017 d1=0.0 d12=-27.0 z=-0.9264197012648809
- **ACCELERATION** `interconnector_net` value=-7017 d1=0.0 d12=-27.0 z=-0.9264197012648809
- **PERSISTENT_UP** `wind_gen` value=1.382e+04 d1=0.0 d12=90.0 z=-0.8172649525547445

## Nearest historical live analogues

- `2026-09-18T03:32:11.466334Z` distance=0.106 → {'next30m_imbalance_delta': 521.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T03:36:24.269730Z` distance=0.106 → {'next30m_imbalance_delta': 521.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T03:40:35.454286Z` distance=0.106 → {'next30m_imbalance_delta': 521.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:53:08.620374Z` distance=5.458 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:57:18.949614Z` distance=5.458 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
