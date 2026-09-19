# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T08:43:35.380561Z`  
Memory snapshots: **1434**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.78e+04 d1=0.0 d12=-1758.0 z=102.522442
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-3.0 z=-50.58673125
- **CHANGE_POINT** `interconnector_net` value=27 d1=0.0 d12=3893.0 z=26.7181030317029
- **ROBUST_OUTLIER** `interconnector_net` value=27 d1=0.0 d12=3893.0 z=26.7181030317029
- **PERSISTENT_DOWN** `ps_gen` value=-423 d1=-1.0 d12=-1.0 z=15.917958100000002
- **ACCELERATION** `ps_gen` value=-423 d1=-1.0 d12=-1.0 z=15.917958100000002
- **ROBUST_OUTLIER** `ps_gen` value=-423 d1=-1.0 d12=-1.0 z=15.917958100000002
- **ROBUST_OUTLIER** `margin` value=3.762e+04 d1=0.0 d12=589.0 z=-14.07997353125
- **CHANGE_POINT** `wind_gen` value=1.509e+04 d1=-14.0 d12=-630.0 z=-3.476915175925926
- **PERSISTENT_DOWN** `wind_gen` value=1.509e+04 d1=-14.0 d12=-630.0 z=-3.476915175925926
- **ROBUST_OUTLIER** `wind_gen` value=1.509e+04 d1=-14.0 d12=-630.0 z=-3.476915175925926
- **ROBUST_OUTLIER** `residual_proxy` value=8953 d1=0.0 d12=-3235.0 z=-3.094968789556962
- **PERSISTENT_DOWN** `biomass_gen` value=691 d1=-1.0 d12=-147.0 z=-0.696073422
- **REVERSAL** `ccgt_gen` value=3417 d1=-3.0 d12=175.0 z=0.638288322740113
- **REVERSAL** `thermal_base` value=6753 d1=-4.0 d12=170.0 z=0.6272565742296919

## Nearest historical live analogues

- `2026-09-19T07:23:46.754706Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:27:59.733660Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:32:11.773694Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:36:22.503128Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:40:34.209614Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
