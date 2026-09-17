# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T20:05:11.645283Z`  
Memory snapshots: **967**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **PERSISTENT_UP** `ind_generation` value=2.652e+04 d1=0.0 d12=7.0 z=-27.467518755319148
- **ROBUST_OUTLIER** `ind_generation` value=2.652e+04 d1=0.0 d12=7.0 z=-27.467518755319148
- **ROBUST_OUTLIER** `ind_demand` value=-1.116e+04 d1=0.0 d12=0.0 z=26.97959
- **PERSISTENT_UP** `imbalance` value=9708 d1=0.0 d12=7.0 z=-4.08535880221519
- **ROBUST_OUTLIER** `imbalance` value=9708 d1=0.0 d12=7.0 z=-4.08535880221519
- **CHANGE_POINT** `wind_gen` value=1.59e+04 d1=0.0 d12=662.0 z=1.3230520388579388
- **CHANGE_POINT** `ps_gen` value=503 d1=0.0 d12=225.0 z=0.9669676061946902
- **CHANGE_POINT** `ccgt_gen` value=5522 d1=0.0 d12=-1178.0 z=0.25868486024624965
- **CHANGE_POINT** `thermal_base` value=8841 d1=0.0 d12=-1184.0 z=0.2583516263387824
- **CHANGE_POINT** `biomass_gen` value=2857 d1=0.0 d12=-131.0 z=0.057331628749999995
- **PERSISTENT_DOWN** `interconnector_net` value=-737 d1=0.0 d12=-275.0 z=-2.0287269652004456
- **ACCELERATION** `interconnector_net` value=-737 d1=0.0 d12=-275.0 z=-2.0287269652004456
- **PERSISTENT_UP** `ps_gen` value=503 d1=0.0 d12=225.0 z=0.9669676061946902
- **PERSISTENT_DOWN** `nuclear_gen` value=3319 d1=0.0 d12=-6.0 z=0.463711703125
- **ACCELERATION** `nuclear_gen` value=3319 d1=0.0 d12=-6.0 z=0.463711703125

## Nearest historical live analogues

- `2026-09-17T18:57:56.745109Z` distance=0.131 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:02:09.783762Z` distance=0.131 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:06:26.402438Z` distance=0.131 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:10:36.600451Z` distance=0.131 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T18:24:17.596696Z` distance=0.191 → {'next30m_imbalance_delta': 10.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
