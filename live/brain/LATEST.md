# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T11:45:51.147987Z`  
Memory snapshots: **1477**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.678e+04 d1=0.0 d12=25.0 z=-84.23999933540372
- **ROBUST_OUTLIER** `ind_generation` value=1.678e+04 d1=0.0 d12=25.0 z=-84.23999933540372
- **CHANGE_POINT** `imbalance` value=-3354 d1=0.0 d12=24.0 z=-8.795375538690475
- **ROBUST_OUTLIER** `imbalance` value=-3354 d1=0.0 d12=24.0 z=-8.795375538690475
- **CHANGE_POINT** `residual_proxy` value=1.298e+04 d1=0.0 d12=0.0 z=3.0673002837931036
- **CHANGE_POINT** `ps_gen` value=-939 d1=-2.0 d12=-244.0 z=-2.2157824431818183
- **ROBUST_OUTLIER** `demand_forecast` value=1.963e+04 d1=0.0 d12=0.0 z=3.40672609795082
- **ROBUST_OUTLIER** `residual_proxy` value=1.298e+04 d1=0.0 d12=0.0 z=3.0673002837931036
- **CHANGE_POINT** `margin` value=3.666e+04 d1=0.0 d12=1108.0 z=-0.43050041434782604
- **PERSISTENT_DOWN** `ps_gen` value=-939 d1=-2.0 d12=-244.0 z=-2.2157824431818183
- **CHANGE_POINT** `ind_demand` value=-1.178e+04 d1=0.0 d12=0.0 z=0.17693481117957746
- **PERSISTENT_DOWN** `thermal_base` value=6116 d1=-3.0 d12=-91.0 z=-2.0499198284313724
- **PERSISTENT_DOWN** `ccgt_gen` value=2786 d1=-4.0 d12=-85.0 z=-2.0036313161764707
- **REVERSAL** `nuclear_gen` value=3330 d1=1.0 d12=-6.0 z=-0.8993196666666666
- **REVERSAL** `biomass_gen` value=476 d1=-1.0 d12=3.0 z=-0.6905108842042754

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.325 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.325 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.325 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.325 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.325 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
