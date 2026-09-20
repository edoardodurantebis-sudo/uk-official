# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T04:07:46.833176Z`  
Memory snapshots: **1710**  
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
- **CHANGE_POINT** `ps_gen` value=-505 d1=185.0 d12=187.0 z=-0.49647192741935486
- **PERSISTENT_DOWN** `interconnector_net` value=-1.218e+04 d1=-110.0 d12=-661.0 z=-1.4812931980842912
- **ACCELERATION** `wind_gen` value=1.507e+04 d1=-111.0 d12=-79.0 z=-0.8508947615384614
- **PERSISTENT_UP** `ps_gen` value=-505 d1=185.0 d12=187.0 z=-0.49647192741935486
- **ACCELERATION** `ps_gen` value=-505 d1=185.0 d12=187.0 z=-0.49647192741935486
- **PERSISTENT_UP** `thermal_base` value=7024 d1=82.0 d12=79.0 z=-0.3575375465616046
- **ACCELERATION** `thermal_base` value=7024 d1=82.0 d12=79.0 z=-0.3575375465616046
- **PERSISTENT_UP** `ccgt_gen` value=3692 d1=82.0 d12=76.0 z=-0.337244875

## Nearest historical live analogues

- `2026-09-20T02:55:09.059110Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:59:20.206892Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:04:06.415873Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:08:52.962663Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 3696.0}
- `2026-09-20T03:13:03.998630Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 3696.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
