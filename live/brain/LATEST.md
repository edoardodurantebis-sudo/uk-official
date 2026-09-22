# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T23:18:30.768489Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.249e+04 d1=0.0 d12=-15.0 z=-10.791836
- **ROBUST_OUTLIER** `thermal_base` value=1.389e+04 d1=-1.0 d12=-436.0 z=-9.577950238026125
- **REVERSAL** `ccgt_gen` value=1.015e+04 d1=4.0 d12=-430.0 z=-9.52060747982709
- **ROBUST_OUTLIER** `ccgt_gen` value=1.015e+04 d1=4.0 d12=-430.0 z=-9.52060747982709
- **CHANGE_POINT** `wind_gen` value=3111 d1=24.0 d12=511.0 z=1.7646618218113612
- **CHANGE_POINT** `margin` value=3.723e+04 d1=0.0 d12=0.0 z=1.0208493513513512
- **PERSISTENT_UP** `wind_gen` value=3111 d1=24.0 d12=511.0 z=1.7646618218113612
- **REVERSAL** `interconnector_net` value=4618 d1=24.0 d12=-477.0 z=-1.5927896859171145
- **PERSISTENT_DOWN** `nuclear_gen` value=3738 d1=-5.0 d12=-6.0 z=1.0117346249999999
- **ACCELERATION** `nuclear_gen` value=3738 d1=-5.0 d12=-6.0 z=1.0117346249999999
- **REVERSAL** `biomass_gen` value=2914 d1=-5.0 d12=5.0 z=0.472142825
- **ACCELERATION** `biomass_gen` value=2914 d1=-5.0 d12=5.0 z=0.472142825

## Nearest historical live analogues

- `2026-09-22T22:19:30.437012Z` distance=0.017 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:23:43.484966Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:50:58.019212Z` distance=0.020 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:54:12.694588Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:58:28.957668Z` distance=0.021 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
