# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T23:26:53.201699Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **PERSISTENT_DOWN** `thermal_base` value=1.362e+04 d1=-160.0 d12=-495.0 z=-10.013503943165468
- **ROBUST_OUTLIER** `thermal_base` value=1.362e+04 d1=-160.0 d12=-495.0 z=-10.013503943165468
- **PERSISTENT_DOWN** `ccgt_gen` value=9886 d1=-165.0 d12=-493.0 z=-9.933569442225393
- **ROBUST_OUTLIER** `ccgt_gen` value=9886 d1=-165.0 d12=-493.0 z=-9.933569442225393
- **ACCELERATION** `ind_demand` value=-1.248e+04 d1=0.0 d12=-6.0 z=-4.72142825
- **ROBUST_OUTLIER** `ind_demand` value=-1.248e+04 d1=0.0 d12=-6.0 z=-4.72142825
- **CHANGE_POINT** `wind_gen` value=3167 d1=31.0 d12=473.0 z=1.9347820164359861
- **CHANGE_POINT** `margin` value=3.723e+04 d1=0.0 d12=0.0 z=1.0208493513513512
- **PERSISTENT_UP** `wind_gen` value=3167 d1=31.0 d12=473.0 z=1.9347820164359861
- **REVERSAL** `interconnector_net` value=4669 d1=24.0 d12=-718.0 z=-1.4378580907759884
- **REVERSAL** `nuclear_gen` value=3735 d1=5.0 d12=-2.0 z=0.5058673124999999
- **ACCELERATION** `nuclear_gen` value=3735 d1=5.0 d12=-2.0 z=0.5058673124999999
- **ACCELERATION** `imbalance` value=-8049 d1=0.0 d12=-2.0 z=-0.496992447368421
- **ACCELERATION** `ind_generation` value=1.312e+04 d1=0.0 d12=-2.0 z=-0.496992447368421

## Nearest historical live analogues

- `2026-09-22T22:19:30.437012Z` distance=0.007 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:23:43.484966Z` distance=0.007 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:27:58.503394Z` distance=0.007 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:32:11.198781Z` distance=0.007 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:50:58.019212Z` distance=0.013 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
