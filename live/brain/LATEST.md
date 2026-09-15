# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T16:00:48.162751Z`  
Memory snapshots: **263**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=7076 d1=347.0 d12=3866.0 z=13.91086374566474
- **CHANGE_POINT** `thermal_base` value=1.04e+04 d1=352.0 d12=3859.0 z=13.78899504206501
- **PERSISTENT_UP** `ccgt_gen` value=7076 d1=347.0 d12=3866.0 z=13.91086374566474
- **ROBUST_OUTLIER** `ccgt_gen` value=7076 d1=347.0 d12=3866.0 z=13.91086374566474
- **PERSISTENT_UP** `thermal_base` value=1.04e+04 d1=352.0 d12=3859.0 z=13.78899504206501
- **ROBUST_OUTLIER** `thermal_base` value=1.04e+04 d1=352.0 d12=3859.0 z=13.78899504206501
- **PERSISTENT_DOWN** `interconnector_net` value=4346 d1=-670.0 d12=-2390.0 z=-11.90829403355263
- **ROBUST_OUTLIER** `interconnector_net` value=4346 d1=-670.0 d12=-2390.0 z=-11.90829403355263
- **REVERSAL** `ps_gen` value=-145 d1=-11.0 d12=134.0 z=3.393586605413106
- **ROBUST_OUTLIER** `ps_gen` value=-145 d1=-11.0 d12=134.0 z=3.393586605413106
- **CHANGE_POINT** `nuclear_gen` value=3325 d1=5.0 d12=-7.0 z=-0.6744897499999999
- **CHANGE_POINT** `margin` value=3.497e+04 d1=0.0 d12=344.0 z=-0.3646401169467787
- **PERSISTENT_UP** `imbalance` value=5825 d1=0.0 d12=7.0 z=1.087886693548387
- **ACCELERATION** `imbalance` value=5825 d1=0.0 d12=7.0 z=1.087886693548387
- **PERSISTENT_UP** `ind_generation` value=2.495e+04 d1=0.0 d12=7.0 z=1.023998075

## Nearest historical live analogues

- `2026-09-15T13:25:09.783150Z` distance=0.182 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:29:22.306019Z` distance=0.182 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:33:32.333732Z` distance=0.182 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:37:45.498739Z` distance=0.182 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:41:57.247780Z` distance=0.182 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
