# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T10:48:52.879849Z`  
Memory snapshots: **189**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **CHANGE_POINT** `biomass_gen` value=1299 d1=-45.0 d12=-741.0 z=-35.63554179166667
- **PERSISTENT_DOWN** `biomass_gen` value=1299 d1=-45.0 d12=-741.0 z=-35.63554179166667
- **ROBUST_OUTLIER** `biomass_gen` value=1299 d1=-45.0 d12=-741.0 z=-35.63554179166667
- **CHANGE_POINT** `imbalance` value=-832 d1=0.0 d12=-467.0 z=-2.2420538912037036
- **CHANGE_POINT** `ind_demand` value=-1.227e+04 d1=0.0 d12=112.0 z=2.02346925
- **ROBUST_OUTLIER** `margin` value=3.449e+04 d1=0.0 d12=145.0 z=3.6232205801282054
- **CHANGE_POINT** `ind_generation` value=1.974e+04 d1=0.0 d12=-467.0 z=-1.5424806577868853
- **PERSISTENT_DOWN** `ccgt_gen` value=1732 d1=-113.0 d12=-210.0 z=-2.522727620380739
- **ACCELERATION** `ccgt_gen` value=1732 d1=-113.0 d12=-210.0 z=-2.522727620380739
- **PERSISTENT_DOWN** `thermal_base` value=5062 d1=-108.0 d12=-204.0 z=-2.5151745436730124
- **ACCELERATION** `thermal_base` value=5062 d1=-108.0 d12=-204.0 z=-2.5151745436730124
- **REVERSAL** `ps_gen` value=-1201 d1=3.0 d12=-100.0 z=-1.8197997960784313
- **PERSISTENT_UP** `nuclear_gen` value=3330 d1=5.0 d12=6.0 z=1.1241495833333335
- **ACCELERATION** `nuclear_gen` value=3330 d1=5.0 d12=6.0 z=1.1241495833333335

## Nearest historical live analogues

- `2026-09-15T09:23:16.973095Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:27:29.987536Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:33:16.363033Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:37:29.655273Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:41:45.287890Z` distance=0.765 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
