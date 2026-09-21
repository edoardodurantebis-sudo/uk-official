# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T02:40:00.109498Z`  
Memory snapshots: **2030**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.755e+04 d1=0.0 d12=1723.0 z=25.400996968085106
- **ROBUST_OUTLIER** `margin` value=3.755e+04 d1=0.0 d12=1723.0 z=25.400996968085106
- **CHANGE_POINT** `ccgt_gen` value=4851 d1=-62.0 d12=-604.0 z=-1.5717628504551364
- **CHANGE_POINT** `thermal_base` value=8190 d1=-66.0 d12=-602.0 z=-1.55598402685422
- **CHANGE_POINT** `ind_demand` value=-1.18e+04 d1=0.0 d12=27.0 z=1.4613944583333334
- **PERSISTENT_DOWN** `wind_gen` value=3839 d1=-49.0 d12=-128.0 z=-2.067964953539823
- **ACCELERATION** `wind_gen` value=3839 d1=-49.0 d12=-128.0 z=-2.067964953539823
- **PERSISTENT_DOWN** `ccgt_gen` value=4851 d1=-62.0 d12=-604.0 z=-1.5717628504551364
- **PERSISTENT_DOWN** `thermal_base` value=8190 d1=-66.0 d12=-602.0 z=-1.55598402685422
- **PERSISTENT_UP** `interconnector_net` value=1.252e+04 d1=5.0 d12=290.0 z=1.2211727625305624
- **PERSISTENT_UP** `biomass_gen` value=3029 d1=16.0 d12=11.0 z=0.8644868626760563
- **ACCELERATION** `biomass_gen` value=3029 d1=16.0 d12=11.0 z=0.8644868626760563
- **REVERSAL** `nuclear_gen` value=3339 d1=-4.0 d12=2.0 z=0.8093876999999999
- **ACCELERATION** `nuclear_gen` value=3339 d1=-4.0 d12=2.0 z=0.8093876999999999
- **REVERSAL** `ps_gen` value=-128 d1=2.0 d12=-116.0 z=None

## Nearest historical live analogues

- `2026-09-21T01:23:21.503053Z` distance=0.869 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:28:09.159328Z` distance=0.869 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:32:22.156789Z` distance=0.869 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:36:33.089731Z` distance=0.869 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:40:46.188494Z` distance=0.869 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
