# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T15:15:13.542235Z`  
Memory snapshots: **1868**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=930 d1=0.0 d12=343.0 z=232.024474
- **PERSISTENT_UP** `biomass_gen` value=930 d1=0.0 d12=343.0 z=232.024474
- **ROBUST_OUTLIER** `biomass_gen` value=930 d1=0.0 d12=343.0 z=232.024474
- **ROBUST_OUTLIER** `imbalance` value=-5158 d1=0.0 d12=573.0 z=25.765508450000002
- **CHANGE_POINT** `ccgt_gen` value=2706 d1=0.0 d12=261.0 z=13.381006330645162
- **CHANGE_POINT** `thermal_base` value=6041 d1=0.0 d12=265.0 z=12.220167235294117
- **PERSISTENT_UP** `ccgt_gen` value=2706 d1=0.0 d12=261.0 z=13.381006330645162
- **ROBUST_OUTLIER** `ccgt_gen` value=2706 d1=0.0 d12=261.0 z=13.381006330645162
- **PERSISTENT_UP** `thermal_base` value=6041 d1=0.0 d12=265.0 z=12.220167235294117
- **ROBUST_OUTLIER** `thermal_base` value=6041 d1=0.0 d12=265.0 z=12.220167235294117
- **CHANGE_POINT** `interconnector_net` value=4994 d1=0.0 d12=5120.0 z=6.2002654029579665
- **PERSISTENT_UP** `interconnector_net` value=4994 d1=0.0 d12=5120.0 z=6.2002654029579665
- **ROBUST_OUTLIER** `interconnector_net` value=4994 d1=0.0 d12=5120.0 z=6.2002654029579665
- **CHANGE_POINT** `margin` value=3.591e+04 d1=0.0 d12=521.0 z=3.587059125
- **ROBUST_OUTLIER** `residual_proxy` value=1.782e+04 d1=0.0 d12=-494.0 z=-3.889865544520548

## Nearest historical live analogues

- `2026-09-20T10:57:55.935414Z` distance=0.055 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:02:06.579348Z` distance=0.055 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:06:18.746524Z` distance=0.055 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:10:29.817646Z` distance=0.055 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:14:40.539694Z` distance=0.055 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
