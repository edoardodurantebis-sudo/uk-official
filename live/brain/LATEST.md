# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T03:18:27.781833Z`  
Memory snapshots: **82**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **PERSISTENT_DOWN** `ps_gen` value=-706 d1=-3.0 d12=-698.0 z=-93.6191773
- **ROBUST_OUTLIER** `ps_gen` value=-706 d1=-3.0 d12=-698.0 z=-93.6191773
- **CHANGE_POINT** `margin` value=3.41e+04 d1=0.0 d12=0.0 z=4.485993148584906
- **CHANGE_POINT** `wind_gen` value=1.364e+04 d1=126.0 d12=1252.0 z=3.702132080717489
- **ROBUST_OUTLIER** `margin` value=3.41e+04 d1=0.0 d12=0.0 z=4.485993148584906
- **PERSISTENT_UP** `wind_gen` value=1.364e+04 d1=126.0 d12=1252.0 z=3.702132080717489
- **ROBUST_OUTLIER** `wind_gen` value=1.364e+04 d1=126.0 d12=1252.0 z=3.702132080717489
- **CHANGE_POINT** `interconnector_net` value=-5568 d1=11.0 d12=-2852.0 z=-0.9983262983140413
- **CHANGE_POINT** `biomass_gen` value=3212 d1=-5.0 d12=17.0 z=0.7083351137992832
- **CHANGE_POINT** `imbalance` value=218 d1=0.0 d12=-29.0 z=0.0
- **CHANGE_POINT** `ind_generation` value=2.07e+04 d1=0.0 d12=-29.0 z=0.0
- **PERSISTENT_UP** `nuclear_gen` value=3330 d1=7.0 d12=5.0 z=1.3489794999999998
- **ACCELERATION** `nuclear_gen` value=3330 d1=7.0 d12=5.0 z=1.3489794999999998
- **REVERSAL** `interconnector_net` value=-5568 d1=11.0 d12=-2852.0 z=-0.9983262983140413
- **REVERSAL** `biomass_gen` value=3212 d1=-5.0 d12=17.0 z=0.7083351137992832

## Nearest historical live analogues

- `2026-09-15T02:23:56.984916Z` distance=0.314 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:19:46.344592Z` distance=0.471 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T01:50:29.007493Z` distance=4.594 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T01:54:40.060641Z` distance=4.594 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 1370.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T01:58:49.966951Z` distance=4.594 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 1370.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
