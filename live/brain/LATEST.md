# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T01:04:52.436304Z`  
Memory snapshots: **1325**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.643e+04 d1=0.0 d12=49.0 z=3.5630654184782604
- **CHANGE_POINT** `margin` value=3.713e+04 d1=0.0 d12=-382.0 z=-3.458553824468085
- **ROBUST_OUTLIER** `ind_generation` value=2.643e+04 d1=0.0 d12=49.0 z=3.5630654184782604
- **ROBUST_OUTLIER** `margin` value=3.713e+04 d1=0.0 d12=-382.0 z=-3.458553824468085
- **CHANGE_POINT** `imbalance` value=9233 d1=0.0 d12=48.0 z=0.996856174632353
- **CHANGE_POINT** `biomass_gen` value=1139 d1=0.0 d12=-62.0 z=-0.86469293329718
- **CHANGE_POINT** `interconnector_net` value=-9555 d1=22.0 d12=-408.0 z=-0.8232802981413772
- **CHANGE_POINT** `ps_gen` value=-834 d1=0.0 d12=-67.0 z=-0.6869342103321033
- **CHANGE_POINT** `ind_demand` value=-1.089e+04 d1=0.0 d12=2.0 z=0.337244875
- **CHANGE_POINT** `wind_gen` value=1.639e+04 d1=0.0 d12=543.0 z=-0.20389155801526718
- **REVERSAL** `interconnector_net` value=-9555 d1=22.0 d12=-408.0 z=-0.8232802981413772
- **ACCELERATION** `interconnector_net` value=-9555 d1=22.0 d12=-408.0 z=-0.8232802981413772
- **PERSISTENT_DOWN** `ps_gen` value=-834 d1=0.0 d12=-67.0 z=-0.6869342103321033
- **PERSISTENT_UP** `nuclear_gen` value=3339 d1=0.0 d12=2.0 z=0.5395918
- **ACCELERATION** `nuclear_gen` value=3339 d1=0.0 d12=2.0 z=0.5395918

## Nearest historical live analogues

- `2026-09-19T00:05:15.769782Z` distance=0.137 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:09:28.868640Z` distance=0.137 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:01:02.143708Z` distance=0.468 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T23:52:35.320958Z` distance=0.905 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T23:56:47.985374Z` distance=0.905 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
