# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T17:50:55.506503Z`  
Memory snapshots: **289**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **ROBUST_OUTLIER** `biomass_gen` value=3204 d1=9.0 d12=485.0 z=58.2044978382353
- **REVERSAL** `ccgt_gen` value=1.042e+04 d1=-14.0 d12=173.0 z=12.387011542656587
- **ROBUST_OUTLIER** `ccgt_gen` value=1.042e+04 d1=-14.0 d12=173.0 z=12.387011542656587
- **REVERSAL** `thermal_base` value=1.374e+04 d1=-14.0 d12=164.0 z=12.306174277419354
- **ROBUST_OUTLIER** `thermal_base` value=1.374e+04 d1=-14.0 d12=164.0 z=12.306174277419354
- **PERSISTENT_DOWN** `interconnector_net` value=-1798 d1=-5.0 d12=-2314.0 z=-3.172512817131648
- **ROBUST_OUTLIER** `interconnector_net` value=-1798 d1=-5.0 d12=-2314.0 z=-3.172512817131648
- **PERSISTENT_DOWN** `nuclear_gen` value=3313 d1=0.0 d12=-9.0 z=-3.147618833333333
- **ROBUST_OUTLIER** `nuclear_gen` value=3313 d1=0.0 d12=-9.0 z=-3.147618833333333
- **PERSISTENT_UP** `margin` value=3.567e+04 d1=851.0 d12=842.0 z=2.2579347345238094
- **ACCELERATION** `margin` value=3.567e+04 d1=851.0 d12=842.0 z=2.2579347345238094
- **CHANGE_POINT** `imbalance` value=5772 d1=0.0 d12=-63.0 z=0.0457281186440678
- **CHANGE_POINT** `ind_generation` value=2.489e+04 d1=0.0 d12=-63.0 z=0.0457281186440678
- **REVERSAL** `wind_gen` value=1.051e+04 d1=-182.0 d12=155.0 z=0.30981347368421047
- **ACCELERATION** `wind_gen` value=1.051e+04 d1=-182.0 d12=155.0 z=0.30981347368421047

## Nearest historical live analogues

- `2026-09-15T11:22:30.581865Z` distance=0.194 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:26:42.593420Z` distance=0.194 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:30:55.285075Z` distance=0.194 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:35:06.452199Z` distance=0.194 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:39:18.571623Z` distance=0.194 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
