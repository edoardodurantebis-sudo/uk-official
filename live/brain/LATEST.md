# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T14:34:10.760422Z`  
Memory snapshots: **1230**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **PERSISTENT_DOWN** `ind_demand` value=-1.077e+04 d1=0.0 d12=-22.0 z=-14.8387745
- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=-22.0 z=-14.8387745
- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=0.0 z=-6.528097223214285
- **CHANGE_POINT** `imbalance` value=8550 d1=0.0 d12=-385.0 z=-4.523732978448276
- **CHANGE_POINT** `wind_gen` value=1.622e+04 d1=131.0 d12=823.0 z=3.595189468012866
- **CHANGE_POINT** `biomass_gen` value=1457 d1=45.0 d12=421.0 z=2.88344368125
- **PERSISTENT_DOWN** `imbalance` value=8550 d1=0.0 d12=-385.0 z=-4.523732978448276
- **ROBUST_OUTLIER** `imbalance` value=8550 d1=0.0 d12=-385.0 z=-4.523732978448276
- **PERSISTENT_UP** `wind_gen` value=1.622e+04 d1=131.0 d12=823.0 z=3.595189468012866
- **ROBUST_OUTLIER** `wind_gen` value=1.622e+04 d1=131.0 d12=823.0 z=3.595189468012866
- **ROBUST_OUTLIER** `residual_proxy` value=9748 d1=0.0 d12=380.0 z=3.3488416087500004
- **CHANGE_POINT** `ps_gen` value=-468 d1=0.0 d12=239.0 z=1.0771188354591836
- **PERSISTENT_UP** `biomass_gen` value=1457 d1=45.0 d12=421.0 z=2.88344368125
- **PERSISTENT_UP** `margin` value=3.83e+04 d1=0.0 d12=122.0 z=1.4716139999999998
- **PERSISTENT_UP** `nuclear_gen` value=3340 d1=4.0 d12=4.0 z=1.1241495833333335

## Nearest historical live analogues

- `2026-09-18T13:22:08.039057Z` distance=0.147 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:26:20.440549Z` distance=0.147 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:30:31.422218Z` distance=0.147 → {'next30m_imbalance_delta': -7.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:34:41.646705Z` distance=0.147 → {'next30m_imbalance_delta': -7.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:38:52.307026Z` distance=0.147 → {'next30m_imbalance_delta': -7.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
