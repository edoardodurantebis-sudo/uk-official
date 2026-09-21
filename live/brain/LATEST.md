# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T03:09:17.893765Z`  
Memory snapshots: **2037**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.756e+04 d1=0.0 d12=1730.0 z=30.71522553846154
- **ROBUST_OUTLIER** `margin` value=3.756e+04 d1=0.0 d12=1730.0 z=30.71522553846154
- **CHANGE_POINT** `ind_demand` value=-1.18e+04 d1=0.0 d12=26.0 z=1.4613944583333334
- **CHANGE_POINT** `wind_gen` value=3783 d1=18.0 d12=-180.0 z=-1.4242462353575833
- **CHANGE_POINT** `imbalance` value=-4865 d1=0.0 d12=34.0 z=1.0516925485781992
- **CHANGE_POINT** `ind_generation` value=1.574e+04 d1=0.0 d12=34.0 z=1.0516925485781992
- **REVERSAL** `wind_gen` value=3783 d1=18.0 d12=-180.0 z=-1.4242462353575833
- **PERSISTENT_UP** `ccgt_gen` value=5149 d1=308.0 d12=101.0 z=-0.8996198401201603
- **ACCELERATION** `ccgt_gen` value=5149 d1=308.0 d12=101.0 z=-0.8996198401201603
- **PERSISTENT_UP** `thermal_base` value=8486 d1=301.0 d12=98.0 z=-0.8987193197596797
- **ACCELERATION** `thermal_base` value=8486 d1=301.0 d12=98.0 z=-0.8987193197596797
- **PERSISTENT_UP** `biomass_gen` value=3028 d1=10.0 d12=15.0 z=0.78240811
- **ACCELERATION** `biomass_gen` value=3028 d1=10.0 d12=15.0 z=0.78240811
- **PERSISTENT_DOWN** `interconnector_net` value=1.148e+04 d1=-832.0 d12=-888.0 z=0.29780749617486335
- **ACCELERATION** `interconnector_net` value=1.148e+04 d1=-832.0 d12=-888.0 z=0.29780749617486335

## Nearest historical live analogues

- `2026-09-21T01:53:20.720277Z` distance=0.820 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:57:30.190951Z` distance=0.820 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:01:42.969969Z` distance=0.820 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:05:53.234228Z` distance=0.820 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:10:04.979412Z` distance=0.820 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
