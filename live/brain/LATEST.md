# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T08:37:51.518329Z`  
Memory snapshots: **804**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `wind_gen` value=1.541e+04 d1=-69.0 d12=114.0 z=5.446012729442971
- **ROBUST_OUTLIER** `ind_demand` value=-1.214e+04 d1=0.0 d12=-3.0 z=-6.79929183467742
- **ROBUST_OUTLIER** `margin` value=3.605e+04 d1=0.0 d12=471.0 z=6.011756467391304
- **REVERSAL** `wind_gen` value=1.541e+04 d1=-69.0 d12=114.0 z=5.446012729442971
- **ACCELERATION** `wind_gen` value=1.541e+04 d1=-69.0 d12=114.0 z=5.446012729442971
- **ROBUST_OUTLIER** `wind_gen` value=1.541e+04 d1=-69.0 d12=114.0 z=5.446012729442971
- **CHANGE_POINT** `thermal_base` value=6120 d1=-150.0 d12=-383.0 z=-1.5966530980392157
- **CHANGE_POINT** `ccgt_gen` value=2801 d1=-150.0 d12=-388.0 z=-1.5927424622807018
- **REVERSAL** `interconnector_net` value=5461 d1=-1.0 d12=1451.0 z=3.017026049652841
- **ACCELERATION** `interconnector_net` value=5461 d1=-1.0 d12=1451.0 z=3.017026049652841
- **ROBUST_OUTLIER** `interconnector_net` value=5461 d1=-1.0 d12=1451.0 z=3.017026049652841
- **CHANGE_POINT** `ps_gen` value=-563 d1=-141.0 d12=-789.0 z=-0.7177935666342412
- **PERSISTENT_UP** `nuclear_gen` value=3319 d1=0.0 d12=5.0 z=2.360714125
- **ACCELERATION** `nuclear_gen` value=3319 d1=0.0 d12=5.0 z=2.360714125
- **PERSISTENT_DOWN** `thermal_base` value=6120 d1=-150.0 d12=-383.0 z=-1.5966530980392157

## Nearest historical live analogues

- `2026-09-17T06:52:29.952634Z` distance=0.216 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:56:43.028097Z` distance=0.216 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:00:51.548981Z` distance=0.216 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:05:06.905847Z` distance=0.216 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:09:19.225959Z` distance=0.216 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
