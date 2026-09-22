# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T23:22:42.187473Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **PERSISTENT_DOWN** `thermal_base` value=1.378e+04 d1=-107.0 d12=-419.0 z=-9.78744342597968
- **ROBUST_OUTLIER** `thermal_base` value=1.378e+04 d1=-107.0 d12=-419.0 z=-9.78744342597968
- **PERSISTENT_DOWN** `ccgt_gen` value=1.005e+04 d1=-99.0 d12=-410.0 z=-9.713041154899136
- **ROBUST_OUTLIER** `ccgt_gen` value=1.005e+04 d1=-99.0 d12=-410.0 z=-9.713041154899136
- **REVERSAL** `ind_demand` value=-1.248e+04 d1=9.0 d12=-6.0 z=-4.72142825
- **ACCELERATION** `ind_demand` value=-1.248e+04 d1=9.0 d12=-6.0 z=-4.72142825
- **ROBUST_OUTLIER** `ind_demand` value=-1.248e+04 d1=9.0 d12=-6.0 z=-4.72142825
- **CHANGE_POINT** `wind_gen` value=3136 d1=25.0 d12=530.0 z=1.8473190251116072
- **CHANGE_POINT** `margin` value=3.723e+04 d1=0.0 d12=0.0 z=1.0208493513513512
- **PERSISTENT_UP** `wind_gen` value=3136 d1=25.0 d12=530.0 z=1.8473190251116072
- **REVERSAL** `interconnector_net` value=4645 d1=27.0 d12=-767.0 z=-1.5078906976439792
- **ACCELERATION** `biomass_gen` value=2915 d1=1.0 d12=7.0 z=0.5395918
- **REVERSAL** `imbalance` value=-8049 d1=7.0 d12=-2.0 z=-0.496992447368421
- **ACCELERATION** `imbalance` value=-8049 d1=7.0 d12=-2.0 z=-0.496992447368421
- **REVERSAL** `ind_generation` value=1.312e+04 d1=7.0 d12=-2.0 z=-0.496992447368421

## Nearest historical live analogues

- `2026-09-22T22:19:30.437012Z` distance=0.007 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:23:43.484966Z` distance=0.007 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:27:58.503394Z` distance=0.007 → {'next30m_imbalance_delta': -9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:50:58.019212Z` distance=0.013 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:54:12.694588Z` distance=0.013 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
