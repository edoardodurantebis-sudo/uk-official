# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T04:05:47.150254Z`  
Memory snapshots: **1368**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.831e+04 d1=0.0 d12=1.0 z=7.507364173913043
- **CHANGE_POINT** `imbalance` value=9802 d1=0.0 d12=406.0 z=6.520067583333334
- **CHANGE_POINT** `ind_generation` value=2.7e+04 d1=0.0 d12=405.0 z=6.509361396825397
- **ROBUST_OUTLIER** `margin` value=3.831e+04 d1=0.0 d12=1.0 z=7.507364173913043
- **ROBUST_OUTLIER** `imbalance` value=9802 d1=0.0 d12=406.0 z=6.520067583333334
- **ROBUST_OUTLIER** `ind_generation` value=2.7e+04 d1=0.0 d12=405.0 z=6.509361396825397
- **PERSISTENT_DOWN** `biomass_gen` value=693 d1=-1.0 d12=-120.0 z=-4.469752970149254
- **ROBUST_OUTLIER** `biomass_gen` value=693 d1=-1.0 d12=-120.0 z=-4.469752970149254
- **CHANGE_POINT** `thermal_base` value=6398 d1=2.0 d12=3.0 z=-1.948714718513854
- **CHANGE_POINT** `ccgt_gen` value=3057 d1=-2.0 d12=0.0 z=-1.9455131482412058
- **CHANGE_POINT** `wind_gen` value=1.578e+04 d1=11.0 d12=-364.0 z=-0.9761658295898438
- **CHANGE_POINT** `interconnector_net` value=-1.106e+04 d1=2.0 d12=97.0 z=-0.6609283811086288
- **CHANGE_POINT** `ps_gen` value=-539 d1=2.0 d12=4.0 z=0.018451087386018236
- **PERSISTENT_DOWN** `ccgt_gen` value=3057 d1=-2.0 d12=0.0 z=-1.9455131482412058
- **ACCELERATION** `ccgt_gen` value=3057 d1=-2.0 d12=0.0 z=-1.9455131482412058

## Nearest historical live analogues

- `2026-09-19T02:54:16.089654Z` distance=0.312 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:58:27.254129Z` distance=0.312 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:02:39.982753Z` distance=0.312 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:06:52.906018Z` distance=0.312 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 748.0}
- `2026-09-19T03:11:04.634985Z` distance=0.312 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 748.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
