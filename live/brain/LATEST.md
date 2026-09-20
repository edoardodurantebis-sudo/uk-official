# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T17:10:24.155719Z`  
Memory snapshots: **1895**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **PERSISTENT_UP** `biomass_gen` value=2210 d1=75.0 d12=292.0 z=273.505593625
- **ROBUST_OUTLIER** `biomass_gen` value=2210 d1=75.0 d12=292.0 z=273.505593625
- **CHANGE_POINT** `thermal_base` value=1.094e+04 d1=468.0 d12=3290.0 z=114.75171517213116
- **CHANGE_POINT** `ccgt_gen` value=7597 d1=469.0 d12=3289.0 z=114.61902866393443
- **PERSISTENT_UP** `thermal_base` value=1.094e+04 d1=468.0 d12=3290.0 z=114.75171517213116
- **ROBUST_OUTLIER** `thermal_base` value=1.094e+04 d1=468.0 d12=3290.0 z=114.75171517213116
- **PERSISTENT_UP** `ccgt_gen` value=7597 d1=469.0 d12=3289.0 z=114.61902866393443
- **ROBUST_OUTLIER** `ccgt_gen` value=7597 d1=469.0 d12=3289.0 z=114.61902866393443
- **CHANGE_POINT** `imbalance` value=-5190 d1=0.0 d12=-24.0 z=13.749214134615384
- **ROBUST_OUTLIER** `imbalance` value=-5190 d1=0.0 d12=-24.0 z=13.749214134615384
- **CHANGE_POINT** `ps_gen` value=62 d1=-103.0 d12=75.0 z=4.317328664096916
- **REVERSAL** `ps_gen` value=62 d1=-103.0 d12=75.0 z=4.317328664096916
- **ACCELERATION** `ps_gen` value=62 d1=-103.0 d12=75.0 z=4.317328664096916
- **ROBUST_OUTLIER** `ps_gen` value=62 d1=-103.0 d12=75.0 z=4.317328664096916
- **REVERSAL** `interconnector_net` value=1.096e+04 d1=-692.0 d12=836.0 z=3.1215995899526563

## Nearest historical live analogues

- `2026-09-20T14:54:10.136499Z` distance=0.029 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:58:25.329493Z` distance=0.029 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:02:37.176302Z` distance=0.029 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:06:50.185709Z` distance=0.029 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:11:00.797261Z` distance=0.029 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
