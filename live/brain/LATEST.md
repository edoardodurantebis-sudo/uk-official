# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T08:30:59.745119Z`  
Memory snapshots: **1431**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low, wind rising.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.78e+04 d1=0.0 d12=-610.0 z=102.522442
- **PERSISTENT_DOWN** `ind_demand` value=-1.208e+04 d1=0.0 d12=-3.0 z=-50.58673125
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-3.0 z=-50.58673125
- **PERSISTENT_UP** `interconnector_net` value=40 d1=1781.0 d12=3943.0 z=27.3505593625
- **ACCELERATION** `interconnector_net` value=40 d1=1781.0 d12=3943.0 z=27.3505593625
- **ROBUST_OUTLIER** `interconnector_net` value=40 d1=1781.0 d12=3943.0 z=27.3505593625
- **ROBUST_OUTLIER** `ps_gen` value=-423 d1=0.0 d12=-2.0 z=20.0660700625
- **PERSISTENT_UP** `margin` value=3.762e+04 d1=0.0 d12=589.0 z=-14.07997353125
- **ROBUST_OUTLIER** `margin` value=3.762e+04 d1=0.0 d12=589.0 z=-14.07997353125
- **CHANGE_POINT** `wind_gen` value=1.514e+04 d1=-115.0 d12=-550.0 z=-3.094968789556962
- **CHANGE_POINT** `ind_generation` value=2.679e+04 d1=0.0 d12=-76.0 z=-2.348223574074074
- **PERSISTENT_DOWN** `residual_proxy` value=8953 d1=-115.0 d12=-725.0 z=-3.094968789556962
- **ROBUST_OUTLIER** `residual_proxy` value=8953 d1=-115.0 d12=-725.0 z=-3.094968789556962
- **PERSISTENT_DOWN** `wind_gen` value=1.514e+04 d1=-115.0 d12=-550.0 z=-3.094968789556962
- **ROBUST_OUTLIER** `wind_gen` value=1.514e+04 d1=-115.0 d12=-550.0 z=-3.094968789556962

## Nearest historical live analogues

- `2026-09-19T07:23:46.754706Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:27:59.733660Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:32:11.773694Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:36:22.503128Z` distance=0.231 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T06:54:14.045129Z` distance=0.675 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
