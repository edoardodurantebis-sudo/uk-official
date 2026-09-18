# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T03:11:05.258880Z`  
Memory snapshots: **1068**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.818e+04 d1=0.0 d12=-32.0 z=16.043220482142857
- **ROBUST_OUTLIER** `margin` value=3.818e+04 d1=0.0 d12=-32.0 z=16.043220482142857
- **ROBUST_OUTLIER** `imbalance` value=1.017e+04 d1=0.0 d12=11.0 z=4.881476665254238
- **ROBUST_OUTLIER** `ind_generation` value=2.699e+04 d1=0.0 d12=11.0 z=4.881476665254238
- **CHANGE_POINT** `wind_gen` value=1.37e+04 d1=-193.0 d12=-633.0 z=-1.2995718157602663
- **CHANGE_POINT** `biomass_gen` value=1752 d1=1.0 d12=-106.0 z=-1.1660670254237289
- **CHANGE_POINT** `interconnector_net` value=-6176 d1=-180.0 d12=-670.0 z=-0.9795318090241344
- **PERSISTENT_DOWN** `wind_gen` value=1.37e+04 d1=-193.0 d12=-633.0 z=-1.2995718157602663
- **REVERSAL** `biomass_gen` value=1752 d1=1.0 d12=-106.0 z=-1.1660670254237289
- **PERSISTENT_DOWN** `interconnector_net` value=-6176 d1=-180.0 d12=-670.0 z=-0.9795318090241344
- **ACCELERATION** `interconnector_net` value=-6176 d1=-180.0 d12=-670.0 z=-0.9795318090241344
- **REVERSAL** `nuclear_gen` value=3331 d1=-2.0 d12=6.0 z=0.9197587500000001
- **PERSISTENT_UP** `ccgt_gen` value=3422 d1=41.0 d12=193.0 z=-0.6566788840413318
- **PERSISTENT_UP** `thermal_base` value=6753 d1=39.0 d12=199.0 z=-0.6553552890070923
- **REVERSAL** `ps_gen` value=513 d1=-18.0 d12=218.0 z=0.6228267053191489

## Nearest historical live analogues

- `2026-09-18T01:54:53.197905Z` distance=0.665 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 1507.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:59:03.576885Z` distance=0.665 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 1507.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T02:03:17.114876Z` distance=0.665 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 1507.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T02:07:28.761763Z` distance=0.665 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 1507.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T02:11:41.515221Z` distance=0.665 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 1507.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
