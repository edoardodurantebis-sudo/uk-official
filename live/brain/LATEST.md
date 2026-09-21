# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T19:29:43.204818Z`  
Memory snapshots: **2268**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3021 d1=1.0 d12=49.0 z=3.888235029411765
- **CHANGE_POINT** `ind_generation` value=1.866e+04 d1=0.0 d12=330.0 z=3.83845985
- **PERSISTENT_DOWN** `margin` value=3.609e+04 d1=0.0 d12=-105.0 z=-5.331680880952381
- **ROBUST_OUTLIER** `margin` value=3.609e+04 d1=0.0 d12=-105.0 z=-5.331680880952381
- **CHANGE_POINT** `imbalance` value=-2794 d1=0.0 d12=330.0 z=2.60636162654321
- **PERSISTENT_UP** `ind_demand` value=-1.226e+04 d1=0.0 d12=18.0 z=4.0469385
- **ACCELERATION** `ind_demand` value=-1.226e+04 d1=0.0 d12=18.0 z=4.0469385
- **ROBUST_OUTLIER** `ind_demand` value=-1.226e+04 d1=0.0 d12=18.0 z=4.0469385
- **CHANGE_POINT** `interconnector_net` value=8391 d1=1.0 d12=1230.0 z=-2.011284919032258
- **PERSISTENT_UP** `biomass_gen` value=3021 d1=1.0 d12=49.0 z=3.888235029411765
- **ROBUST_OUTLIER** `biomass_gen` value=3021 d1=1.0 d12=49.0 z=3.888235029411765
- **PERSISTENT_UP** `ind_generation` value=1.866e+04 d1=0.0 d12=330.0 z=3.83845985
- **ACCELERATION** `ind_generation` value=1.866e+04 d1=0.0 d12=330.0 z=3.83845985
- **ROBUST_OUTLIER** `ind_generation` value=1.866e+04 d1=0.0 d12=330.0 z=3.83845985
- **CHANGE_POINT** `ps_gen` value=526 d1=0.0 d12=-74.0 z=0.9474597194117647

## Nearest historical live analogues

- `2026-09-21T17:21:51.078919Z` distance=0.045 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:26:03.425273Z` distance=0.046 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:30:18.299231Z` distance=0.046 → {'next30m_imbalance_delta': -24.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:34:31.100527Z` distance=0.046 → {'next30m_imbalance_delta': -24.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:38:44.713713Z` distance=0.046 → {'next30m_imbalance_delta': -24.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
