# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T03:19:33.246104Z`  
Memory snapshots: **1070**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.818e+04 d1=0.0 d12=-32.0 z=11.389837221649485
- **ROBUST_OUTLIER** `margin` value=3.818e+04 d1=0.0 d12=-32.0 z=11.389837221649485
- **CHANGE_POINT** `wind_gen` value=1.362e+04 d1=-81.0 d12=-612.0 z=-1.4996988145061727
- **CHANGE_POINT** `interconnector_net` value=-6195 d1=-19.0 d12=-742.0 z=-1.0194577900763357
- **PERSISTENT_DOWN** `wind_gen` value=1.362e+04 d1=-81.0 d12=-612.0 z=-1.4996988145061727
- **REVERSAL** `biomass_gen` value=1754 d1=2.0 d12=-35.0 z=-1.1736715914096918
- **PERSISTENT_DOWN** `interconnector_net` value=-6195 d1=-19.0 d12=-742.0 z=-1.0194577900763357
- **PERSISTENT_UP** `thermal_base` value=6778 d1=25.0 d12=142.0 z=-0.6276379062909567
- **PERSISTENT_UP** `ccgt_gen` value=3452 d1=30.0 d12=144.0 z=-0.61982522124183
- **REVERSAL** `ps_gen` value=463 d1=-50.0 d12=167.0 z=0.4793182478723404
- **PERSISTENT_DOWN** `nuclear_gen` value=3326 d1=-5.0 d12=-2.0 z=0.245269
- **ACCELERATION** `nuclear_gen` value=3326 d1=-5.0 d12=-2.0 z=0.245269

## Nearest historical live analogues

- `2026-09-18T02:20:05.299900Z` distance=0.030 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T02:24:14.818372Z` distance=0.051 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:54:53.197905Z` distance=0.665 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 1507.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:59:03.576885Z` distance=0.665 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 1507.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T02:03:17.114876Z` distance=0.665 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 1507.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
