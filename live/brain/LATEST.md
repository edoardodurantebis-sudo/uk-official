# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T04:11:59.929558Z`  
Memory snapshots: **1711**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-6527 d1=0.0 d12=-2712.0 z=-35.851724403846156
- **CHANGE_POINT** `ind_generation` value=1.342e+04 d1=0.0 d12=-2712.0 z=-35.851724403846156
- **ROBUST_OUTLIER** `imbalance` value=-6527 d1=0.0 d12=-2712.0 z=-35.851724403846156
- **ROBUST_OUTLIER** `ind_generation` value=1.342e+04 d1=0.0 d12=-2712.0 z=-35.851724403846156
- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=-1.0 z=28.55982312857143
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=-1.0 z=28.55982312857143
- **CHANGE_POINT** `ind_demand` value=-1.229e+04 d1=0.0 d12=-6.0 z=-6.218466475609755
- **ROBUST_OUTLIER** `ind_demand` value=-1.229e+04 d1=0.0 d12=-6.0 z=-6.218466475609755
- **CHANGE_POINT** `ps_gen` value=-421 d1=84.0 d12=276.0 z=-0.4532788259557344
- **PERSISTENT_DOWN** `interconnector_net` value=-1.228e+04 d1=-98.0 d12=-756.0 z=-1.5310994822864803
- **PERSISTENT_DOWN** `wind_gen` value=1.503e+04 d1=-41.0 d12=-183.0 z=-0.972451156043956
- **ACCELERATION** `wind_gen` value=1.503e+04 d1=-41.0 d12=-183.0 z=-0.972451156043956
- **PERSISTENT_UP** `ps_gen` value=-421 d1=84.0 d12=276.0 z=-0.4532788259557344
- **ACCELERATION** `ps_gen` value=-421 d1=84.0 d12=276.0 z=-0.4532788259557344
- **PERSISTENT_UP** `thermal_base` value=7166 d1=142.0 d12=236.0 z=-0.05738336785216179

## Nearest historical live analogues

- `2026-09-20T02:55:09.059110Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:59:20.206892Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:04:06.415873Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:08:52.962663Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 3696.0}
- `2026-09-20T03:13:03.998630Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 3696.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
