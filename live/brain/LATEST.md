# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T17:01:26.148147Z`  
Memory snapshots: **1893**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **PERSISTENT_UP** `biomass_gen` value=2135 d1=40.0 d12=423.0 z=260.8589108125
- **ROBUST_OUTLIER** `biomass_gen` value=2135 d1=40.0 d12=423.0 z=260.8589108125
- **CHANGE_POINT** `thermal_base` value=1.047e+04 d1=432.0 d12=3264.0 z=104.40216753278688
- **CHANGE_POINT** `ccgt_gen` value=7128 d1=434.0 d12=3259.0 z=104.24736660655738
- **PERSISTENT_UP** `thermal_base` value=1.047e+04 d1=432.0 d12=3264.0 z=104.40216753278688
- **ROBUST_OUTLIER** `thermal_base` value=1.047e+04 d1=432.0 d12=3264.0 z=104.40216753278688
- **PERSISTENT_UP** `ccgt_gen` value=7128 d1=434.0 d12=3259.0 z=104.24736660655738
- **ROBUST_OUTLIER** `ccgt_gen` value=7128 d1=434.0 d12=3259.0 z=104.24736660655738
- **CHANGE_POINT** `imbalance` value=-5190 d1=0.0 d12=-24.0 z=13.749214134615384
- **PERSISTENT_DOWN** `imbalance` value=-5190 d1=0.0 d12=-24.0 z=13.749214134615384
- **ROBUST_OUTLIER** `imbalance` value=-5190 d1=0.0 d12=-24.0 z=13.749214134615384
- **CHANGE_POINT** `ps_gen` value=165 d1=-26.0 d12=178.0 z=5.10949084589041
- **REVERSAL** `ps_gen` value=165 d1=-26.0 d12=178.0 z=5.10949084589041
- **ROBUST_OUTLIER** `ps_gen` value=165 d1=-26.0 d12=178.0 z=5.10949084589041
- **REVERSAL** `interconnector_net` value=1.165e+04 d1=-307.0 d12=1973.0 z=3.2882854975868727

## Nearest historical live analogues

- `2026-09-20T14:54:10.136499Z` distance=0.029 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:58:25.329493Z` distance=0.029 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:02:37.176302Z` distance=0.029 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:06:50.185709Z` distance=0.029 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:11:00.797261Z` distance=0.029 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
