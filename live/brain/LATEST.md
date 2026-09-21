# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T03:13:30.575344Z`  
Memory snapshots: **2038**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.756e+04 d1=0.0 d12=14.0 z=35.50634848134328
- **ROBUST_OUTLIER** `margin` value=3.756e+04 d1=0.0 d12=14.0 z=35.50634848134328
- **CHANGE_POINT** `ind_demand` value=-1.18e+04 d1=0.0 d12=0.0 z=1.4613944583333334
- **CHANGE_POINT** `imbalance` value=-4865 d1=0.0 d12=39.0 z=1.0516925485781992
- **CHANGE_POINT** `ind_generation` value=1.574e+04 d1=0.0 d12=39.0 z=1.0516925485781992
- **CHANGE_POINT** `ps_gen` value=-22 d1=57.0 d12=109.0 z=None
- **REVERSAL** `nuclear_gen` value=3341 d1=4.0 d12=-3.0 z=1.1241495833333335
- **ACCELERATION** `nuclear_gen` value=3341 d1=4.0 d12=-3.0 z=1.1241495833333335
- **REVERSAL** `biomass_gen` value=3023 d1=-5.0 d12=11.0 z=0.6305012880434783
- **ACCELERATION** `biomass_gen` value=3023 d1=-5.0 d12=11.0 z=0.6305012880434783
- **PERSISTENT_UP** `ccgt_gen` value=5422 d1=273.0 d12=424.0 z=-0.3179352483355526
- **PERSISTENT_UP** `thermal_base` value=8763 d1=277.0 d12=421.0 z=-0.3084394651773982
- **PERSISTENT_DOWN** `interconnector_net` value=1.13e+04 d1=-182.0 d12=-1069.0 z=0.15728340157266812
- **ACCELERATION** `interconnector_net` value=1.13e+04 d1=-182.0 d12=-1069.0 z=0.15728340157266812
- **PERSISTENT_UP** `ps_gen` value=-22 d1=57.0 d12=109.0 z=None

## Nearest historical live analogues

- `2026-09-21T01:53:20.720277Z` distance=0.816 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:57:30.190951Z` distance=0.816 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:01:42.969969Z` distance=0.816 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:05:53.234228Z` distance=0.816 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:10:04.979412Z` distance=0.816 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
