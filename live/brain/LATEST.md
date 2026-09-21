# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T19:42:26.244827Z`  
Memory snapshots: **2271**  
Current physical regime: **BALANCED**

Regime read: margin low, wind rising.

## Active patterns

- **CHANGE_POINT** `margin` value=3.609e+04 d1=0.0 d12=-45.0 z=-5.331680880952381
- **CHANGE_POINT** `ind_generation` value=1.866e+04 d1=0.0 d12=330.0 z=3.83845985
- **CHANGE_POINT** `biomass_gen` value=3016 d1=-7.0 d12=49.0 z=3.4914763529411763
- **ROBUST_OUTLIER** `margin` value=3.609e+04 d1=0.0 d12=-45.0 z=-5.331680880952381
- **CHANGE_POINT** `imbalance` value=-2794 d1=0.0 d12=330.0 z=2.60636162654321
- **ROBUST_OUTLIER** `ind_demand` value=-1.226e+04 d1=0.0 d12=18.0 z=4.0469385
- **ROBUST_OUTLIER** `ind_generation` value=1.866e+04 d1=0.0 d12=330.0 z=3.83845985
- **REVERSAL** `biomass_gen` value=3016 d1=-7.0 d12=49.0 z=3.4914763529411763
- **ROBUST_OUTLIER** `biomass_gen` value=3016 d1=-7.0 d12=49.0 z=3.4914763529411763
- **CHANGE_POINT** `interconnector_net` value=9505 d1=2.0 d12=2343.0 z=-0.37140803340559714
- **CHANGE_POINT** `thermal_base` value=1.641e+04 d1=-24.0 d12=-682.0 z=0.18232551895613738
- **CHANGE_POINT** `ccgt_gen` value=1.289e+04 d1=-24.0 d12=-690.0 z=0.17937333958404364
- **PERSISTENT_UP** `nuclear_gen` value=3515 d1=0.0 d12=8.0 z=1.5176019375
- **ACCELERATION** `nuclear_gen` value=3515 d1=0.0 d12=8.0 z=1.5176019375
- **PERSISTENT_DOWN** `residual_proxy` value=1.234e+04 d1=0.0 d12=-1.0 z=-0.8431121875

## Nearest historical live analogues

- `2026-09-21T17:21:51.078919Z` distance=0.045 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:26:03.425273Z` distance=0.046 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:30:18.299231Z` distance=0.046 → {'next30m_imbalance_delta': -24.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:34:31.100527Z` distance=0.046 → {'next30m_imbalance_delta': -24.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:38:44.713713Z` distance=0.046 → {'next30m_imbalance_delta': -24.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
