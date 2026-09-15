# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T23:41:14.503194Z`  
Memory snapshots: **372**  
Current physical regime: **BALANCED**

Regime read: wind rising.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.208e+04 d1=0.0 d12=-166.0 z=-37.546596083333334
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-166.0 z=-37.546596083333334
- **CHANGE_POINT** `thermal_base` value=6557 d1=-1.0 d12=63.0 z=-8.25223546304348
- **CHANGE_POINT** `ccgt_gen` value=3228 d1=0.0 d12=62.0 z=-8.138380608183377
- **REVERSAL** `thermal_base` value=6557 d1=-1.0 d12=63.0 z=-8.25223546304348
- **ROBUST_OUTLIER** `thermal_base` value=6557 d1=-1.0 d12=63.0 z=-8.25223546304348
- **PERSISTENT_UP** `ccgt_gen` value=3228 d1=0.0 d12=62.0 z=-8.138380608183377
- **ROBUST_OUTLIER** `ccgt_gen` value=3228 d1=0.0 d12=62.0 z=-8.138380608183377
- **CHANGE_POINT** `biomass_gen` value=3223 d1=-12.0 d12=-31.0 z=-2.4849622368421054
- **PERSISTENT_DOWN** `biomass_gen` value=3223 d1=-12.0 d12=-31.0 z=-2.4849622368421054
- **REVERSAL** `interconnector_net` value=3985 d1=23.0 d12=-167.0 z=2.1930742476467953
- **CHANGE_POINT** `wind_gen` value=1.063e+04 d1=22.0 d12=-1287.0 z=-0.11970315798952194
- **CHANGE_POINT** `ps_gen` value=115 d1=-75.0 d12=270.0 z=-0.015027949868938401
- **REVERSAL** `nuclear_gen` value=3329 d1=-1.0 d12=1.0 z=1.7536733500000001
- **ACCELERATION** `nuclear_gen` value=3329 d1=-1.0 d12=1.0 z=1.7536733500000001

## Nearest historical live analogues

- `2026-09-15T17:50:55.506503Z` distance=0.725 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:55:09.760503Z` distance=0.725 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:59:22.215947Z` distance=0.725 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:03:35.364442Z` distance=0.725 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:07:47.333244Z` distance=0.725 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
