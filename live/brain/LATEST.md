# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T03:05:55.843764Z`  
Memory snapshots: **79**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **REVERSAL** `ps_gen` value=-704 d1=3.0 d12=-697.0 z=-93.3493814
- **ROBUST_OUTLIER** `ps_gen` value=-704 d1=3.0 d12=-697.0 z=-93.3493814
- **CHANGE_POINT** `margin` value=3.41e+04 d1=0.0 d12=1370.0 z=4.809331676065163
- **CHANGE_POINT** `wind_gen` value=1.333e+04 d1=256.0 d12=780.0 z=3.0327541543583534
- **ROBUST_OUTLIER** `margin` value=3.41e+04 d1=0.0 d12=1370.0 z=4.809331676065163
- **PERSISTENT_UP** `wind_gen` value=1.333e+04 d1=256.0 d12=780.0 z=3.0327541543583534
- **ROBUST_OUTLIER** `wind_gen` value=1.333e+04 d1=256.0 d12=780.0 z=3.0327541543583534
- **CHANGE_POINT** `biomass_gen` value=3223 d1=-11.0 d12=19.0 z=0.8139995957264957
- **CHANGE_POINT** `ind_generation` value=2.07e+04 d1=0.0 d12=-26.0 z=0.05506038775510204
- **CHANGE_POINT** `imbalance` value=218 d1=0.0 d12=-26.0 z=0.05395918
- **REVERSAL** `nuclear_gen` value=3328 d1=-2.0 d12=3.0 z=1.2365645416666666
- **ACCELERATION** `nuclear_gen` value=3328 d1=-2.0 d12=3.0 z=1.2365645416666666
- **PERSISTENT_DOWN** `interconnector_net` value=-5093 d1=-1170.0 d12=-2414.0 z=-0.8636378771186441
- **REVERSAL** `biomass_gen` value=3223 d1=-11.0 d12=19.0 z=0.8139995957264957
- **ACCELERATION** `biomass_gen` value=3223 d1=-11.0 d12=19.0 z=0.8139995957264957

## Nearest historical live analogues

- `2026-09-15T01:50:29.007493Z` distance=4.880 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T01:54:40.060641Z` distance=4.880 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 1370.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T01:58:49.966951Z` distance=4.880 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 1370.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:03:02.297179Z` distance=4.880 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 1370.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T02:07:13.122668Z` distance=4.880 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 1370.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
