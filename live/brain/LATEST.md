# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T11:07:25.674417Z`  
Memory snapshots: **2150**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.224e+04 d1=0.0 d12=568.0 z=14.735006846153848
- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=0.0 d12=568.0 z=14.735006846153848
- **CHANGE_POINT** `nuclear_gen` value=3519 d1=10.0 d12=23.0 z=3.37244875
- **CHANGE_POINT** `margin` value=3.65e+04 d1=0.0 d12=-3324.0 z=-1.6940672790697675
- **REVERSAL** `ccgt_gen` value=6683 d1=32.0 d12=-435.0 z=-3.6671194492907797
- **ROBUST_OUTLIER** `ccgt_gen` value=6683 d1=32.0 d12=-435.0 z=-3.6671194492907797
- **REVERSAL** `thermal_base` value=1.02e+04 d1=42.0 d12=-412.0 z=-3.3824344663526245
- **ROBUST_OUTLIER** `thermal_base` value=1.02e+04 d1=42.0 d12=-412.0 z=-3.3824344663526245
- **PERSISTENT_UP** `nuclear_gen` value=3519 d1=10.0 d12=23.0 z=3.37244875
- **ROBUST_OUTLIER** `nuclear_gen` value=3519 d1=10.0 d12=23.0 z=3.37244875
- **CHANGE_POINT** `residual_proxy` value=1.218e+04 d1=0.0 d12=1462.0 z=1.2135229663561076
- **CHANGE_POINT** `interconnector_net` value=1.126e+04 d1=-21.0 d12=481.0 z=1.0157304173578199
- **CHANGE_POINT** `imbalance` value=-3871 d1=0.0 d12=-4440.0 z=-0.5238932564276049
- **CHANGE_POINT** `ind_generation` value=1.774e+04 d1=0.0 d12=-3991.0 z=-0.11899781625375375
- **REVERSAL** `interconnector_net` value=1.126e+04 d1=-21.0 d12=481.0 z=1.0157304173578199

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.508 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.508 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.508 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.508 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.508 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
