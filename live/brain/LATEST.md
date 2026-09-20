# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T16:32:01.838816Z`  
Memory snapshots: **1886**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2020 d1=8.0 d12=809.0 z=483.271905875
- **PERSISTENT_UP** `biomass_gen` value=2020 d1=8.0 d12=809.0 z=483.271905875
- **ROBUST_OUTLIER** `biomass_gen` value=2020 d1=8.0 d12=809.0 z=483.271905875
- **CHANGE_POINT** `ccgt_gen` value=5113 d1=422.0 d12=1896.0 z=76.06277118229167
- **CHANGE_POINT** `thermal_base` value=8446 d1=422.0 d12=1901.0 z=74.52423482653062
- **PERSISTENT_UP** `ccgt_gen` value=5113 d1=422.0 d12=1896.0 z=76.06277118229167
- **ROBUST_OUTLIER** `ccgt_gen` value=5113 d1=422.0 d12=1896.0 z=76.06277118229167
- **PERSISTENT_UP** `thermal_base` value=8446 d1=422.0 d12=1901.0 z=74.52423482653062
- **ROBUST_OUTLIER** `thermal_base` value=8446 d1=422.0 d12=1901.0 z=74.52423482653062
- **CHANGE_POINT** `imbalance` value=-5182 d1=0.0 d12=-22.0 z=13.956749442307693
- **PERSISTENT_DOWN** `imbalance` value=-5182 d1=0.0 d12=-22.0 z=13.956749442307693
- **ACCELERATION** `imbalance` value=-5182 d1=0.0 d12=-22.0 z=13.956749442307693
- **ROBUST_OUTLIER** `imbalance` value=-5182 d1=0.0 d12=-22.0 z=13.956749442307693
- **PERSISTENT_UP** `interconnector_net` value=1.196e+04 d1=1845.0 d12=4021.0 z=5.771664604067322
- **ACCELERATION** `interconnector_net` value=1.196e+04 d1=1845.0 d12=4021.0 z=5.771664604067322

## Nearest historical live analogues

- `2026-09-20T14:54:10.136499Z` distance=0.032 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:58:25.329493Z` distance=0.032 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:02:37.176302Z` distance=0.032 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:06:50.185709Z` distance=0.032 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:11:00.797261Z` distance=0.032 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
