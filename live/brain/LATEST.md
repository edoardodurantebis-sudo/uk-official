# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T03:17:48.255541Z`  
Memory snapshots: **2039**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.756e+04 d1=0.0 d12=14.0 z=35.788834916666666
- **ROBUST_OUTLIER** `margin` value=3.756e+04 d1=0.0 d12=14.0 z=35.788834916666666
- **CHANGE_POINT** `ind_demand` value=-1.18e+04 d1=0.0 d12=0.0 z=1.4613944583333334
- **CHANGE_POINT** `imbalance` value=-4865 d1=0.0 d12=39.0 z=0.8658439849094567
- **CHANGE_POINT** `ind_generation` value=1.574e+04 d1=0.0 d12=39.0 z=0.8658439849094567
- **CHANGE_POINT** `interconnector_net` value=1.128e+04 d1=-16.0 d12=-1087.0 z=0.13721503770799787
- **PERSISTENT_DOWN** `nuclear_gen` value=3339 d1=-2.0 d12=-3.0 z=0.6744897499999999
- **ACCELERATION** `nuclear_gen` value=3339 d1=-2.0 d12=-3.0 z=0.6744897499999999
- **PERSISTENT_UP** `biomass_gen` value=3024 d1=1.0 d12=13.0 z=0.5978431875
- **ACCELERATION** `biomass_gen` value=3024 d1=1.0 d12=13.0 z=0.5978431875
- **PERSISTENT_UP** `ccgt_gen` value=5444 d1=22.0 d12=438.0 z=-0.2729416683813443
- **ACCELERATION** `ccgt_gen` value=5444 d1=22.0 d12=438.0 z=-0.2729416683813443
- **PERSISTENT_UP** `thermal_base` value=8783 d1=20.0 d12=435.0 z=-0.2697959
- **ACCELERATION** `thermal_base` value=8783 d1=20.0 d12=435.0 z=-0.2697959
- **PERSISTENT_DOWN** `interconnector_net` value=1.128e+04 d1=-16.0 d12=-1087.0 z=0.13721503770799787

## Nearest historical live analogues

- `2026-09-21T02:22:39.819793Z` distance=0.007 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:53:20.720277Z` distance=0.816 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:57:30.190951Z` distance=0.816 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:01:42.969969Z` distance=0.816 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:05:53.234228Z` distance=0.816 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
