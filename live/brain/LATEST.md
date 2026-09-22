# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T22:32:11.198781Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.42e+04 d1=-124.0 d12=-2829.0 z=-8.96709159651669
- **CHANGE_POINT** `ccgt_gen` value=1.046e+04 d1=-119.0 d12=-2828.0 z=-8.916093611671469
- **PERSISTENT_DOWN** `thermal_base` value=1.42e+04 d1=-124.0 d12=-2829.0 z=-8.96709159651669
- **ROBUST_OUTLIER** `thermal_base` value=1.42e+04 d1=-124.0 d12=-2829.0 z=-8.96709159651669
- **PERSISTENT_DOWN** `ccgt_gen` value=1.046e+04 d1=-119.0 d12=-2828.0 z=-8.916093611671469
- **ROBUST_OUTLIER** `ccgt_gen` value=1.046e+04 d1=-119.0 d12=-2828.0 z=-8.916093611671469
- **CHANGE_POINT** `wind_gen` value=2606 d1=6.0 d12=150.0 z=1.5732114647606383
- **CHANGE_POINT** `imbalance` value=-8047 d1=0.0 d12=-28.0 z=-0.79712425
- **CHANGE_POINT** `ind_generation` value=1.313e+04 d1=0.0 d12=-28.0 z=-0.79712425
- **PERSISTENT_UP** `ps_gen` value=145 d1=0.0 d12=2.0 z=-2.4464543474576272
- **PERSISTENT_UP** `interconnector_net` value=5412 d1=317.0 d12=652.0 z=-1.8026398656583629
- **ACCELERATION** `interconnector_net` value=5412 d1=317.0 d12=652.0 z=-1.8026398656583629
- **ACCELERATION** `nuclear_gen` value=3739 d1=-5.0 d12=-1.0 z=1.7986393333333333
- **PERSISTENT_UP** `wind_gen` value=2606 d1=6.0 d12=150.0 z=1.5732114647606383
- **PERSISTENT_DOWN** `biomass_gen` value=2908 d1=-1.0 d12=-5.0 z=0.08431121874999999

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.011 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:24:47.718083Z` distance=0.011 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:28:58.806773Z` distance=0.011 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:33:11.512074Z` distance=0.011 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:37:22.236065Z` distance=0.011 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
