# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T10:35:05.307726Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high, wind rising.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.374e+04 d1=0.0 d12=-1055.0 z=-59.26516603333334
- **ROBUST_OUTLIER** `ind_demand` value=-1.374e+04 d1=0.0 d12=-1055.0 z=-59.26516603333334
- **CHANGE_POINT** `imbalance` value=-2300 d1=0.0 d12=2815.0 z=7.6274902144420125
- **ROBUST_OUTLIER** `ind_generation` value=1.873e+04 d1=0.0 d12=2815.0 z=8.232025503012048
- **ROBUST_OUTLIER** `imbalance` value=-2300 d1=0.0 d12=2815.0 z=7.6274902144420125
- **ROBUST_OUTLIER** `margin` value=4.078e+04 d1=0.0 d12=57.0 z=5.957497571585903
- **CHANGE_POINT** `ps_gen` value=-870 d1=0.0 d12=-409.0 z=-3.695686649361022
- **ROBUST_OUTLIER** `ps_gen` value=-870 d1=0.0 d12=-409.0 z=-3.695686649361022
- **PERSISTENT_DOWN** `thermal_base` value=5925 d1=0.0 d12=-641.0 z=-2.4938729433053743
- **CHANGE_POINT** `nuclear_gen` value=3805 d1=0.0 d12=6.0 z=0.3854227142857143
- **PERSISTENT_DOWN** `residual_proxy` value=1.31e+04 d1=0.0 d12=-182.0 z=-1.497038225609756
- **ACCELERATION** `residual_proxy` value=1.31e+04 d1=0.0 d12=-182.0 z=-1.497038225609756
- **PERSISTENT_UP** `biomass_gen` value=2677 d1=0.0 d12=20.0 z=0.8243763611111111
- **PERSISTENT_UP** `wind_forecast` value=7178 d1=0.0 d12=182.0 z=-0.49802440843023255
- **ACCELERATION** `wind_forecast` value=7178 d1=0.0 d12=182.0 z=-0.49802440843023255

## Nearest historical live analogues

- `2026-09-22T10:20:52.187902Z` distance=0.962 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -614.0}
- `2026-09-22T10:25:04.719488Z` distance=0.962 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -127.0}
- `2026-09-22T10:29:21.446166Z` distance=0.962 → {'next30m_imbalance_delta': -11397.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3381.0, 'next30m_residual_proxy_delta': -127.0}
- `2026-09-22T10:50:36.865474Z` distance=1.006 → {'next30m_imbalance_delta': -11397.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3381.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:33:45.224867Z` distance=1.009 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
