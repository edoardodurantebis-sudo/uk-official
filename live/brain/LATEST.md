# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T19:53:59.381022Z`  
Memory snapshots: **1277**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.624e+04 d1=17.0 d12=12.0 z=18.592456586956523
- **CHANGE_POINT** `ccgt_gen` value=4086 d1=-28.0 d12=-959.0 z=18.222655279661016
- **CHANGE_POINT** `thermal_base` value=7422 d1=-28.0 d12=-962.0 z=18.029847855042018
- **PERSISTENT_UP** `ind_generation` value=2.624e+04 d1=17.0 d12=12.0 z=18.592456586956523
- **ACCELERATION** `ind_generation` value=2.624e+04 d1=17.0 d12=12.0 z=18.592456586956523
- **ROBUST_OUTLIER** `ind_generation` value=2.624e+04 d1=17.0 d12=12.0 z=18.592456586956523
- **PERSISTENT_DOWN** `ccgt_gen` value=4086 d1=-28.0 d12=-959.0 z=18.222655279661016
- **ROBUST_OUTLIER** `ccgt_gen` value=4086 d1=-28.0 d12=-959.0 z=18.222655279661016
- **PERSISTENT_DOWN** `thermal_base` value=7422 d1=-28.0 d12=-962.0 z=18.029847855042018
- **ROBUST_OUTLIER** `thermal_base` value=7422 d1=-28.0 d12=-962.0 z=18.029847855042018
- **ROBUST_OUTLIER** `ind_demand` value=-1.089e+04 d1=0.0 d12=-6.0 z=-10.94172261111111
- **REVERSAL** `interconnector_net` value=-1358 d1=2.0 d12=-845.0 z=-5.66844355825718
- **ROBUST_OUTLIER** `interconnector_net` value=-1358 d1=2.0 d12=-845.0 z=-5.66844355825718
- **PERSISTENT_UP** `margin` value=3.753e+04 d1=26.0 d12=5.0 z=-4.39184803125
- **ACCELERATION** `margin` value=3.753e+04 d1=26.0 d12=5.0 z=-4.39184803125

## Nearest historical live analogues

- `2026-09-18T18:54:36.333288Z` distance=0.301 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:58:51.197302Z` distance=0.301 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:51:12.400587Z` distance=0.324 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:55:26.775797Z` distance=0.325 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:59:39.675441Z` distance=0.325 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
