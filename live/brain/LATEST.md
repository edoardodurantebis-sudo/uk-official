# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T15:36:16.570983Z`  
Memory snapshots: **1873**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1211 d1=51.0 d12=624.0 z=210.440802
- **PERSISTENT_UP** `biomass_gen` value=1211 d1=51.0 d12=624.0 z=210.440802
- **ROBUST_OUTLIER** `biomass_gen` value=1211 d1=51.0 d12=624.0 z=210.440802
- **CHANGE_POINT** `ccgt_gen` value=3217 d1=182.0 d12=747.0 z=35.61741034677419
- **PERSISTENT_UP** `ccgt_gen` value=3217 d1=182.0 d12=747.0 z=35.61741034677419
- **ROBUST_OUTLIER** `ccgt_gen` value=3217 d1=182.0 d12=747.0 z=35.61741034677419
- **CHANGE_POINT** `thermal_base` value=6545 d1=178.0 d12=746.0 z=32.21680452941177
- **PERSISTENT_UP** `thermal_base` value=6545 d1=178.0 d12=746.0 z=32.21680452941177
- **ROBUST_OUTLIER** `thermal_base` value=6545 d1=178.0 d12=746.0 z=32.21680452941177
- **ROBUST_OUTLIER** `imbalance` value=-5160 d1=0.0 d12=490.0 z=25.675576483333334
- **CHANGE_POINT** `interconnector_net` value=7944 d1=-1.0 d12=6281.0 z=6.6834768482293425
- **REVERSAL** `interconnector_net` value=7944 d1=-1.0 d12=6281.0 z=6.6834768482293425
- **ACCELERATION** `interconnector_net` value=7944 d1=-1.0 d12=6281.0 z=6.6834768482293425
- **ROBUST_OUTLIER** `interconnector_net` value=7944 d1=-1.0 d12=6281.0 z=6.6834768482293425
- **CHANGE_POINT** `margin` value=3.592e+04 d1=0.0 d12=535.0 z=4.016279875

## Nearest historical live analogues

- `2026-09-20T10:57:55.935414Z` distance=0.059 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:02:06.579348Z` distance=0.059 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:06:18.746524Z` distance=0.059 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:10:29.817646Z` distance=0.059 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:14:40.539694Z` distance=0.059 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
