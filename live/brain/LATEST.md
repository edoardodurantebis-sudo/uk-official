# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T01:00:39.226474Z`  
Memory snapshots: **1324**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.643e+04 d1=0.0 d12=49.0 z=3.5630654184782604
- **CHANGE_POINT** `margin` value=3.713e+04 d1=0.0 d12=-382.0 z=-3.458553824468085
- **PERSISTENT_UP** `ind_generation` value=2.643e+04 d1=0.0 d12=49.0 z=3.5630654184782604
- **ROBUST_OUTLIER** `ind_generation` value=2.643e+04 d1=0.0 d12=49.0 z=3.5630654184782604
- **PERSISTENT_DOWN** `margin` value=3.713e+04 d1=0.0 d12=-382.0 z=-3.458553824468085
- **ROBUST_OUTLIER** `margin` value=3.713e+04 d1=0.0 d12=-382.0 z=-3.458553824468085
- **CHANGE_POINT** `imbalance` value=9233 d1=0.0 d12=48.0 z=0.996856174632353
- **CHANGE_POINT** `biomass_gen` value=1139 d1=1.0 d12=-63.0 z=-0.8819102704646017
- **CHANGE_POINT** `interconnector_net` value=-9577 d1=-195.0 d12=-572.0 z=-0.8256551986554429
- **CHANGE_POINT** `ps_gen` value=-834 d1=-5.0 d12=-289.0 z=-0.6894784111111112
- **CHANGE_POINT** `wind_gen` value=1.639e+04 d1=67.0 d12=515.0 z=-0.2005239797297297
- **PERSISTENT_UP** `imbalance` value=9233 d1=0.0 d12=48.0 z=0.996856174632353
- **REVERSAL** `biomass_gen` value=1139 d1=1.0 d12=-63.0 z=-0.8819102704646017
- **PERSISTENT_DOWN** `interconnector_net` value=-9577 d1=-195.0 d12=-572.0 z=-0.8256551986554429
- **PERSISTENT_DOWN** `ps_gen` value=-834 d1=-5.0 d12=-289.0 z=-0.6894784111111112

## Nearest historical live analogues

- `2026-09-19T00:05:15.769782Z` distance=0.137 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:01:02.143708Z` distance=0.468 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T23:52:35.320958Z` distance=0.905 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T23:56:47.985374Z` distance=0.905 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T23:30:48.879695Z` distance=0.907 → {'next30m_imbalance_delta': -8.0, 'next30m_margin_delta': -32.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
