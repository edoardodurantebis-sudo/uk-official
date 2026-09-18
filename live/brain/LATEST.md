# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T10:04:17.308046Z`  
Memory snapshots: **1166**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1616 d1=-34.0 d12=-128.0 z=-23.059118328125
- **PERSISTENT_DOWN** `biomass_gen` value=1616 d1=-34.0 d12=-128.0 z=-23.059118328125
- **ROBUST_OUTLIER** `biomass_gen` value=1616 d1=-34.0 d12=-128.0 z=-23.059118328125
- **CHANGE_POINT** `ind_demand` value=-1.319e+04 d1=0.0 d12=-1454.0 z=-15.394236647058824
- **ROBUST_OUTLIER** `ind_demand` value=-1.319e+04 d1=0.0 d12=-1454.0 z=-15.394236647058824
- **CHANGE_POINT** `imbalance` value=7801 d1=0.0 d12=-1801.0 z=-9.321448345
- **ROBUST_OUTLIER** `imbalance` value=7801 d1=0.0 d12=-1801.0 z=-9.321448345
- **CHANGE_POINT** `margin` value=3.616e+04 d1=0.0 d12=-1517.0 z=-6.1283184861111115
- **ROBUST_OUTLIER** `margin` value=3.616e+04 d1=0.0 d12=-1517.0 z=-6.1283184861111115
- **CHANGE_POINT** `ind_generation` value=2.689e+04 d1=0.0 d12=-352.0 z=-3.29150998
- **PERSISTENT_DOWN** `ps_gen` value=-490 d1=0.0 d12=-424.0 z=-3.7942794731270357
- **ROBUST_OUTLIER** `ps_gen` value=-490 d1=0.0 d12=-424.0 z=-3.7942794731270357
- **ROBUST_OUTLIER** `ind_generation` value=2.689e+04 d1=0.0 d12=-352.0 z=-3.29150998
- **CHANGE_POINT** `interconnector_net` value=4864 d1=38.0 d12=974.0 z=0.865180691218047
- **REVERSAL** `wind_gen` value=1.178e+04 d1=-18.0 d12=20.0 z=-1.6007008380718954

## Nearest historical live analogues

- `2026-09-18T08:34:36.525091Z` distance=1.876 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:38:47.543853Z` distance=1.876 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:43:00.251145Z` distance=1.876 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:47:16.640835Z` distance=1.876 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:22:03.400207Z` distance=1.877 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 74.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
