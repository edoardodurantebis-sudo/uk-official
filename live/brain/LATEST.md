# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T19:11:44.164120Z`  
Memory snapshots: **1583**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.621e+04 d1=0.0 d12=-603.0 z=-38.378466775
- **ROBUST_OUTLIER** `ind_generation` value=1.621e+04 d1=0.0 d12=-603.0 z=-38.378466775
- **CHANGE_POINT** `imbalance` value=-3742 d1=0.0 d12=-603.0 z=-10.081846789473685
- **ROBUST_OUTLIER** `imbalance` value=-3742 d1=0.0 d12=-603.0 z=-10.081846789473685
- **PERSISTENT_UP** `interconnector_net` value=630 d1=493.0 d12=2736.0 z=3.0809966727369167
- **ROBUST_OUTLIER** `interconnector_net` value=630 d1=493.0 d12=2736.0 z=3.0809966727369167
- **PERSISTENT_DOWN** `ccgt_gen` value=6212 d1=-107.0 d12=-541.0 z=2.6204252104099677
- **PERSISTENT_DOWN** `thermal_base` value=9542 d1=-105.0 d12=-539.0 z=2.6019116596
- **REVERSAL** `biomass_gen` value=953 d1=-6.0 d12=118.0 z=2.0680390572687224
- **ACCELERATION** `biomass_gen` value=953 d1=-6.0 d12=118.0 z=2.0680390572687224
- **PERSISTENT_DOWN** `wind_gen` value=1.394e+04 d1=-130.0 d12=-387.0 z=-1.3254829308401639
- **PERSISTENT_UP** `ps_gen` value=825 d1=1.0 d12=1.0 z=0.6754780133699634
- **ACCELERATION** `ps_gen` value=825 d1=1.0 d12=1.0 z=0.6754780133699634
- **ACCELERATION** `nuclear_gen` value=3330 d1=2.0 d12=2.0 z=-0.2697959

## Nearest historical live analogues

- `2026-09-19T17:22:38.318939Z` distance=0.017 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:26:48.291042Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:31:01.384129Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:35:13.165368Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:39:26.231429Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
