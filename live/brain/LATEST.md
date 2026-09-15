# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T17:55:09.760503Z`  
Memory snapshots: **290**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **ROBUST_OUTLIER** `biomass_gen` value=3204 d1=0.0 d12=403.0 z=58.2044978382353
- **ROBUST_OUTLIER** `ccgt_gen` value=1.042e+04 d1=0.0 d12=138.0 z=11.432567504254255
- **ROBUST_OUTLIER** `thermal_base` value=1.374e+04 d1=0.0 d12=126.0 z=11.28984874900892
- **CHANGE_POINT** `nuclear_gen` value=3313 d1=0.0 d12=-12.0 z=-2.697959
- **CHANGE_POINT** `margin` value=3.567e+04 d1=0.0 d12=842.0 z=2.2579347345238094
- **PERSISTENT_DOWN** `interconnector_net` value=-1798 d1=0.0 d12=-1733.0 z=-2.5918089745417516
- **PERSISTENT_UP** `margin` value=3.567e+04 d1=0.0 d12=842.0 z=2.2579347345238094
- **ACCELERATION** `margin` value=3.567e+04 d1=0.0 d12=842.0 z=2.2579347345238094
- **CHANGE_POINT** `imbalance` value=5775 d1=3.0 d12=-60.0 z=0.08002420762711863
- **CHANGE_POINT** `ind_generation` value=2.49e+04 d1=3.0 d12=-60.0 z=0.08002420762711863
- **ACCELERATION** `wind_gen` value=1.051e+04 d1=0.0 d12=234.0 z=0.31356424213075057
- **REVERSAL** `imbalance` value=5775 d1=3.0 d12=-60.0 z=0.08002420762711863
- **REVERSAL** `ind_generation` value=2.49e+04 d1=3.0 d12=-60.0 z=0.08002420762711863

## Nearest historical live analogues

- `2026-09-15T11:22:30.581865Z` distance=0.186 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:26:42.593420Z` distance=0.186 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:30:55.285075Z` distance=0.186 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:35:06.452199Z` distance=0.186 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:39:18.571623Z` distance=0.186 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
