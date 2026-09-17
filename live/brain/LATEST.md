# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T04:25:05.573185Z`  
Memory snapshots: **744**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.636e+04 d1=0.0 d12=712.0 z=24.382804462499998
- **ROBUST_OUTLIER** `ind_generation` value=2.636e+04 d1=0.0 d12=712.0 z=24.382804462499998
- **ROBUST_OUTLIER** `interconnector_net` value=-1.063e+04 d1=0.0 d12=-807.0 z=-20.512572172284646
- **CHANGE_POINT** `imbalance` value=7239 d1=0.0 d12=712.0 z=15.491506516129032
- **ROBUST_OUTLIER** `imbalance` value=7239 d1=0.0 d12=712.0 z=15.491506516129032
- **CHANGE_POINT** `margin` value=3.585e+04 d1=0.0 d12=-4.0 z=9.129457222222223
- **PERSISTENT_UP** `ind_demand` value=-1.145e+04 d1=0.0 d12=62.0 z=9.41073794047619
- **ACCELERATION** `ind_demand` value=-1.145e+04 d1=0.0 d12=62.0 z=9.41073794047619
- **ROBUST_OUTLIER** `ind_demand` value=-1.145e+04 d1=0.0 d12=62.0 z=9.41073794047619
- **ACCELERATION** `margin` value=3.585e+04 d1=0.0 d12=-4.0 z=9.129457222222223
- **ROBUST_OUTLIER** `margin` value=3.585e+04 d1=0.0 d12=-4.0 z=9.129457222222223
- **CHANGE_POINT** `wind_gen` value=1.384e+04 d1=0.0 d12=352.0 z=0.935350769569245
- **CHANGE_POINT** `biomass_gen` value=3182 d1=0.0 d12=1149.0 z=-0.7291781081081081
- **CHANGE_POINT** `ps_gen` value=-349 d1=0.0 d12=192.0 z=-0.6803043168103449
- **PERSISTENT_UP** `wind_gen` value=1.384e+04 d1=0.0 d12=352.0 z=0.935350769569245

## Nearest historical live analogues

- `2026-09-17T03:21:28.633529Z` distance=0.602 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1126.0}
- `2026-09-17T03:26:17.197207Z` distance=0.602 → {'next30m_imbalance_delta': 746.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 1126.0}
- `2026-09-17T03:30:29.291178Z` distance=0.602 → {'next30m_imbalance_delta': 746.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 1126.0}
- `2026-09-17T02:52:02.690108Z` distance=0.602 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:56:14.879410Z` distance=0.602 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
