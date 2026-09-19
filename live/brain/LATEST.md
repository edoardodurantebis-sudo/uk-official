# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T08:39:24.027463Z`  
Memory snapshots: **1433**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low, wind rising.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.78e+04 d1=0.0 d12=-1758.0 z=102.522442
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-3.0 z=-50.58673125
- **REVERSAL** `interconnector_net` value=27 d1=-13.0 d12=3904.0 z=26.867789331056468
- **ROBUST_OUTLIER** `interconnector_net` value=27 d1=-13.0 d12=3904.0 z=26.867789331056468
- **PERSISTENT_UP** `ps_gen` value=-422 d1=1.0 d12=1.0 z=16.05285605
- **ACCELERATION** `ps_gen` value=-422 d1=1.0 d12=1.0 z=16.05285605
- **ROBUST_OUTLIER** `ps_gen` value=-422 d1=1.0 d12=1.0 z=16.05285605
- **ROBUST_OUTLIER** `margin` value=3.762e+04 d1=0.0 d12=589.0 z=-14.07997353125
- **CHANGE_POINT** `wind_gen` value=1.51e+04 d1=-39.0 d12=-608.0 z=-3.4086629647651003
- **PERSISTENT_DOWN** `wind_gen` value=1.51e+04 d1=-39.0 d12=-608.0 z=-3.4086629647651003
- **ROBUST_OUTLIER** `wind_gen` value=1.51e+04 d1=-39.0 d12=-608.0 z=-3.4086629647651003
- **PERSISTENT_DOWN** `residual_proxy` value=8953 d1=0.0 d12=-3235.0 z=-3.094968789556962
- **ROBUST_OUTLIER** `residual_proxy` value=8953 d1=0.0 d12=-3235.0 z=-3.094968789556962
- **REVERSAL** `biomass_gen` value=692 d1=1.0 d12=-165.0 z=-0.6833066094771242
- **PERSISTENT_UP** `ccgt_gen` value=3420 d1=19.0 d12=181.0 z=0.6406713224233983

## Nearest historical live analogues

- `2026-09-19T07:23:46.754706Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:27:59.733660Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:32:11.773694Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:36:22.503128Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:40:34.209614Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
