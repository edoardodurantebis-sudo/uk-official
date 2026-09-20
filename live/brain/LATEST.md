# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T14:49:59.741529Z`  
Memory snapshots: **1862**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=673 d1=86.0 d12=87.0 z=58.68060825
- **PERSISTENT_UP** `biomass_gen` value=673 d1=86.0 d12=87.0 z=58.68060825
- **ACCELERATION** `biomass_gen` value=673 d1=86.0 d12=87.0 z=58.68060825
- **ROBUST_OUTLIER** `biomass_gen` value=673 d1=86.0 d12=87.0 z=58.68060825
- **ROBUST_OUTLIER** `margin` value=3.539e+04 d1=0.0 d12=-409.0 z=-11.19102381122449
- **CHANGE_POINT** `interconnector_net` value=1663 d1=0.0 d12=3845.0 z=4.362201397075209
- **CHANGE_POINT** `ccgt_gen` value=2479 d1=9.0 d12=70.0 z=3.5029951532258066
- **CHANGE_POINT** `thermal_base` value=5816 d1=17.0 d12=77.0 z=3.2930970147058822
- **ROBUST_OUTLIER** `interconnector_net` value=1663 d1=0.0 d12=3845.0 z=4.362201397075209
- **PERSISTENT_DOWN** `residual_proxy` value=1.782e+04 d1=-494.0 d12=-494.0 z=-3.889865544520548
- **ACCELERATION** `residual_proxy` value=1.782e+04 d1=-494.0 d12=-494.0 z=-3.889865544520548
- **ROBUST_OUTLIER** `residual_proxy` value=1.782e+04 d1=-494.0 d12=-494.0 z=-3.889865544520548
- **ROBUST_OUTLIER** `imbalance` value=-5650 d1=0.0 d12=81.0 z=3.6422446500000003
- **ROBUST_OUTLIER** `ind_generation` value=1.545e+04 d1=0.0 d12=81.0 z=3.6422446500000003
- **PERSISTENT_UP** `ccgt_gen` value=2479 d1=9.0 d12=70.0 z=3.5029951532258066

## Nearest historical live analogues

- `2026-09-20T12:51:54.502713Z` distance=0.143 → {'next30m_imbalance_delta': -11.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T12:56:06.352950Z` distance=0.143 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T13:00:16.706728Z` distance=0.143 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T13:04:27.263290Z` distance=0.143 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T13:08:37.856452Z` distance=0.143 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
