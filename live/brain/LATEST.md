# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T04:16:12.031984Z`  
Memory snapshots: **1712**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-6527 d1=0.0 d12=-2712.0 z=-35.851724403846156
- **CHANGE_POINT** `ind_generation` value=1.342e+04 d1=0.0 d12=-2712.0 z=-35.851724403846156
- **ROBUST_OUTLIER** `imbalance` value=-6527 d1=0.0 d12=-2712.0 z=-35.851724403846156
- **ROBUST_OUTLIER** `ind_generation` value=1.342e+04 d1=0.0 d12=-2712.0 z=-35.851724403846156
- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=-1.0 z=23.759704407738095
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=-1.0 z=23.759704407738095
- **CHANGE_POINT** `ind_demand` value=-1.229e+04 d1=0.0 d12=-6.0 z=-4.198117237068965
- **ROBUST_OUTLIER** `ind_demand` value=-1.229e+04 d1=0.0 d12=-6.0 z=-4.198117237068965
- **CHANGE_POINT** `ps_gen` value=-529 d1=-108.0 d12=173.0 z=-0.754002769308943
- **PERSISTENT_UP** `biomass_gen` value=1229 d1=1.0 d12=5.0 z=2.689084134868421
- **PERSISTENT_DOWN** `interconnector_net` value=-1.232e+04 d1=-43.0 d12=-801.0 z=-1.5524626251914242
- **REVERSAL** `ps_gen` value=-529 d1=-108.0 d12=173.0 z=-0.754002769308943
- **ACCELERATION** `ps_gen` value=-529 d1=-108.0 d12=173.0 z=-0.754002769308943
- **REVERSAL** `wind_gen` value=1.513e+04 d1=95.0 d12=-136.0 z=-0.6907960956043956
- **ACCELERATION** `wind_gen` value=1.513e+04 d1=95.0 d12=-136.0 z=-0.6907960956043956

## Nearest historical live analogues

- `2026-09-20T03:21:25.229596Z` distance=1.030 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 3696.0}
- `2026-09-20T02:55:09.059110Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:59:20.206892Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:04:06.415873Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:08:52.962663Z` distance=1.031 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': -62.0, 'next30m_residual_proxy_delta': 3696.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
