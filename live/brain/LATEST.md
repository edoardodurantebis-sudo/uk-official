# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T08:33:39.112740Z`  
Memory snapshots: **803**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.214e+04 d1=0.0 d12=-3.0 z=-6.79929183467742
- **CHANGE_POINT** `wind_gen` value=1.548e+04 d1=-165.0 d12=481.0 z=5.7125882539787805
- **ROBUST_OUTLIER** `ind_demand` value=-1.214e+04 d1=0.0 d12=-3.0 z=-6.79929183467742
- **ROBUST_OUTLIER** `margin` value=3.605e+04 d1=0.0 d12=471.0 z=6.011756467391304
- **REVERSAL** `wind_gen` value=1.548e+04 d1=-165.0 d12=481.0 z=5.7125882539787805
- **ACCELERATION** `wind_gen` value=1.548e+04 d1=-165.0 d12=481.0 z=5.7125882539787805
- **ROBUST_OUTLIER** `wind_gen` value=1.548e+04 d1=-165.0 d12=481.0 z=5.7125882539787805
- **PERSISTENT_UP** `interconnector_net` value=5462 d1=572.0 d12=1477.0 z=3.0535378234559913
- **ACCELERATION** `interconnector_net` value=5462 d1=572.0 d12=1477.0 z=3.0535378234559913
- **ROBUST_OUTLIER** `interconnector_net` value=5462 d1=572.0 d12=1477.0 z=3.0535378234559913
- **PERSISTENT_UP** `nuclear_gen` value=3319 d1=4.0 d12=4.0 z=2.360714125
- **CHANGE_POINT** `ps_gen` value=-422 d1=3.0 d12=-645.0 z=-0.3477427699416342
- **PERSISTENT_DOWN** `ccgt_gen` value=2951 d1=-29.0 d12=-253.0 z=-1.33800227079566
- **PERSISTENT_DOWN** `thermal_base` value=6270 d1=-25.0 d12=-249.0 z=-1.313988081842576
- **REVERSAL** `residual_proxy` value=-999 d1=10.0 d12=-355.0 z=-0.8285254714532871

## Nearest historical live analogues

- `2026-09-17T06:52:29.952634Z` distance=0.216 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:56:43.028097Z` distance=0.216 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:00:51.548981Z` distance=0.216 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:05:06.905847Z` distance=0.216 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:09:19.225959Z` distance=0.216 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
