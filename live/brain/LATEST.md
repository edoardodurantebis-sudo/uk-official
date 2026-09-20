# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T04:03:34.178375Z`  
Memory snapshots: **1709**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-6527 d1=0.0 d12=-2778.0 z=-35.851724403846156
- **CHANGE_POINT** `ind_generation` value=1.342e+04 d1=0.0 d12=-2778.0 z=-35.851724403846156
- **ROBUST_OUTLIER** `imbalance` value=-6527 d1=0.0 d12=-2778.0 z=-35.851724403846156
- **ROBUST_OUTLIER** `ind_generation` value=1.342e+04 d1=0.0 d12=-2778.0 z=-35.851724403846156
- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=-63.0 z=28.55982312857143
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=-63.0 z=28.55982312857143
- **ROBUST_OUTLIER** `ind_demand` value=-1.229e+04 d1=0.0 d12=-15.0 z=-6.218466475609755
- **CHANGE_POINT** `ps_gen` value=-690 d1=3.0 d12=3.0 z=-0.8598758216374269
- **REVERSAL** `biomass_gen` value=1228 d1=-1.0 d12=6.0 z=2.689084134868421
- **CHANGE_POINT** `wind_gen` value=1.518e+04 d1=50.0 d12=-71.0 z=-0.518385135371179
- **PERSISTENT_DOWN** `interconnector_net` value=-1.207e+04 d1=-152.0 d12=-582.0 z=-1.4244396559386974
- **PERSISTENT_UP** `ps_gen` value=-690 d1=3.0 d12=3.0 z=-0.8598758216374269
- **REVERSAL** `thermal_base` value=6942 d1=1.0 d12=-19.0 z=-0.5753849793152639
- **ACCELERATION** `thermal_base` value=6942 d1=1.0 d12=-19.0 z=-0.5753849793152639
- **PERSISTENT_DOWN** `ccgt_gen` value=3610 d1=-1.0 d12=-23.0 z=-0.5659180381054131

## Nearest historical live analogues

- `2026-09-20T02:55:09.059110Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:59:20.206892Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:04:06.415873Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:08:52.962663Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 3696.0}
- `2026-09-20T02:20:49.967105Z` distance=1.036 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
