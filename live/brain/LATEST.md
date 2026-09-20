# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T08:38:07.929445Z`  
Memory snapshots: **1774**  
Current physical regime: **TIGHT**

Regime read: residual high, wind falling.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=583 d1=-2.0 d12=-306.0 z=-12.784174953846154
- **PERSISTENT_DOWN** `biomass_gen` value=583 d1=-2.0 d12=-306.0 z=-12.784174953846154
- **ROBUST_OUTLIER** `biomass_gen` value=583 d1=-2.0 d12=-306.0 z=-12.784174953846154
- **CHANGE_POINT** `ccgt_gen` value=2754 d1=-148.0 d12=-1179.0 z=-4.144162247747747
- **CHANGE_POINT** `thermal_base` value=6094 d1=-154.0 d12=-1174.0 z=-4.050906086764706
- **PERSISTENT_UP** `interconnector_net` value=-3245 d1=0.0 d12=3508.0 z=5.0370507263157895
- **ACCELERATION** `interconnector_net` value=-3245 d1=0.0 d12=3508.0 z=5.0370507263157895
- **ROBUST_OUTLIER** `interconnector_net` value=-3245 d1=0.0 d12=3508.0 z=5.0370507263157895
- **PERSISTENT_DOWN** `ccgt_gen` value=2754 d1=-148.0 d12=-1179.0 z=-4.144162247747747
- **ROBUST_OUTLIER** `ccgt_gen` value=2754 d1=-148.0 d12=-1179.0 z=-4.144162247747747
- **PERSISTENT_DOWN** `thermal_base` value=6094 d1=-154.0 d12=-1174.0 z=-4.050906086764706
- **ROBUST_OUTLIER** `thermal_base` value=6094 d1=-154.0 d12=-1174.0 z=-4.050906086764706
- **CHANGE_POINT** `ps_gen` value=-933 d1=2.0 d12=-6.0 z=-1.6395841263297872
- **CHANGE_POINT** `wind_gen` value=1.509e+04 d1=27.0 d12=-577.0 z=-0.9994711749999999
- **REVERSAL** `nuclear_gen` value=3340 d1=-6.0 d12=5.0 z=2.0234692499999998

## Nearest historical live analogues

- `2026-09-20T05:53:50.250426Z` distance=0.063 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:58:00.386850Z` distance=0.063 → {'next30m_imbalance_delta': -80.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:02:09.934243Z` distance=0.063 → {'next30m_imbalance_delta': -80.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:06:21.393634Z` distance=0.063 → {'next30m_imbalance_delta': -80.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:11:07.730851Z` distance=0.063 → {'next30m_imbalance_delta': -80.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
