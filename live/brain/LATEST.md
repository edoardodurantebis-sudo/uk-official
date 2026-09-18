# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T19:28:30.603747Z`  
Memory snapshots: **1271**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.089e+04 d1=0.0 d12=-155.0 z=-98.4755035
- **PERSISTENT_DOWN** `ind_demand` value=-1.089e+04 d1=0.0 d12=-155.0 z=-98.4755035
- **ROBUST_OUTLIER** `ind_demand` value=-1.089e+04 d1=0.0 d12=-155.0 z=-98.4755035
- **PERSISTENT_DOWN** `ccgt_gen` value=4612 d1=-65.0 d12=-191.0 z=24.23590288135593
- **ROBUST_OUTLIER** `ccgt_gen` value=4612 d1=-65.0 d12=-191.0 z=24.23590288135593
- **PERSISTENT_DOWN** `thermal_base` value=7942 d1=-66.0 d12=-202.0 z=23.92454819117647
- **ROBUST_OUTLIER** `thermal_base` value=7942 d1=-66.0 d12=-202.0 z=23.92454819117647
- **CHANGE_POINT** `ind_generation` value=2.623e+04 d1=0.0 d12=0.0 z=18.09392068478261
- **ACCELERATION** `ind_generation` value=2.623e+04 d1=0.0 d12=0.0 z=18.09392068478261
- **ROBUST_OUTLIER** `ind_generation` value=2.623e+04 d1=0.0 d12=0.0 z=18.09392068478261
- **REVERSAL** `interconnector_net` value=-911 d1=1.0 d12=-605.0 z=-6.330994170093096
- **ROBUST_OUTLIER** `interconnector_net` value=-911 d1=1.0 d12=-605.0 z=-6.330994170093096
- **PERSISTENT_DOWN** `margin` value=3.75e+04 d1=0.0 d12=-262.0 z=-5.050242003125
- **ROBUST_OUTLIER** `margin` value=3.75e+04 d1=0.0 d12=-262.0 z=-5.050242003125
- **CHANGE_POINT** `biomass_gen` value=1530 d1=0.0 d12=0.0 z=2.8399568421052632

## Nearest historical live analogues

- `2026-09-18T17:51:12.400587Z` distance=0.126 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:55:26.775797Z` distance=0.127 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:59:39.675441Z` distance=0.127 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:03:52.862865Z` distance=0.127 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:08:04.608022Z` distance=0.127 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
