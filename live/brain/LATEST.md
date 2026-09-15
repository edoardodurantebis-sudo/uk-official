# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T06:18:52.397173Z`  
Memory snapshots: **125**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.99e+04 d1=0.0 d12=-63.0 z=-12.080860855555557
- **CHANGE_POINT** `imbalance` value=-587 d1=0.0 d12=-63.0 z=-11.803570625
- **ROBUST_OUTLIER** `ind_generation` value=1.99e+04 d1=0.0 d12=-63.0 z=-12.080860855555557
- **ROBUST_OUTLIER** `imbalance` value=-587 d1=0.0 d12=-63.0 z=-11.803570625
- **CHANGE_POINT** `ccgt_gen` value=4008 d1=-72.0 d12=179.0 z=1.0680781997578692
- **CHANGE_POINT** `thermal_base` value=7331 d1=-72.0 d12=176.0 z=1.0499286228915663
- **CHANGE_POINT** `margin` value=3.393e+04 d1=0.0 d12=-65.0 z=-0.39144494419642856
- **CHANGE_POINT** `interconnector_net` value=-2101 d1=-33.0 d12=3243.0 z=0.3728897379120879
- **REVERSAL** `ccgt_gen` value=4008 d1=-72.0 d12=179.0 z=1.0680781997578692
- **REVERSAL** `thermal_base` value=7331 d1=-72.0 d12=176.0 z=1.0499286228915663
- **ACCELERATION** `wind_gen` value=1.348e+04 d1=-24.0 d12=-24.0 z=0.6918991462020648
- **REVERSAL** `biomass_gen` value=3209 d1=-2.0 d12=13.0 z=0.5138969523809523
- **ACCELERATION** `biomass_gen` value=3209 d1=-2.0 d12=13.0 z=0.5138969523809523
- **PERSISTENT_DOWN** `nuclear_gen` value=3323 d1=0.0 d12=-3.0 z=-0.4496598333333333
- **ACCELERATION** `nuclear_gen` value=3323 d1=0.0 d12=-3.0 z=-0.4496598333333333

## Nearest historical live analogues

- `2026-09-15T05:24:11.392435Z` distance=0.119 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -671.0}
- `2026-09-15T05:20:00.210059Z` distance=0.121 → {'next30m_imbalance_delta': -51.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -671.0}
- `2026-09-15T04:50:38.818178Z` distance=0.198 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:54:51.558349Z` distance=0.198 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -73.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:59:03.674440Z` distance=0.198 → {'next30m_imbalance_delta': -51.0, 'next30m_margin_delta': -73.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
