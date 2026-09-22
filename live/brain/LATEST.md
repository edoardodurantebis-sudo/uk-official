# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T22:48:59.705430Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.397e+04 d1=-46.0 d12=-2552.0 z=-9.40957253555878
- **CHANGE_POINT** `ccgt_gen` value=1.023e+04 d1=-48.0 d12=-2556.0 z=-9.35927419668588
- **PERSISTENT_DOWN** `thermal_base` value=1.397e+04 d1=-46.0 d12=-2552.0 z=-9.40957253555878
- **ROBUST_OUTLIER** `thermal_base` value=1.397e+04 d1=-46.0 d12=-2552.0 z=-9.40957253555878
- **PERSISTENT_DOWN** `ccgt_gen` value=1.023e+04 d1=-48.0 d12=-2556.0 z=-9.35927419668588
- **ROBUST_OUTLIER** `ccgt_gen` value=1.023e+04 d1=-48.0 d12=-2556.0 z=-9.35927419668588
- **CHANGE_POINT** `wind_gen` value=2798 d1=71.0 d12=358.0 z=1.7713787059375
- **PERSISTENT_UP** `ps_gen` value=148 d1=2.0 d12=5.0 z=-2.4395951296610168
- **ACCELERATION** `ps_gen` value=148 d1=2.0 d12=5.0 z=-2.4395951296610168
- **PERSISTENT_UP** `nuclear_gen` value=3741 d1=2.0 d12=4.0 z=2.248299166666667
- **ACCELERATION** `nuclear_gen` value=3741 d1=2.0 d12=4.0 z=2.248299166666667
- **PERSISTENT_UP** `wind_gen` value=2798 d1=71.0 d12=358.0 z=1.7713787059375
- **REVERSAL** `interconnector_net` value=5334 d1=-27.0 d12=572.0 z=-1.7045131426247289
- **PERSISTENT_DOWN** `biomass_gen` value=2911 d1=-4.0 d12=-5.0 z=0.275927625
- **ACCELERATION** `biomass_gen` value=2911 d1=-4.0 d12=-5.0 z=0.275927625

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.011 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:24:47.718083Z` distance=0.011 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:28:58.806773Z` distance=0.011 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:33:11.512074Z` distance=0.011 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:37:22.236065Z` distance=0.011 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
