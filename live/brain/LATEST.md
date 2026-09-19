# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T08:47:46.727541Z`  
Memory snapshots: **1435**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.78e+04 d1=0.0 d12=-1758.0 z=102.522442
- **ROBUST_OUTLIER** `ind_demand` value=-1.208e+04 d1=0.0 d12=-3.0 z=-50.58673125
- **ROBUST_OUTLIER** `interconnector_net` value=28 d1=1.0 d12=3871.0 z=25.44422300431779
- **ACCELERATION** `ps_gen` value=-423 d1=0.0 d12=-2.0 z=15.917958100000002
- **ROBUST_OUTLIER** `ps_gen` value=-423 d1=0.0 d12=-2.0 z=15.917958100000002
- **ROBUST_OUTLIER** `margin` value=3.762e+04 d1=0.0 d12=589.0 z=-14.07997353125
- **CHANGE_POINT** `wind_gen` value=1.506e+04 d1=-30.0 d12=-656.0 z=-3.7050096684027776
- **PERSISTENT_DOWN** `wind_gen` value=1.506e+04 d1=-30.0 d12=-656.0 z=-3.7050096684027776
- **ROBUST_OUTLIER** `wind_gen` value=1.506e+04 d1=-30.0 d12=-656.0 z=-3.7050096684027776
- **ROBUST_OUTLIER** `residual_proxy` value=8953 d1=0.0 d12=-3235.0 z=-3.094968789556962
- **PERSISTENT_DOWN** `nuclear_gen` value=3335 d1=-1.0 d12=0.0 z=-0.6744897499999999
- **REVERSAL** `ccgt_gen` value=3336 d1=-81.0 d12=78.0 z=0.33055729957507085
- **ACCELERATION** `ccgt_gen` value=3336 d1=-81.0 d12=78.0 z=0.33055729957507085
- **REVERSAL** `thermal_base` value=6671 d1=-82.0 d12=78.0 z=0.31829853370786515
- **ACCELERATION** `thermal_base` value=6671 d1=-82.0 d12=78.0 z=0.31829853370786515

## Nearest historical live analogues

- `2026-09-19T07:23:46.754706Z` distance=0.230 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:27:59.733660Z` distance=0.230 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:32:11.773694Z` distance=0.230 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:36:22.503128Z` distance=0.230 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}
- `2026-09-19T07:40:34.209614Z` distance=0.230 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 2510.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
