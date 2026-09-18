# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T10:08:28.605618Z`  
Memory snapshots: **1167**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **PERSISTENT_DOWN** `biomass_gen` value=1564 d1=-52.0 d12=-167.0 z=-25.251210015625
- **ROBUST_OUTLIER** `biomass_gen` value=1564 d1=-52.0 d12=-167.0 z=-25.251210015625
- **CHANGE_POINT** `ind_demand` value=-1.319e+04 d1=0.0 d12=-1454.0 z=-15.394236647058824
- **ROBUST_OUTLIER** `ind_demand` value=-1.319e+04 d1=0.0 d12=-1454.0 z=-15.394236647058824
- **CHANGE_POINT** `imbalance` value=7801 d1=0.0 d12=-1801.0 z=-9.321448345
- **ROBUST_OUTLIER** `imbalance` value=7801 d1=0.0 d12=-1801.0 z=-9.321448345
- **CHANGE_POINT** `margin` value=3.616e+04 d1=0.0 d12=-1517.0 z=-6.1283184861111115
- **ROBUST_OUTLIER** `margin` value=3.616e+04 d1=0.0 d12=-1517.0 z=-6.1283184861111115
- **CHANGE_POINT** `ind_generation` value=2.689e+04 d1=0.0 d12=-352.0 z=-3.29150998
- **PERSISTENT_DOWN** `ps_gen` value=-702 d1=-212.0 d12=-458.0 z=-4.693051658576052
- **ACCELERATION** `ps_gen` value=-702 d1=-212.0 d12=-458.0 z=-4.693051658576052
- **ROBUST_OUTLIER** `ps_gen` value=-702 d1=-212.0 d12=-458.0 z=-4.693051658576052
- **ROBUST_OUTLIER** `ind_generation` value=2.689e+04 d1=0.0 d12=-352.0 z=-3.29150998
- **CHANGE_POINT** `interconnector_net` value=5037 d1=173.0 d12=1187.0 z=0.884427649912075
- **REVERSAL** `wind_gen` value=1.17e+04 d1=-75.0 d12=32.0 z=-1.638914604890605

## Nearest historical live analogues

- `2026-09-18T08:34:36.525091Z` distance=1.876 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:38:47.543853Z` distance=1.876 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:43:00.251145Z` distance=1.876 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:47:16.640835Z` distance=1.876 → {'next30m_imbalance_delta': -23.0, 'next30m_margin_delta': 28.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T08:22:03.400207Z` distance=1.877 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 74.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
