# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T20:22:00.773279Z`  
Memory snapshots: **971**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.116e+04 d1=0.0 d12=0.0 z=26.97959
- **CHANGE_POINT** `ind_generation` value=2.652e+04 d1=0.0 d12=24.0 z=-15.926389221874999
- **ROBUST_OUTLIER** `ind_generation` value=2.652e+04 d1=0.0 d12=24.0 z=-15.926389221874999
- **CHANGE_POINT** `imbalance` value=9708 d1=0.0 d12=24.0 z=-3.7363962983870964
- **CHANGE_POINT** `interconnector_net` value=-1708 d1=-1.0 d12=-1398.0 z=-3.3477899849462363
- **ROBUST_OUTLIER** `imbalance` value=9708 d1=0.0 d12=24.0 z=-3.7363962983870964
- **PERSISTENT_DOWN** `interconnector_net` value=-1708 d1=-1.0 d12=-1398.0 z=-3.3477899849462363
- **ROBUST_OUTLIER** `interconnector_net` value=-1708 d1=-1.0 d12=-1398.0 z=-3.3477899849462363
- **CHANGE_POINT** `ps_gen` value=503 d1=0.0 d12=76.0 z=0.6756348938879457
- **CHANGE_POINT** `thermal_base` value=8249 d1=-180.0 d12=-1634.0 z=-0.05298671788354899
- **CHANGE_POINT** `ccgt_gen` value=4929 d1=-180.0 d12=-1628.0 z=-0.05234908078231293
- **PERSISTENT_UP** `biomass_gen` value=3175 d1=53.0 d12=297.0 z=1.1229724633507854
- **REVERSAL** `wind_gen` value=1.565e+04 d1=-216.0 d12=63.0 z=1.099068955179283
- **ACCELERATION** `wind_gen` value=1.565e+04 d1=-216.0 d12=63.0 z=1.099068955179283
- **PERSISTENT_DOWN** `margin` value=3.645e+04 d1=-68.0 d12=-42.0 z=-0.9927882837078652

## Nearest historical live analogues

- `2026-09-17T19:23:15.447841Z` distance=0.129 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:27:27.221396Z` distance=0.129 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 26.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T18:57:56.745109Z` distance=0.142 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:02:09.783762Z` distance=0.142 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:06:26.402438Z` distance=0.142 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
