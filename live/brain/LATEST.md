# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T07:35:56.436252Z`  
Memory snapshots: **485**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.632e+04 d1=0.0 d12=-1122.0 z=-50.628886859375
- **ROBUST_OUTLIER** `margin` value=3.632e+04 d1=0.0 d12=-1122.0 z=-50.628886859375
- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=-444.0 z=-18.290574985294118
- **REVERSAL** `thermal_base` value=1.149e+04 d1=73.0 d12=-458.0 z=2.963506145669291
- **REVERSAL** `ccgt_gen` value=8165 d1=76.0 d12=-456.0 z=2.9607945635135136
- **CHANGE_POINT** `ind_generation` value=2.644e+04 d1=0.0 d12=126.0 z=0.6790937755972697
- **PERSISTENT_UP** `interconnector_net` value=9784 d1=0.0 d12=6198.0 z=2.6364099893358532
- **ACCELERATION** `interconnector_net` value=9784 d1=0.0 d12=6198.0 z=2.6364099893358532
- **CHANGE_POINT** `imbalance` value=6872 d1=0.0 d12=-318.0 z=-0.342999906996587
- **REVERSAL** `wind_gen` value=7844 d1=-55.0 d12=295.0 z=-1.875606524821287
- **PERSISTENT_DOWN** `biomass_gen` value=3229 d1=-3.0 d12=-3.0 z=-1.0117346249999999
- **ACCELERATION** `biomass_gen` value=3229 d1=-3.0 d12=-3.0 z=-1.0117346249999999
- **PERSISTENT_UP** `ps_gen` value=226 d1=4.0 d12=4.0 z=1.0117346249999999
- **ACCELERATION** `ps_gen` value=226 d1=4.0 d12=4.0 z=1.0117346249999999
- **PERSISTENT_DOWN** `nuclear_gen` value=3327 d1=-3.0 d12=-2.0 z=-0.67448975

## Nearest historical live analogues

- `2026-09-16T06:20:37.850603Z` distance=1.317 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:24:49.356241Z` distance=1.317 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:29:00.658838Z` distance=1.317 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:33:09.371452Z` distance=1.317 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:37:20.897017Z` distance=1.317 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
