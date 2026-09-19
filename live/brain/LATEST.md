# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T04:14:11.383607Z`  
Memory snapshots: **1370**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=9802 d1=0.0 d12=380.0 z=7.1925676880530975
- **CHANGE_POINT** `ind_generation` value=2.7e+04 d1=0.0 d12=379.0 z=7.180629816371681
- **ROBUST_OUTLIER** `imbalance` value=9802 d1=0.0 d12=380.0 z=7.1925676880530975
- **ROBUST_OUTLIER** `ind_generation` value=2.7e+04 d1=0.0 d12=379.0 z=7.180629816371681
- **PERSISTENT_DOWN** `biomass_gen` value=693 d1=0.0 d12=-110.0 z=-4.3571053193430656
- **ROBUST_OUTLIER** `biomass_gen` value=693 d1=0.0 d12=-110.0 z=-4.3571053193430656
- **CHANGE_POINT** `ind_demand` value=-1.088e+04 d1=0.0 d12=2.0 z=2.02346925
- **CHANGE_POINT** `thermal_base` value=6394 d1=-4.0 d12=-8.0 z=-1.936821952141058
- **CHANGE_POINT** `ccgt_gen` value=3058 d1=1.0 d12=0.0 z=-1.9167032845477388
- **CHANGE_POINT** `interconnector_net` value=-1.103e+04 d1=30.0 d12=128.0 z=-0.6623403123184196
- **CHANGE_POINT** `wind_gen` value=1.599e+04 d1=208.0 d12=-167.0 z=-0.4183713757455268
- **CHANGE_POINT** `ps_gen` value=-540 d1=-1.0 d12=4.0 z=0.018588300196850392
- **PERSISTENT_DOWN** `thermal_base` value=6394 d1=-4.0 d12=-8.0 z=-1.936821952141058
- **ACCELERATION** `thermal_base` value=6394 d1=-4.0 d12=-8.0 z=-1.936821952141058
- **ACCELERATION** `ccgt_gen` value=3058 d1=1.0 d12=0.0 z=-1.9167032845477388

## Nearest historical live analogues

- `2026-09-19T02:54:16.089654Z` distance=0.312 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:58:27.254129Z` distance=0.312 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:02:39.982753Z` distance=0.312 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T03:06:52.906018Z` distance=0.312 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 748.0}
- `2026-09-19T03:11:04.634985Z` distance=0.312 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 748.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
