# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T06:14:39.871456Z`  
Memory snapshots: **124**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.99e+04 d1=0.0 d12=-63.0 z=-12.080860855555557
- **CHANGE_POINT** `imbalance` value=-587 d1=0.0 d12=-63.0 z=-11.803570625
- **ROBUST_OUTLIER** `ind_generation` value=1.99e+04 d1=0.0 d12=-63.0 z=-12.080860855555557
- **ROBUST_OUTLIER** `imbalance` value=-587 d1=0.0 d12=-63.0 z=-11.803570625
- **CHANGE_POINT** `ccgt_gen` value=4080 d1=-51.0 d12=253.0 z=1.303251381355932
- **CHANGE_POINT** `thermal_base` value=7403 d1=-54.0 d12=248.0 z=1.2839684397590363
- **CHANGE_POINT** `margin` value=3.393e+04 d1=0.0 d12=-65.0 z=-0.39144494419642856
- **CHANGE_POINT** `interconnector_net` value=-2068 d1=453.0 d12=3226.0 z=0.38178410824175824
- **REVERSAL** `ccgt_gen` value=4080 d1=-51.0 d12=253.0 z=1.303251381355932
- **REVERSAL** `thermal_base` value=7403 d1=-54.0 d12=248.0 z=1.2839684397590363
- **PERSISTENT_UP** `wind_gen` value=1.35e+04 d1=96.0 d12=38.0 z=0.8133839542991329
- **ACCELERATION** `wind_gen` value=1.35e+04 d1=96.0 d12=38.0 z=0.8133839542991329
- **PERSISTENT_UP** `biomass_gen` value=3211 d1=13.0 d12=10.0 z=0.6131725
- **ACCELERATION** `biomass_gen` value=3211 d1=13.0 d12=10.0 z=0.6131725
- **ACCELERATION** `nuclear_gen` value=3323 d1=-3.0 d12=-5.0 z=-0.4496598333333333

## Nearest historical live analogues

- `2026-09-15T05:20:00.210059Z` distance=0.121 → {'next30m_imbalance_delta': -51.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -671.0}
- `2026-09-15T04:50:38.818178Z` distance=0.198 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:54:51.558349Z` distance=0.198 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -73.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:59:03.674440Z` distance=0.198 → {'next30m_imbalance_delta': -51.0, 'next30m_margin_delta': -73.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T05:03:14.856536Z` distance=0.198 → {'next30m_imbalance_delta': -51.0, 'next30m_margin_delta': -73.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
