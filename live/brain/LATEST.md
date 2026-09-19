# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T08:26:46.042793Z`  
Memory snapshots: **1430**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **PERSISTENT_DOWN** `ts_demand_forecast` value=1.78e+04 d1=0.0 d12=-610.0 z=102.522442
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.78e+04 d1=0.0 d12=-610.0 z=102.522442
- **PERSISTENT_DOWN** `ind_demand` value=-1.208e+04 d1=0.0 d12=-3.0 z=-50.58673125
- **ACCELERATION** `ind_demand` value=-1.208e+04 d1=0.0 d12=-3.0 z=-50.58673125
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-3.0 z=-50.58673125
- **REVERSAL** `interconnector_net` value=-1741 d1=-2.0 d12=2186.0 z=23.78484335721154
- **ROBUST_OUTLIER** `interconnector_net` value=-1741 d1=-2.0 d12=2186.0 z=23.78484335721154
- **ACCELERATION** `ps_gen` value=-423 d1=0.0 d12=-2.0 z=20.0660700625
- **ROBUST_OUTLIER** `ps_gen` value=-423 d1=0.0 d12=-2.0 z=20.0660700625
- **PERSISTENT_UP** `margin` value=3.762e+04 d1=0.0 d12=589.0 z=-14.07997353125
- **ACCELERATION** `margin` value=3.762e+04 d1=0.0 d12=589.0 z=-14.07997353125
- **ROBUST_OUTLIER** `margin` value=3.762e+04 d1=0.0 d12=589.0 z=-14.07997353125
- **CHANGE_POINT** `wind_gen` value=1.526e+04 d1=-114.0 d12=-448.0 z=-2.5848458121118014
- **CHANGE_POINT** `ind_generation` value=2.679e+04 d1=0.0 d12=-76.0 z=-2.348223574074074
- **PERSISTENT_DOWN** `residual_proxy` value=9068 d1=0.0 d12=-610.0 z=-2.6040427056962026

## Nearest historical live analogues

- `2026-09-19T07:23:46.754706Z` distance=0.218 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:27:59.733660Z` distance=0.218 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:32:11.773694Z` distance=0.218 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T06:54:14.045129Z` distance=0.671 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T06:58:26.669758Z` distance=0.671 → {'next30m_imbalance_delta': -1020.0, 'next30m_margin_delta': -1004.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
