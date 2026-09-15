# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T18:12:00.243287Z`  
Memory snapshots: **294**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **PERSISTENT_UP** `biomass_gen` value=3250 d1=23.0 d12=244.0 z=49.665476957317075
- **ROBUST_OUTLIER** `biomass_gen` value=3250 d1=23.0 d12=244.0 z=49.665476957317075
- **CHANGE_POINT** `thermal_base` value=1.393e+04 d1=121.0 d12=220.0 z=6.714992022768124
- **CHANGE_POINT** `ccgt_gen` value=1.061e+04 d1=114.0 d12=221.0 z=6.693385156324582
- **PERSISTENT_UP** `thermal_base` value=1.393e+04 d1=121.0 d12=220.0 z=6.714992022768124
- **ROBUST_OUTLIER** `thermal_base` value=1.393e+04 d1=121.0 d12=220.0 z=6.714992022768124
- **PERSISTENT_UP** `ccgt_gen` value=1.061e+04 d1=114.0 d12=221.0 z=6.693385156324582
- **ROBUST_OUTLIER** `ccgt_gen` value=1.061e+04 d1=114.0 d12=221.0 z=6.693385156324582
- **CHANGE_POINT** `margin` value=3.567e+04 d1=0.0 d12=851.0 z=2.2579347345238094
- **CHANGE_POINT** `nuclear_gen` value=3318 d1=7.0 d12=-1.0 z=-1.5176019375
- **CHANGE_POINT** `ps_gen` value=806 d1=68.0 d12=305.0 z=1.2790899370888158
- **CHANGE_POINT** `imbalance` value=5775 d1=0.0 d12=-60.0 z=0.08002420762711863
- **CHANGE_POINT** `ind_generation` value=2.49e+04 d1=0.0 d12=-60.0 z=0.08002420762711863
- **REVERSAL** `interconnector_net` value=-1674 d1=13.0 d12=-925.0 z=-1.9733783167626553
- **REVERSAL** `nuclear_gen` value=3318 d1=7.0 d12=-1.0 z=-1.5176019375

## Nearest historical live analogues

- `2026-09-15T11:22:30.581865Z` distance=0.186 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:26:42.593420Z` distance=0.186 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:30:55.285075Z` distance=0.186 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:35:06.452199Z` distance=0.186 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:39:18.571623Z` distance=0.186 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
