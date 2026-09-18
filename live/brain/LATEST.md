# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T03:02:37.955663Z`  
Memory snapshots: **1066**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.818e+04 d1=0.0 d12=1475.0 z=16.043220482142857
- **ROBUST_OUTLIER** `margin` value=3.818e+04 d1=0.0 d12=1475.0 z=16.043220482142857
- **CHANGE_POINT** `imbalance` value=1.017e+04 d1=0.0 d12=11.0 z=4.881476665254238
- **CHANGE_POINT** `ind_generation` value=2.699e+04 d1=0.0 d12=11.0 z=4.881476665254238
- **ROBUST_OUTLIER** `imbalance` value=1.017e+04 d1=0.0 d12=11.0 z=4.881476665254238
- **ROBUST_OUTLIER** `ind_generation` value=2.699e+04 d1=0.0 d12=11.0 z=4.881476665254238
- **CHANGE_POINT** `ind_demand` value=-1.124e+04 d1=0.0 d12=-21.0 z=-1.8395175000000001
- **CHANGE_POINT** `biomass_gen` value=1751 d1=-1.0 d12=-108.0 z=-1.169684756329114
- **CHANGE_POINT** `wind_gen` value=1.394e+04 d1=-27.0 d12=-515.0 z=-0.9440019529442691
- **PERSISTENT_DOWN** `ind_demand` value=-1.124e+04 d1=0.0 d12=-21.0 z=-1.8395175000000001
- **PERSISTENT_UP** `nuclear_gen` value=3336 d1=5.0 d12=11.0 z=1.7536733500000001
- **ACCELERATION** `nuclear_gen` value=3336 d1=5.0 d12=11.0 z=1.7536733500000001
- **PERSISTENT_DOWN** `wind_gen` value=1.394e+04 d1=-27.0 d12=-515.0 z=-0.9440019529442691
- **REVERSAL** `ccgt_gen` value=3303 d1=-34.0 d12=97.0 z=-0.8534360102040816
- **REVERSAL** `thermal_base` value=6639 d1=-29.0 d12=108.0 z=-0.840018197821101

## Nearest historical live analogues

- `2026-09-18T01:54:53.197905Z` distance=0.665 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 1507.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:59:03.576885Z` distance=0.665 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 1507.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T02:03:17.114876Z` distance=0.665 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 1507.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T02:07:28.761763Z` distance=0.665 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 1507.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:50:42.136685Z` distance=0.668 → {'next30m_imbalance_delta': 34.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
