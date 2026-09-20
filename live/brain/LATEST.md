# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T10:28:27.509845Z`  
Memory snapshots: **1800**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.978e+04 d1=0.0 d12=889.0 z=27.6908701
- **PERSISTENT_UP** `margin` value=3.978e+04 d1=0.0 d12=889.0 z=27.6908701
- **ROBUST_OUTLIER** `margin` value=3.978e+04 d1=0.0 d12=889.0 z=27.6908701
- **CHANGE_POINT** `ind_generation` value=1.603e+04 d1=0.0 d12=47.0 z=24.0118351
- **PERSISTENT_UP** `ind_generation` value=1.603e+04 d1=0.0 d12=47.0 z=24.0118351
- **ROBUST_OUTLIER** `ind_generation` value=1.603e+04 d1=0.0 d12=47.0 z=24.0118351
- **CHANGE_POINT** `ind_demand` value=-1.247e+04 d1=0.0 d12=-90.0 z=-13.40548378125
- **PERSISTENT_DOWN** `ind_demand` value=-1.247e+04 d1=0.0 d12=-90.0 z=-13.40548378125
- **ROBUST_OUTLIER** `ind_demand` value=-1.247e+04 d1=0.0 d12=-90.0 z=-13.40548378125
- **CHANGE_POINT** `imbalance` value=-4140 d1=0.0 d12=47.0 z=7.1927368481781375
- **PERSISTENT_UP** `imbalance` value=-4140 d1=0.0 d12=47.0 z=7.1927368481781375
- **ROBUST_OUTLIER** `imbalance` value=-4140 d1=0.0 d12=47.0 z=7.1927368481781375
- **CHANGE_POINT** `wind_gen` value=1.403e+04 d1=22.0 d12=-857.0 z=-2.7280979872881357
- **REVERSAL** `wind_gen` value=1.403e+04 d1=22.0 d12=-857.0 z=-2.7280979872881357
- **CHANGE_POINT** `biomass_gen` value=595 d1=3.0 d12=8.0 z=-0.663172807885906

## Nearest historical live analogues

- `2026-09-20T09:20:07.153673Z` distance=0.336 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:24:18.809197Z` distance=0.336 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:28:32.169507Z` distance=0.336 → {'next30m_imbalance_delta': 33.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:32:44.320157Z` distance=0.336 → {'next30m_imbalance_delta': 33.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T07:22:31.595881Z` distance=0.658 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
