# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T04:09:59.344574Z`  
Memory snapshots: **1369**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=9802 d1=0.0 d12=406.0 z=6.520067583333334
- **CHANGE_POINT** `ind_generation` value=2.7e+04 d1=0.0 d12=405.0 z=6.509361396825397
- **ROBUST_OUTLIER** `margin` value=3.831e+04 d1=0.0 d12=1.0 z=8.215506299180328
- **ROBUST_OUTLIER** `imbalance` value=9802 d1=0.0 d12=406.0 z=6.520067583333334
- **ROBUST_OUTLIER** `ind_generation` value=2.7e+04 d1=0.0 d12=405.0 z=6.509361396825397
- **CHANGE_POINT** `ind_demand` value=-1.088e+04 d1=0.0 d12=3.0 z=2.697959
- **PERSISTENT_DOWN** `biomass_gen` value=693 d1=0.0 d12=-119.0 z=-4.431647468518519
- **ROBUST_OUTLIER** `biomass_gen` value=693 d1=0.0 d12=-119.0 z=-4.431647468518519
- **CHANGE_POINT** `thermal_base` value=6398 d1=0.0 d12=0.0 z=-1.936821952141058
- **CHANGE_POINT** `ccgt_gen` value=3057 d1=0.0 d12=0.0 z=-1.9353449610552764
- **CHANGE_POINT** `wind_gen` value=1.578e+04 d1=0.0 d12=-363.0 z=-0.9788817445328032
- **CHANGE_POINT** `interconnector_net` value=-1.106e+04 d1=0.0 d12=99.0 z=-0.6668424739229025
- **CHANGE_POINT** `ps_gen` value=-539 d1=0.0 d12=5.0 z=0.020718115187713312
- **ACCELERATION** `thermal_base` value=6398 d1=0.0 d12=0.0 z=-1.936821952141058
- **ACCELERATION** `ccgt_gen` value=3057 d1=0.0 d12=0.0 z=-1.9353449610552764

## Nearest historical live analogues

- `2026-09-19T02:54:16.089654Z` distance=0.312 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:58:27.254129Z` distance=0.312 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:02:39.982753Z` distance=0.312 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:06:52.906018Z` distance=0.312 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 748.0}
- `2026-09-19T03:11:04.634985Z` distance=0.312 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 748.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
