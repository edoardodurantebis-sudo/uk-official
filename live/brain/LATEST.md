# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T10:12:40.575314Z`  
Memory snapshots: **1168**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **PERSISTENT_DOWN** `biomass_gen` value=1515 d1=-49.0 d12=-217.0 z=-27.316834875
- **ROBUST_OUTLIER** `biomass_gen` value=1515 d1=-49.0 d12=-217.0 z=-27.316834875
- **CHANGE_POINT** `ind_demand` value=-1.319e+04 d1=0.0 d12=-4.0 z=-15.394236647058824
- **ROBUST_OUTLIER** `ind_demand` value=-1.319e+04 d1=0.0 d12=-4.0 z=-15.394236647058824
- **CHANGE_POINT** `imbalance` value=7801 d1=0.0 d12=-299.0 z=-9.321448345
- **ROBUST_OUTLIER** `imbalance` value=7801 d1=0.0 d12=-299.0 z=-9.321448345
- **CHANGE_POINT** `margin` value=3.616e+04 d1=0.0 d12=-45.0 z=-6.2551517125323
- **ROBUST_OUTLIER** `margin` value=3.616e+04 d1=0.0 d12=-45.0 z=-6.2551517125323
- **CHANGE_POINT** `ind_generation` value=2.689e+04 d1=0.0 d12=-299.0 z=-3.29150998
- **PERSISTENT_DOWN** `ps_gen` value=-718 d1=-16.0 d12=-290.0 z=-4.695569218051118
- **ACCELERATION** `ps_gen` value=-718 d1=-16.0 d12=-290.0 z=-4.695569218051118
- **ROBUST_OUTLIER** `ps_gen` value=-718 d1=-16.0 d12=-290.0 z=-4.695569218051118
- **ROBUST_OUTLIER** `ind_generation` value=2.689e+04 d1=0.0 d12=-299.0 z=-3.29150998
- **CHANGE_POINT** `interconnector_net` value=5104 d1=67.0 d12=1232.0 z=0.8904368482174168
- **ACCELERATION** `wind_gen` value=1.17e+04 d1=3.0 d12=68.0 z=-1.6233555353939781

## Nearest historical live analogues

- `2026-09-18T08:34:36.525091Z` distance=1.876 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:38:47.543853Z` distance=1.876 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:43:00.251145Z` distance=1.876 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:47:16.640835Z` distance=1.876 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:22:03.400207Z` distance=1.877 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 74.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
