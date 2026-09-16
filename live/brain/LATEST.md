# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T07:44:20.791628Z`  
Memory snapshots: **487**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.632e+04 d1=0.0 d12=-1077.0 z=-50.628886859375
- **ROBUST_OUTLIER** `margin` value=3.632e+04 d1=0.0 d12=-1077.0 z=-50.628886859375
- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=-195.0 z=-19.995357427419354
- **CHANGE_POINT** `interconnector_net` value=9787 d1=3.0 d12=6201.0 z=2.515917985835694
- **CHANGE_POINT** `ps_gen` value=228 d1=2.0 d12=6.0 z=1.4453351785714286
- **REVERSAL** `thermal_base` value=1.158e+04 d1=85.0 d12=-358.0 z=2.8528838165266106
- **REVERSAL** `ccgt_gen` value=8249 d1=84.0 d12=-355.0 z=2.8521101089085823
- **CHANGE_POINT** `ind_generation` value=2.644e+04 d1=0.0 d12=2.0 z=0.6803548782608695
- **PERSISTENT_UP** `interconnector_net` value=9787 d1=3.0 d12=6201.0 z=2.515917985835694
- **CHANGE_POINT** `imbalance` value=6872 d1=0.0 d12=-442.0 z=-0.4135760195473251
- **REVERSAL** `wind_gen` value=7795 d1=-49.0 d12=143.0 z=-1.7642833011235954
- **PERSISTENT_DOWN** `biomass_gen` value=3227 d1=-2.0 d12=-5.0 z=-1.686224375
- **ACCELERATION** `biomass_gen` value=3227 d1=-2.0 d12=-5.0 z=-1.686224375
- **PERSISTENT_UP** `ps_gen` value=228 d1=2.0 d12=6.0 z=1.4453351785714286
- **REVERSAL** `nuclear_gen` value=3328 d1=1.0 d12=-3.0 z=-0.337244875

## Nearest historical live analogues

- `2026-09-16T06:49:55.430272Z` distance=1.248 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:20:37.850603Z` distance=1.257 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:24:49.356241Z` distance=1.257 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:29:00.658838Z` distance=1.257 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:33:09.371452Z` distance=1.257 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
