# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T03:42:30.347706Z`  
Memory snapshots: **1704**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=-62.0 z=28.579094264285715
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=-62.0 z=28.579094264285715
- **ROBUST_OUTLIER** `ind_demand` value=-1.229e+04 d1=0.0 d12=-90.0 z=-17.896461366666664
- **CHANGE_POINT** `ps_gen` value=-695 d1=0.0 d12=0.0 z=-0.8746672635233919
- **CHANGE_POINT** `imbalance` value=-3815 d1=0.0 d12=-60.0 z=-0.6376994
- **CHANGE_POINT** `ind_generation` value=1.614e+04 d1=0.0 d12=-60.0 z=-0.6376994
- **REVERSAL** `biomass_gen` value=1219 d1=-3.0 d12=51.0 z=2.6313975115131583
- **CHANGE_POINT** `thermal_base` value=7037 d1=1.0 d12=-147.0 z=-0.5099438989010989
- **CHANGE_POINT** `ccgt_gen` value=3703 d1=2.0 d12=-152.0 z=-0.5065972797619047
- **PERSISTENT_DOWN** `interconnector_net` value=-1.188e+04 d1=0.0 d12=-834.0 z=-1.6654135960359624
- **ACCELERATION** `ps_gen` value=-695 d1=0.0 d12=0.0 z=-0.8746672635233919
- **PERSISTENT_DOWN** `wind_gen` value=1.507e+04 d1=-54.0 d12=-368.0 z=-0.8412990430107526
- **REVERSAL** `thermal_base` value=7037 d1=1.0 d12=-147.0 z=-0.5099438989010989
- **REVERSAL** `ccgt_gen` value=3703 d1=2.0 d12=-152.0 z=-0.5065972797619047
- **REVERSAL** `nuclear_gen` value=3334 d1=-1.0 d12=5.0 z=0.0

## Nearest historical live analogues

- `2026-09-20T02:20:49.967105Z` distance=1.035 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:25:01.524399Z` distance=1.035 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:29:13.820300Z` distance=1.035 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:33:25.726465Z` distance=1.035 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T02:37:39.122581Z` distance=1.035 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 1.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
