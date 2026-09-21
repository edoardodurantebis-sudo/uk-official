# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T19:38:10.834672Z`  
Memory snapshots: **2270**  
Current physical regime: **BALANCED**

Regime read: margin low, wind rising.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3023 d1=-1.0 d12=55.0 z=4.0469385
- **CHANGE_POINT** `ind_generation` value=1.866e+04 d1=0.0 d12=330.0 z=3.83845985
- **ROBUST_OUTLIER** `margin` value=3.609e+04 d1=0.0 d12=-105.0 z=-5.331680880952381
- **CHANGE_POINT** `imbalance` value=-2794 d1=0.0 d12=330.0 z=2.60636162654321
- **REVERSAL** `biomass_gen` value=3023 d1=-1.0 d12=55.0 z=4.0469385
- **ROBUST_OUTLIER** `biomass_gen` value=3023 d1=-1.0 d12=55.0 z=4.0469385
- **ROBUST_OUTLIER** `ind_demand` value=-1.226e+04 d1=0.0 d12=18.0 z=4.0469385
- **ROBUST_OUTLIER** `ind_generation` value=1.866e+04 d1=0.0 d12=330.0 z=3.83845985
- **CHANGE_POINT** `interconnector_net` value=9503 d1=-2.0 d12=2341.0 z=-0.4326968425385577
- **CHANGE_POINT** `thermal_base` value=1.643e+04 d1=40.0 d12=-645.0 z=0.22137431756324047
- **CHANGE_POINT** `ccgt_gen` value=1.292e+04 d1=37.0 d12=-654.0 z=0.21840207773851592
- **PERSISTENT_UP** `nuclear_gen` value=3515 d1=3.0 d12=9.0 z=1.5176019375
- **PERSISTENT_DOWN** `residual_proxy` value=1.234e+04 d1=0.0 d12=-1.0 z=-0.8431121875
- **ACCELERATION** `residual_proxy` value=1.234e+04 d1=0.0 d12=-1.0 z=-0.8431121875
- **REVERSAL** `interconnector_net` value=9503 d1=-2.0 d12=2341.0 z=-0.4326968425385577

## Nearest historical live analogues

- `2026-09-21T17:21:51.078919Z` distance=0.045 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:26:03.425273Z` distance=0.046 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:30:18.299231Z` distance=0.046 → {'next30m_imbalance_delta': -24.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:34:31.100527Z` distance=0.046 → {'next30m_imbalance_delta': -24.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:38:44.713713Z` distance=0.046 → {'next30m_imbalance_delta': -24.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
