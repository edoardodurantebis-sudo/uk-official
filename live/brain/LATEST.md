# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T00:01:48.158190Z`  
Memory snapshots: **1652**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **PERSISTENT_DOWN** `ps_gen` value=-253 d1=0.0 d12=-66.0 z=-62.96215188043478
- **ROBUST_OUTLIER** `ps_gen` value=-253 d1=0.0 d12=-66.0 z=-62.96215188043478
- **PERSISTENT_DOWN** `ind_demand` value=-1.189e+04 d1=0.0 d12=-1.0 z=-10.791836
- **ROBUST_OUTLIER** `ind_demand` value=-1.189e+04 d1=0.0 d12=-1.0 z=-10.791836
- **CHANGE_POINT** `wind_gen` value=1.614e+04 d1=-39.0 d12=321.0 z=3.260485257362785
- **CHANGE_POINT** `margin` value=3.599e+04 d1=0.0 d12=-65.0 z=-2.80587736
- **REVERSAL** `wind_gen` value=1.614e+04 d1=-39.0 d12=321.0 z=3.260485257362785
- **ACCELERATION** `wind_gen` value=1.614e+04 d1=-39.0 d12=321.0 z=3.260485257362785
- **ROBUST_OUTLIER** `wind_gen` value=1.614e+04 d1=-39.0 d12=321.0 z=3.260485257362785
- **REVERSAL** `ccgt_gen` value=3149 d1=3.0 d12=-439.0 z=-3.081016190261866
- **ROBUST_OUTLIER** `ccgt_gen` value=3149 d1=3.0 d12=-439.0 z=-3.081016190261866
- **REVERSAL** `thermal_base` value=6489 d1=10.0 d12=-437.0 z=-3.051942636086249
- **ROBUST_OUTLIER** `thermal_base` value=6489 d1=10.0 d12=-437.0 z=-3.051942636086249
- **CHANGE_POINT** `imbalance` value=-3708 d1=0.0 d12=231.0 z=0.9684981025641025
- **CHANGE_POINT** `ind_generation` value=1.624e+04 d1=0.0 d12=231.0 z=0.9684981025641025

## Nearest historical live analogues

- `2026-09-19T19:24:22.442601Z` distance=0.537 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -119.0}
- `2026-09-19T19:28:35.593770Z` distance=0.537 → {'next30m_imbalance_delta': -36.0, 'next30m_margin_delta': 40.0, 'next30m_residual_proxy_delta': -119.0}
- `2026-09-19T18:21:25.144867Z` distance=0.538 → {'next30m_imbalance_delta': -611.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T18:25:36.560673Z` distance=0.538 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T18:29:47.180961Z` distance=0.538 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
