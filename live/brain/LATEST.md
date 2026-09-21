# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T19:33:55.455548Z`  
Memory snapshots: **2269**  
Current physical regime: **BALANCED**

Regime read: margin low, wind rising.

## Active patterns

- **CHANGE_POINT** `margin` value=3.609e+04 d1=0.0 d12=-105.0 z=-5.331680880952381
- **CHANGE_POINT** `biomass_gen` value=3024 d1=3.0 d12=52.0 z=4.1262902352941175
- **CHANGE_POINT** `ind_generation` value=1.866e+04 d1=0.0 d12=330.0 z=3.83845985
- **ROBUST_OUTLIER** `margin` value=3.609e+04 d1=0.0 d12=-105.0 z=-5.331680880952381
- **CHANGE_POINT** `imbalance` value=-2794 d1=0.0 d12=330.0 z=2.60636162654321
- **PERSISTENT_UP** `biomass_gen` value=3024 d1=3.0 d12=52.0 z=4.1262902352941175
- **ROBUST_OUTLIER** `biomass_gen` value=3024 d1=3.0 d12=52.0 z=4.1262902352941175
- **PERSISTENT_UP** `ind_demand` value=-1.226e+04 d1=0.0 d12=18.0 z=4.0469385
- **ROBUST_OUTLIER** `ind_demand` value=-1.226e+04 d1=0.0 d12=18.0 z=4.0469385
- **PERSISTENT_UP** `ind_generation` value=1.866e+04 d1=0.0 d12=330.0 z=3.83845985
- **ROBUST_OUTLIER** `ind_generation` value=1.866e+04 d1=0.0 d12=330.0 z=3.83845985
- **CHANGE_POINT** `interconnector_net` value=9505 d1=1114.0 d12=2344.0 z=-0.6519056354322839
- **PERSISTENT_UP** `imbalance` value=-2794 d1=0.0 d12=330.0 z=2.60636162654321
- **CHANGE_POINT** `thermal_base` value=1.639e+04 d1=-9.0 d12=-669.0 z=0.24165572657631113
- **CHANGE_POINT** `ccgt_gen` value=1.288e+04 d1=-11.0 d12=-669.0 z=0.2396633697485207

## Nearest historical live analogues

- `2026-09-21T17:21:51.078919Z` distance=0.045 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:26:03.425273Z` distance=0.046 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:30:18.299231Z` distance=0.046 → {'next30m_imbalance_delta': -24.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:34:31.100527Z` distance=0.046 → {'next30m_imbalance_delta': -24.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:38:44.713713Z` distance=0.046 → {'next30m_imbalance_delta': -24.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
